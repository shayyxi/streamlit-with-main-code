from freezegun import freeze_time
from datetime import date

from api_response_processor import helpers

@freeze_time("2025-07-29")
def test_generate_start_and_end_dates_for_three_weeks():
    this_week, last_week, week_before_last = helpers.generate_start_and_end_dates_for_three_weeks()
    assert this_week[0] == date(2025, 7, 28)
    assert this_week[1] == date(2025, 7, 29)
    assert last_week[0] == date(2025, 7, 21)
    assert last_week[1] == date(2025, 7, 27)
    assert week_before_last[0] == date(2025, 7, 14)
    assert week_before_last[1] == date(2025, 7, 20)

@freeze_time("2025-07-28")
def test_generate_start_and_end_dates_for_three_weeks_when_it_is_monday():
    this_week, last_week, week_before_last = helpers.generate_start_and_end_dates_for_three_weeks()
    assert this_week[0] == date(2025, 7, 28)
    assert this_week[1] == date(2025, 7, 28)
    assert last_week[0] == date(2025, 7, 21)
    assert last_week[1] == date(2025, 7, 27)
    assert week_before_last[0] == date(2025, 7, 14)
    assert week_before_last[1] == date(2025, 7, 20)

@freeze_time("2025-10-10")
def test_get_first_and_last_dates_for_three_months():
    current_month, next_month, ntn_month = helpers.get_first_and_last_dates_for_three_months()
    assert current_month[0] == date(2025, 10, 1)
    assert current_month[1] == date(2025, 10, 31)
    assert next_month[0] == date(2025, 11, 1)
    assert next_month[1] == date(2025, 11, 30)
    assert ntn_month[0] == date(2025, 12, 1)
    assert ntn_month[1] == date(2025, 12, 31)

@freeze_time("2025-11-10")
def test_get_first_and_last_dates_for_three_months():
    current_month, next_month, ntn_month = helpers.get_first_and_last_dates_for_three_months()
    assert current_month[0] == date(2025, 11, 1)
    assert current_month[1] == date(2025, 11, 30)
    assert next_month[0] == date(2025, 12, 1)
    assert next_month[1] == date(2025, 12, 31)
    assert ntn_month[0] == date(2026, 1, 1)
    assert ntn_month[1] == date(2026, 1, 31)

@freeze_time("2025-12-10")
def test_get_first_and_last_dates_for_three_months():
    current_month, next_month, ntn_month = helpers.get_first_and_last_dates_for_three_months()
    assert current_month[0] == date(2025, 12, 1)
    assert current_month[1] == date(2025, 12, 31)
    assert next_month[0] == date(2026, 1, 1)
    assert next_month[1] == date(2026, 1, 31)
    assert ntn_month[0] == date(2026, 2, 1)
    assert ntn_month[1] == date(2026, 2, 28)

@freeze_time("2025-12-10")
def test_get_first_and_last_date_for_past_three_months():
    current_month, last_month, month_before_last = helpers.get_first_and_last_date_for_current_and_past_two_months()
    assert current_month[0] == date(2025, 12, 1)
    assert current_month[1] == date(2025, 12, 10)
    assert last_month[0] == date(2025, 11, 1)
    assert last_month[1] == date(2025, 11, 30)
    assert month_before_last[0] == date(2025, 10, 1)
    assert month_before_last[1] == date(2025, 10, 31)

@freeze_time("2025-11-10")
def test_get_first_and_last_date_for_past_three_months():
    current_month, last_month, month_before_last = helpers.get_first_and_last_date_for_current_and_past_two_months()
    assert current_month[0] == date(2025, 11, 1)
    assert current_month[1] == date(2025, 11, 10)
    assert last_month[0] == date(2025, 10, 1)
    assert last_month[1] == date(2025, 10, 31)
    assert month_before_last[0] == date(2025, 9, 1)
    assert month_before_last[1] == date(2025, 9, 30)

@freeze_time("2026-01-05")
def test_get_first_and_last_date_for_past_three_months():
    current_month, last_month, month_before_last = helpers.get_first_and_last_date_for_current_and_past_two_months()
    assert current_month[0] == date(2026, 1, 1)
    assert current_month[1] == date(2026, 1, 5)
    assert last_month[0] == date(2025, 12, 1)
    assert last_month[1] == date(2025, 12, 31)
    assert month_before_last[0] == date(2025, 11, 1)
    assert month_before_last[1] == date(2025, 11, 30)

@freeze_time("2026-01-05")
def test_get_last_and_month_before_last_5th():
    last_month_5th, month_before_last_5th = helpers.get_last_and_month_before_last_5th()
    assert last_month_5th == date(2025, 12, 5)
    assert month_before_last_5th == date(2025, 11, 5)

@freeze_time("2026-02-05")
def test_get_last_and_month_before_last_5th():
    last_month_5th, month_before_last_5th = helpers.get_last_and_month_before_last_5th()
    assert last_month_5th == date(2026, 1, 5)
    assert month_before_last_5th == date(2025, 12, 5)