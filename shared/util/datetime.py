"""To get utc Date and Time """

from datetime import datetime, date, timedelta



def utc_now():
    """return date and time in UTC standard"""
    date = datetime.utcnow()
    return date


def now():
    """
    @return: datetime object
    """
    return datetime.utcnow()


def date_to_datetime(date: date):
    """
    convert date object to datetime object
    @param date:
    @return: datetime object
    """
    return datetime.combine(date, datetime.max.time())


def date_today():
    return utc_now().replace(hour=0, minute=0, second=0, microsecond=0)


def now_delta(duration_mins):
    return utc_now() + timedelta(minutes=duration_mins)


def str_to_date(date_time_str):
    if date_time_str:
        return datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f%z')
    else:
        return None


def time_difference_in_seconds(date2, date1):
    if isinstance(date1, datetime) and isinstance(date2, datetime):
        date2 = date2.replace(tzinfo=None)
        date1 = date1.replace(tzinfo=None)
        return (date2 - date1).total_seconds()
    return None


def now_iso_format():
    return datetime.utcnow()


