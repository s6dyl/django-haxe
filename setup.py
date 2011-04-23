#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup
import sys

reload(sys).setdefaultencoding("UTF-8")

setup(
    name='django-haxe',
    version='0.0.1-alpha',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=['django_haxe'],
    url='https://github.com/satels/django-haxe',
    download_url = 'https://github.com/satels/django-haxe/tarball/master',
    license = 'MIT license',
    description = u'Haxe Generator in Django'.encode('utf8'),
    long_description = open('README').read().decode('utf8'),

    classifiers=(
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
