from api_response_processor import api_response_processor_resident_retention
from config import constants_for_testing

def test_calculate_resident_retention_summary_from_leases():
    (notice_non_renewed_leases_count,
     notice_eviction_leases_count,
     need_renewal_mtm_leases_count) = api_response_processor_resident_retention.calculate_resident_retention_summary_for_notice_and_mtm_info(constants_for_testing.LEASES_RESPONSE_JSON_FOR_RESIDENT_RETENTION_SUMMARY)
    assert notice_eviction_leases_count == 2
    assert notice_non_renewed_leases_count == 2
    assert need_renewal_mtm_leases_count == 2
    (notice_non_renewed_leases_count,
     notice_eviction_leases_count,
     need_renewal_mtm_leases_count) = api_response_processor_resident_retention.calculate_resident_retention_summary_for_notice_and_mtm_info(None)
    assert notice_non_renewed_leases_count is None
    assert notice_eviction_leases_count is None
    assert need_renewal_mtm_leases_count is None

def test_calculate_resident_retention_summary_for_expiry_and_renewal_info():
    (total_expiring_leases_count,
     current_month_renewed_leases_count,
     current_month_under_renewal_leases_count,
     current_month_need_renewal_leases_count) = api_response_processor_resident_retention.calculate_resident_retention_summary_for_expiry_and_renewal_info(constants_for_testing.LEASES_RESPONSE_JSON_WITH_EXPIRY_DATE_FILTER,
                                                                                                                                                           constants_for_testing.EXPIRING_LEASES_RESPONSE_JSON)
    assert total_expiring_leases_count == 5
    assert current_month_renewed_leases_count == 2
    assert current_month_under_renewal_leases_count == 1
    assert current_month_need_renewal_leases_count == 2

    (total_expiring_leases_count,
     current_month_renewed_leases_count,
     current_month_under_renewal_leases_count,
     current_month_need_renewal_leases_count) = api_response_processor_resident_retention.calculate_resident_retention_summary_for_expiry_and_renewal_info(
        constants_for_testing.BAD_RESPONSE_JSON,
        constants_for_testing.BAD_RESPONSE_JSON)
    assert total_expiring_leases_count is None
    assert current_month_renewed_leases_count is None
    assert current_month_under_renewal_leases_count is None
    assert current_month_need_renewal_leases_count is None

    (total_expiring_leases_count,
     current_month_renewed_leases_count,
     current_month_under_renewal_leases_count,
     current_month_need_renewal_leases_count) = api_response_processor_resident_retention.calculate_resident_retention_summary_for_expiry_and_renewal_info(
        constants_for_testing.EMPTY_RESPONSE_JSON,
        constants_for_testing.EMPTY_RESPONSE_JSON)
    assert total_expiring_leases_count is None
    assert current_month_renewed_leases_count is None
    assert current_month_under_renewal_leases_count is None
    assert current_month_need_renewal_leases_count is None