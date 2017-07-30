from datetime import datetime


def get_days(begin_date, end_date):
    """获得2个日期间的天数"""
    return (end_date - begin_date).days


def to_datetime(date):
    """日期转时间 date ==> datetime"""
    return datetime(date.year, date.month, date.day)


def get_current_date_str():
    dt = datetime.now()
    return dt.strftime('%Y-%m-%d')
