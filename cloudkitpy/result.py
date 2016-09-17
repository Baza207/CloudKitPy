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

    def __init__(self, json, status_code, request, payload):
        error = CKError(json, status_code, request, payload)
        is_ck_error = error.is_error is True or error.is_server_error is True
        if status_code != 200 or is_ck_error:
            self.error = error
            self.is_failure = True
        else:
            self.value = json
            self.is_success = True
