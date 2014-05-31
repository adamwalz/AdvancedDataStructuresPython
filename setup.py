#!/usr/bin/python
# -*- coding: utf-8 -*-

VERSION = '0.1'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'advancedDataStructures',
    'description': 'Advanced Data Structures for Python',
    'long_description': open('README').read(),
    'author': 'Adam Walz',
    'author_email': 'adam@adamwalz.new',
    'version': VERSION,
    'url': 'https://github.com/adamwalz/AdvancedDataStructuresPython',
    'test_suite': 'nose2.collector.collector',
    'packages': ['advanced_data_structures'],
    'scripts': [],
    'license': 'MIT',
    'keywords': 'linked list, list',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: C',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    }

setup(**config)
