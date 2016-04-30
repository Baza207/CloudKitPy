#
# container.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

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

    # Discovering Users

    def fetch_user_info(self):
        """Fetch information about the current user asynchronously."""
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
        json = Request.perform_request(
            'POST',
            self,
            'public',
            'users/lookup/email',
            {
                'users': [
                    {'emailAddress': email_address}
                ]
            }
        )
        users = []
        users_json = json['users']
        for user_json in users_json:
            users.append(User(user_json))
        return users

    def discover_user_info_with_user_record_name(self, record_name):
        """Fetch information about a single user using the record name."""
        json = Request.perform_request(
            'POST',
            self,
            'public',
            'users/lookup/id',
            {
                'users': [
                    {'userRecordName': record_name}
                ]
            }
        )
        users = []
        users_json = json['users']
        for user_json in users_json:
            users.append(User(user_json))
        return users
