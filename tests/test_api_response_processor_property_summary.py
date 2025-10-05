from config import constants_for_testing
from api_response_processor import api_response_processor_property_summary, data_classes

def test_generate_property_summary():
    api_responses = data_classes.ApiResponsesForGeneratingPropertySummary(
        constants_for_testing.PROPERTY_UNITS_RESPONSE_JSON,
        constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING,
        constants_for_testing.LEASES_RESPONSE_JSON,
        constants_for_testing.LEASES_RESPONSE_JSON
    )
    property_summary = api_response_processor_property_summary.generate_property_summary(api_responses)
    assert property_summary.total_units == 153
    assert property_summary.total_rentable_units == 150
    assert property_summary.excluded_units == property_summary.total_units - property_summary.total_rentable_units
    assert property_summary.occupied_units_percentage == "4.67%"
    assert property_summary.leased_units_percentage == "4.67%"
    assert property_summary.evictions_and_skips_occurred_for_current_month == 4

def test_get_leased_units_percentage():
    preleased_units_percentage = api_response_processor_property_summary.get_leased_units_percentage(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_PROPERTY_SUMMARY_TESTING, 200)
    assert preleased_units_percentage == "3.0%"
    preleased_units_percentage = api_response_processor_property_summary.get_leased_units_percentage(None, 200)
    assert preleased_units_percentage is None
    preleased_units_percentage = api_response_processor_property_summary.get_leased_units_percentage(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_PROPERTY_SUMMARY_TESTING, None)
    assert preleased_units_percentage is None
    preleased_units_percentage = api_response_processor_property_summary.get_leased_units_percentage(None, None)
    assert preleased_units_percentage is None
    preleased_units_percentage = api_response_processor_property_summary.get_leased_units_percentage(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_PROPERTY_SUMMARY_TESTING, 0)
    assert preleased_units_percentage is None

def test_get_excluded_units():
    excluded_units = api_response_processor_property_summary.get_count_of_excluded_units(153, 150)
    assert excluded_units == 3
    excluded_units = api_response_processor_property_summary.get_count_of_excluded_units(None, 150)
    assert excluded_units is None
    excluded_units = api_response_processor_property_summary.get_count_of_excluded_units(150, None)
    assert excluded_units is None
    excluded_units = api_response_processor_property_summary.get_count_of_excluded_units(None, None)
    assert excluded_units is None

def test_get_total_units():
    total_units = api_response_processor_property_summary.get_count_of_all_units(constants_for_testing.PROPERTY_UNITS_RESPONSE_JSON)
    assert total_units == 153
    total_units = api_response_processor_property_summary.get_count_of_all_units(constants_for_testing.EMPTY_RESPONSE_JSON)
    assert total_units is None
    total_units = api_response_processor_property_summary.get_count_of_all_units(constants_for_testing.BAD_RESPONSE_JSON)
    assert total_units is None
    total_units = api_response_processor_property_summary.get_count_of_all_units(None)
    assert total_units is None


def test_get_total_rentable_units():
    total_rentable_units = api_response_processor_property_summary.get_count_of_rentable_units(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING)
    assert total_rentable_units == 150
    total_rentable_units = api_response_processor_property_summary.get_count_of_rentable_units(constants_for_testing.EMPTY_RESPONSE_JSON)
    assert total_rentable_units is None
    total_rentable_units = api_response_processor_property_summary.get_count_of_rentable_units(constants_for_testing.BAD_RESPONSE_JSON)
    assert total_rentable_units is None
    total_rentable_units = api_response_processor_property_summary.get_count_of_rentable_units(None)
    assert total_rentable_units is None

def test_get_list_of_properties():
    list_of_properties = api_response_processor_property_summary.get_list_of_properties(constants_for_testing.PROPERTIES_RESPONSE_JSON)
    correct_list_of_properties = {
        1234: "abc",
        2345: "def",
        4567: "ghi"
    }
    assert list_of_properties == correct_list_of_properties
    list_of_properties = api_response_processor_property_summary.get_list_of_properties(None)
    assert list_of_properties == []
    list_of_properties = api_response_processor_property_summary.get_list_of_properties(constants_for_testing.EMPTY_RESPONSE_JSON)
    assert list_of_properties == []
    list_of_properties = api_response_processor_property_summary.get_list_of_properties(constants_for_testing.BAD_RESPONSE_JSON)
    assert list_of_properties == []

def test_get_preleased_units():
    preleased_units = api_response_processor_property_summary.get_count_of_preleased_units(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, 153)
    assert preleased_units == 144
    preleased_units = api_response_processor_property_summary.get_count_of_preleased_units(constants_for_testing.EMPTY_RESPONSE_JSON, 153)
    assert preleased_units is None
    preleased_units = api_response_processor_property_summary.get_count_of_preleased_units(None, 153)
    assert preleased_units is None
    preleased_units = api_response_processor_property_summary.get_count_of_preleased_units(constants_for_testing.BAD_RESPONSE_JSON, 153)
    assert preleased_units is None
    preleased_units = api_response_processor_property_summary.get_count_of_preleased_units(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, None)
    assert preleased_units is None

def test_get_occupied_units_percentage():
    occupied_units_percentage = api_response_processor_property_summary.get_occupied_units_percentage(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, 150)
    assert occupied_units_percentage == "4.67%"
    occupied_units_percentage = api_response_processor_property_summary.get_occupied_units_percentage(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_VACANT_STATUS, 150)
    assert occupied_units_percentage == "0.0%"
    occupied_units_percentage = api_response_processor_property_summary.get_occupied_units_percentage(None, 150)
    assert occupied_units_percentage is None
    occupied_units_percentage = api_response_processor_property_summary.get_occupied_units_percentage(None, None)
    assert occupied_units_percentage is None
    occupied_units_percentage = api_response_processor_property_summary.get_occupied_units_percentage(constants_for_testing.BAD_RESPONSE_JSON, 150)
    assert occupied_units_percentage is None
    occupied_units_percentage = api_response_processor_property_summary.get_occupied_units_percentage(constants_for_testing.EMPTY_RESPONSE_JSON, 150)
    assert occupied_units_percentage is None
    occupied_units_percentage = api_response_processor_property_summary.get_occupied_units_percentage(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, None)
    assert occupied_units_percentage is None

def test_get_occurred_evictions_and_skips():
    evictions_and_skips = api_response_processor_property_summary.get_count_of_occurred_evictions_and_skips(constants_for_testing.LEASES_RESPONSE_JSON)
    assert evictions_and_skips == 4
    evictions_and_skips = api_response_processor_property_summary.get_count_of_occurred_evictions_and_skips(constants_for_testing.EMPTY_RESPONSE_JSON)
    assert evictions_and_skips is None
    evictions_and_skips = api_response_processor_property_summary.get_count_of_occurred_evictions_and_skips(constants_for_testing.BAD_RESPONSE_JSON)
    assert evictions_and_skips is None
    evictions_and_skips = api_response_processor_property_summary.get_count_of_occurred_evictions_and_skips(None)
    assert evictions_and_skips is None