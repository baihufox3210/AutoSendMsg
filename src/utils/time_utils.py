import calendar
from datetime import datetime, timedelta

def getTime(dt: float, days: list):
    dt = datetime.fromtimestamp(dt)

    return (
        dt + timedelta(
            days = min(
                (d - dt.weekday()) % 7 or 7 for d in days
            )
        )
    ).timestamp()

def getWeeklyTime(dt: float, frequency: int):
    dt = datetime.fromtimestamp(dt) + timedelta(weeks=frequency)

    return dt.timestamp()

def getMonthlyTime(dt: float, day: int, frequency: int):
    dt = datetime.fromtimestamp(dt)

    year = dt.year + (dt.month + frequency - 1) // 12
    month = (dt.month + frequency - 1) % 12 + 1

    return datetime(
        year,
        month,
        min(day, calendar.monthrange(year, month)[1]),
        dt.hour,
        dt.minute,
        dt.second
    ).timestamp()