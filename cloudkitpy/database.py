#
# database.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

from datatypes import Record
from request import Request


class Database:

    container = None
    database_type = None

    def __init__(
        self,
        container,
        database_type
    ):
        self.container = container
        self.database_type = database_type

    # Accessing Records

    def save_records(self, records, auto_fetch=False, options=None):
        """Save records to the database."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyRecords/ModifyRecords.html#//apple_ref/doc/uid/TP40015240-CH2-SW9
        operations = []
        for record in records:
            operation_type = None
            if record.record_change_tag is not None:
                operation_type = 'update'
            elif record.record_type is not None:
                operation_type = 'create'
            elif auto_fetch is True:
                # Fetch, and if record is returned,
                # append the change tap and update
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

        payload = {
            'operations': operations,
        }
        if options is not None:
            payload.update(options)

        json = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/modify',
            payload
        )

        objects = []
        objects_json = json['records']
        for object_json in objects_json:
            objects.append(Record(object_json))
        return objects

    def fetch_records(self, records, options=None):
        """Fetch one or more records."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/LookupRecords/LookupRecords.html#//apple_ref/doc/uid/TP40015240-CH6-SW2
        payload = {
            'records': records,
        }
        if options is not None:
            payload.update(options)

        json = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/lookup',
            payload
        )

        objects = []
        objects_json = json['records']
        for object_json in objects_json:
            objects.append(Record(object_json))
        return objects

    def delete_records(self, records, force=False, options=None):
        """Delete one or more records."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/ModifyRecords/ModifyRecords.html#//apple_ref/doc/uid/TP40015240-CH2-SW9
        operation_type = 'delete'
        if force is True:
            operation_type = 'forceDelete'

        operations = []
        for record in records:
            operation = {
                'operationType': operation_type
                'record': record.json()
            }
            operations.append(operation)

        payload = {
            'operations': operations,
        }
        if options is not None:
            payload.update(options)

        json = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/modify',
            payload
        )

        objects = []
        objects_json = json['records']
        for object_json in objects_json:
            objects.append(Record(object_json))
        return objects

    def perform_query(self, query, options=None):
        """Fetch records using a query."""
        # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/QueryingRecords/QueryingRecords.html#//apple_ref/doc/uid/TP40015240-CH5-SW4
        payload = {
            'query': query,
        }
        if options is not None:
            payload.update(options)

        json = Request.perform_request(
            'POST',
            self.container,
            self.database_type,
            'records/query',
            payload
        )

        objects = []
        objects_json = json['records']
        for object_json in objects_json:
            objects.append(Record(object_json))
        continuation_marker = Request.parse(json, 'continuationMarker')
        return (objects, continuation_marker)

    # Syncing Records

    def fetch_changed_records(self, zone_id=None):
        """Fetch changed records in a given custom zone."""
        pass

    # Accessing Record Zones

    def save_record_zones(self, zone_ids):
        """Create one or more zones in the database."""
        pass

    def fetch_record_zones(self, zone_ids):
        """Fetch one or more zones."""
        pass

    def fetch_all_record_zones(self):
        """Fetch all zones in the database."""
        pass

    def delete_record_zones(self, zone_ids):
        """Delete the specified zones."""
        pass
