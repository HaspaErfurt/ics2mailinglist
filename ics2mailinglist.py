#!/usr/bin/env python2
"""
ics2mailinglist

Sends calendar dates to a mailing list

"""

from icalendar      import Calendar, Event
from datetime       import datetime
from textwrap       import wrap
import pytz

f = open('calendar.ics', 'rb')
cal = Calendar.from_ical(f.read())
for ev in cal.walk():
    if ev.name == 'VEVENT':
        print('Betreff:      ' + str(ev.get('summary').encode('utf-8')))
        print('Start:        ' + str(ev.get('dtstart').dt))
        print('Ende:         ' + str(ev.get('dtend').dt))
        if ev.get('description'):
            description = wrap(ev.get('description'), 65, subsequent_indent='              ')
            print('Beschreibung: ' + "\n".join(description))
        print('')

f.close()

