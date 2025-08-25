"""
API Response processor for calculating rent summary
"""
from datetime import date

from config import constants
from api_client import api_client
from api_response_processor import helpers, data_classes
from metrics_persistence import summary_table_name
from metrics_persistence.metrics_persistence import MetricsPersistence


def get_rent_summary(property_id, metrics_persistence: MetricsPersistence):
    """
    Method to calculate rent summary
    """
    (current_month_dates,
     last_month_dates,
     month_before_last_dates) = helpers.get_first_and_last_date_for_current_and_past_two_months()

    response_from_leases_api_with_current_and_notice_type = api_client.get_leases(property_id,
                                                                                  constants.LEASES_CURRENT_AND_NOTICE_TYPE_ID,
                                                                                  False, False, None)
    response_from_lease_artransactions_api = api_client.get_lease_artransactions(property_id,
                                                                                 current_month_dates[0].strftime("%m/%d/%Y"),
                                                                                 current_month_dates[1].strftime("%m/%d/%Y"))

    total_rent_billed = get_total_amount_of_rent_billed(response_from_leases_api_with_current_and_notice_type)
    total_rent_collected, rent_collected_percentage = get_rent_collected_total_and_percentage(response_from_lease_artransactions_api, total_rent_billed)

    rent_summary = data_classes.RentSummaryForPersistence(
        total_rent_billed,
    )

    metrics_persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(property_id, rent_summary, summary_table_name.SummaryTableName.RENT_SUMMARY.value)

    last_month_rent_summary, month_before_last_rent_summary = get_previous_two_months_rent_summary(property_id,
                                                                                                   metrics_persistence,
                                                                                                   last_month_dates,
                                                                                                   month_before_last_dates)
    print("Calculated the rent summary for " + f"{property_id}")
    return data_classes.RentSummaryForCurrentAndLastTwoMonths(
        current_month_dates[0].strftime("%m/%d/%Y"),
        current_month_dates[1].strftime("%m/%d/%Y"),
        total_rent_billed,
        total_rent_collected,
        rent_collected_percentage,

        last_month_dates[0].strftime("%m/%d/%Y"),
        last_month_dates[1].strftime("%m/%d/%Y"),
        last_month_rent_summary[0],
        last_month_rent_summary[1],
        last_month_rent_summary[2],

        month_before_last_dates[0].strftime("%m/%d/%Y"),
        month_before_last_dates[1].strftime("%m/%d/%Y"),
        month_before_last_rent_summary[0],
        month_before_last_rent_summary[1],
        month_before_last_rent_summary[2],
    )

def get_previous_two_months_rent_summary(property_id,
                                         metrics_persistence: MetricsPersistence,
                                         last_month_dates: tuple[date, date],
                                         month_before_last_dates: tuple[date, date]):
    """
    Get previous two months rent summary
    """
    previous_rent_billed_summary = metrics_persistence.get_property_metrics(property_id,
                                                                            summary_table_name.SummaryTableName.RENT_SUMMARY.value)
    last_month_rent_billed = None
    last_month_rent_collected = None
    last_month_rent_collected_percentage = None

    month_before_last_rent_billed = None
    month_before_last_rent_collected = None
    month_before_last_rent_collected_percentage = None

    if len(previous_rent_billed_summary) == 0:
        return (None, None, None), (None, None, None)

    last_month_5th, month_before_last_5th = helpers.get_last_and_month_before_last_5th()

    if last_month_5th in previous_rent_billed_summary:
        last_month_rent_billed = previous_rent_billed_summary[last_month_5th].total_rent_billed
        response_from_lease_artransactions_api_for_last_month = api_client.get_lease_artransactions(property_id,
                                                                       last_month_dates[0].strftime("%m/%d/%Y"),
                                                                       last_month_dates[1].strftime("%m/%d/%Y"))
        (last_month_rent_collected,
         last_month_rent_collected_percentage) = get_rent_collected_total_and_percentage(response_from_lease_artransactions_api_for_last_month,
                                                                                                                  last_month_rent_billed)

    if month_before_last_5th in previous_rent_billed_summary:
        month_before_last_rent_billed = previous_rent_billed_summary[month_before_last_5th].total_rent_billed
        response_from_lease_artransactions_api_for_month_before_last = api_client.get_lease_artransactions(property_id,
                                                                                                           month_before_last_dates[0].strftime("%m/%d/%Y"),
                                                                                                           month_before_last_dates[1].strftime("%m/%d/%Y"))
        (month_before_last_rent_collected,
         month_before_last_rent_collected_percentage) = get_rent_collected_total_and_percentage(response_from_lease_artransactions_api_for_month_before_last,
                                                                                                                                month_before_last_rent_billed)
    return ((last_month_rent_billed, last_month_rent_collected, last_month_rent_collected_percentage),
            (month_before_last_rent_billed, month_before_last_rent_collected, month_before_last_rent_collected_percentage))

def get_total_amount_of_rent_billed(leases_response_with_current_and_notice_status_json):
    """
    method for calculating the amount of rent billed to a property
    """
    leases = helpers.get_leases_from_leases_response_json(leases_response_with_current_and_notice_status_json)
    if leases is None:
        return None

    total_amount = 0.0
    for lease in leases:
        charges = lease.get("scheduledCharges", {}).get("scheduledCharge", [])
        for charge in charges:
            chargeType = charge.get("chargeType", "")
            if chargeType == "Security Deposit":
                continue
            amount = charge.get("amount", "0.00")
            total_amount += float(amount)
    return round(total_amount, 2)

def get_rent_collected_total_and_percentage(leases_artransactions_response_json, total_rent_billed):
    """
    method for calculating the percentage of rent collected from a property
    """
    if leases_artransactions_response_json is None or total_rent_billed is None or not total_rent_billed > 0:
        return None, None

    result = leases_artransactions_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        leases = result.get("leases", {}).get("lease", [])
    else:
        return None, None

    total_due_amount = 0.0
    for lease in leases:
        ledger = lease.get("ledgers", {}).get("ledger", [])[0]
        total_due_amount += ledger.get("balance", "0.00")

    return (total_rent_billed-total_due_amount,
            str(round(((total_rent_billed-total_due_amount) / total_rent_billed) * 100, 2)) + "%")
