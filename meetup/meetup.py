import calendar
import datetime
import re


WEEKDAYS = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}


class MeetupDayException(Exception):
    pass


def is_teenth(descriptor):
    return descriptor == 'teenth'


def is_last(descriptor):
    return descriptor == 'last'


def is_nth(descriptor):
    return re.match(r'^[1-5](st|nd|rd|th)$', descriptor)


def weekdays_diff(begin, end):
    return (end - begin) % 7


def parse_nth(descriptor):
    return int(descriptor[0])


def get_teenth_day(year, month, weekday):
    first_teenth_day = 13
    teenth = datetime.date(year=year, month=month, day=first_teenth_day)
    begin = teenth.weekday()
    end = WEEKDAYS.get(weekday)
    diff = weekdays_diff(begin, end)
    return teenth + datetime.timedelta(days=diff)


def get_last_day(year, month, weekday):
    _, last_day = calendar.monthrange(year, month)
    last = datetime.date(year=year, month=month, day=last_day)
    begin = WEEKDAYS.get(weekday)
    end = last.weekday()
    diff = weekdays_diff(begin, end)
    return last - datetime.timedelta(days=diff)


def get_nth_day(year, month, weekday, nth):
    first = datetime.date(year=year, month=month, day=1)
    begin = first.weekday()
    end = WEEKDAYS.get(weekday)
    diff = weekdays_diff(begin, end)
    nth_day = (nth - 1) * 7 + diff + 1

    try:
        return datetime.date(year=year, month=month, day=nth_day)
    except ValueError:
        raise MeetupDayException('nth day is out of range for month')


def meetup_day(year, month, day, descriptor):
    if is_teenth(descriptor):
        return get_teenth_day(year, month, day)

    elif is_last(descriptor):
        return get_last_day(year, month, day)

    elif is_nth(descriptor):
        nth = parse_nth(descriptor)
        return get_nth_day(year, month, day, nth)

    raise MeetupDayException('uknown descriptor')
