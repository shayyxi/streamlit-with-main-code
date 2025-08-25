"""
API response processor to calculate units summary
"""
from api_response_processor import helpers, data_classes
from config import constants
from api_client import api_client

def get_units_summary(property_id):
    """
    method for calling the APIs, providing the API responses to process,
    and giving back the units summary data
    """
    response_from_units_availability_and_pricing_api = api_client.get_units_availability_and_pricing(property_id)

    current_week_dates, _, _, = helpers.generate_start_and_end_dates_for_three_weeks()
    response_from_leases_api_with_move_in_date = api_client.get_leases_with_move_in_date_range(property_id,
                                                                                               current_week_dates[0].strftime("%m/%d/%Y"),
                                                                                               current_week_dates[1].strftime("%m/%d/%Y"))

    response_from_leases_api_with_move_out_date = api_client.get_leases_with_move_out_date_range(property_id,
                                                                                                 current_week_dates[0].strftime("%m/%d/%Y"),
                                                                                                 current_week_dates[1].strftime("%m/%d/%Y"))

    api_responses = data_classes.ApiResponsesForGeneratingUnitsSummary(response_from_units_availability_and_pricing_api,
                                                                       response_from_leases_api_with_move_in_date,
                                                                       response_from_leases_api_with_move_out_date)
    units_summary = generate_units_summary(api_responses)
    print("Calculated the units summary for " + f"{property_id}")
    return units_summary

def generate_units_summary(api_response_json: data_classes.ApiResponsesForGeneratingUnitsSummary):
    """
    method for generating the units summary data
    """
    count_of_occupied_units = get_count_of_units_with_matching_status_and_availability(api_response_json.response_from_units_availability_and_pricing_api, constants.UNIT_OCCUPIED_NOTICE_STATUS, None)
    count_of_on_notice_preleased_units = get_count_of_units_with_matching_status_and_availability(api_response_json.response_from_units_availability_and_pricing_api, constants.UNIT_NOTICE_STATUS, False)
    count_of_on_notice_not_preleased_units = get_count_of_units_with_matching_status_and_availability(api_response_json.response_from_units_availability_and_pricing_api, constants.UNIT_NOTICE_STATUS, True)

    count_of_vacant_units = get_count_of_units_with_matching_status_and_availability(api_response_json.response_from_units_availability_and_pricing_api, constants.UNIT_VACANT_STATUS, None)
    count_of_vacant_preleased_units = get_count_of_units_with_matching_status_and_availability(api_response_json.response_from_units_availability_and_pricing_api, constants.UNIT_VACANT_STATUS, False)
    count_of_vacant_not_preleased_units = get_count_of_units_with_matching_status_and_availability(api_response_json.response_from_units_availability_and_pricing_api, constants.UNIT_VACANT_STATUS, True)

    count_of_total_move_ins = len(helpers.get_leases_from_leases_response_json(api_response_json.response_from_leases_api_with_move_in_date))
    count_of_total_move_out = len(helpers.get_leases_from_leases_response_json(api_response_json.response_from_leases_api_with_move_out_date))

    units_summary = data_classes.UnitsSummary(
        count_of_occupied_units,
        count_of_on_notice_preleased_units,
        count_of_on_notice_not_preleased_units,
        count_of_vacant_units,
        count_of_vacant_preleased_units,
        count_of_vacant_not_preleased_units,
        count_of_total_move_ins,
        count_of_total_move_out,
    )
    return units_summary

def get_count_of_units_with_matching_status_and_availability(units_availability_and_pricing_response_json, status_keywords, is_available):
    """
    method for giving back the units based on the status and availability
    """
    list_of_units = helpers.get_units_from_units_availability_json(units_availability_and_pricing_response_json)
    if list_of_units is None:
        return None
    total_count_of_units_with_matching_status_and_availability = 0
    for unit in list_of_units.values():
        status = unit.get("@attributes", {}).get("Status", "")
        availability = unit.get("@attributes", {}).get("Availability", "")
        if len(status_keywords) > 0:
            for status_keyword in status_keywords:
                if status_keyword in status:
                    if is_available is None:
                        total_count_of_units_with_matching_status_and_availability += 1
                    elif is_available and 'Available' == availability:
                        total_count_of_units_with_matching_status_and_availability += 1
                    elif not is_available and 'Not Available' == availability:
                        total_count_of_units_with_matching_status_and_availability += 1
            continue
        if is_available and "Available" == availability:
            total_count_of_units_with_matching_status_and_availability += 1
        elif not is_available and "Not Available" == availability:
            total_count_of_units_with_matching_status_and_availability += 1
    return total_count_of_units_with_matching_status_and_availability
