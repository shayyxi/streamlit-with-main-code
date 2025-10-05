"""
API Response Processor for generating property summary data
"""
from api_response_processor import helpers, api_response_processor_units_summary, data_classes
from config import constants
from api_client import api_client

def get_property_summary(property_id):
    """
    method for calling the APIs, providing the API responses to process,
    and giving back the property summary data
    """
    response_from_property_units_api = api_client.get_property_units(property_id)
    response_from_units_availability_and_pricing_api = api_client.get_units_availability_and_pricing(property_id)
    response_from_leases_api_with_notice_type = api_client.get_leases(property_id,
                                                                  constants.LEASES_NOTICE_TYPE_ID, False, False,
                                                                  None)
    response_from_leases_api_with_past_type = api_client.get_leases(property_id,
                                                                constants.LEASES_PAST_TYPE_ID, True, False, True)

    api_responses = data_classes.ApiResponsesForGeneratingPropertySummary(
        response_from_property_units_api,
        response_from_units_availability_and_pricing_api,
        response_from_leases_api_with_notice_type,
        response_from_leases_api_with_past_type
    )
    property_summary = generate_property_summary(api_responses)
    print("Calculated the property summary for " + f"{property_id}")
    return property_summary

def generate_property_summary(api_response_json: data_classes.ApiResponsesForGeneratingPropertySummary):
    """
    method for calling the processor methods,
    and giving back the property summary data
    """
    total_units = get_count_of_all_units(api_response_json.response_from_property_units_api)
    total_rentable_units = get_count_of_rentable_units(api_response_json.response_from_units_availability_and_pricing_api)
    excluded_units = get_count_of_excluded_units(total_units, total_rentable_units)
    occupied_units_percentage = get_occupied_units_percentage(api_response_json.response_from_units_availability_and_pricing_api, total_rentable_units)
    leased_units_percentage = get_leased_units_percentage(api_response_json.response_from_units_availability_and_pricing_api, total_rentable_units)
    trend_percentage = get_trend_percentage(api_response_json.response_from_units_availability_and_pricing_api,total_rentable_units)
    evictions_and_skips_occurred_for_current_month = get_count_of_occurred_evictions_and_skips(api_response_json.response_from_leases_api_with_past_type)
    property_summary = data_classes.PropertySummary(
        total_units,
        total_rentable_units,
        excluded_units,
        occupied_units_percentage,
        leased_units_percentage,
        trend_percentage,
        evictions_and_skips_occurred_for_current_month
    )
    return property_summary

def get_trend_percentage(units_availability_and_pricing_response_json, total_rentable_units):
    """
    method for calculating the trend percentage
    """
    count_of_occupied_units = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(
        units_availability_and_pricing_response_json, constants.UNIT_OCCUPIED_NOTICE_STATUS, None)
    count_of_on_notice_not_rented_units = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(
        units_availability_and_pricing_response_json, constants.UNIT_NOTICE_STATUS, True)
    count_of_vacant_rented_units = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(
        units_availability_and_pricing_response_json, constants.UNIT_VACANT_STATUS, False)
    if (count_of_occupied_units is None or
    count_of_on_notice_not_rented_units is None or
    total_rentable_units is None or
    total_rentable_units == 0 or
    count_of_vacant_rented_units is None):
        return None
    trend_percentage = ((count_of_occupied_units - count_of_on_notice_not_rented_units + count_of_vacant_rented_units) / total_rentable_units) * 100
    return str(round(trend_percentage, 2)) + "%"

def get_leased_units_percentage(units_availability_and_pricing_response_json, total_rentable_units):
    """
    method for calculating the percentage of leased units in a property
    """
    count_of_occupied_units = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(
        units_availability_and_pricing_response_json, constants.UNIT_OCCUPIED_NOTICE_STATUS, None)
    count_of_vacant_rented_units = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(
        units_availability_and_pricing_response_json, constants.UNIT_VACANT_STATUS, False)
    if count_of_occupied_units is None or total_rentable_units is None or total_rentable_units == 0 or count_of_vacant_rented_units is None:
        return None
    leased_units_percentage = ((count_of_occupied_units + count_of_vacant_rented_units) / total_rentable_units) * 100
    return str(round(leased_units_percentage, 2)) + "%"

def get_count_of_excluded_units(total_units, total_rentable_units):
    """
    method for calculating the number of excluded units
    """
    if total_units is not None and total_rentable_units is not None:
        return total_units - total_rentable_units
    return None


def get_list_of_properties(properties_response_json):
    """
    method for getting the list of propertyIDs and their names
    """
    if properties_response_json is None:
        return {}

    result = properties_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        properties = result.get("PhysicalProperty", {}).get("Property", [])
    else:
        return {}

    properties_id_and_name = {}
    for property_item in properties:
        try:
            property_id = property_item.get("PropertyID")
        except (KeyError, IndexError):
            continue

        try:
            property_name = property_item.get("MarketingName")
        except (KeyError, IndexError):
            continue
        properties_id_and_name[property_id] = property_name
    return properties_id_and_name

def get_count_of_all_units(property_units_response_json):
    """
    method for calculating the total number of units in a property
    """
    if property_units_response_json is None:
        return None

    result = property_units_response_json.get("response", {}).get("result", {})
    if isinstance(result, dict) and len(result) > 0:
        total_units = result.get("properties", {}).get("property", [])[0].get("unitCount", 0)
    else:
        return None

    return total_units

def get_count_of_rentable_units(units_availability_and_pricing_response_json):
    """
    method for calculating the number of rentable units in a property
    """
    floorplans = helpers.get_floorplans_from_units_availability_json(units_availability_and_pricing_response_json)
    if floorplans is None:
        return None

    list_of_rentable_units = [floorplan.get("UnitCount") for floorplan in floorplans]
    total_rentable_units = sum(int(num) for num in list_of_rentable_units if num.strip() != "")
    return total_rentable_units

def get_count_of_preleased_units(units_availability_and_pricing_response_json, total_units):
    """
    method for calculating the number of preleased units in a property
    """
    floorplans = helpers.get_floorplans_from_units_availability_json(units_availability_and_pricing_response_json)
    if floorplans is None or total_units is None:
        return None

    list_of_available_units = [floorplan.get("UnitsAvailable") for floorplan in floorplans]
    total_available_units = sum(int(num) for num in list_of_available_units if num.strip() != "")
    return total_units - total_available_units

def get_occupied_units_percentage(units_availability_and_pricing_response_json, total_rentable_units):
    """
    method for calculating the percentage of occupied units in a property
    """
    count_of_occupied_units = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(units_availability_and_pricing_response_json, constants.UNIT_OCCUPIED_NOTICE_STATUS, None)
    if count_of_occupied_units is None or total_rentable_units is None or total_rentable_units == 0:
        return None
    occupied_units_percentage = (count_of_occupied_units / total_rentable_units) * 100
    return str(round(occupied_units_percentage, 2)) + "%"

def get_count_of_occurred_evictions_and_skips(leases_response_with_past_status_json):
    """
    method for calculating the evictions and skips occurred for a property
    """
    leases = helpers.get_leases_from_leases_response_json(leases_response_with_past_status_json)
    if leases is None:
        return None
    evictions_and_skips = 0
    for lease in leases:
        lease_sub_status = lease.get("leaseSubStatus", "")
        if "eviction" in lease_sub_status.lower() or "skip" in lease_sub_status.lower():
            evictions_and_skips += 1
    return evictions_and_skips
