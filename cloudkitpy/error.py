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

    def __init__(self, json, code, payload):
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
