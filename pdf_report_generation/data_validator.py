from dataclasses import fields
from datetime import date, timedelta

from api_response_processor.data_classes import (PropertySummary,
                                                 UnitsSummary,
                                                 MaintenanceSummaryForThreeWeeks,
                                                 LeadsSummaryForThreeWeeks,
                                                 ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths,
                                                 ResidentRetentionSummaryForNoticeAndMTM,
                                                 RentSummaryForCurrentAndLastTwoMonths)


def sanitize_units_summary_dict(units_summary: dict[date, UnitsSummary]) -> dict[date, UnitsSummary]:
    first_date_key = next(iter(units_summary))
    last_two_sundays_date = get_last_two_sundays(first_date_key)
    if not last_two_sundays_date[0] in units_summary:
        units_summary[last_two_sundays_date[0]] = get_empty_units_summary_dataclass()
    if not last_two_sundays_date[1] in units_summary:
        units_summary[last_two_sundays_date[1]] = get_empty_units_summary_dataclass()
    for key, value in units_summary.items():
        units_summary[key] = replace_none_with_dash_in_dataclass(units_summary[key])
    return units_summary

def sanitize_property_summary_dict(property_summary: dict[date, PropertySummary]) -> dict[date, PropertySummary]:
    first_date_key = next(iter(property_summary))
    last_two_sundays_date = get_last_two_sundays(first_date_key)
    if not last_two_sundays_date[0] in property_summary:
        property_summary[last_two_sundays_date[0]] = get_empty_property_summary_dataclass()
    if not last_two_sundays_date[1] in property_summary:
        property_summary[last_two_sundays_date[1]] = get_empty_property_summary_dataclass()
    for key, value in property_summary.items():
        property_summary[key] = replace_none_with_dash_in_dataclass(property_summary[key])
    return property_summary

def sanitize_maintenance_summary(maintenance_summary: MaintenanceSummaryForThreeWeeks) -> MaintenanceSummaryForThreeWeeks:
    return replace_none_with_dash_in_dataclass(maintenance_summary)

def sanitize_leads_summary(leads_summary: LeadsSummaryForThreeWeeks) -> LeadsSummaryForThreeWeeks:
    return replace_none_with_dash_in_dataclass(leads_summary)

def sanitize_resident_retention_for_expiry_and_renewal_for_three_months_summary(resident_retention_summary: ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths) -> ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths:
    return replace_none_with_dash_in_dataclass(resident_retention_summary)

def sanitize_resident_retention_for_notice_and_mtm_summary(resident_retention_summary: ResidentRetentionSummaryForNoticeAndMTM) -> ResidentRetentionSummaryForNoticeAndMTM:
    return replace_none_with_dash_in_dataclass(resident_retention_summary)

def sanitize_rent_collection_summary(rent_collection_summary: RentSummaryForCurrentAndLastTwoMonths) -> RentSummaryForCurrentAndLastTwoMonths:
    return replace_none_with_dash_in_dataclass(rent_collection_summary)

def get_last_two_sundays(today_date: date) -> list[date]:
    reference_date = today_date - timedelta(days=1) if today_date.weekday() == 6 else today_date
    days_since_sunday = (reference_date.weekday() + 1) % 7
    last_sunday = reference_date - timedelta(days=days_since_sunday)
    second_last_sunday = last_sunday - timedelta(weeks=1)
    return [last_sunday, second_last_sunday]

def get_empty_property_summary_dataclass() -> PropertySummary:
    return PropertySummary(
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
    )

def get_empty_units_summary_dataclass() -> UnitsSummary:
    return UnitsSummary(
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
    )

def replace_none_with_dash_in_dataclass(instance):
    updated_values = {
        field.name: getattr(instance, field.name) if getattr(instance, field.name) is not None else "-"
        for field in fields(instance)
    }
    return type(instance)(**updated_values)