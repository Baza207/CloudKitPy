#
# setup.py
# CloudKitPy
#
# Created by James Barrow on 28/04/2016.
# Copyright (c) 2016 James Barrow - Pig on a Hill Productions.
# All rights reserved.
#

# !/usr/bin/env python
# flake8: noqa

import cloudkitpy
from setuptools import setup


description = 'CloudKitPy - A python wrapper of CloudKit Web Services'

setup(
    name='cloudkitpy',
    version=cloudkitpy.__version__,
    description=description,
    author=cloudkitpy.__author__,
    author_email='james@pigonahill.com',
    url='https://github.com/Baza207/CloudKitPy',
    license=cloudkitpy.__license__,
    zip_safe=False,
    packages=['cloudkitpy'],
    scripts=['scripts/cloudkitpy'],
    install_requires=['ecdsa', 'requests'],
    classifiers=[
        'Development Status :: 1 - Development',
        'Environment :: Console',
        'Framework :: CloudKitPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
