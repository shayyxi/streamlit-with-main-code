"""
Main file, Executes the code
"""
import datetime

from dotenv import load_dotenv

from api_response_processor import (api_response_processor_property_summary, api_response_processor_units_summary,
                                    api_response_processor_resident_retention, api_response_processor_leads_summary,
                                    api_response_processor_maintenance_summary, api_response_processor_rent_summary)
from api_client import api_client
from pdf_report_generation import pdf_report_generator
from metrics_persistence import metrics_persistence, summary_table_name
from email_sending import email_sending
import os

if __name__ == "__main__":
    #initiate db
    load_dotenv()
    db_url = os.getenv("DATABASE_URL")
    metrics_persistence = metrics_persistence.MetricsPersistence(db_url)
    # email sender
    email_password = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO")
    email_sender = email_sending.EmailSender(app_password=email_password, email_to=email_to)
    # get list of properties
    response_from_properties_api = api_client.get_properties()
    properties_list = (api_response_processor_property_summary
                       .get_list_of_properties(response_from_properties_api))
    properties_list.pop(100082998)

    # iterate through each property, get the dataclass, send to pdf
    for property_id in properties_list:
        # property summary
        property_summary = api_response_processor_property_summary.get_property_summary(property_id)
        #rent summary
        rent_summary = api_response_processor_rent_summary.get_rent_summary(property_id, metrics_persistence)
        # units summary
        units_summary = api_response_processor_units_summary.get_units_summary(property_id)
        # resident retention summary
        (resident_retention_summary_for_expiry_and_renewal_for_three_months,
            resident_retention_summary_for_notice_and_mtm) = api_response_processor_resident_retention.get_resident_retention_summary(property_id)
        # leads summary
        leads_summary_for_three_weeks = api_response_processor_leads_summary.get_leads_summary(property_id)
        # maintenance summary
        maintenance_summary_for_three_weeks = api_response_processor_maintenance_summary.get_maintenance_summary(property_id)

        # put db data for property summary
        metrics_persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(property_id, property_summary,
                                                                                            summary_table_name.SummaryTableName.PROPERTY_SUMMARY.value)
        # put db data for units summary
        metrics_persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(property_id, units_summary,
                                                                                            summary_table_name.SummaryTableName.UNITS_SUMMARY.value)

        # property summary dict
        previous_property_summary = metrics_persistence.get_property_metrics(property_id,
                                                                             summary_table_name.SummaryTableName.PROPERTY_SUMMARY.value)

        if len(previous_property_summary.keys()) > 0:
            all_property_summary = {datetime.date.today(): property_summary, **previous_property_summary}
        else:
            all_property_summary = {datetime.date.today(): property_summary}

        # units summary dict
        previous_units_summary = metrics_persistence.get_property_metrics(property_id,
                                                                             summary_table_name.SummaryTableName.UNITS_SUMMARY.value)

        if len(previous_units_summary.keys()) > 0:
            all_units_summary = {datetime.date.today(): units_summary, **previous_units_summary}
        else:
            all_units_summary = {datetime.date.today(): units_summary}

        #pdf report generation
        pdf_report_generator.generate_pdf_with_dataclasses(properties_list.get(property_id),
                                                           all_property_summary,
                                                           rent_summary,
                                                           all_units_summary,
                                                           resident_retention_summary_for_expiry_and_renewal_for_three_months,
                                                           resident_retention_summary_for_notice_and_mtm,
                                                           leads_summary_for_three_weeks,
                                                           maintenance_summary_for_three_weeks)
        email_sender.send_email('Property Summary Report ' + properties_list.get(property_id), 'Please find attached the property summary report for ' + properties_list.get(property_id), properties_list.get(property_id) + "_table.pdf")
        break
    metrics_persistence.close()