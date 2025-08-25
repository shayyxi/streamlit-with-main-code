from api_response_processor import api_response_processor_leads_summary
from config import constants_for_testing


def test_generate_leads_summary():
    leads_summary = api_response_processor_leads_summary.generate_leads_summary(constants_for_testing.LEADS_RESPONSE_JSON)
    assert leads_summary.total_new_leads_count == 1
    assert leads_summary.total_applications_started_count == 2
    assert leads_summary.total_approved_applications_count == 1
    assert leads_summary.total_cancelled_applications_count == 1
    leads_summary = api_response_processor_leads_summary.generate_leads_summary(constants_for_testing.EMPTY_RESPONSE_JSON)
    assert leads_summary is None
    leads_summary = api_response_processor_leads_summary.generate_leads_summary(constants_for_testing.BAD_RESPONSE_JSON)
    assert leads_summary is None