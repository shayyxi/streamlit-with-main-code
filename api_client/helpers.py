"""
Helper methods for api clients, mainly related to date
"""
import datetime, calendar

def get_previous_months_date_for_maintenance_data(current_date: datetime.date):
    """
    Method for generating previous 3 months date for maintenance data.
    """
    month_3_ago = current_date.month - 3
    year_3_ago = current_date.year
    if month_3_ago <= 0:
        month_3_ago += 12
        year_3_ago -= 1
    from_date = f"{month_3_ago:02d}/01/{year_3_ago}"

    month_1_ago = current_date.month - 1
    year_1_ago = current_date.year
    if month_1_ago <= 0:
        month_1_ago += 12
        year_1_ago -= 1
    last_day = calendar.monthrange(year_1_ago, month_1_ago)[1]
    to_date = f"{month_1_ago:02d}/{last_day:02d}/{year_1_ago}"
    return from_date, to_date
