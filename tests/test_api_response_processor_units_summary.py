from api_response_processor import api_response_processor_units_summary
from config import constants_for_testing

def test_get_count_of_units_with_matching_status_and_availability():
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, ["On Notice"], True)
    assert count_of_units_with_matching_status == 1
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.BAD_RESPONSE_JSON, [], True)
    assert count_of_units_with_matching_status == None
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.EMPTY_RESPONSE_JSON, [], True)
    assert count_of_units_with_matching_status == None
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, ["On Notice"], False)
    assert count_of_units_with_matching_status == 3
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, ["Occupied"], False)
    assert count_of_units_with_matching_status == 2
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, ["On Notice", "Occupied"], True)
    assert count_of_units_with_matching_status == 2
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, ["On Notice", "Occupied"], False)
    assert count_of_units_with_matching_status == 5
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, [], True)
    assert count_of_units_with_matching_status == 2
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, [], False)
    assert count_of_units_with_matching_status == 5
    count_of_units_with_matching_status = api_response_processor_units_summary.get_count_of_units_with_matching_status_and_availability(constants_for_testing.UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING, ["On Notice", "Occupied"], None)
    assert count_of_units_with_matching_status == 7
