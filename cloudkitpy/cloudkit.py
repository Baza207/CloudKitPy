#
# cloudkit.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

from datetime import datetime
import base64
import hashlib
import os
from ecdsa import SigningKey
import ecdsa
import requests
import ckdatatypes


class CloudKit:

    # Enviroments - Constants to use when configuring the
    # environment of containers.
    DEVELOPMENT_ENVIRONMENT = 'DEVELOPMENT_ENVIRONMENT'
    """The container environment is not accessible by apps available
     on the store."""
    PRODUCTION_ENVIRONMENT = 'PRODUCTION_ENVIRONMENT'
    """The container environment is accessible by both development
     apps and apps available on the store."""

    # Comparator Values - The following values are allowed for
    # the comparator key in a filter dictionary.
    EQUALS = 'EQUALS'
    """The left-hand value is equal to the right-hand value."""
    NOT_EQUALS = 'NOT_EQUALS'
    """The left-hand value is not equal to the right-hand value."""
    LESS_THAN = 'LESS_THAN'
    """The left-hand value is less than the right-hand value."""
    LESS_THAN_OR_EQUALS = 'LESS_THAN_OR_EQUALS'
    """The left-hand value is less than or equal to the right-hand value."""
    GREATER_THAN = 'GREATER_THAN'
    """The left-hand value is greater than the right-hand value."""
    GREATER_THAN_OR_EQUALS = 'GREATER_THAN_OR_EQUALS'
    """The left-hand value is greater than or equal to the right-hand value."""
    NEAR = 'NEAR'
    """The left-hand location is within the specified distance
     of the right-hand location."""
    CONTAINS_ALL_TOKENS = 'CONTAINS_ALL_TOKENS'
    """The records have text fields that contain all specified tokens."""
    IN = 'IN'
    """The left-hand value is in the right-hand list."""
    NOT_IN = 'NOT_IN'
    """The left-hand value is not in the right-hand list."""
    CONTAINS_ANY_TOKENS = 'CONTAINS_ANY_TOKENS'
    """The records with text fields contain any of the specified tokens."""
    LIST_CONTAINS = 'LIST_CONTAINS'
    """The records contain values in a list field."""
    NOT_LIST_CONTAINS = 'NOT_LIST_CONTAINS'
    """The records don't contain the specified values in a list field."""
    NOT_LIST_CONTAINS_ANY = 'NOT_LIST_CONTAINS_ANY'
    """The records don't contain any of the specified values in
     a list field."""
    BEGINS_WITH = 'BEGINS_WITH'
    """The records with a field that begins with a specified value."""
    NOT_BEGINS_WITH = 'NOT_BEGINS_WITH'
    """The records with a field that doesn't begin with a specified value."""
    LIST_MEMBER_BEGINS_WITH = 'LIST_MEMBER_BEGINS_WITH'
    """The records contain a specified value as the first item in
     a list field."""
    NOT_LIST_MEMBER_BEGINS_WITH = 'NOT_LIST_MEMBER_BEGINS_WITH'
    """The records don't contain a specified value as the first item
     in a list field."""
    LIST_CONTAINS_ALL = 'LIST_CONTAINS_ALL'
    """The records contain all values in a list field."""
    NOT_LIST_CONTAINS_ALL = 'NOT_LIST_CONTAINS_ALL'
    """The records don't contain all specified values in a list field."""

    # Actions for a Reference Dictionary
    # The delete action for the reference object.
    NONE = 'NONE'
    """No action when a referenced record is deleted."""
    DELETE_SELF = 'DELETE_SELF'
    """Deletes a source record when the target record is deleted."""
    VALIDATE = 'VALIDATE'
    """Deletes a target record only after all source records are deleted.
     Verifies that the target record exists before creating this type of
     reference. If it doesn't exist, creating the reference fails."""

    __root_path = 'https://api.apple-cloudkit.com'
    __ck_version = '1'
    __container = None
    __environment = None
    __server_to_server_key = None
    __cert_path = None

    def __init__(self, config):
        """Configure CloudKitPy."""
        container = None
        try:
            # Current setup just uses the first passed in container
            container = config.containers[0]
        except Exception, e:
            raise e

        self.__container = container.identifier
        self.__environment = container.environment
        self.__server_to_server_key = container.server_to_server_key
        self.__cert_path = container.cert_path

    def __iso_date(self):
        return datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'

    def __encode_string(self, string):
        return base64.b64encode(string)

    def __hash_string(self, string):
        return hashlib.sha256(string).digest()

    def __encode_and_hash_string(self, string):
        hashed = self.__hash_string(string)
        encoded = self.__encode_string(hashed)
        return encoded

    def __cloud_kit_path(self, database, operation_subpath):
        return os.path.join(
            '/database',
            self.__ck_version,
            self.__container,
            self.__environment,
            database,
            operation_subpath
        )

    def __create_message(self, date, payload, path):
        request_body = self.__encode_and_hash_string(payload)
        return '%s:%s:%s' % (date, request_body, path)

    def __sign_message(self, key_path, message):
        key_data = open(key_path).read()
        signing_key = SigningKey.from_pem(key_data)
        signature = signing_key.sign(
            message,
            hashfunc=hashlib.sha256,
            sigencode=ecdsa.util.sigencode_der
        )
        signature = base64.b64encode(signature)
        return signature

    def __create_request(self, method, database, operation_subpath, payload):
        date = self.__iso_date()
        path = self.__cloud_kit_path(database, operation_subpath)
        url = self.__root_path + path

        message = self.__create_message(date, payload, path)
        signed_message = self.__sign_message(
            self.__cert_path,
            message
        )

        headers = {
            'X-Apple-CloudKit-Request-KeyID': self.__server_to_server_key,
            'X-Apple-CloudKit-Request-ISO8601Date': date,
            'X-Apple-CloudKit-Request-SignatureV1': signed_message
        }

        if method == "POST":
            r = requests.post(url, headers=headers, data=payload)
        elif method == "GET":
            r = requests.get(url, headers=headers, data=payload)
        status_code = r.status_code
        print "Code: %s" % status_code
        print "Response: %s" % r.text

    def get_current_user(self):
        self.__create_request('GET', 'public', 'users/current', '')
