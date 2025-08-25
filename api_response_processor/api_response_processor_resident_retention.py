"""
API Response Processor for generating resident retention summary data
"""
from api_client import api_client
from api_response_processor import helpers, data_classes

def get_resident_retention_summary(property_id):
    """
    method for getting the resident retention summary for each property against the properties list
    """
    leases_api_response = api_client.get_leases(property_id,
                                            None,
                                            False,
                                            False,
                                            False)
    (notice_non_renewed_leases_count,
     notice_eviction_leases_count,
     need_renewal_mtm_leases_count) = calculate_resident_retention_summary_for_notice_and_mtm_info(leases_api_response)

    (current_month_dates,
     next_month_dates,
     ntn_month_dates) = helpers.get_first_and_last_dates_for_three_months()

    leases_api_response_current_month = api_client.get_leases_with_expiry_date_range(property_id,
                                                                                     current_month_dates[0].strftime("%m/%d/%Y"),
                                                                                     current_month_dates[1].strftime("%m/%d/%Y"))
    expiring_leases_api_response_current_month = api_client.get_expiring_leases_with_date_range(property_id,
                                                                                current_month_dates[0].strftime("%m/%d/%Y"),
                                                                                current_month_dates[1].strftime("%m/%d/%Y"))
    (total_expiring_leases_count_for_current_month,
     current_month_renewed_leases_count_for_current_month,
     current_month_under_renewal_leases_count_for_current_month,
     current_month_need_renewal_leases_count_for_current_month) = calculate_resident_retention_summary_for_expiry_and_renewal_info(leases_api_response_current_month,
                                                                                                                                   expiring_leases_api_response_current_month)

    leases_api_response_next_month = api_client.get_leases_with_expiry_date_range(property_id,
                                                                                  next_month_dates[0].strftime("%m/%d/%Y"),
                                                                                  next_month_dates[1].strftime("%m/%d/%Y"))
    expiring_leases_api_response_next_month = api_client.get_expiring_leases_with_date_range(property_id,
                                                                                              next_month_dates[0].strftime("%m/%d/%Y"),
                                                                                              next_month_dates[1].strftime("%m/%d/%Y"))
    (total_expiring_leases_count_for_next_month,
     current_month_renewed_leases_count_for_next_month,
     current_month_under_renewal_leases_count_for_next_month,
     current_month_need_renewal_leases_count_for_next_month) = calculate_resident_retention_summary_for_expiry_and_renewal_info(
        leases_api_response_next_month,
        expiring_leases_api_response_next_month)

    leases_api_response_ntn_month = api_client.get_leases_with_expiry_date_range(property_id,
                                                                                  ntn_month_dates[0].strftime("%m/%d/%Y"),
                                                                                  ntn_month_dates[1].strftime("%m/%d/%Y"))
    expiring_leases_api_response_ntn_month = api_client.get_expiring_leases_with_date_range(property_id,
                                                                                           ntn_month_dates[0].strftime("%m/%d/%Y"),
                                                                                           ntn_month_dates[1].strftime("%m/%d/%Y"))
    (total_expiring_leases_count_for_ntn_month,
     current_month_renewed_leases_count_for_ntn_month,
     current_month_under_renewal_leases_count_for_ntn_month,
     current_month_need_renewal_leases_count_for_ntn_month) = calculate_resident_retention_summary_for_expiry_and_renewal_info(
        leases_api_response_ntn_month,
        expiring_leases_api_response_ntn_month)

    resident_retention_summary_for_expiry_and_renewal_for_three_months = data_classes.ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths(
        current_month_dates[0].strftime("%m/%d/%Y"),
        current_month_dates[1].strftime("%m/%d/%Y"),
        total_expiring_leases_count_for_current_month,
        current_month_renewed_leases_count_for_current_month,
        current_month_under_renewal_leases_count_for_current_month,
        current_month_need_renewal_leases_count_for_current_month,

        next_month_dates[0].strftime("%m/%d/%Y"),
        next_month_dates[1].strftime("%m/%d/%Y"),
        total_expiring_leases_count_for_next_month,
        current_month_renewed_leases_count_for_next_month,
        current_month_under_renewal_leases_count_for_next_month,
        current_month_need_renewal_leases_count_for_next_month,

        ntn_month_dates[0].strftime("%m/%d/%Y"),
        ntn_month_dates[1].strftime("%m/%d/%Y"),
        total_expiring_leases_count_for_ntn_month,
        current_month_renewed_leases_count_for_ntn_month,
        current_month_under_renewal_leases_count_for_ntn_month,
        current_month_need_renewal_leases_count_for_ntn_month
    )

    resident_retention_summary_for_notice_and_mtm = data_classes.ResidentRetentionSummaryForNoticeAndMTM(
        notice_non_renewed_leases_count,
        notice_eviction_leases_count,
        need_renewal_mtm_leases_count
    )
    print("Calculated the resident retention summary for " + f"{property_id}")
    return resident_retention_summary_for_expiry_and_renewal_for_three_months, resident_retention_summary_for_notice_and_mtm

def calculate_resident_retention_summary_for_notice_and_mtm_info(leases_api_response):
    """
    method for calculating the notice and mtm resident retention summary for a property
    """
    leases = helpers.get_leases_from_leases_response_json(leases_api_response)
    if leases is None:
        return None, None, None

    notice_non_renewed_leases_count = 0
    notice_eviction_leases_count = 0
    need_renewal_mtm_leases_count = 0

    for lease in leases:
        lease_interval_status = lease.get("leaseIntervalStatus", "")
        lease_sub_status = lease.get("leaseSubStatus", "")
        if lease_interval_status == "Current":
            if lease_sub_status == "Month To Month":
                need_renewal_mtm_leases_count += 1
        elif lease_interval_status == "Notice":
            if lease_sub_status == "Eviction":
                notice_eviction_leases_count += 1
            else:
                notice_non_renewed_leases_count += 1

    return (notice_non_renewed_leases_count,
            notice_eviction_leases_count,
            need_renewal_mtm_leases_count)

def calculate_resident_retention_summary_for_expiry_and_renewal_info(leases_api_response, expiry_leases_api_response):
    """
    method for calculating the expiry and renewal resident retention summary for a property
    """
    leases = helpers.get_leases_from_leases_response_json(leases_api_response)
    if leases is None:
        return None, None, None, None

    expiry_leases = helpers.get_leases_from_expiry_leases_response_json(expiry_leases_api_response)
    if expiry_leases is None:
        return None, None, None, None

    total_expiring_leases_count = len(leases)
    current_month_renewed_leases_count = 0
    current_month_need_renewal_leases_count = len(expiry_leases)

    for lease in leases:
        lease_sub_status = lease.get("leaseSubStatus", "")
        if lease_sub_status == "Renewed":
            current_month_renewed_leases_count += 1

    current_month_under_renewal_leases_count = total_expiring_leases_count - current_month_renewed_leases_count - current_month_need_renewal_leases_count

    return (total_expiring_leases_count,
            current_month_renewed_leases_count,
            current_month_under_renewal_leases_count,
            current_month_need_renewal_leases_count)
