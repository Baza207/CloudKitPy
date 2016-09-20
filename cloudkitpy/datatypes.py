#
# datatypes.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python

# References for Types and Dictionaries can be found at:
# https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/Types/Types.html

from helpers import parse


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
            self.file_checksum = parse(json, 'fileChecksum')
            self.size = parse(json, 'size')
            self.reference_checksum = parse(json, 'referenceChecksum')
            self.wrapping_key = parse(json, 'wrappingKey')
            self.receipt = parse(json, 'receipt')
            self.download_url = parse(json, 'downloadURL')

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.file_checksum,
            self.size,
            self.reference_checksum,
            self.receipt
        ]):
            return None

        json_object = {
            'fileChecksum': self.file_checksum,
            'size': self.size,
            'referenceChecksum': self.reference_checksum,
            'receipt': self.receipt
        }

        if self.wrapping_key is not None:
            json_object['wrappingKey'] = self.wrapping_key

        if self.download_url is not None:
            json_object['downloadURL'] = self.download_url

        return json_object


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
            self.comparator = parse(json, 'comparator')
            self.field_name = parse(json, 'fieldName')
            self.field_value = parse(json, 'fieldValue')
            self.distance = parse(json, 'distance')

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.comparator,
            self.field_name,
            self.field_value
        ]):
            return None

        json_object = {
            'comparator': self.comparator,
            'fieldName': self.field_name,
            'fieldValue': self.field_value
        }

        if self.distance is not None:
            json_object['distance'] = self.distance

        return json_object


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
            self.latitude = parse(json, 'latitude')
            self.longitude = parse(json, 'longitude')
            self.horizontal_accuracy = parse(
                json,
                'horizontalAccuracy'
            )
            self.vertical_accuracy = parse(json, 'verticalAccuracy')
            self.altitude = parse(json, 'altitude')
            self.speed = parse(json, 'speed')
            self.course = parse(json, 'course')
            self.timestamp = parse(json, 'timestamp')

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.latitude,
            self.longitude
        ]):
            return None

        json_object = {
            'latitude': self.latitude,
            'longitude': self.longitude
        }

        if self.horizontal_accuracy is not None:
            json_object['horizontalAccuracy'] = self.horizontal_accuracy

        if self.vertical_accuracy is not None:
            json_object['verticalAccuracy'] = self.vertical_accuracy

        if self.altitude is not None:
            json_object['altitude'] = self.altitude

        if self.speed is not None:
            json_object['speed'] = self.speed

        if self.course is not None:
            json_object['course'] = self.course

        if self.timestamp is not None:
            json_object['timestamp'] = self.timestamp

        return json_object


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
    should_badge = False
    should_send_content_available = True

    def __init__(self, json=None):
        if json is not None:
            self.alert_body = parse(json, 'alertBody')
            self.alert_localization_key = parse(
                json,
                'alertLocalizationKey'
            )
            self.alert_localization_args = parse(
                json,
                'alertLocalizationArgs'
            )
            self.alert_action_localization_key = parse(
                json,
                'alertActionLocalizationKey'
            )
            self.alert_launch_image = parse(json, 'alertLaunchImage')
            self.sound_name = parse(json, 'soundName')
            self.should_badge = parse(json, 'shouldBadge')
            self.should_send_content_available = parse(
                json,
                'shouldSendContentAvailable'
            )

    def json(self):
        """Create a JSON object from the object's properties."""
        json_object = {}

        if self.alert_body is not None:
            json_object['alertBody'] = self.alert_body

        if self.alert_localization_key is not None:
            json_object['alertLocalizationKey'] = self.alert_localization_key

        if self.alert_localization_args is not None:
            json_object['alertLocalizationArgs'] = self.alert_localization_args

        if self.alert_action_localization_key is not None:
            json_object[
                'alertActionLocalizationKey'
            ] = self.alert_action_localization_key

        if len(json_object) == 0:
            return None

        if self.alert_launch_image is not None:
            json_object['alertLaunchImage'] = self.alert_launch_image

        if self.sound_name is not None:
            json_object['soundName'] = self.sound_name

        if self.should_badge is not None:
            json_object['shouldBadge'] = self.should_badge
        else:
            json_object['shouldBadge'] = False

        if self.should_send_content_available is not None:
            json_object[
                'shouldSendContentAvailable'
            ] = self.should_send_content_available
        else:
            json_object['shouldSendContentAvailable'] = False

        return json_object


class Query:
    """A query dictionary.

    This represents a query used when fetching records
     from the database.
    """

    record_type = None
    filter_by = []
    sort_by = []

    def __init__(self, json=None):
        filter_by_json = None
        sort_by_json = None
        if json is not None:
            self.record_type = parse(json, 'recordType')
            filter_by_json = parse(json, 'filterBy')
            sort_by_json = parse(json, 'sortBy')

        if filter_by_json is not None and len(filter_by_json) > 0:
            self.filter_by = []
            for query_filter in filter_by_json:
                self.filter_by.append(Filter(query_filter))

        if sort_by_json is not None and len(sort_by_json) > 0:
            self.sort_by = []
            for sort_descriptor in sort_by_json:
                self.sort_by.append(SortDescriptor(sort_descriptor))

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.record_type
        ]):
            return None

        json_object = {
            'recordType': self.record_type
        }

        if self.filter_by is not None and len(self.filter_by) > 0:
            filter_by = []

            for query_filter in self.filter_by:
                filter_by.append(query_filter.json())

            json_object['filterBy'] = filter_by

        if self.sort_by is not None and len(self.sort_by) > 0:
            sort_by = []

            for sort_descriptor in self.sort_by:
                sort_by.append(sort_descriptor.json())

            json_object['sortBy'] = sort_by

        return json_object


class Record:
    """A record dictionary describes a successful operation."""

    record_name = None
    record_type = None
    record_change_tag = None
    fields = None
    created = None
    modified = None
    deleted = False

    def __init__(self, json=None):
        if json is not None:
            self.record_name = parse(json, 'recordName')
            self.record_type = parse(json, 'recordType')
            self.record_change_tag = parse(json, 'recordChangeTag')
            self.fields = parse(json, 'fields')
            self.created = parse(json, 'created')
            self.modified = parse(json, 'modified')
            self.deleted = parse(json, 'deleted')

    def json(self):
        """Create a JSON object from the object's properties."""
        if self.record_name is None and self.record_type is None:
            return None

        json_object = {
            'fields': self.fields
        }

        if self.record_name is not None:
            json_object['recordName'] = self.record_name

        if self.record_type is not None:
            json_object['recordType'] = self.record_type

        if self.record_change_tag is not None:
            json_object['recordChangeTag'] = self.record_change_tag

        if self.created is not None:
            json_object['created'] = self.created

        if self.modified is not None:
            json_object['modified'] = self.modified

        if self.deleted is not None:
            json_object['deleted'] = self.deleted

        return json_object


class Reference:
    """A reference dictionary represents a Reference field type."""

    record_name = None
    zone_id = None
    action = None

    def __init__(self, json=None):
        if json is not None:
            self.record_name = parse(json, 'recordName')
            self.zone_id = parse(json, 'zoneID')
            self.action = parse(json, 'action')

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.record_name,
            self.action
        ]):
            return None

        json_object = {
            'recordName': self.record_name,
            'action': self.action
        }

        if self.zone_id is not None:
            json_object['zoneID'] = self.zone_id

        return json_object


class SortDescriptor:
    """A sort descriptor dictionary.

    This determines the order of the fetched records.
    """

    field_name = None
    ascending = True
    relative_location = None

    def __init__(self, json=None):
        if json is not None:
            self.field_name = parse(json, 'fieldName')
            self.ascending = parse(json, 'ascending')
            self.relative_location = parse(json, 'relativeLocation')

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.field_name
        ]):
            return None

        json_object = {
            'fieldName': self.field_name
        }

        if self.ascending is not None:
            json_object['ascending'] = self.ascending
        else:
            json_object['ascending'] = True

        if self.relative_location is not None:
            json_object['relativeLocation'] = self.relative_location

        return json_object


class Subscription:
    """A subscription dictionary.

    This describes a successful subscription fetch.
    """

    zone_id = None
    subscription_id = None
    subscription_type = None
    query = None
    fires_on = None
    fires_once = False
    notification_info = None
    zone_wide = True

    def __init__(self, json=None):
        if json is not None:
            self.zone_id = ZoneID(parse(json, 'zoneID'))
            self.subscription_id = parse(json, 'subscriptionID')
            self.subscription_type = parse(json, 'subscriptionType')
            self.query = Query(parse(json, 'query'))
            self.fires_on = parse(json, 'firesOn')
            self.fires_once = parse(json, 'firesOnce')
            self.notification_info = NotificationInfo(
                parse(json, 'notificationInfo')
            )
            self.zone_wide = parse(json, 'zoneWide')

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.subscription_type
        ]):
            return None

        json_object = {
            'subscriptionType': self.subscription_type
        }

        if self.zone_id is None:
            json_object['zoneID'] = self.zone_id

        if self.subscription_id is not None:
            json_object['subscriptionID'] = self.subscription_id

        query = self.query.json()
        if query is not None:
            json_object['query'] = query

        if self.fires_on is not None:
            json_object['firesOn'] = self.fires_on

        if self.fires_once is not None:
            json_object['firesOnce'] = self.fires_once
        else:
            json_object['firesOnce'] = False

        notification_info = self.notification_info.json()
        if notification_info is not None:
            json_object['notificationInfo'] = notification_info

        if self.zone_wide is not None:
            json_object['zoneWide'] = self.zone_wide

        return json_object


class UserInfo:
    """A user dictionary describes a user."""

    user_record_name = None
    first_name = None
    last_name = None
    email_address = None
    is_discoverable = False

    def __init__(self, json=None):
        if json is not None:
            self.user_record_name = parse(json, 'userRecordName')
            self.first_name = parse(json, 'firstName')
            self.last_name = parse(json, 'lastName')
            self.email_address = parse(json, 'emailAddress')
            self.is_discoverable = parse(json, 'isDiscoverable')

    def json(self):
        """Create a JSON object from the object's properties."""
        json_object = {}

        if self.user_record_name is not None:
            json_object['userRecordName'] = self.user_record_name

        if self.first_name is not None:
            json_object['firstName'] = self.first_name

        if self.last_name is not None:
            json_object['lastName'] = self.last_name

        if self.email_address is not None:
            json_object['emailAddress'] = self.email_address

        if self.is_discoverable is not None:
            json_object['isDiscoverable'] = self.is_discoverable

        if len(json_object) == 0:
            return None

        return json_object


class Zone:
    """A zone dictionary describes a successful zone fetch."""

    zone_id = None
    sync_token = None
    atomic = False

    def __init__(self, json=None):
        if json is not None:
            self.zone_id = ZoneID(parse(json, 'zoneID'))
            self.sync_token = parse(json, 'syncToken')
            self.atomic = parse(json, 'atomic')

    def json(self):
        """Create a JSON object from the object's properties."""
        zone_id = self.zone_id.json()
        if not all([
            zone_id
        ]):
            return None

        json_object = {
            'zoneID': zone_id
        }

        if self.sync_token is not None:
            json_object['syncToken'] = self.sync_token

        if self.atomic is not None:
            json_object['atomic'] = self.atomic
        else:
            json_object['atomic'] = False

        return json_object


class ZoneID:
    """The zone ID identifies an area for organizing related records."""

    zone_name = None

    def __init__(self, json=None):
        if json is not None:
            self.zone_name = parse(json, 'zoneName')

    def json(self):
        """Create a JSON object from the object's properties."""
        if not all([
            self.zone_name
        ]):
            return None

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
