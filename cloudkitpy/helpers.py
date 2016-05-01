#
# error.py
# CloudKitPy
#
# Created by James Barrow on 01/05/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
#

# !/usr/bin/env python


def parse(json, key):
    value = None
    try:
        value = json[key]
    except KeyError:
        return None
    except Exception, e:
        raise e

    return value
