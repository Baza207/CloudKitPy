#
# ckhelpers.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python


class CKHelpers:
    """Describes the CloudKit web services protocol.

    Several common dictionaries are used by multiple requests and responses
     throughout CloudKit web services.
    """

    # References for Types and Dictionaries can be found at:
    # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/Types/Types.html

    @classmethod
    def asset_dictionary(
        cls,
        file_checksum,
        size,
        reference_checksum,
        wrapping_key,
        receipt,
        download_url
    ):
        """An asset dictionary.

        This represents an Asset field type.
        """
        return {
            'fileChecksum': file_checksum,
            'size': size,
            'referenceChecksum': reference_checksum,
            'wrappingKey': wrapping_key,
            'receipt': receipt,
            'downloadURL': download_url
        }

    @classmethod
    def filter_dictionary(
        cls,
        comparator,
        field_name,
        field_value,
        distance
    ):
        """A filter dictionary.

        This defines the logical conditions for determining whether a record
         matches the query.
        """
        return {
            'comparator': comparator,
            'fieldName': field_name,
            'fieldValue': field_value,
            'distance': distance
        }

    @classmethod
    def location_dictionary(
        cls,
        latitude,
        longitude,
        horizontal_accuracy,
        vertical_accuracy,
        altitude,
        speed,
        course,
        timestamp
    ):
        """A location dictionary.

        This represents values used to set a field of type Location.
        """
        return {
            'latitude': latitude,
            'longitude': longitude,
            'horizontalAccuracy': horizontal_accuracy,
            'verticalAccuracy': vertical_accuracy,
            'altitude': altitude,
            'speed': speed,
            'course': course,
            'timestamp': timestamp
        }

    @classmethod
    def notification_info_dictionary(
        cls,
        alert_body,
        alert_localization_key,
        alert_localization_args,
        alert_action_localization_key,
        alert_launch_image,
        sound_name,
        should_badge,
        should_send_content_available
    ):
        """A notification info dictionary.

        This represents information about a notification.
        """
        return {
            'alertBody': alert_body,
            'alertLocalizationKey': alert_localization_key,
            'alertLocalizationArgs': alert_localization_args,
            'alertActionLocalizationKey': alert_action_localization_key,
            'alertLaunchImage': alert_launch_image,
            'soundName': sound_name,
            'shouldBadge': should_badge,
            'shouldSendContentAvailable': should_send_content_available
        }

    @classmethod
    def query_dictionary(
        cls,
        record_type,
        filter_by,
        sort_by
    ):
        """A query dictionary.

        This represents a query used when fetching records
         from the database.
        """
        return {
            'recordType': record_type,
            'filterBy': filter_by,
            'sortBy': sort_by
        }

    @classmethod
    def record_dictionary(
        cls,
        record_name,
        record_type,
        record_change_tag,
        fields,
        created,
        modified,
        deleted
    ):
        """A record dictionary describes a successful operation."""
        return {
            'recordName': record_name,
            'recordType': record_type,
            'recordChangeTag': record_change_tag,
            'fields': fields,
            'created': created,
            'modified': modified,
            'deleted': deleted
        }

    @classmethod
    def reference_dictionary(
        cls,
        record_name,
        zone_id,
        action
    ):
        """A reference dictionary represents a Reference field type."""
        return {
            'recordName': record_name,
            'zoneID': zone_id,
            'action': action
        }

    @classmethod
    def sort_descriptor_dictionary(
        cls,
        field_name,
        ascending,
        relative_location
    ):
        """A sort descriptor dictionary.

        This determines the order of the fetched records.
        """
        return {
            'fieldName': field_name,
            'ascending': ascending,
            'relativeLocation': relative_location
        }

    @classmethod
    def subscription_dictionary(
        cls,
        zone_id,
        subscription_id,
        subscription_type,
        query,
        fires_on,
        fires_once,
        notification_info,
        zone_wide
    ):
        """A subscription dictionary.

        This describes a successful subscription fetch.
        """
        return {
            'zoneID': zone_id,
            'subscriptionID': subscription_id,
            'subscriptionType': subscription_type,
            'query': query,
            'firesOn': fires_on,
            'firesOnce': fires_once,
            'notificationInfo': notification_info,
            'zoneWide': zone_wide
        }

    @classmethod
    def user_dictionary(
        cls,
        user_record_name,
        first_name,
        last_name,
        email_address
    ):
        """A user dictionary describes a user."""
        return {
            'userRecordName': user_record_name,
            'firstName': first_name,
            'lastName': last_name,
            'emailAddress': email_address
        }

    @classmethod
    def zone_dictionary(
        cls,
        zone_id,
        sync_token,
        atomic
    ):
        """A zone dictionary describes a successful zone fetch."""
        return {
            'zoneID': zone_id,
            'syncToken': sync_token,
            'atomic': atomic
        }

    @classmethod
    def zone_id_dictionary(cls, zone_name):
        if zone_name is None or zone_name == '':
            zone_name = '_defaultZone'
        return {'zoneName': zone_name}
