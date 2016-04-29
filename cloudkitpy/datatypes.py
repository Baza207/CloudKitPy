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

    def __init__(
        self,
        file_checksum,
        size,
        reference_checksum,
        wrapping_key,
        receipt,
        download_url
    ):
        self.file_checksum = file_checksum
        self.size = size
        self.reference_checksum = reference_checksum
        self.wrapping_key = wrapping_key
        self.receipt = receipt
        self.download_url = download_url

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.file_checksum = json['fileChecksum']
            self.size = json['size']
            self.reference_checksum = json['referenceChecksum']
            self.wrapping_key = json['wrappingKey']
            self.receipt = json['receipt']
            self.download_url = json['downloadURL']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        comparator,
        field_name,
        field_value,
        distance=None
    ):
        self.comparator = comparator
        self.field_name = field_name
        self.field_value = field_value
        self.distance = distance

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.comparator = json['comparator']
            self.field_name = json['fieldName']
            self.field_value = json['fieldValue']
            self.distance = json['distance']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        latitude,
        longitude,
        horizontal_accuracy,
        vertical_accuracy,
        altitude,
        speed,
        course,
        timestamp
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.vertical_accuracy = vertical_accuracy
        self.altitude = altitude
        self.speed = speed
        self.course = course
        self.timestamp = timestamp

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.latitude = json['latitude']
            self.longitude = json['longitude']
            self.horizontal_accuracy = json['horizontalAccuracy']
            self.vertical_accuracy = json['verticalAccuracy']
            self.altitude = json['altitude']
            self.speed = json['speed']
            self.course = json['course']
            self.timestamp = json['timestamp']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        alert_body,
        alert_localization_key,
        alert_localization_args,
        alert_action_localization_key,
        alert_launch_image,
        sound_name,
        should_badge,
        should_send_content_available
    ):
        self.alert_body = alert_body
        self.alert_localization_key = alert_localization_key
        self.alert_localization_args = alert_localization_args
        self.alert_action_localization_key = alert_action_localization_key
        self.alert_launch_image = alert_launch_image
        self.sound_name = sound_name
        self.should_badge = should_badge
        self.should_send_content_available = should_send_content_available

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.alert_body = json['alertBody']
            self.alert_localization_key = json['alertLocalizationKey']
            self.alert_localization_args = json['alertLocalizationArgs']
            self.alert_action_localization_key = json[
                'alertActionLocalizationKey'
            ]
            self.alert_launch_image = json['alertLaunchImage']
            self.sound_name = json['soundName']
            self.should_badge = json['shouldBadge']
            self.should_send_content_available = json[
                'shouldSendContentAvailable'
            ]
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        record_type,
        filter_by,
        sort_by
    ):
        self.record_type = record_type
        self.filter_by = filter_by
        self.sort_by = sort_by

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.record_type = json['recordType']
            self.filter_by = json['filterBy']
            self.sort_by = json['sortBy']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        record_name,
        record_type,
        record_change_tag,
        fields,
        created,
        modified,
        deleted
    ):
        self.record_name = record_name
        self.record_type = record_type
        self.record_change_tag = record_change_tag
        self.fields = fields
        self.created = created
        self.modified = modified
        self.deleted = deleted

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.record_name = json['recordName']
            self.record_type = json['recordType']
            self.record_change_tag = json['recordChangeTag']
            self.fields = json['fields']
            self.created = json['created']
            self.modified = json['modified']
            self.deleted = json['deleted']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        record_name,
        zone_id,
        action
    ):
        self.record_name = record_name
        self.zone_id = zone_id
        self.action = action

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.record_name = json['recordName']
            self.zone_id = json['zoneID']
            self.action = json['action']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        field_name,
        ascending,
        relative_location
    ):
        self.field_name = field_name
        self.ascending = ascending
        self.relative_location = relative_location

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.field_name = json['fieldName']
            self.ascending = json['ascending']
            self.relative_location = json['relativeLocation']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        zone_id,
        subscription_id,
        subscription_type,
        query,
        fires_on,
        fires_once,
        notification_info,
        zone_wide
    ):
        self.zone_id = zone_id
        self.subscription_id = subscription_id
        self.subscription_type = subscription_type
        self.query = query
        self.fires_on = fires_on
        self.fires_once = fires_once
        self.notification_info = notification_info
        self.zone_wide = zone_wide

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.zone_id = json['zoneID']
            self.subscription_id = json['subscriptionID']
            self.subscription_type = json['subscriptionType']
            self.query = json['query']
            self.fires_on = json['firesOn']
            self.fires_once = json['firesOnce']
            self.notification_info = json['notificationInfo']
            self.zone_wide = json['zoneWide']
        except KeyError:
            pass
        except Exception, e:
            raise e

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


class User:
    """A user dictionary describes a user."""

    user_record_name = None
    first_name = None
    last_name = None
    email_address = None
    is_discoverable = False

    def __init__(
        self,
        user_record_name,
        first_name,
        last_name,
        email_address,
        is_discoverable
    ):
        self.user_record_name = user_record_name
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.is_discoverable = is_discoverable

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.user_record_name = json['userRecordName']
            self.first_name = json['firstName']
            self.last_name = json['lastName']
            self.email_address = json['emailAddress']
            self.is_discoverable = json['isDiscoverable']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        zone_id,
        sync_token,
        atomic
    ):
        self.zone_id = zone_id
        self.sync_token = sync_token
        self.atomic = atomic

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.zone_id = json['zoneID']
            self.sync_token = json['syncToken']
            self.atomic = json['atomic']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def __init__(
        self,
        zone_name
    ):
        self.zone_name = zone_name

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.zone_name = json['zoneName']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.containers = json['containers']
            self.services = json['services']
        except KeyError:
            pass
        except Exception, e:
            raise e

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

    def update_with_json(self, json):
        """Populate the class from a JSON object."""
        try:
            self.container_identifier = json['containerIdentifier']
            self.environment = json['environment']
            self.apns_environment = json['apnsEnvironment']
            self.api_token = json['apiTokenAuth']
            self.server_to_server_key = json['serverToServerKeyAuth']
        except KeyError:
            pass
        except Exception, e:
            raise e

    def json(self):
        """Create a JSON object from the object's properties."""
        return {
            'containerIdentifier': self.container_identifier,
            'environment': self.environment,
            'apnsEnvironment': self.apns_environment,
            'apiTokenAuth': self.api_token,
            'serverToServerKeyAuth': self.server_to_server_key
        }
