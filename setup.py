#!/usr/bin/env python

import os
import re

from setuptools import find_packages, setup


def text_of(relpath):
    thisdir = os.path.dirname(__file__)
    file_path = os.path.join(thisdir, os.path.normpath(relpath))
    with open(file_path) as f:
        text = f.read()
    return text

version = re.search(
    "__version__ = '([^']+)'", text_of('docxxslt/__init__.py')).group(1)


NAME = 'docx-xslt'
VERSION = version
DESCRIPTION = 'XSL transformation for Microsoft Word .docx files.'
KEYWORDS = 'docx xslt office word'
AUTHOR = 'Frank Bohnsack'
AUTHOR_EMAIL = 'frank.bohnsack@gmail.com'
URL = 'https://github.com/backbohne/docx-xslt'
LICENSE = text_of('LICENSE')
PACKAGES = find_packages(exclude=['tests', 'tests.*'])
PACKAGE_DATA = {}

INSTALL_REQUIRES = ['lxml>=2.3.2']
TEST_SUITE = 'tests'
TESTS_REQUIRE = []

CLASSIFIERS = [
    'Development Status :: 1 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Office/Business :: Office Suites',
    'Topic :: Software Development :: Libraries'
]

LONG_DESCRIPTION = text_of('README.rst')

params = {
    'name':             NAME,
    'version':          VERSION,
    'description':      DESCRIPTION,
    'keywords':         KEYWORDS,
    'long_description': LONG_DESCRIPTION,
    'author':           AUTHOR,
    'author_email':     AUTHOR_EMAIL,
    'url':              URL,
    'license':          LICENSE,
    'packages':         PACKAGES,
    'package_data':     PACKAGE_DATA,
    'install_requires': INSTALL_REQUIRES,
    'tests_require':    TESTS_REQUIRE,
    'test_suite':       TEST_SUITE,
    'classifiers':      CLASSIFIERS,
}

setup(**params)