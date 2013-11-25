#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
"""
ics2mailinglist

Sends calendar dates to a mailing list

"""
cal_link     = 'http://www.google.com/calendar/ical/2eskb61g20prl65k2qd01uktis%40group.calendar.google.com/public/basic.ics'
mail_from    = 'Weekly Event Notifier <SENDER_MAIL_HERE>'
mail_to      = 'LIST_MAIL_HERE'
mail_subject = 'Weekly event notifier'
smtp_user    = 'SMTP_USER_HERE'
smtp_pass    = 'SMPT_PASS_HERE'
smtp_server  = 'SMTP_SERVER_HERE'

from icalendar      import Calendar, Event
from icalendar.prop import vDDDTypes
from datetime       import *
from textwrap       import wrap
from urllib         import urlopen
import pytz
import smtplib

f     = urlopen(cal_link)
cal   = Calendar.from_ical(f.read())
mail  = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" 
         % (mail_from, mail_to, mail_subject))
now   = datetime.now(pytz.utc).replace(hour=0, minute=0, second=0, microsecond=0)
nweek = now + timedelta(weeks=1)

for ev in cal.walk():
    if ev.name == 'VEVENT':
        # Check the start and end dates of the event
        if len(str(vDDDTypes.from_ical(ev.get('dtstart'))).split(' ')) > 1:
            start = vDDDTypes.from_ical(ev.get('dtstart')).replace(tzinfo=pytz.utc)
            end   = vDDDTypes.from_ical(ev.get('dtend')).replace(tzinfo=pytz.utc)
            if start < now or start > nweek:
                continue
        else:
            start = vDDDTypes.from_ical(ev.get('dtstart'))
            end   = vDDDTypes.from_ical(ev.get('dtend'))
            if start < now.date() or start > nweek.date():
                continue

        mail += 'Betreff:      ' + ev.get('summary') + "\n"
        mail += 'Start:        ' + str(ev.get('dtstart').dt) + "\n"
        mail += 'Ende:         ' + str(ev.get('dtend').dt)
        if ev.get('description'):
            mail += "\nBeschreibung: "
            mail += "\n".join(wrap(ev.get('description'), 65, subsequent_indent=(' ' * 14)))

        mail += "\n\n"

# Send mail via SMTP
server = smtplib.SMTP_SSL(host = smtp_server)
server.login(smtp_user, smtp_pass)
server.sendmail(mail_from, mail_to, mail)

# Cleanup
server.quit()
f.close()
