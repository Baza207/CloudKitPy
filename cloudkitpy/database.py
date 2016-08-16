#
# database.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python

from datatypes import Record
from datatypes import Zone
from request import Request
from helpers import parse


class Database:

    __logger = None

    container = None
    database_type = None

    def __init__(
        self,
        container,
        database_type,
        logger=None
    ):
        self.__logger = logger

        self.container = container
        self.database_type = database_type

    # Accessing Records

    def save_records(
        self,
        records,
        auto_fetch=False,
        force=False,
        options=None
    ):
        """Save records to the database."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyRecords/ModifyRecords.html#//apple_ref/doc/uid/TP40015240-CH2-SW9
        operations = self.__create_modify_operations(
            records,
            auto_fetch,
            force
        )

        payload = {
            'operations': operations,
        }
        if options is not None:
            payload.update(options)

        result = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/modify',
            payload,
            logger=self.__logger
        )

        if result.is_success is True:
            objects = []
            objects_json = parse(result.value, 'records')
            for object_json in objects_json:
                objects.append(Record(object_json))

            result.value = objects

        return result

    def __create_modify_operations(self, records, auto_fetch, force):
        operations = []
        for record in records:
            operation_type = None
            if force is True:
                operation_type = 'forceUpdate'
            elif record.record_change_tag is not None:
                operation_type = 'update'
            elif record.record_type is not None:
                operation_type = 'create'
            elif auto_fetch is True:
                # Fetch, and if record is returned,
                # append the change tag and update
                fetch_record_dict = {
                    'recordName': record.record_name,
                    'desiredKeys': None
                }
                fetched_record = self.fetch_records([fetch_record_dict])
                if fetched_record is not None:
                    operation_type = 'update'
                    record.record_change_tag = fetched_record.record_change_tag
                else:
                    print """Record doesn't already exist and is
                     missing a record type!"""

            if operation_type is not None:
                operation = {
                    'operationType': operation_type,
                    'record': record.json()
                }
                operations.append(operation)

        return operations

    def fetch_records(
        self,
        records=None,
        record_names=None,
        references=None,
        options=None
    ):
        """Fetch one or more records."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/LookupRecords/LookupRecords.html#//apple_ref/doc/uid/TP40015240-CH6-SW2
        json_records = self.__create_fetch_json_records(
            records,
            record_names,
            references
        )

        payload = {
            'records': json_records,
        }
        if options is not None:
            payload.update(options)

        result = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/lookup',
            payload,
            logger=self.__logger
        )

        if result.is_success is True:
            objects = []
            objects_json = parse(result.value, 'records')
            for object_json in objects_json:
                objects.append(Record(object_json))

            result.value = objects

        return result

    def __create_fetch_json_records(
        self,
        records=None,
        record_names=None,
        references=None
    ):
        json_records = []

        # Create JSON for records
        if records is not None:
            for record in records:
                json_records.append(record.json())

        # Create JSON for record names
        if record_names is not None:
            for record_name in record_names:
                record = Record()
                record.record_name = record_name
                json_records.append(record.json())

        # Create JSON for record names
        if references is not None:
            for reference in references:
                record = Record()
                record_name = reference.record_name
                if record_name is not None and len(record_name) > 0:
                    record.record_name = record_name
                    json_records.append(record.json())

        return json_records

    def delete_records(self, records, force=False, options=None):
        """Delete one or more records."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyRecords/ModifyRecords.html#//apple_ref/doc/uid/TP40015240-CH2-SW9
        operation_type = 'delete'
        if force is True:
            operation_type = 'forceDelete'

        operations = []
        for record in records:
            operation = {
                'operationType': operation_type,
                'record': record.json()
            }
            operations.append(operation)

        payload = {
            'operations': operations,
        }
        if options is not None:
            payload.update(options)

        result = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/modify',
            payload,
            logger=self.__logger
        )

        if result.is_success is True:
            objects = []
            objects_json = parse(result.value, 'records')
            for object_json in objects_json:
                objects.append(Record(object_json))

            result.value = objects

        return result

    def perform_query(self, query, continuation_marker=None, options=None):
        """Fetch records using a query."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/QueryingRecords/QueryingRecords.html#//apple_ref/doc/uid/TP40015240-CH5-SW4
        payload = {
            'query': query.json(),
        }

        if continuation_marker is not None:
            if options is None:
                options = {}
            options['continuationMarker'] = continuation_marker

        if options is not None:
            payload.update(options)

        result = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/query',
            payload,
            logger=self.__logger
        )

        if result.is_success is True:
            objects = []
            objects_json = parse(result.value, 'records')
            for object_json in objects_json:
                objects.append(Record(object_json))
            continuation_marker = parse(result.value, 'continuationMarker')

            result.value = (objects, continuation_marker)

        return result

    # Syncing Records

    def fetch_changed_records(self, zone_id, options=None):
        """Fetch changed records in a given custom zone."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ChangeRecords/ChangeRecords.html#//apple_ref/doc/uid/TP40015240-CH7-SW1
        if self.database_type == 'private':
            return None

        payload = {
            'zoneID': zone_id,
        }
        if options is not None:
            payload.update(options)

        result = Request.perform_request(
            'POST',
            self.container,
            'private',
            'records/changes',
            payload,
            logger=self.__logger
        )

        if result.is_success is True:
            objects = []
            objects_json = parse(result.value, 'records')
            for object_json in objects_json:
                objects.append(Record(object_json))

            more_coming = parse(result.value, 'moreComing')
            reverse = parse(result.value, 'reverse')
            sync_token = parse(result.value, 'syncToken')

            result.value = (objects, more_coming, reverse, sync_token)

        return result

    # Accessing Record Zones

    def save_record_zones(self, zone_ids):
        """Create one or more zones in the database."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyZones/ModifyZones.html#//apple_ref/doc/uid/TP40015240-CH10-SW1
        return self.__modify_record_zones(zone_ids, 'create')

    def fetch_record_zones(self, zones):
        """Fetch one or more zones."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/GettingZonesbyIdentifier/GettingZonesbyIdentifier.html#//apple_ref/doc/uid/TP40015240-CH22-SW1
        zones_json = []
        for zone in zones:
            zones_json.append(zone.json())

        payload = {
            'zones': zones_json,
        }

        result = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'zones/lookup',
            payload,
            logger=self.__logger
        )

        if result.is_success is True:
            objects = []
            objects_json = parse(result.value, 'zones')
            for object_json in objects_json:
                objects.append(Zone(object_json))

            result.value = objects

        return result

    def fetch_all_record_zones(self):
        """Fetch all zones in the database."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/GettingAllZones/GettingAllZones.html#//apple_ref/doc/uid/TP40015240-CH21-SW3
        result = Request.perform_request(
            'GET',
            self.container,
            self.database_type,
            'zones/list',
            logger=self.__logger
        )

        if result.is_success is True:
            zones = []
            objects_json = parse(result.value, 'zones')
            for object_json in objects_json:
                zones.append(Zone(object_json))

            if len(zones) > 0:
                result.value = self.fetch_record_zones(zones)
            else:
                result.value = []

        return result

    def delete_record_zones(self, zone_ids):
        """Delete the specified zones."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyZones/ModifyZones.html#//apple_ref/doc/uid/TP40015240-CH10-SW1
        return self.__modify_record_zones(zone_ids, 'delete')

    def __modify_record_zones(self, zone_ids, operation_type):
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyZones/ModifyZones.html#//apple_ref/doc/uid/TP40015240-CH10-SW1
        operations = []
        for zone_id in zone_ids:
            operation = {
                'operationType': operation_type,
                'zone': zone_id.json()
            }
            operations.append(operation)

        payload = {
            'operations': operations,
        }

        result = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'zones/modify',
            payload,
            logger=self.__logger
        )

        if result.is_success is True:
            objects = []
            objects_json = parse(result.value, 'zones')
            for object_json in objects_json:
                objects.append(Zone(object_json))

            result.value = objects

        return result
