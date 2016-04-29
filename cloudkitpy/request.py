#
# request.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
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


class Request:

    __root_path = 'https://api.apple-cloudkit.com'
    __ck_version = '1'

    @classmethod
    def __iso_date(cls):
        return datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'

    @classmethod
    def __encode_string(cls, string):
        return base64.b64encode(string)

    @classmethod
    def __hash_string(cls, string):
        return hashlib.sha256(string).digest()

    @classmethod
    def __encode_and_hash_string(cls, string):
        hashed = cls.__hash_string(string)
        encoded = cls.__encode_string(hashed)
        return encoded

    @classmethod
    def __cloud_kit_path(
        cls,
        database,
        container,
        operation_subpath
    ):
        return os.path.join(
            '/database',
            cls.__ck_version,
            container.container_identifier,
            container.environment,
            database,
            operation_subpath
        )

    @classmethod
    def __create_message(cls, date, payload, path):
        request_body = cls.__encode_and_hash_string(payload)
        return '%s:%s:%s' % (date, request_body, path)

    @classmethod
    def __sign_message(cls, key_path, message):
        key_data = open(key_path).read()
        signing_key = SigningKey.from_pem(key_data)
        signature = signing_key.sign(
            message,
            hashfunc=hashlib.sha256,
            sigencode=ecdsa.util.sigencode_der
        )
        signature = base64.b64encode(signature)
        return signature

    @classmethod
    def create_request(
        cls,
        method,
        container,
        database,
        operation_subpath,
        payload=''
    ):
        date = cls.__iso_date()
        path = cls.__cloud_kit_path(database, container, operation_subpath)
        url = cls.__root_path + path

        message = cls.__create_message(date, payload, path)
        signed_message = cls.__sign_message(
            container.cert_path,
            message
        )

        headers = {
            'X-Apple-CloudKit-Request-KeyID': container.server_to_server_key,
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
