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
            self.value_type = 'NUMBER_DOUBLE'
        elif type(value) == int:
            self.value = value
            self.value_type = 'NUMBER_INT64'
        elif type(value) == bool:
            self.value = int(value)
            self.value_type = value_type
        elif type(value) == datetime.datetime:
            timestamp = int(time.mktime(value.timetuple()))
            timestamp = timestamp * 1000    # Timestamp with nanoseconds
            self.value = timestamp
            self.value_type = 'TIMESTAMP'
        else:
            self.value = value
            self.value_type = value_type

    def update_json(self, json):
        self.value_type = parse(json, 'type')
        if self.value_type == 'TIMESTAMP':
            timestamp = int(parse(json, 'value'))
            timestamp = float(timestamp) / 1000    # Timestamp with nanoseconds
            self.value = datetime.datetime.fromtimestamp(timestamp)
        else:
            self.value = parse(json, 'value')

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

    @classmethod
    def fields(cls, fields):
        json = {}
        for key in fields:
            json[key] = CKValue(fields[key]).json()

        return json
