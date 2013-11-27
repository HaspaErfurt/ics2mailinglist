# ics2mailinglist

This script will parse a calendar ICS(e.g. from Google Calendar) and send the 
parsed events to a mail address. It is currently set up to take the events of 
the next week. 

Without modification the script will retrieve the ICS from a URL. To use it 
with a file, just change the link of the calendar to a valid file system 
location and replace the following line

    f = urlopen(cal_file)

with this:

    f = open(cal_file)

## Setup

Just replace all upper case strings with their corresponding settings:

    cal_file     = 'CALENDAR_ICS_URL'
    mail_from    = 'Weekly Event Notifier <SENDER_MAIL_HERE>'
    mail_to      = 'LIST_MAIL_HERE'
    mail_subject = 'Weekly event notifier'
    smtp_user    = 'SMTP_USER_HERE'
    smtp_pass    = 'SMPT_PASS_HERE'

## Todo

* Configuration file for settings
* Switch for file/url
* Configuration option for time range to parse
