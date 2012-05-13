#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from setuptools import setup
import sys

requires = ['PIL', 'jinja2', 'docutils']
if sys.version_info < (2,7):
    requires.append('argparse')

entry_points = {
    'console_scripts':
        ['sigal = sigal:main']
    }

setup(
    name = 'sigal',
    version = '0.1-dev',
    description = 'simple static gallery generator',
    long_description = open('README.rst').read(),
    url = 'https://github.com/saimn/sigal',
    author = 'Simon C.',
    author_email = 'contact@saimon.org',
    license = 'GPLv3',
    include_package_data = True,
    install_requires  =  requires,
    entry_points = entry_points,
    packages = ['sigal'],
    )
