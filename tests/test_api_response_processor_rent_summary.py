from api_response_processor import api_response_processor_rent_summary
from config import constants_for_testing

def test_get_rent_billed():
    rent_billed = api_response_processor_rent_summary.get_total_amount_of_rent_billed(constants_for_testing.LEASES_RESPONSE_JSON)
    assert rent_billed == 7680.0
    rent_billed = api_response_processor_rent_summary.get_total_amount_of_rent_billed(None)
    assert rent_billed is None
    rent_billed = api_response_processor_rent_summary.get_total_amount_of_rent_billed(constants_for_testing.EMPTY_RESPONSE_JSON)
    assert rent_billed is None
    rent_billed = api_response_processor_rent_summary.get_total_amount_of_rent_billed(constants_for_testing.BAD_RESPONSE_JSON)
    assert rent_billed is None

def test_get_rent_collected_percentage():
    total_rent_collected, rent_collected_percentage = api_response_processor_rent_summary.get_rent_collected_total_and_percentage(constants_for_testing.LEASE_ARTRANSACTIONS_RESPONSE_JSON, 6144.0)
    assert total_rent_collected == 5018.14
    assert rent_collected_percentage == "81.68%"
    total_rent_collected, rent_collected_percentage = api_response_processor_rent_summary.get_rent_collected_total_and_percentage(None, 6144.0)
    assert total_rent_collected is None
    assert rent_collected_percentage is None
    total_rent_collected, rent_collected_percentage = api_response_processor_rent_summary.get_rent_collected_total_and_percentage(None, None)
    assert total_rent_collected is None
    assert rent_collected_percentage is None
    total_rent_collected, rent_collected_percentage = api_response_processor_rent_summary.get_rent_collected_total_and_percentage(constants_for_testing.BAD_RESPONSE_JSON, 6144.0)
    assert total_rent_collected is None
    assert rent_collected_percentage is None
    total_rent_collected, rent_collected_percentage = api_response_processor_rent_summary.get_rent_collected_total_and_percentage(constants_for_testing.EMPTY_RESPONSE_JSON, 6144.0)
    assert total_rent_collected is None
    assert rent_collected_percentage is None
    total_rent_collected, rent_collected_percentage = api_response_processor_rent_summary.get_rent_collected_total_and_percentage(constants_for_testing.LEASE_ARTRANSACTIONS_RESPONSE_JSON, 0)
    assert total_rent_collected is None
    assert rent_collected_percentage is None