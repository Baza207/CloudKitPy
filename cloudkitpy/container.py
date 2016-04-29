#
# container.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python


class Container:

    public_cloud_database = None
    private_cloud_database = None
    container_identifier = None
    environment = None
    apns_environment = None

    def __init__(
        self,
        container_identifier,
        environment,
        apns_environment=None
    ):
        pass

    def fetch_user_info(self):
        """Fetch information about the current user asynchronously."""
        pass

    def discover_user_info_with_email_address(self, email_address):
        """Fetch information about a single user.

        Based on the user's email address.
        """
        pass

    def discover_user_info_with_user_record_name(self, record_name):
        """Fetch information about a single user using the record name."""
        pass
