'''Remember: This may fail because of a few microseconds. Run again and try.'''
from __future__ import print_function

from pretty import date as pd
from datetime import datetime
from datetime import timedelta as td

from freezegun import freeze_time

now = datetime.now()

freezer = freeze_time(now)

freezer.start()
# day  ago, short
assert pd(now, asdays=True, short=True) == 'today'
assert pd(now - td(days=1), asdays=True, short=True) == 'yest'
assert pd(now - td(days=2), asdays=True, short=True) == '2d ago'
assert pd(now - td(days=5), asdays=True, short=True) == '5d ago'
assert pd(now - td(days=10), asdays=True, short=True) == '1w ago'
assert pd(now - td(days=20), asdays=True, short=True) == '3w ago'
assert pd(now - td(days=50), asdays=True, short=True) == '2mo ago'
assert pd(now - td(days=100), asdays=True, short=True) == '3mo ago'
assert pd(now - td(days=200), asdays=True, short=True) == '7mo ago'
assert pd(now - td(days=500), asdays=True, short=True) == '1y ago'

# in days, short
assert pd(now, asdays=True, short=True) == 'today'
assert pd(now + td(days=1), asdays=True, short=True) == 'tom'
assert pd(now + td(days=2), asdays=True, short=True) == 'in 2d'
assert pd(now + td(days=5), asdays=True, short=True) == 'in 5d'
assert pd(now + td(days=10), asdays=True, short=True) == 'in 1w'
assert pd(now + td(days=20), asdays=True, short=True) == 'in 3w'
assert pd(now + td(days=50), asdays=True, short=True) == 'in 2mo'
assert pd(now + td(days=100), asdays=True, short=True) == 'in 3mo'
assert pd(now + td(days=200), asdays=True, short=True) == 'in 7mo'
assert pd(now + td(days=500), asdays=True, short=True) == 'in 1y'

# seconds ago, short
assert pd(now, asdays=False, short=True) == 'now'
assert pd(now - td(seconds=10), asdays=False, short=True) == '10s ago'
assert pd(now - td(seconds=20), asdays=False, short=True) == '20s ago'
assert pd(now - td(seconds=50), asdays=False, short=True) == '50s ago'
assert pd(now - td(seconds=100), asdays=False, short=True) == '2m ago'
assert pd(now - td(seconds=200), asdays=False, short=True) == '3m ago'
assert pd(now - td(seconds=500), asdays=False, short=True) == '8m ago'
assert pd(now - td(seconds=1000), asdays=False, short=True) == '17m ago'
assert pd(now - td(seconds=2000), asdays=False, short=True) == '33m ago'
assert pd(now - td(seconds=5000), asdays=False, short=True) == '1h ago'
assert pd(now - td(seconds=10000), asdays=False, short=True) == '3h ago'
assert pd(now - td(seconds=20000), asdays=False, short=True) == '6h ago'
assert pd(now - td(seconds=50000), asdays=False, short=True) == '14h ago'

# in seconds, short
assert pd(now, asdays=False, short=True) == 'now'
assert pd(now + td(seconds=10), asdays=False, short=True) == 'in 10s'
assert pd(now + td(seconds=20), asdays=False, short=True) == 'in 20s'
assert pd(now + td(seconds=50), asdays=False, short=True) == 'in 50s'
assert pd(now + td(seconds=100), asdays=False, short=True) == 'in 2m'
assert pd(now + td(seconds=200), asdays=False, short=True) == 'in 3m'
assert pd(now + td(seconds=500), asdays=False, short=True) == 'in 8m'
assert pd(now + td(seconds=1000), asdays=False, short=True) == 'in 17m'
assert pd(now + td(seconds=2000), asdays=False, short=True) == 'in 33m'
assert pd(now + td(seconds=5000), asdays=False, short=True) == 'in 1h'
assert pd(now + td(seconds=10000), asdays=False, short=True) == 'in 3h'
assert pd(now + td(seconds=20000), asdays=False, short=True) == 'in 6h'
assert pd(now + td(seconds=50000), asdays=False, short=True) == 'in 14h'


# days ago, long
assert pd(now, asdays=True, short=False) == 'today'
assert pd(now - td(days=1), asdays=True, short=False) == 'yesterday'
assert pd(now - td(days=2), asdays=True, short=False) == 'day before'
assert pd(now - td(days=5), asdays=True, short=False) == '5 days ago'
assert pd(now - td(days=10), asdays=True, short=False) == 'last week'
assert pd(now - td(days=20), asdays=True, short=False) == '3 weeks ago'
assert pd(now - td(days=50), asdays=True, short=False) == 'last month'
assert pd(now - td(days=100), asdays=True, short=False) == '3 months ago'
assert pd(now - td(days=200), asdays=True, short=False) == '7 months ago'
assert pd(now - td(days=500), asdays=True, short=False) == 'last year'
assert pd(now - td(days=1000), asdays=True, short=False) == '3 years ago'

# in days, long
assert pd(now, asdays=True, short=False) == 'today'
assert pd(now + td(days=1), asdays=True, short=False) == 'tomorrow'
assert pd(now + td(days=2), asdays=True, short=False) == 'day after'
assert pd(now + td(days=5), asdays=True, short=False) == 'in 5 days'
assert pd(now + td(days=10), asdays=True, short=False) == 'next week'
assert pd(now + td(days=20), asdays=True, short=False) == 'in 3 weeks'
assert pd(now + td(days=50), asdays=True, short=False) == 'next month'
assert pd(now + td(days=100), asdays=True, short=False) == 'in 3 months'
assert pd(now + td(days=200), asdays=True, short=False) == 'in 7 months'
assert pd(now + td(days=500), asdays=True, short=False) == 'next year'
assert pd(now + td(days=1000), asdays=True, short=False) == 'in 3 years'

# seconds ago, long
assert pd(now, asdays=False, short=False) == 'now'
assert pd(now - td(seconds=10), asdays=False, short=False) == '10 seconds ago'
assert pd(now - td(seconds=20), asdays=False, short=False) == '20 seconds ago'
assert pd(now - td(seconds=50), asdays=False, short=False) == '50 seconds ago'
assert pd(now - td(seconds=100), asdays=False, short=False) == 'a minute ago'
assert pd(now - td(seconds=200), asdays=False, short=False) == '3 minutes ago'
assert pd(now - td(seconds=500), asdays=False, short=False) == '8 minutes ago'
assert pd(now - td(seconds=1000), asdays=False, short=False) == '17 minutes ago'
assert pd(now - td(seconds=2000), asdays=False, short=False) == '33 minutes ago'
assert pd(now - td(seconds=5000), asdays=False, short=False) == 'an hour ago'
assert pd(now - td(seconds=10000), asdays=False, short=False) == '3 hours ago'
assert pd(now - td(seconds=20000), asdays=False, short=False) == '6 hours ago'
assert pd(now - td(seconds=50000), asdays=False, short=False) == '14 hours ago'

# in seconds, long
assert pd(now, asdays=False, short=False) == 'now'
assert pd(now + td(seconds=10), asdays=False, short=False) == 'in 10 seconds'
assert pd(now + td(seconds=20), asdays=False, short=False) == 'in 20 seconds'
assert pd(now + td(seconds=50), asdays=False, short=False) == 'in 50 seconds'
assert pd(now + td(seconds=100), asdays=False, short=False) == 'in a minute'
assert pd(now + td(seconds=200), asdays=False, short=False) == 'in 3 minutes'
assert pd(now + td(seconds=500), asdays=False, short=False) == 'in 8 minutes'
assert pd(now + td(seconds=1000), asdays=False, short=False) == 'in 17 minutes'
assert pd(now + td(seconds=2000), asdays=False, short=False) == 'in 33 minutes'
assert pd(now + td(seconds=5000), asdays=False, short=False) == 'in an hour'
assert pd(now + td(seconds=10000), asdays=False, short=False) == 'in 3 hours'
assert pd(now + td(seconds=20000), asdays=False, short=False) == 'in 6 hours'
assert pd(now + td(seconds=50000), asdays=False, short=False) == 'in 14 hours'

freezer.stop()

print('No errors')
