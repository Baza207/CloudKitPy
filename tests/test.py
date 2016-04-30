#
# test.py
# CloudKitPy
#
# Created by James Barrow on 30/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

import unittest
from datetime import datetime
import time
from cloudkitpy.cloudkit import CloudKit
from cloudkitpy.value import CKValue
from cloudkitpy.datatypes import CloudKitConfig
from cloudkitpy.datatypes import ContainerConfig


class CKValueTests(unittest.TestCase):

    def test_string_value(self):
        string = 'Hello World'
        comp_value = {
            'value': string,
            'type': 'STRING'
        }
        gen_value = CKValue(string)
        self.failUnless(comp_value == gen_value)

    def test_int_value(self):
        integer = 1234
        comp_value = {
            'value': integer,
            'type': 'INT'
        }
        gen_value = CKValue(integer)
        self.failUnless(comp_value == gen_value)

    def test_double_value(self):
        double = 1234.56789
        comp_value = {
            'value': double,
            'type': 'DOUBLE'
        }
        gen_value = CKValue(double)
        self.failUnless(comp_value == gen_value)

    def test_bool_value(self):
        boolean = False
        comp_value = {
            'value': boolean,
        }
        gen_value = CKValue(boolean)
        self.failUnless(comp_value == gen_value)

    def test_datetime_value(self):
        date = datetime.utcnow()
        timestamp = time.mktime(date.timetuple())
        comp_value = {
            'value': timestamp,
        }
        gen_value = CKValue(date)
        self.failUnless(comp_value == gen_value)

    def test_list_value(self):
        list_array = ['a', 'b', 'c']
        comp_value = {
            'value': list_array,
        }
        gen_value = CKValue(list_array)
        self.failUnless(comp_value == gen_value)

    def test_asset_value(self):
        pass

    def test_location_value(self):
        pass

    def test_reference_value(self):
        pass


class DataTypeTests(unittest.TestCase):

    def test_asset(self):
        pass

    def test_filter(self):
        pass

    def test_location(self):
        pass

    def test_notification_info(self):
        pass

    def test_query(self):
        pass

    def test_record(self):
        pass

    def test_reference(self):
        pass

    def test_sort_descriptor(self):
        pass

    def test_subscription(self):
        pass

    def test_user_info(self):
        pass

    def test_zone(self):
        pass

    def test_zone_id(self):
        pass

    def test_cloudkit_config(self):
        identifier = 'iCloud.com.company.app'
        environment = CloudKit.DEVELOPMENT_ENVIRONMENT
        server_to_server_key_auth = '1234567890qwerty'
        cert_path = 'eckey.pem'
        container = ContainerConfig(
            identifier,
            environment,
            server_to_server_key=server_to_server_key_auth,
            cert_path=cert_path
        )
        comp_config = {
            'containers': [
                container
            ],
            'services': None
        }
        gen_config = CloudKitConfig([container]).json()
        self.failUnless(comp_config == gen_config)

    def test_container_config(self):
        identifier = 'iCloud.com.company.app'
        environment = CloudKit.DEVELOPMENT_ENVIRONMENT
        apns_environment = None
        api_token_auth = None
        server_to_server_key_auth = '1234567890qwerty'
        cert_path = 'eckey.pem'
        comp_config = {
            'containerIdentifier': identifier,
            'environment': environment,
            'apnsEnvironment': apns_environment,
            'apiTokenAuth': api_token_auth,
            'serverToServerKeyAuth': server_to_server_key_auth
        }
        gen_config = ContainerConfig(
            identifier,
            environment,
            server_to_server_key=server_to_server_key_auth,
            cert_path=cert_path
        ).json()
        self.failUnless(comp_config == gen_config)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
