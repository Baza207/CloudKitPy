#
# database.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python


class Database:

    container_identifier = None

    def __init__(self, container_identifier):
        self.container_identifier = container_identifier

    # Accessing Records

    def save_records(self, records, zone_id=None):
        """Save records to the database."""
        pass

    def fetch_records(self, records, zone_id=None):
        """Fetch one or more records."""
        pass

    def delete_records(self, records, zone_id=None):
        """Delete one or more records."""
        pass

    def perform_query(self, query, zone_id=None):
        """Fetch records using a query."""
        pass

    def new_records_batch(self, zone_id=None):
        """Create records batch builder.

        An object for modifying multiple records.
        """
        pass

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
