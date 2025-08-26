"""
API Response Processor for generating leads summary data
"""
from api_client import api_client
from api_response_processor import helpers, data_classes

def get_leads_summary(property_id):
    """
    method for calling the APIs, providing the API responses to process,
    and giving back the leads summary data
    """
    current_week, last_week, week_before_last = helpers.generate_start_and_end_dates_for_three_weeks()
    leads_api_response_for_current_week = api_client.get_leads(property_id,
                                                               current_week[0].strftime("%m/%d/%Y"),
                                                               current_week[1].strftime("%m/%d/%Y"))

    leads_api_response_for_last_week = api_client.get_leads(property_id,
                                                            last_week[0].strftime("%m/%d/%Y"),
                                                            last_week[1].strftime("%m/%d/%Y"))

    leads_api_response_for_week_before_last = api_client.get_leads(property_id,
                                                                   week_before_last[0].strftime("%m/%d/%Y"),
                                                                   week_before_last[1].strftime("%m/%d/%Y"))

    (count_of_new_leads_for_current_week,
     count_of_started_applications_for_current_week,
     count_of_completed_applications_for_current_week,
     count_of_approved_applications_for_current_week,
     count_of_lease_signed_for_current_week,
     count_of_cancelled_applications_for_current_week) = generate_leads_summary(leads_api_response_for_current_week)

    (count_of_new_leads_for_last_week,
     count_of_started_applications_for_last_week,
     count_of_completed_applications_for_last_week,
     count_of_approved_applications_for_last_week,
     count_of_lease_signed_for_last_week,
     count_of_cancelled_applications_for_last_week) = generate_leads_summary(leads_api_response_for_last_week)

    (count_of_new_leads_for_week_before_last,
     count_of_started_applications_for_week_before_last,
     count_of_completed_applications_for_week_before_last,
     count_of_approved_applications_for_week_before_last,
     count_of_lease_signed_for_week_before_last,
     count_of_cancelled_applications_for_week_before_last) = generate_leads_summary(leads_api_response_for_week_before_last)

    leads_summary_for_three_weeks = data_classes.LeadsSummaryForThreeWeeks(
        current_week[0].strftime("%m/%d/%Y"),
        current_week[1].strftime("%m/%d/%Y"),
        count_of_new_leads_for_current_week,
        count_of_started_applications_for_current_week,
        count_of_completed_applications_for_current_week,
        count_of_approved_applications_for_current_week,
        count_of_lease_signed_for_current_week,
        count_of_cancelled_applications_for_current_week,

        last_week[0].strftime("%m/%d/%Y"),
        last_week[1].strftime("%m/%d/%Y"),
        count_of_new_leads_for_last_week,
        count_of_started_applications_for_last_week,
        count_of_completed_applications_for_last_week,
        count_of_approved_applications_for_last_week,
        count_of_lease_signed_for_last_week,
        count_of_cancelled_applications_for_last_week,

        week_before_last[0].strftime("%m/%d/%Y"),
        week_before_last[1].strftime("%m/%d/%Y"),
        count_of_new_leads_for_week_before_last,
        count_of_started_applications_for_week_before_last,
        count_of_completed_applications_for_week_before_last,
        count_of_approved_applications_for_week_before_last,
        count_of_lease_signed_for_week_before_last,
        count_of_cancelled_applications_for_week_before_last
    )
    print("Calculated the lead summary for " + f"{property_id}")
    return leads_summary_for_three_weeks

def generate_leads_summary(leads_api_response):
    """
    method for generating the leads summary data
    """
    prospect = helpers.get_leads_from_leads_response_json(leads_api_response)
    if prospect is None:
        return None, None, None, None, None, None
    count_of_new_leads = 0
    count_of_started_applications = 0
    count_of_completed_applications = 0
    count_of_approved_applications = 0
    count_of_cancelled_applications = 0
    count_of_lease_signed = 0
    for lead in prospect:
        lead_status = lead["status"]
        match lead_status:
            case "Guest Card Completed":
                count_of_new_leads += 1
            case "Application Started":
                count_of_started_applications += 1
            case "Application Completed":
                count_of_completed_applications += 1
            case "Application Approved":
                count_of_approved_applications += 1
            case "Application Cancelled":
                count_of_cancelled_applications += 1
            case "Lease Started":
                count_of_lease_signed += 1
    return (count_of_new_leads,
            count_of_started_applications,
            count_of_completed_applications,
            count_of_approved_applications,
            count_of_lease_signed,
            count_of_cancelled_applications)
