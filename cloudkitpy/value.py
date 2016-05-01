#
# value.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python

import datetime
import time
from helpers import parse


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

    def __init__(self, value=None, value_type=None, json=None):
        if value is not None:
            self.update_value(value, value_type)
        elif json is not None:
            self.update_json(json)

    def update_value(self, value, value_type):
        if type(value) == str:
            self.value = value
            self.value_type = 'STRING'
        elif type(value) == float:
            self.value = value
            self.value_type = 'DOUBLE'
        elif type(value) == int:
            self.value = value
            self.value_type = 'INT'
        elif type(value) == bool:
            self.value = value
            self.value = int(value)
            self.value_type = value_type
        elif type(value) == datetime.datetime:
            self.value = value
            self.value = int(time.mktime(value.timetuple()))
            self.value_type = value_type
        else:
            self.value = value
            self.value_type = value_type

    def update_json(self, json):
        self.value = parse(json, 'value')
        self.value_type = parse(json, 'type')

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
