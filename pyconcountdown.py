#! /usr/bin/env python3

from dateutil import parser, tz
from datetime import datetime

PYCON_DATE = parser.parse("May 12, 2021 8:00 AM")
PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("America/New_York"))
now = datetime.now(tz=tz.tzlocal())

countdown = PYCON_DATE - now
print(f"Countdown to PyCon US 2021: {countdown}")
