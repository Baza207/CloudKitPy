#
# test.py
# CloudKitPy
#
# Created by James Barrow on 30/04/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python

import unittest
from datetime import datetime
import time
from cloudkitpy.cloudkit import CloudKit
from cloudkitpy.value import CKValue
from cloudkitpy.datatypes import Asset
from cloudkitpy.datatypes import Filter
from cloudkitpy.datatypes import Location
from cloudkitpy.datatypes import NotificationInfo
from cloudkitpy.datatypes import Query
from cloudkitpy.datatypes import Record
from cloudkitpy.datatypes import Reference
from cloudkitpy.datatypes import SortDescriptor
from cloudkitpy.datatypes import Subscription
from cloudkitpy.datatypes import UserInfo
from cloudkitpy.datatypes import Zone
from cloudkitpy.datatypes import ZoneID
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
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_int_value(self):
        integer = 1234
        comp_value = {
            'value': integer,
            'type': 'NUMBER_INT64'
        }
        gen_value = CKValue(integer)
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_double_value(self):
        double = 1234.56789
        comp_value = {
            'value': double,
            'type': 'DOUBLE'
        }
        gen_value = CKValue(double)
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_bool_value(self):
        boolean = False
        comp_value = {
            'value': boolean,
        }
        gen_value = CKValue(boolean)
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_datetime_value(self):
        date = datetime.utcnow()
        timestamp = time.mktime(date.timetuple())
        comp_value = {
            'value': timestamp,
        }
        gen_value = CKValue(date)
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_list_value(self):
        list_array = ['a', 'b', 'c']
        comp_value = {
            'value': list_array,
        }
        gen_value = CKValue(list_array)
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_asset_value(self):
        file_checksum = 'qwerty1234567890'
        size = 1234567890
        reference_checksum = '1234567890qwerty'
        wrapping_key = '12345qwerty67890'
        receipt = 'receipt'
        download_url = 'some/download/path'
        json = {
            'fileChecksum': file_checksum,
            'size': size,
            'referenceChecksum': reference_checksum,
            'wrappingKey': wrapping_key,
            'receipt': receipt,
            'downloadURL': download_url
        }
        asset_json = Asset(json).json()
        comp_value = {
            'value': asset_json,
            'type': 'ASSET'
        }
        gen_value = CKValue(asset_json, 'ASSET')
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_location_value(self):
        latitude = 12345.67890
        longitude = 09876.54321
        horizontal_accuracy = 10
        vertical_accuracy = 20
        altitude = 30
        speed = 0
        course = 90.0
        timestamp = 1234567890
        json = {
            'latitude': latitude,
            'longitude': longitude,
            'horizontalAccuracy': horizontal_accuracy,
            'verticalAccuracy': vertical_accuracy,
            'altitude': altitude,
            'speed': speed,
            'course': course,
            'timestamp': timestamp
        }
        location_json = Location(json).json()
        comp_value = {
            'value': location_json,
            'type': 'LOCATION'
        }
        gen_value = CKValue(location_json, 'LOCATION')
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())

    def test_reference_value(self):
        zone_name = 'Zone Name'
        zone_id_json = {
            'zoneName': zone_name
        }
        record_name = 'Record Name'
        zone_id = ZoneID(zone_id_json).json()
        action = CloudKit.NONE
        json = {
            'recordName': record_name,
            'zoneID': zone_id,
            'action': action
        }
        reference_json = Reference(json).json()
        comp_value = {
            'value': reference_json,
            'type': 'REFERENCE'
        }
        gen_value = CKValue(reference_json, 'REFERENCE')
        gen_json_value = CKValue(json=comp_value)
        self.failUnless(comp_value == gen_value.json())
        self.failUnless(comp_value == gen_json_value.json())


class DataTypeTests(unittest.TestCase):

    def test_asset(self):
        file_checksum = 'qwerty1234567890'
        size = 1234567890
        reference_checksum = '1234567890qwerty'
        wrapping_key = '12345qwerty67890'
        receipt = 'receipt'
        download_url = 'some/download/path'
        json = {
            'fileChecksum': file_checksum,
            'size': size,
            'referenceChecksum': reference_checksum,
            'wrappingKey': wrapping_key,
            'receipt': receipt,
            'downloadURL': download_url
        }
        gen_asset = Asset(json)
        self.failUnless(file_checksum == gen_asset.file_checksum)
        self.failUnless(size == gen_asset.size)
        self.failUnless(reference_checksum == gen_asset.reference_checksum)
        self.failUnless(wrapping_key == gen_asset.wrapping_key)
        self.failUnless(receipt == gen_asset.receipt)
        self.failUnless(download_url == gen_asset.download_url)

    def test_filter(self):
        comparator = CloudKit.EQUALS
        field_name = 'fieldName'
        field_value = 'value'
        distance = None
        json = {
            'comparator': comparator,
            'fieldName': field_name,
            'fieldValue': field_value,
            'distance': distance
        }
        gen_filter = Filter(json)
        self.failUnless(comparator == gen_filter.comparator)
        self.failUnless(field_name == gen_filter.field_name)
        self.failUnless(field_value == gen_filter.field_value)
        self.failUnless(distance == gen_filter.distance)

    def test_location(self):
        latitude = 12345.67890
        longitude = 09876.54321
        horizontal_accuracy = 10
        vertical_accuracy = 20
        altitude = 30
        speed = 0
        course = 90.0
        timestamp = 1234567890
        json = {
            'latitude': latitude,
            'longitude': longitude,
            'horizontalAccuracy': horizontal_accuracy,
            'verticalAccuracy': vertical_accuracy,
            'altitude': altitude,
            'speed': speed,
            'course': course,
            'timestamp': timestamp
        }
        gen_location = Location(json)
        self.failUnless(latitude == gen_location.latitude)
        self.failUnless(longitude == gen_location.longitude)
        self.failUnless(
            horizontal_accuracy == gen_location.horizontal_accuracy
        )
        self.failUnless(vertical_accuracy == gen_location.vertical_accuracy)
        self.failUnless(altitude == gen_location.altitude)
        self.failUnless(speed == gen_location.speed)
        self.failUnless(course == gen_location.course)
        self.failUnless(timestamp == gen_location.timestamp)

    def test_notification_info(self):
        alert_body = 'Alert body'
        alert_localization_key = 'ALERT_BODY'
        alert_localization_args = [
            'LOCALE_KEY_ONE',
            'LOCALE_KEY_TWO',
            'LOCALE_KEY_THREE'
        ]
        alert_action_localization_key = 'Action'
        alert_launch_image = 'LaunchImage.png'
        sound_name = 'Sound.aif'
        should_badge = True
        should_send_content_available = False
        json = {
            'alertBody': alert_body,
            'alertLocalizationKey': alert_localization_key,
            'alertLocalizationArgs': alert_localization_args,
            'alertActionLocalizationKey': alert_action_localization_key,
            'alertLaunchImage': alert_launch_image,
            'soundName': sound_name,
            'shouldBadge': should_badge,
            'shouldSendContentAvailable': should_send_content_available
        }
        gen_notification_info = NotificationInfo(json)
        self.failUnless(alert_body == gen_notification_info.alert_body)
        self.failUnless(
            alert_localization_key ==
            gen_notification_info.alert_localization_key
        )
        self.failUnless(
            alert_localization_args ==
            gen_notification_info.alert_localization_args
        )
        self.failUnless(
            alert_action_localization_key ==
            gen_notification_info.alert_action_localization_key
        )
        self.failUnless(
            alert_launch_image == gen_notification_info.alert_launch_image
        )
        self.failUnless(sound_name == gen_notification_info.sound_name)
        self.failUnless(should_badge == gen_notification_info.should_badge)
        self.failUnless(
            should_send_content_available ==
            gen_notification_info.should_send_content_available
        )

    # def test_query(self):
    #     comparator = CloudKit.EQUALS
    #     field_name = 'fieldName'
    #     field_value = 'value'
    #     distance = None
    #     filter_json = {
    #         'comparator': comparator,
    #         'fieldName': field_name,
    #         'fieldValue': field_value,
    #         'distance': distance
    #     }
    #     gen_filter_json = Filter(filter_json).json()
    #     ascending = False
    #     relative_location = None
    #     json = {
    #         'fieldName': field_name,
    #         'ascending': ascending,
    #         'relativeLocation': relative_location
    #     }
    #     gen_sort_descriptor = SortDescriptor(json).json()
    #     record_type = 'Type'
    #     filter_by = [gen_filter_json]
    #     sort_by = [gen_sort_descriptor]
    #     json = {
    #         'recordType': record_type,
    #         'filterBy': filter_by,
    #         'sortBy': sort_by
    #     }
    #     gen_query = Query(json)
    #     self.failUnless(record_type == gen_query.record_type)
    #     self.failUnless(filter_by == gen_query.filter_by)
    #     self.failUnless(sort_by == gen_query.sort_by)

    def test_record(self):
        record_name = 'Record Name'
        record_type = 'Type'
        record_change_tag = 'a1'
        fields = {
            'intField': CKValue(1),
            'stringField': CKValue('Hello World')
        }
        created = None
        modified = None
        deleted = True
        json = {
            'recordName': record_name,
            'recordType': record_type,
            'recordChangeTag': record_change_tag,
            'fields': fields,
            'created': created,
            'modified': modified,
            'deleted': deleted
        }
        gen_recrod = Record(json)
        self.failUnless(record_name == gen_recrod.record_name)
        self.failUnless(record_type == gen_recrod.record_type)
        self.failUnless(record_change_tag == gen_recrod.record_change_tag)
        self.failUnless(fields == gen_recrod.fields)
        self.failUnless(created == gen_recrod.created)
        self.failUnless(modified == gen_recrod.modified)
        self.failUnless(deleted == gen_recrod.deleted)

    def test_reference(self):
        zone_name = 'Zone Name'
        zone_id_json = {
            'zoneName': zone_name
        }
        record_name = 'Record Name'
        zone_id = ZoneID(zone_id_json).json()
        action = CloudKit.NONE
        json = {
            'recordName': record_name,
            'zoneID': zone_id,
            'action': action
        }
        gen_reference = Reference(json)
        self.failUnless(record_name == gen_reference.record_name)
        self.failUnless(zone_id == gen_reference.zone_id)
        self.failUnless(action == gen_reference.action)

    def test_sort_descriptor(self):
        field_name = 'fieldName'
        ascending = False
        relative_location = None
        json = {
            'fieldName': field_name,
            'ascending': ascending,
            'relativeLocation': relative_location
        }
        gen_sort_descriptor = SortDescriptor(json)
        self.failUnless(field_name == gen_sort_descriptor.field_name)
        self.failUnless(ascending == gen_sort_descriptor.ascending)
        self.failUnless(
            relative_location == gen_sort_descriptor.relative_location
        )

    # def test_subscription(self):
    #     alert_body = None
    #     alert_localization_key = None
    #     alert_localization_args = None
    #     alert_action_localization_key = None
    #     alert_launch_image = None
    #     sound_name = None
    #     should_badge = False
    #     should_send_content_available = True
    #     json = {
    #         'alertBody': alert_body,
    #         'alertLocalizationKey': alert_localization_key,
    #         'alertLocalizationArgs': alert_localization_args,
    #         'alertActionLocalizationKey': alert_action_localization_key,
    #         'alertLaunchImage': alert_launch_image,
    #         'soundName': sound_name,
    #         'shouldBadge': should_badge,
    #         'shouldSendContentAvailable': should_send_content_available
    #     }
    #     notification_info = NotificationInfo(json)
    #     comparator = CloudKit.EQUALS
    #     field_name = 'fieldName'
    #     field_value = 'value'
    #     distance = None
    #     filter_json = {
    #         'comparator': comparator,
    #         'fieldName': field_name,
    #         'fieldValue': field_value,
    #         'distance': distance
    #     }
    #     gen_filter_json = Filter(filter_json).json()
    #     ascending = False
    #     relative_location = None
    #     json = {
    #         'fieldName': field_name,
    #         'ascending': ascending,
    #         'relativeLocation': relative_location
    #     }
    #     gen_sort_descriptor = SortDescriptor(json).json()
    #     record_type = 'Type'
    #     filter_by = [gen_filter_json]
    #     sort_by = [gen_sort_descriptor]

    #     json = {
    #         'recordType': record_type,
    #         'filterBy': filter_by,
    #         'sortBy': sort_by
    #     }
    #     query = Query(json)
    #     zone_name = 'Zone Name'
    #     zone_id = ZoneID()
    #     zone_id.zone_name = zone_name
    #     subscription_id = 'Subscription ID'
    #     subscription_type = 'query'
    #     fires_on = 'update'
    #     fires_once = False
    #     zone_wide = True
    #     json = {
    #         'zoneID': zone_id,
    #         'subscriptionID': subscription_id,
    #         'subscriptionType': subscription_type,
    #         'query': query,
    #         'firesOn': fires_on,
    #         'firesOnce': fires_once,
    #         'notificationInfo': notification_info,
    #         'zoneWide': zone_wide
    #     }
    #     gen_subscription = Subscription(json)
    #     self.failUnless(zone_id.json() == gen_subscription.zone_id.json())
    #     self.failUnless(subscription_id == gen_subscription.subscription_id)
    #     self.failUnless(
    #         subscription_type == gen_subscription.subscription_type
    #     )
    #     self.failUnless(query.json() == gen_subscription.query.json())
    #     self.failUnless(fires_on == gen_subscription.fires_on)
    #     self.failUnless(fires_once == gen_subscription.fires_once)
    #     self.failUnless(
    #         notification_info.json() ==
    #         gen_subscription.notification_info.json()
    #     )
    #     self.failUnless(zone_wide == gen_subscription.zone_wide)

    def test_user_info(self):
        user_record_name = 'Record name'
        first_name = 'First name'
        last_name = 'Last name'
        email_address = 'name@email.com'
        is_discoverable = False
        json = {
            'userRecordName': user_record_name,
            'firstName': first_name,
            'lastName': last_name,
            'emailAddress': email_address,
            'isDiscoverable': is_discoverable
        }
        gen_user_info = UserInfo(json)
        self.failUnless(user_record_name == gen_user_info.user_record_name)
        self.failUnless(first_name == gen_user_info.first_name)
        self.failUnless(last_name == gen_user_info.last_name)
        self.failUnless(email_address == gen_user_info.email_address)
        self.failUnless(is_discoverable == gen_user_info.is_discoverable)

    def test_zone(self):
        zone_name = 'Zone Name'
        zone_id = ZoneID()
        zone_id.zone_name = zone_name
        sync_token = None
        atomic = False
        json = {
            'zoneID': zone_id.json(),
            'syncToken': sync_token,
            'atomic': atomic
        }
        gen_zone = Zone(json)
        self.failUnless(zone_id.json() == gen_zone.zone_id)
        self.failUnless(sync_token == gen_zone.sync_token)
        self.failUnless(atomic == gen_zone.atomic)

    def test_zone_id(self):
        comp_zone_name = 'Zone Name'
        json = {
            'zoneName': comp_zone_name
        }
        gen_zone = ZoneID(json)
        self.failUnless(comp_zone_name == gen_zone.zone_name)

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
