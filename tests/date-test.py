'''Remember: This may fail because of a few microseconds. Run again and try.'''
from __future__ import print_function

import sys, os.path
sys.path.append(os.path.split(os.path.split(__file__)[0])[0]) # Add the parent directory as the root package for the pretty package

import pretty
from datetime import datetime, timedelta

# days ago, short
now = datetime.now()
assert pretty.date(now                      , asdays=True, short=True) == 'today'
assert pretty.date(now - timedelta(days=  1), asdays=True, short=True) == 'yest'
assert pretty.date(now - timedelta(days=  2), asdays=True, short=True) == '2d ago'
assert pretty.date(now - timedelta(days=  5), asdays=True, short=True) == '5d ago'
assert pretty.date(now - timedelta(days= 10), asdays=True, short=True) == '1w ago'
assert pretty.date(now - timedelta(days= 20), asdays=True, short=True) == '3w ago'
assert pretty.date(now - timedelta(days= 50), asdays=True, short=True) == '2mo ago'
assert pretty.date(now - timedelta(days=100), asdays=True, short=True) == '3mo ago'
assert pretty.date(now - timedelta(days=200), asdays=True, short=True) == '7mo ago'
assert pretty.date(now - timedelta(days=500), asdays=True, short=True) == '1y ago'

# in days, short
now = datetime.now()
assert pretty.date(now                      , asdays=True, short=True) == 'today'
assert pretty.date(now + timedelta(days=  1), asdays=True, short=True) == 'tom'
assert pretty.date(now + timedelta(days=  2), asdays=True, short=True) == 'in 2d'
assert pretty.date(now + timedelta(days=  5), asdays=True, short=True) == 'in 5d'
assert pretty.date(now + timedelta(days= 10), asdays=True, short=True) == 'in 1w'
assert pretty.date(now + timedelta(days= 20), asdays=True, short=True) == 'in 3w'
assert pretty.date(now + timedelta(days= 50), asdays=True, short=True) == 'in 2mo'
assert pretty.date(now + timedelta(days=100), asdays=True, short=True) == 'in 3mo'
assert pretty.date(now + timedelta(days=200), asdays=True, short=True) == 'in 7mo'
assert pretty.date(now + timedelta(days=500), asdays=True, short=True) == 'in 1y'

# seconds ago, short
now = datetime.now()
assert pretty.date(now                           , asdays=False, short=True) == 'now'
assert pretty.date(now - timedelta(seconds=   10), asdays=False, short=True) == '10s ago'
assert pretty.date(now - timedelta(seconds=   20), asdays=False, short=True) == '20s ago'
assert pretty.date(now - timedelta(seconds=   50), asdays=False, short=True) == '50s ago'
assert pretty.date(now - timedelta(seconds=  100), asdays=False, short=True) == '2m ago'
assert pretty.date(now - timedelta(seconds=  200), asdays=False, short=True) == '3m ago'
assert pretty.date(now - timedelta(seconds=  500), asdays=False, short=True) == '8m ago'
assert pretty.date(now - timedelta(seconds= 1000), asdays=False, short=True) == '17m ago'
assert pretty.date(now - timedelta(seconds= 2000), asdays=False, short=True) == '33m ago'
assert pretty.date(now - timedelta(seconds= 5000), asdays=False, short=True) == '1h ago'
assert pretty.date(now - timedelta(seconds=10000), asdays=False, short=True) == '3h ago'
assert pretty.date(now - timedelta(seconds=20000), asdays=False, short=True) == '6h ago'
assert pretty.date(now - timedelta(seconds=50000), asdays=False, short=True) == '14h ago'

# in seconds, short
now = datetime.now()
assert pretty.date(now                           , asdays=False, short=True) == 'now'
assert pretty.date(now + timedelta(seconds=   10), asdays=False, short=True) == 'in 10s'
assert pretty.date(now + timedelta(seconds=   20), asdays=False, short=True) == 'in 20s'
assert pretty.date(now + timedelta(seconds=   50), asdays=False, short=True) == 'in 50s'
assert pretty.date(now + timedelta(seconds=  100), asdays=False, short=True) == 'in 2m'
assert pretty.date(now + timedelta(seconds=  200), asdays=False, short=True) == 'in 3m'
assert pretty.date(now + timedelta(seconds=  500), asdays=False, short=True) == 'in 8m'
assert pretty.date(now + timedelta(seconds= 1000), asdays=False, short=True) == 'in 17m'
assert pretty.date(now + timedelta(seconds= 2000), asdays=False, short=True) == 'in 33m'
assert pretty.date(now + timedelta(seconds= 5000), asdays=False, short=True) == 'in 1h'
assert pretty.date(now + timedelta(seconds=10000), asdays=False, short=True) == 'in 3h'
assert pretty.date(now + timedelta(seconds=20000), asdays=False, short=True) == 'in 6h'
assert pretty.date(now + timedelta(seconds=50000), asdays=False, short=True) == 'in 14h'



# days ago, long
now = datetime.now()
assert pretty.date(now                       , asdays=True, short=False) == 'today'
assert pretty.date(now - timedelta(days=   1), asdays=True, short=False) == 'yesterday'
assert pretty.date(now - timedelta(days=   2), asdays=True, short=False) == 'day before'
assert pretty.date(now - timedelta(days=   5), asdays=True, short=False) == '5 days ago'
assert pretty.date(now - timedelta(days=  10), asdays=True, short=False) == 'last week'
assert pretty.date(now - timedelta(days=  20), asdays=True, short=False) == '3 weeks ago'
assert pretty.date(now - timedelta(days=  50), asdays=True, short=False) == 'last month'
assert pretty.date(now - timedelta(days= 100), asdays=True, short=False) == '3 months ago'
assert pretty.date(now - timedelta(days= 200), asdays=True, short=False) == '7 months ago'
assert pretty.date(now - timedelta(days= 500), asdays=True, short=False) == 'last year'
assert pretty.date(now - timedelta(days=1000), asdays=True, short=False) == '3 years ago'

# in days, long
now = datetime.now()
assert pretty.date(now                       , asdays=True, short=False) == 'today'
assert pretty.date(now + timedelta(days=   1), asdays=True, short=False) == 'tomorrow'
assert pretty.date(now + timedelta(days=   2), asdays=True, short=False) == 'day after'
assert pretty.date(now + timedelta(days=   5), asdays=True, short=False) == 'in 5 days'
assert pretty.date(now + timedelta(days=  10), asdays=True, short=False) == 'next week'
assert pretty.date(now + timedelta(days=  20), asdays=True, short=False) == 'in 3 weeks'
assert pretty.date(now + timedelta(days=  50), asdays=True, short=False) == 'next month'
assert pretty.date(now + timedelta(days= 100), asdays=True, short=False) == 'in 3 months'
assert pretty.date(now + timedelta(days= 200), asdays=True, short=False) == 'in 7 months'
assert pretty.date(now + timedelta(days= 500), asdays=True, short=False) == 'next year'
assert pretty.date(now + timedelta(days=1000), asdays=True, short=False) == 'in 3 years'

# seconds ago, long
now = datetime.now()
assert pretty.date(now                           , asdays=False, short=False) == 'now'
assert pretty.date(now - timedelta(seconds=   10), asdays=False, short=False) == '10 seconds ago'
assert pretty.date(now - timedelta(seconds=   20), asdays=False, short=False) == '20 seconds ago'
assert pretty.date(now - timedelta(seconds=   50), asdays=False, short=False) == '50 seconds ago'
assert pretty.date(now - timedelta(seconds=  100), asdays=False, short=False) == 'a minute ago'
assert pretty.date(now - timedelta(seconds=  200), asdays=False, short=False) == '3 minutes ago'
assert pretty.date(now - timedelta(seconds=  500), asdays=False, short=False) == '8 minutes ago'
assert pretty.date(now - timedelta(seconds= 1000), asdays=False, short=False) == '17 minutes ago'
assert pretty.date(now - timedelta(seconds= 2000), asdays=False, short=False) == '33 minutes ago'
assert pretty.date(now - timedelta(seconds= 5000), asdays=False, short=False) == 'an hour ago'
assert pretty.date(now - timedelta(seconds=10000), asdays=False, short=False) == '3 hours ago'
assert pretty.date(now - timedelta(seconds=20000), asdays=False, short=False) == '6 hours ago'
assert pretty.date(now - timedelta(seconds=50000), asdays=False, short=False) == '14 hours ago'

# in seconds, long
now = datetime.now()
assert pretty.date(now                           , asdays=False, short=False) == 'now'
assert pretty.date(now + timedelta(seconds=   10), asdays=False, short=False) == 'in 10 seconds'
assert pretty.date(now + timedelta(seconds=   20), asdays=False, short=False) == 'in 20 seconds'
assert pretty.date(now + timedelta(seconds=   50), asdays=False, short=False) == 'in 50 seconds'
assert pretty.date(now + timedelta(seconds=  100), asdays=False, short=False) == 'in a minute'
assert pretty.date(now + timedelta(seconds=  200), asdays=False, short=False) == 'in 3 minutes'
assert pretty.date(now + timedelta(seconds=  500), asdays=False, short=False) == 'in 8 minutes'
assert pretty.date(now + timedelta(seconds= 1000), asdays=False, short=False) == 'in 17 minutes'
assert pretty.date(now + timedelta(seconds= 2000), asdays=False, short=False) == 'in 33 minutes'
assert pretty.date(now + timedelta(seconds= 5000), asdays=False, short=False) == 'in an hour'
assert pretty.date(now + timedelta(seconds=10000), asdays=False, short=False) == 'in 3 hours'
assert pretty.date(now + timedelta(seconds=20000), asdays=False, short=False) == 'in 6 hours'
assert pretty.date(now + timedelta(seconds=50000), asdays=False, short=False) == 'in 14 hours'

print('No errors')
