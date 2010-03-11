#!/usr/bin/env python

from distutils.core import setup

setup(
    name        = 'py-pretty',
    version     = '1',
    description = 'Formats dates, numbers, etc. in a pretty, human readable format.',
    author      = 'S Anand',
    author_email= 'sanand@s-anand.net',
    url         = 'http://code.google.com/p/py-pretty/',
    packages    = ['pretty'],
    requires    = ['datetime'],
)
