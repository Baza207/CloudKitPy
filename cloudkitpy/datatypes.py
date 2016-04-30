#
# datatypes.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

# References for Types and Dictionaries can be found at:
# https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/Types/Types.html

from request import Request


class Asset:
    """An asset dictionary.

    This represents an Asset field type.
    """

    file_checksum = None
    size = None
    reference_checksum = None
    wrapping_key = None
    receipt = None
    download_url = None

    def __init__(self, json=None):
        if json is not None:
            self.file_checksum = Request.parse(json, 'fileChecksum')
            self.size = Request.parse(json, 'size')
            self.reference_checksum = Request.parse(json, 'referenceChecksum')
            self.wrapping_key = Request.parse(json, 'wrappingKey')
            self.receipt = Request.parse(json, 'receipt')
            self.download_url = Request.parse(json, 'downloadURL')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'fileChecksum': self.file_checksum,
            'size': self.size,
            'referenceChecksum': self.reference_checksum,
            'wrappingKey': self.wrapping_key,
            'receipt': self.receipt,
            'downloadURL': self.download_url
        }


class Filter:
    """A filter dictionary.

    This defines the logical conditions for determining whether a record
     matches the query.
    """

    comparator = None
    field_name = None
    field_value = None
    distance = None

    def __init__(self, json=None):
        if json is not None:
            self.comparator = Request.parse(json, 'comparator')
            self.field_name = Request.parse(json, 'fieldName')
            self.field_value = Request.parse(json, 'fieldValue')
            self.distance = Request.parse(json, 'distance')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'comparator': self.comparator,
            'fieldName': self.field_name,
            'fieldValue': self.field_value,
            'distance': self.distance
        }


class Location:
    """A location dictionary.

    This represents values used to set a field of type Location.
    """

    latitude = None
    longitude = None
    horizontal_accuracy = None
    vertical_accuracy = None
    altitude = None
    speed = None
    course = None
    timestamp = None

    def __init__(self, json=None):
        if json is not None:
            self.latitude = Request.parse(json, 'latitude')
            self.longitude = Request.parse(json, 'longitude')
            self.horizontal_accuracy = Request.parse(
                json,
                'horizontalAccuracy'
            )
            self.vertical_accuracy = Request.parse(json, 'verticalAccuracy')
            self.altitude = Request.parse(json, 'altitude')
            self.speed = Request.parse(json, 'speed')
            self.course = Request.parse(json, 'course')
            self.timestamp = Request.parse(json, 'timestamp')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'horizontalAccuracy': self.horizontal_accuracy,
            'verticalAccuracy': self.vertical_accuracy,
            'altitude': self.altitude,
            'speed': self.speed,
            'course': self.course,
            'timestamp': self.timestamp
        }


class NotificationInfo:
    """A notification info dictionary.

    This represents information about a notification.
    """

    alert_body = None
    alert_localization_key = None
    alert_localization_args = None
    alert_action_localization_key = None
    alert_launch_image = None
    sound_name = None
    should_badge = None
    should_send_content_available = None

    def __init__(self, json=None):
        if json is not None:
            self.alert_body = Request.parse(json, 'alertBody')
            self.alert_localization_key = Request.parse(
                json,
                'alertLocalizationKey'
            )
            self.alert_localization_args = Request.parse(
                json,
                'alertLocalizationArgs'
            )
            self.alert_action_localization_key = Request.parse(
                json,
                'alertActionLocalizationKey'
            )
            self.alert_launch_image = Request.parse(json, 'alertLaunchImage')
            self.sound_name = Request.parse(json, 'soundName')
            self.should_badge = Request.parse(json, 'shouldBadge')
            self.should_send_content_available = Request.parse(
                json,
                'shouldSendContentAvailable'
            )

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'alertBody': self.alert_body,
            'alertLocalizationKey': self.alert_localization_key,
            'alertLocalizationArgs': self.alert_localization_args,
            'alertActionLocalizationKey': self.alert_action_localization_key,
            'alertLaunchImage': self.alert_launch_image,
            'soundName': self.sound_name,
            'shouldBadge': self.should_badge,
            'shouldSendContentAvailable': self.should_send_content_available
        }


class Query:
    """A query dictionary.

    This represents a query used when fetching records
     from the database.
    """

    record_type = None
    filter_by = None
    sort_by = None

    def __init__(self, json=None):
        if json is not None:
            self.record_type = Request.parse(json, 'recordType')
            self.filter_by = Request.parse(json, 'filterBy')
            self.sort_by = Request.parse(json, 'sortBy')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'recordType': self.record_type,
            'filterBy': self.filter_by,
            'sortBy': self.sort_by
        }


class Record:
    """A record dictionary describes a successful operation."""

    record_name = None
    record_type = None
    record_change_tag = None
    fields = None
    created = None
    modified = None
    deleted = None

    def __init__(self, json=None):
        if json is not None:
            self.record_name = Request.parse(json, 'recordName')
            self.record_type = Request.parse(json, 'recordType')
            self.record_change_tag = Request.parse(json, 'recordChangeTag')
            self.fields = Request.parse(json, 'fields')
            self.created = Request.parse(json, 'created')
            self.modified = Request.parse(json, 'modified')
            self.deleted = Request.parse(json, 'deleted')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'recordName': self.record_name,
            'recordType': self.record_type,
            'recordChangeTag': self.record_change_tag,
            'fields': self.fields,
            'created': self.created,
            'modified': self.modified,
            'deleted': self.deleted
        }


class Reference:
    """A reference dictionary represents a Reference field type."""

    record_name = None
    zone_id = None
    action = None

    def __init__(self, json=None):
        if json is not None:
            self.record_name = Request.parse(json, 'recordName')
            self.zone_id = Request.parse(json, 'zoneID')
            self.action = Request.parse(json, 'action')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'recordName': self.record_name,
            'zoneID': self.zone_id,
            'action': self.action
        }


class SortDescriptor:
    """A sort descriptor dictionary.

    This determines the order of the fetched records.
    """

    properties = None

    def __init__(self, json=None):
        if json is not None:
            self.field_name = Request.parse(json, 'fieldName')
            self.ascending = Request.parse(json, 'ascending')
            self.relative_location = Request.parse(json, 'relativeLocation')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'fieldName': self.field_name,
            'ascending': self.ascending,
            'relativeLocation': self.relative_location
        }


class Subscription:
    """A subscription dictionary.

    This describes a successful subscription fetch.
    """

    zone_id = None
    subscription_id = None
    subscription_type = None
    query = None
    fires_on = None
    fires_once = None
    notification_info = None
    zone_wide = None

    def __init__(self, json=None):
        if json is not None:
            self.zone_id = Request.parse(json, 'zoneID')
            self.subscription_id = Request.parse(json, 'subscriptionID')
            self.subscription_type = Request.parse(json, 'subscriptionType')
            self.query = Request.parse(json, 'query')
            self.fires_on = Request.parse(json, 'firesOn')
            self.fires_once = Request.parse(json, 'firesOnce')
            self.notification_info = Request.parse(json, 'notificationInfo')
            self.zone_wide = Request.parse(json, 'zoneWide')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'zoneID': self.zone_id,
            'subscriptionID': self.subscription_id,
            'subscriptionType': self.subscription_type,
            'query': self.query,
            'firesOn': self.fires_on,
            'firesOnce': self.fires_once,
            'notificationInfo': self.notification_info,
            'zoneWide': self.zone_wide
        }


class UserInfo:
    """A user dictionary describes a user."""

    user_record_name = None
    first_name = None
    last_name = None
    email_address = None
    is_discoverable = False

    def __init__(self, json=None):
        if json is not None:
            self.user_record_name = Request.parse(json, 'userRecordName')
            self.first_name = Request.parse(json, 'firstName')
            self.last_name = Request.parse(json, 'lastName')
            self.email_address = Request.parse(json, 'emailAddress')
            self.is_discoverable = Request.parse(json, 'isDiscoverable')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'userRecordName': self.user_record_name,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'emailAddress': self.email_address,
            'isDiscoverable': self.is_discoverable
        }


class Zone:
    """A zone dictionary describes a successful zone fetch."""

    zone_id = None
    sync_token = None
    atomic = None

    def __init__(self, json=None):
        if json is not None:
            self.zone_id = Request.parse(json, 'zoneID')
            self.sync_token = Request.parse(json, 'syncToken')
            self.atomic = Request.parse(json, 'atomic')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'zoneID': self.zone_id,
            'syncToken': self.sync_token,
            'atomic': self.atomic
        }


class ZoneID:
    """The zone ID identifies an area for organizing related records."""

    zone_name = None

    def __init__(self, json=None):
        if json is not None:
            self.zone_name = Request.parse(json, 'zoneName')

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'zoneName': self.zone_name,
        }


class CloudKitConfig:
    """Dictionary used to configure the CloudKit environment."""

    containers = None
    services = None

    def __init__(
        self,
        containers,
        services=None
    ):
        self.containers = containers
        self.services = services

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'containers': self.containers,
            'services': self.services
        }


class ContainerConfig:
    """Dictionary used to create a configuration for a container."""

    container_identifier = None
    environment = None
    apns_environment = None
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

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'containerIdentifier': self.container_identifier,
            'environment': self.environment,
            'apnsEnvironment': self.apns_environment,
            'apiTokenAuth': self.api_token,
            'serverToServerKeyAuth': self.server_to_server_key
        }
