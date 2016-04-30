#
# test.py
# CloudKitPy
#
# Created by James Barrow on 30/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

import unittest
from datetime import datetime
import time
from cloudkitpy.value import CKValue


class CKValueTests(unittest.TestCase):

    def test_string_value(self):
        string = 'Hello World'
        comp_value = {
            'value': string,
            'type': 'STRING'
        }
        gen_value = CKValue(string)
        self.failUnless(comp_value == gen_value)

    def test_int_value(self):
        integer = 1234
        comp_value = {
            'value': integer,
            'type': 'INT'
        }
        gen_value = CKValue(integer)
        self.failUnless(comp_value == gen_value)

    def test_double_value(self):
        double = 1234.56789
        comp_value = {
            'value': double,
            'type': 'DOUBLE'
        }
        gen_value = CKValue(double)
        self.failUnless(comp_value == gen_value)

    def test_bool_value(self):
        boolean = False
        comp_value = {
            'value': boolean,
        }
        gen_value = CKValue(boolean)
        self.failUnless(comp_value == gen_value)

    def test_datetime_value(self):
        date = datetime.utcnow()
        timestamp = time.mktime(date.timetuple())
        comp_value = {
            'value': timestamp,
        }
        gen_value = CKValue(date)
        self.failUnless(comp_value == gen_value)

    def test_list_value(self):
        list_array = ['a', 'b', 'c']
        comp_value = {
            'value': list_array,
        }
        gen_value = CKValue(list_array)
        self.failUnless(comp_value == gen_value)

    def test_asset_value(self):
        pass

    def test_location_value(self):
        pass

    def test_reference_value(self):
        pass


def main():
    unittest.main()

if __name__ == '__main__':
    main()
