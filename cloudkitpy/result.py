#
# result.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python

from error import CKError


class Result:

    is_success = False
    is_failure = False
    value = None
    error = None

    def __init__(self, json, payload):
        error = CKError(json, payload)
        is_ck_error = error.is_error is True or error.is_server_error is True
        if json is None or is_ck_error:
            if json is None:
                error.reason = 'JSON response was None'
            self.error = error
            self.is_failure = True
        else:
            self.value = json
            self.is_success = True
