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
    long_description = '''Sample code::

    from datetime import datetime, timedelta
    now = datetime.now()
    hrago = now - timedelta(hours=1)
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)
    dayafter = now + timedelta(days=2)

    import pretty
    print pretty.date(now)                      # 'now'
    print pretty.date(hrago)                    # 'an hour ago'
    print pretty.date(hrago, short=True)        # '1h ago'
    print pretty.date(hrago, asdays=True)       # 'today'
    print pretty.date(yesterday, short=True)    # 'yest'
    print pretty.date(tomorrow)                 # 'tomorrow'
'''
)
