#
# container.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

from database import Database
from request import Request
from datatypes import User


class Container:

    # Getting the Public and Private Databases

    public_cloud_database = None
    private_cloud_database = None

    # Getting the Identifier and Environment

    container_identifier = None
    environment = None
    apns_environment = None

    # Getting tokens and cert path

    api_token = None
    server_to_server_key = None
    cert_path = None

    def __init__(
        self,
        container_identifier,
        environment,
        apns_environment=None,
        api_token=None,
        server_to_server_key=None,
        cert_path=None
    ):
        self.container_identifier = container_identifier
        self.environment = environment
        self.apns_environment = apns_environment
        self.api_token = api_token
        self.server_to_server_key = server_to_server_key
        self.cert_path = cert_path

        # Setup public and private cloud databases
        self.public_cloud_database = Database(self, 'public')
        self.private_cloud_database = Database(self, 'private')

    # Discovering Users

    def fetch_user_info(self):
        """Fetch information about the current user asynchronously."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/GetCurrentUser/GetCurrentUser.html#//apple_ref/doc/uid/TP40015240-CH12-SW1
        json = Request.perform_request(
            'GET',
            self,
            'public',
            'users/current'
        )
        return User(json)

    def discover_user_info_with_email_address(self, email_address):
        """Fetch information about a single user.

        Based on the user's email address.
        """
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/LookupUsersbyEmail/LookupUsersbyEmail.html#//apple_ref/doc/uid/TP40015240-CH14-SW1
        payload = {
            'users': [
                {'emailAddress': email_address}
            ]
        }

        json = Request.perform_request(
            'POST',
            self,
            'public',
            'users/lookup/email',
            payload
        )

        objects = []
        objects_json = Request.parse(json, 'records')
        if objects_json is not None:
            for object_json in objects_json:
                objects.append(User(object_json))
        return objects

    def discover_user_info_with_user_record_name(self, record_name):
        """Fetch information about a single user using the record name."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/LookupUsersbyID/LookupUsersbyID.html#//apple_ref/doc/uid/TP40015240-CH15-SW1
        payload = {
            'users': [
                {'userRecordName': record_name}
            ]
        }

        json = Request.perform_request(
            'POST',
            self,
            'public',
            'users/lookup/id',
            payload
        )

        objects = []
        objects_json = Request.parse(json, 'records')
        if objects_json is not None:
            for object_json in objects_json:
                objects.append(User(object_json))
        return objects
