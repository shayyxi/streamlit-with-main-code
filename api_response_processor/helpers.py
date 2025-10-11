from datetime import date, timedelta

from dateutil.relativedelta import relativedelta


def get_floorplans_from_units_availability_json(units_availability_and_pricing_response_json):
    if units_availability_and_pricing_response_json is None:
        return None
    result = units_availability_and_pricing_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        return result.get("Properties", {}).get("Property", [])[0].get("Floorplans", {}).get("Floorplan", [])
    return None

def get_leases_from_leases_response_json(leases_response_json):
    if leases_response_json is None:
        return None
    result = leases_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        return result.get("leases", {}).get("lease", [])
    return None

def get_leases_from_expiry_leases_response_json(expiry_leases_response_json):
    if expiry_leases_response_json is None:
        return None
    result = expiry_leases_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        return result.get("Leases", {}).get("Lease", [])
    return None

def get_units_from_units_availability_json(units_availability_and_pricing_response_json):
    if units_availability_and_pricing_response_json is None:
        return None
    result = units_availability_and_pricing_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        return result.get("ILS_Units", {}).get("Unit", {})
    return None

def get_leads_from_leads_response_json(leads_response_json):
    if leads_response_json is None:
        return None
    result = leads_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        if result.get("prospects"):
            first_container = result["prospects"][0]
            if first_container.get("prospect"):
                return first_container["prospect"]
    return None

def get_work_orders_from_maintenance_response_json(maintenance_response_json):
    if maintenance_response_json is None:
        return None
    result = maintenance_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        return result.get("workOrders", {}).get("workOrder", [])
    return None

def generate_start_and_end_dates_for_three_weeks() -> tuple[tuple[date, date], tuple[date, date], tuple[date, date]]:
    current_date = date.today()
    this_week_monday = current_date - timedelta(days=current_date.weekday())
    this_week = (this_week_monday, current_date)

    last_week_monday = this_week_monday - timedelta(weeks=1)
    last_week_sunday = this_week_monday - timedelta(days=1)
    last_week = (last_week_monday, last_week_sunday)

    week_before_last_monday = this_week_monday - timedelta(weeks=2)
    week_before_last_sunday = last_week_monday - timedelta(days=1)
    week_before_last = (week_before_last_monday, week_before_last_sunday)

    return this_week, last_week, week_before_last

def get_first_and_last_dates_for_three_months() -> tuple[tuple[date, date], tuple[date, date], tuple[date, date]]:
    today = date.today()

    # First day of the current month
    current_first = date(today.year, today.month, 1)

    # First day of next month
    if today.month == 12:
        next_first = date(today.year + 1, 1, 1)
    else:
        next_first = date(today.year, today.month + 1, 1)

    # First day of next-to-next month
    if today.month >= 11:
        ntn_month = today.month - 10
        ntn_year = today.year + 1
    else:
        ntn_month = today.month + 2
        ntn_year = today.year
    ntn_first = date(ntn_year, ntn_month, 1)

    # Last day of each month is one day before the first of the following month
    current_last = next_first - timedelta(days=1)
    next_last = ntn_first - timedelta(days=1)
    # Last of next-to-next month
    if ntn_month == 12:
        ntn_last = date(ntn_year + 1, 1, 1) - timedelta(days=1)
    else:
        ntn_last = date(ntn_year, ntn_month + 1, 1) - timedelta(days=1)

    current_month = (current_first, current_last)
    next_month = (next_first, next_last)
    ntn_month = (ntn_first, ntn_last)
    return current_month, next_month, ntn_month

def get_first_and_last_date_for_current_and_past_two_months() -> tuple[tuple[date, date], tuple[date, date], tuple[date, date]]:
    # Current date
    today = date.today()

    # First date of the current month
    first_date_current_month = today.replace(day=1)

    # First date of last month
    first_date_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)

    # Last date of last month
    last_date_last_month = today.replace(day=1) - timedelta(days=1)

    # First date of the month before last
    first_date_month_before_last = (first_date_last_month - timedelta(days=1)).replace(day=1)

    # Last date of the month before last
    last_date_month_before_last = first_date_last_month - timedelta(days=1)
    current_month = (first_date_current_month, today)
    last_month = (first_date_last_month, last_date_last_month)
    month_before_last = (first_date_month_before_last, last_date_month_before_last)
    return current_month, last_month, month_before_last

def get_last_and_month_before_last_5th():
    today = date.today()
    last_month = today - relativedelta(months=1)
    last_month_5th_date = last_month.replace(day=5)
    month_before_last = today - relativedelta(months=2)
    month_before_last_5th_date = month_before_last.replace(day=5)
    return last_month_5th_date, month_before_last_5th_date

def get_last_monday_date(d: date) -> date:
    return d - timedelta(days=d.weekday())