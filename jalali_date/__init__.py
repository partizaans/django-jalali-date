from django.conf import settings
from pytz import timezone
import jdatetime


def datet2jalali(g_date):
    return jdatetime.date.fromgregorian(date=g_date) if g_date else None


def datetime2jalali(g_date):
    if g_date is None:
        return None

    if settings.USE_TZ:
        g_date = g_date.astimezone(timezone(settings.TIME_ZONE))

    return jdatetime.datetime.fromgregorian(datetime=g_date)
