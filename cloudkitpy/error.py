#
# error.py
# CloudKitPy
#
# Created by James Barrow on 01/05/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python

from datatypes import ZoneID
from helpers import parse


class CKError:

    is_error = False
    ck_error_code = None
    is_server_error = False
    server_error_code = None
    reason = None
    retry_after = None
    uuid = None
    redirect_url = None
    record_name = None
    subscription_id = None
    zone_id = None
    payload = None
    status_code = None
    status_code_reason = None

    def __init__(self, json, status_code, payload):
        if json is not None:
            self.ck_error_code = parse(json, 'ckErrorCode')
            self.is_error = self.ck_error_code is not None
            self.server_error_code = parse(json, 'serverErrorCode')
            self.is_server_error = self.server_error_code is not None
            self.reason = parse(json, 'reason')
            self.retry_after = parse(json, 'retryAfter')
            self.uuid = parse(json, 'uuid')
            self.redirect_url = parse(json, 'redirectURL')
            self.record_name = parse(json, 'recordName')
            self.subscription_id = parse(json, 'subscriptionID')
            zone_id_json = parse(json, 'zoneID')
            if zone_id_json is not None:
                zone_id = ZoneID(zone_id_json)
                self.zone_id = zone_id
        self.payload = payload
        self.status_code = status_code
        self.status_code_reason = self.__error_from_satus_code(status_code)
        if self.reason is None:
            self.reason = self.status_code_reason

    def __error_from_satus_code(self, status_code):   # noqa
        if status_code is None:
            return None
        elif status_code == 403:
            return CKError.ACCESS_DENIED_REASON
        elif status_code == 400:
            return CKError.BAD_REQUEST_REASON
        elif status_code == 401:
            return CKError.AUTHENTICATION_FAILED_REASON
        elif status_code == 404:
            return CKError.NOT_FOUND_REASON
        elif status_code == 409:
            return CKError.EXISTS_REASON
        elif status_code == 412:
            return CKError.VALIDATING_REFERENCE_ERROR_REASON
        elif status_code == 413:
            return CKError.QUOTA_EXCEEDED_REASON
        elif status_code == 421:
            return CKError.AUTHENTICATION_REQUIRED_REASON
        elif status_code == 429:
            return CKError.THROTTLED_REASON
        elif status_code == 500:
            return CKError.INTERNAL_ERROR_REASON
        elif status_code == 503:
            return CKError.TRY_AGAIN_LATER_REASON
        else:
            return None

    ACCESS_DENIED = 'ACCESS_DENIED'
    ATOMIC_ERROR = 'ATOMIC_ERROR'
    AUTHENTICATION_FAILED = 'AUTHENTICATION_FAILED'
    AUTHENTICATION_REQUIRED = 'AUTHENTICATION_REQUIRED'
    BAD_REQUEST = 'BAD_REQUEST'
    CONFLICT = 'CONFLICT'
    EXISTS = 'EXISTS'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    NOT_FOUND = 'NOT_FOUND'
    QUOTA_EXCEEDED = 'QUOTA_EXCEEDED'
    SIGN_IN_FAILED = 'SIGN_IN_FAILED'
    THROTTLED = 'THROTTLED'
    TRY_AGAIN_LATER = 'TRY_AGAIN_LATER'
    VALIDATING_REFERENCE_ERROR = 'VALIDATING_REFERENCE_ERROR'
    UNIQUE_FIELD_ERROR = 'UNIQUE_FIELD_ERROR'
    ZONE_NOT_FOUND = 'ZONE_NOT_FOUND'
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'
    NETWORK_ERROR = 'NETWORK_ERROR'
    SERVICE_UNAVAILABLE = 'SERVICE_UNAVAILABLE'
    INVALID_ARGUMENTS = 'INVALID_ARGUMENTS'
    UNEXPECTED_SERVER_RESPONSE = 'UNEXPECTED_SERVER_RESPONSE'
    CONFIGURATION_ERROR = 'CONFIGURATION_ERROR'

    ACCESS_DENIED_REASON = 'You don’t have permission to access the endpoint, record, zone, or database.'   # noqa
    ATOMIC_ERROR_REASON = 'An atomic batch operation failed.'
    AUTHENTICATION_FAILED_REASON = 'Authentication was rejected.'
    AUTHENTICATION_REQUIRED_REASON = 'The request requires authentication but none was provided.'   # noqa
    BAD_REQUEST_REASON = 'The request was not valid.'
    CONFLICT_REASON = 'The recordChangeTag value expired. (Retry the request with the latest tag.)'   # noqa
    EXISTS_REASON = 'The resource that you attempted to create already exists.'
    INTERNAL_ERROR_REASON = 'An internal error occurred.'
    NOT_FOUND_REASON = 'The resource was not found.'
    QUOTA_EXCEEDED_REASON = 'If accessing the public database, you exceeded the app’s quota. If accessing the private database, you exceeded the user’s iCloud quota.'   # noqa
    THROTTLED_REASON = 'The request was throttled. Try the request again later.'   # noqa
    TRY_AGAIN_LATER_REASON = 'An internal error occurred. Try the request again.'   # noqa
    VALIDATING_REFERENCE_ERROR_REASON = 'The request violates a validating reference constraint.'   # noqa
    ZONE_NOT_FOUND_REASON = 'The zone specified in the request was not found.'
