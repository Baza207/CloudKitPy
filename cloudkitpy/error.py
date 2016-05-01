#
# error.py
# CloudKitPy
#
# Created by James Barrow on 01/05/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python


class CKError:

    is_error = False
    error_code = None
    is_server_error = False
    server_error_code = None
    reason = None
    retry_after = 0
    uuid = None
    redirect_url = None
    record_name = None
    subscription_id = None
    zone_id = None

    def __init__(self):
        pass

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
