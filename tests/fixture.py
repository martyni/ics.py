from __future__ import unicode_literals


cal1 = """
BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:plop
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
X-APPLE-CALENDAR-COLOR:#882F00
X-WR-TIMEZONE:Europe/Brussels
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Europe/Brussels
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
DTSTART:19810329T020000
TZNAME:UTC+2
TZOFFSETTO:+0200
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
DTSTART:19961027T030000
TZNAME:UTC+1
TZOFFSETTO:+0100
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20131024T204716Z
UID:ABBF2903-092F-4202-98B6-F757437A5B28
DTEND;TZID=Europe/Brussels:20131029T113000
TRANSP:OPAQUE
SUMMARY:dfqsdfjqkshflqsjdfhqs fqsfhlqs dfkqsldfkqsdfqsfqsfqsfs
DTSTART;TZID=Europe/Brussels:20131029T103000
DTSTAMP:20131024T204741Z
SEQUENCE:3
DESCRIPTION:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
 vitae facilisis enim. Morbi blandit et lectus venenatis tristique. Donec
 sit amet egestas lacus. Donec ullamcorper, mi vitae congue dictum, quam
 dolor luctus augue, id cursus purus justo vel lorem. Ut feugiat enim ips
 um, quis porta nibh ultricies congue. Pellentesque nisl mi, molestie id
 sem vel, vehicula nullam.
END:VEVENT
BEGIN:VTODO
DTSTAMP:20180218T154700Z
UID:Uid
DESCRIPTION:Lorem ipsum dolor sit amet.
PERCENT-COMPLETE:0
PRIORITY:0
SUMMARY:Name
END:VTODO
END:VCALENDAR
"""

cal2 = """
BEGIN:VCALENDAR
BEGIN:VEVENT
DTEND;TZID=Europe/Berlin:20120608T212500
SUMMARY:Name
DTSTART;TZID=Europe/Berlin:20120608T202500
LOCATION:MUC
SEQUENCE:0
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""


cal3 = """
BEGIN:VCALENDAR
END:VCALENDAR
"""

cal4 = """BEGIN:VCALENDAR"""

cal5 = """
BEGIN:VCALENDAR
VERSION:2.0
END:VCALENDAR
"""

cal6 = """
DESCRIPTION:a
 b
"""

cal7 = """
BEGIN:VCALENDAR

END:VCALENDAR
"""

cal8 = """
BEGIN:VCALENDAR
\t
END:VCALENDAR
"""

cal9 = """

BEGIN:VCALENDAR
END:VCALENDAR
"""

cal10 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
BEGIN:VEVENT
DTEND;TZID=Europe/Berlin:20120608T212500
DTSTAMP:20131024T204741Z
SUMMARY:Name
DTSTART;TZID=Europe/Berlin:20120608T202500
LOCATION:MUC
SEQUENCE:0
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

cal11 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
END:VCAL
"""

cal12 = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.8//EN
BEGIN:VEVENT
SUMMARY:Name
DTSTART;TZID=Europe/Berlin:20120608T202500
DURATION:P1DT1H
LOCATION:MUC
SEQUENCE:0
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

cal13 = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
BEGIN:VEVENT
SUMMARY:Name
DTSTART;TZID=Europe/Berlin:20120608T202500
DTEND;TZID=Europe/Berlin:20120608T212500
DURATION:P1DT1H
LOCATION:MUC
SEQUENCE:0
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

cal14 = u"""
BEGIN:VCALENDAR
VERSION:2.0;42
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
END:VCALENDAR
"""

cal15 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Hello, \\n World\\; This is a backslash : \\\\ and another new \\N line
DTSTART;TZID=Europe/Berlin:20120608T202500
DTEND;TZID=Europe/Berlin:20120608T212500
LOCATION:MUC
END:VEVENT

END:VCALENDAR
"""

# Event with URL
cal16 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Hello, \\n World\\; This is a backslash : \\\\ and another new \\N line
DTSTART;TZID=Europe/Berlin:20120608T202500
DTEND;TZID=Europe/Berlin:20120608T212500
LOCATION:MUC
URL:http://example.com/pub/calendars/jsmith/mytime.ics
CATEGORIES:Simple Category,My "Quoted" Category,Category\\, with comma
END:VEVENT

END:VCALENDAR
"""

cal17 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Some special \\; chars
DTSTART;TZID=Europe/Berlin:20130608T202501
DTEND;TZID=Europe/Berlin:20130608T212501
LOCATION:In\\, every text field
DESCRIPTION:Yes\\, all of them\\;
END:VEVENT
END:VCALENDAR
"""


# long event which is not all_day
cal18 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:ownCloud Calendar 0.7.3
X-WR-CALNAME:test
BEGIN:VEVENT
UID:3912dcd3d4
DTSTAMP:20151113T004809Z
CREATED:20151113T004809Z
LAST-MODIFIED:20151113T004809Z
SUMMARY:long event
DTSTART;TZID=Europe/Berlin:20151113T140000
DTEND;TZID=Europe/Berlin:20151124T080000
LOCATION:
DESCRIPTION:
CATEGORIES:
END:VEVENT
END:VCALENDAR
"""

# Event with TRANSP
cal19 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Hello, \\n World\\; This is a backslash : \\\\ and another new \\N line
DTSTART;TZID=Europe/Berlin:20120608T202500
DTEND;TZID=Europe/Berlin:20120608T212500
LOCATION:MUC
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
"""

# 3 days all-day event including end date
cal20 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:manually crafted from an ownCloud 8.0 ics
BEGIN:VEVENT
SUMMARY:3 days party
DTSTART;VALUE=DATE:20151114
DTEND;VALUE=DATE:20151116
END:VEVENT
END:VCALENDAR
"""

# Event with Display alarm without repeats
cal21 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Some special \\; chars
DTSTART;TZID=Europe/Berlin:20130608T202501
DTEND;TZID=Europe/Berlin:20130608T212501
LOCATION:In\\, every text field
DESCRIPTION:Yes\\, all of them\\;
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

# Event with Display alarm WITH repeats
cal22 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Some special \\; chars
DTSTART;TZID=Europe/Berlin:20130608T202501
DTEND;TZID=Europe/Berlin:20130608T212501
LOCATION:In\\, every text field
DESCRIPTION:Yes\\, all of them\\;
BEGIN:VALARM
TRIGGER:-PT1H
REPEAT:2
DURATION:PT10M
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

# Event with Display alarm without repeats
cal23 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Some special \\; chars
DTSTART;TZID=Europe/Berlin:20130608T202501
DTEND;TZID=Europe/Berlin:20130608T212501
LOCATION:In\\, every text field
DESCRIPTION:Yes\\, all of them\\;
BEGIN:VALARM
TRIGGER;VALUE=DATE-TIME:20160101T000000Z
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

# Event with AUDIO alarm without attach
cal24 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Some special \\; chars
DTSTART;TZID=Europe/Berlin:20130608T202501
DTEND;TZID=Europe/Berlin:20130608T212501
LOCATION:In\\, every text field
DESCRIPTION:Yes\\, all of them\\;
BEGIN:VALARM
TRIGGER;VALUE=DATE-TIME:20160101T000000Z
ACTION:AUDIO
END:VALARM
END:VEVENT
END:VCALENDAR
"""

# Event with AUDIO alarm WITH attach
cal25 = u"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN

BEGIN:VEVENT
SUMMARY:Some special \\; chars
DTSTART;TZID=Europe/Berlin:20130608T202501
DTEND;TZID=Europe/Berlin:20130608T212501
LOCATION:In\\, every text field
DESCRIPTION:Yes\\, all of them\\;
BEGIN:VALARM
TRIGGER;VALUE=DATE-TIME:20160101T000000Z
ACTION:AUDIO
ATTACH;FMTTYPE=audio/basic:ftp://example.com/pub/sounds/bell-01.aud
END:VALARM
END:VEVENT
END:VCALENDAR
"""

# Event with a tabbed line fold
cal26 = u"""
BEGIN:VCALENDAR
BEGIN:VEVENT
DTEND;TZID=Europe/Berlin:20120608T212500
SUMMARY:Name
DTSTART;TZID=Europe/Berlin:20120608T202500
LOCATION:MUC
SEQUENCE:0
UID:040000008200E00074C5B7101A82E0080000000050B9861DFE30D101000000000000000
	010000000DC18788D5CDAF947A99D8A91D04C601C
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

# All VTODO attributes beside duration.
cal27 = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
BEGIN:VTODO
DTSTAMP:20180218T154700Z
UID:Uid
COMPLETED:20180418T150000Z
CREATED:20180218T154800Z
DESCRIPTION:Lorem ipsum dolor sit amet.
DTSTART:20180218T164800Z
LOCATION:Earth
PERCENT-COMPLETE:0
PRIORITY:0
SUMMARY:Name
URL:https://www.example.com/cal.php/todo.ics
DURATION:PT10M
SEQUENCE:0
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM
END:VTODO
END:VCALENDAR
"""

# Test due.
cal28 = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
BEGIN:VTODO
DTSTAMP:20180218T154741Z
UID:Uid
DUE:20180218T164800Z
END:VTODO
END:VCALENDAR
"""

# Test error due and duration.
cal29 = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
BEGIN:VTODO
DTSTAMP:20180218T154741Z
UID:Uid
DURATION:PT10M
DUE:20180218T164800Z
END:VTODO
END:VCALENDAR
"""

cal30 = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
BEGIN:VTODO
DTSTAMP:20180218T154741Z
UID:Uid
DUE:20180218T164800Z
DURATION:PT10M
END:VTODO
END:VCALENDAR
"""

cal31 = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//Mac OS X 10.9//EN
BEGIN:VTODO
DTSTAMP:20180218T154741Z
UID:Uid
SUMMARY:Hello, \\n World\\; This is a backslash : \\\\ and another new \\N line
LOCATION:In\\, every text field
DESCRIPTION:Yes\\, all of them\\;
END:VTODO
END:VCALENDAR
"""

unfolded_cal2 = [
    'BEGIN:VCALENDAR',
    'BEGIN:VEVENT',
    'DTEND;TZID=Europe/Berlin:20120608T212500',
    'SUMMARY:Name',
    'DTSTART;TZID=Europe/Berlin:20120608T202500',
    'LOCATION:MUC',
    'SEQUENCE:0',
    'BEGIN:VALARM',
    'TRIGGER:-PT1H',
    'DESCRIPTION:Event reminder',
    'ACTION:DISPLAY',
    'END:VALARM',
    'END:VEVENT',
    'END:VCALENDAR',
]

unfolded_cal1 = [
    'BEGIN:VCALENDAR',
    'METHOD:PUBLISH',
    'VERSION:2.0',
    'X-WR-CALNAME:plop',
    'PRODID:-//Apple Inc.//Mac OS X 10.9//EN',
    'X-APPLE-CALENDAR-COLOR:#882F00',
    'X-WR-TIMEZONE:Europe/Brussels',
    'CALSCALE:GREGORIAN',
    'BEGIN:VTIMEZONE',
    'TZID:Europe/Brussels',
    'BEGIN:DAYLIGHT',
    'TZOFFSETFROM:+0100',
    'RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU',
    'DTSTART:19810329T020000',
    'TZNAME:UTC+2',
    'TZOFFSETTO:+0200',
    'END:DAYLIGHT',
    'BEGIN:STANDARD',
    'TZOFFSETFROM:+0200',
    'RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU',
    'DTSTART:19961027T030000',
    'TZNAME:UTC+1',
    'TZOFFSETTO:+0100',
    'END:STANDARD',
    'END:VTIMEZONE',
    'BEGIN:VEVENT',
    'CREATED:20131024T204716Z',
    'UID:ABBF2903-092F-4202-98B6-F757437A5B28',
    'DTEND;TZID=Europe/Brussels:20131029T113000',
    'TRANSP:OPAQUE',
    'SUMMARY:dfqsdfjqkshflqsjdfhqs fqsfhlqs dfkqsldfkqsdfqsfqsfqsfs',
    'DTSTART;TZID=Europe/Brussels:20131029T103000',
    'DTSTAMP:20131024T204741Z',
    'SEQUENCE:3',
    'DESCRIPTION:Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Sedvitae facilisis enim. Morbi blandit et lectus venenatis tristique. \
Donecsit amet egestas lacus. Donec ullamcorper, mi vitae congue dictum, \
quamdolor luctus augue, id cursus purus justo vel lorem. \
Ut feugiat enim ipsum, quis porta nibh ultricies congue. \
Pellentesque nisl mi, molestie idsem vel, vehicula nullam.',
    'END:VEVENT',
    'BEGIN:VTODO',
    'DTSTAMP:20180218T154700Z',
    'UID:Uid',
    'DESCRIPTION:Lorem ipsum dolor sit amet.',
    'PERCENT-COMPLETE:0',
    'PRIORITY:0',
    'SUMMARY:Name',
    'END:VTODO',
    'END:VCALENDAR',
]

unfolded_cal6 = ['DESCRIPTION:ab']

unfolded_cal21 = [
    'BEGIN:VCALENDAR',
    'BEGIN:VEVENT',
    'DTEND;TZID=Europe/Berlin:20120608T212500',
    'SUMMARY:Name',
    'DTSTART;TZID=Europe/Berlin:20120608T202500',
    'LOCATION:MUC',
    'SEQUENCE:0',
    'BEGIN:VALARM',
    'TRIGGER:-PT1H',
    'REPEAT:2',
    'DURATION:PT10M',
    'DESCRIPTION:Event reminder',
    'ACTION:DISPLAY',
    'END:VALARM',
    'END:VEVENT',
    'END:VCALENDAR',
]

unfolded_cal26 = [
    'BEGIN:VCALENDAR',
    'BEGIN:VEVENT',
    'DTEND;TZID=Europe/Berlin:20120608T212500',
    'SUMMARY:Name',
    'DTSTART;TZID=Europe/Berlin:20120608T202500',
    'LOCATION:MUC',
    'SEQUENCE:0',
    'UID:040000008200E00074C5B7101A82E0080000000050B9861DFE30D101000000000000000010000000DC18788D5CDAF947A99D8A91D04C601C',
    'BEGIN:VALARM',
    'TRIGGER:-PT1H',
    'DESCRIPTION:Event reminder',
    'ACTION:DISPLAY',
    'END:VALARM',
    'END:VEVENT',
    'END:VCALENDAR',
]
