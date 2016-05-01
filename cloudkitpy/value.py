#
# value.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

import datetime
import time
from request import Request


class CKValue:
    """Describes the CloudKit web services protocol.

    Several common dictionaries are used by multiple requests and responses
     throughout CloudKit web services.
    """

    # References for Types and Dictionaries can be found at:
    # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/Types/Types.html

    # TODO: Work out how to correctly use `type` without
    # getting BAD_REQUEST errors.

    value = None
    value_type = None

    def __init__(self, value=None, json=None):
        if value is not None:
            self.update_value(value)
        elif json is not None:
            self.update_json(json)

    def update_value(self, value):
        if type(value) == str:
            self.value = value
            self.value_type = 'STRING'
        elif type(value) == float:
            self.value = value
            self.value_type = 'DOUBLE'
        elif type(value) == int:
            self.value = value
            self.value_type = 'INT'
        if type(value) == bool:
            self.value = value
            self.value = int(value)
        elif type(value) == datetime.datetime:
            self.value = value
            self.value = int(time.mktime(value.timetuple()))
        else:
            self.value = value

    def update_json(self, json):
        self.value = Request.parse(json, 'value')
        self.value_type = Request.parse(json, 'type')

    def json(self):
        if self.value_type is None:
            return {
                'value': self.value
            }
        else:
            return {
                'value': self.value,
                'type': self.value_type
            }
