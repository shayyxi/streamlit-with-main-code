from dataclasses import asdict
from datetime import datetime, date

from api_response_processor.data_classes import (PropertySummary,
                                                 UnitsSummary,
                                                 MaintenanceSummaryForThreeWeeks,
                                                 LeadsSummaryForThreeWeeks)
from pdf_report_generation import data_validator
from freezegun import freeze_time

def test_get_last_two_sundays():
    date_str = "2025-07-29"
    last_sunday = "2025-07-27"
    second_last_sunday = "2025-07-20"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    last_two_sundays = data_validator.get_last_two_sundays(date_obj)
    assert len(last_two_sundays) == 2
    assert last_two_sundays[0] == datetime.strptime(last_sunday, "%Y-%m-%d").date()
    assert last_two_sundays[1] == datetime.strptime(second_last_sunday, "%Y-%m-%d").date()
    date_str = "2025-06-28"
    last_sunday = "2025-06-22"
    second_last_sunday = "2025-06-15"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    last_two_sundays = data_validator.get_last_two_sundays(date_obj)
    assert len(last_two_sundays) == 2
    assert last_two_sundays[0] == datetime.strptime(last_sunday, "%Y-%m-%d").date()
    assert last_two_sundays[1] == datetime.strptime(second_last_sunday, "%Y-%m-%d").date()

def test_replace_none_with_dash_in_dataclass():
    property_summary = PropertySummary(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    property_summary_with_dashes = data_validator.replace_none_with_dash_in_dataclass(property_summary)
    assert all(value is not None for value in asdict(property_summary_with_dashes).values()) is True
    property_summary = PropertySummary(
        "-",
        "-",
        "-",
        None,
        None,
        None,
        None,
        None,
    )
    property_summary_with_dashes = data_validator.replace_none_with_dash_in_dataclass(property_summary)
    assert all(value is not None for value in asdict(property_summary_with_dashes).values()) is True

@freeze_time("2025-07-29")
def test_sanitize_property_summary_dict():
    # case1: property summary has one date
    # case2: property summary has two dates
    # case3: property summary has three dates
    property_summary_dc = PropertySummary(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    property_summary = {
        date(2025, 7, 29): property_summary_dc
    }
    sanitized_summary = data_validator.sanitize_property_summary_dict(property_summary)
    assert len(sanitized_summary) is 3
    assert date(2025, 7, 27) in sanitized_summary.keys()
    assert date(2025, 7, 20) in sanitized_summary.keys()
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 29)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 27)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 20)]).values()) is True
    property_summary_dc = PropertySummary(
        100,
        200,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    property_summary = {
        date(2025, 7, 29): property_summary_dc
    }
    sanitized_summary = data_validator.sanitize_property_summary_dict(property_summary)
    assert len(sanitized_summary) is 3
    assert date(2025, 7, 27) in sanitized_summary.keys()
    assert date(2025, 7, 20) in sanitized_summary.keys()
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 29)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 27)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 20)]).values()) is True
    assert sanitized_summary[date(2025, 7, 29)].total_units == 100
    assert sanitized_summary[date(2025, 7, 29)].total_rentable_units == 200

@freeze_time("2025-07-29")
def test_sanitize_units_summary_dict():
    units_summary_dc = UnitsSummary(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    units_summary = {
        date(2025, 7, 29): units_summary_dc
    }
    sanitized_summary = data_validator.sanitize_units_summary_dict(units_summary)
    assert len(sanitized_summary) is 3
    assert date(2025, 7, 27) in sanitized_summary.keys()
    assert date(2025, 7, 20) in sanitized_summary.keys()
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 29)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 27)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 20)]).values()) is True
    units_summary_dc = UnitsSummary(
        100,
        200,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    units_summary = {
        date(2025, 7, 29): units_summary_dc
    }
    sanitized_summary = data_validator.sanitize_units_summary_dict(units_summary)
    assert len(sanitized_summary) is 3
    assert date(2025, 7, 27) in sanitized_summary.keys()
    assert date(2025, 7, 20) in sanitized_summary.keys()
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 29)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 27)]).values()) is True
    assert all(value is not None for value in asdict(sanitized_summary[date(2025, 7, 20)]).values()) is True
    assert sanitized_summary[date(2025, 7, 29)].count_of_occupied_units == 100
    assert sanitized_summary[date(2025, 7, 29)].count_of_on_notice_rented_units == 200

def test_sanitize_maintenance_summary_table():
    maintenance_summary_table = MaintenanceSummaryForThreeWeeks(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    sanitized_maintenance_summary_table = data_validator.sanitize_maintenance_summary(maintenance_summary_table)
    assert all(value is not None for value in asdict(sanitized_maintenance_summary_table).values()) is True

def test_sanitize_leads_summary_table():
    leads_summary_table = LeadsSummaryForThreeWeeks(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    sanitized_leads_summary_table = data_validator.sanitize_leads_summary(leads_summary_table)
    assert all(value is not None for value in asdict(sanitized_leads_summary_table).values()) is True