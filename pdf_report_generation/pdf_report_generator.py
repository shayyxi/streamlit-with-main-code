from datetime import date, timedelta
from fpdf import FPDF

from api_response_processor import helpers
from api_response_processor.data_classes import (PropertySummary,
                                                 UnitsSummary,
                                                 ResidentRetentionSummaryForNoticeAndMTM,
                                                 ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths,
                                                 RentSummaryForCurrentAndLastTwoMonths,
                                                 MaintenanceSummaryForThreeWeeks,
                                                 LeadsSummaryForThreeWeeks)
from pdf_report_generation import data_validator
from pdf_report_generation.data_validator import sanitize_leads_summary


def generate_pdf_with_dataclasses(property_name: str,
                                  property_summary: dict[date, PropertySummary],
                                  rent_summary: RentSummaryForCurrentAndLastTwoMonths,
                                  units_summary: dict[date, UnitsSummary],
                                  resident_retention_summary_for_expiry_and_renewal_for_three_months: ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths,
                                  resident_retention_summary_for_notice_and_mtm: ResidentRetentionSummaryForNoticeAndMTM,
                                  leads_summary_for_last_three_weeks: LeadsSummaryForThreeWeeks,
                                  maintenance_summary_for_last_three_weeks: MaintenanceSummaryForThreeWeeks):
    pdf = FPDF()
    pdf = generate_property_summary_table(property_name,
                                        property_summary,
                                        pdf)
    pdf = generate_rent_summary_table(rent_summary,
                                      pdf)
    pdf = generate_units_summary_table(units_summary,pdf)
    pdf = generate_resident_retention_summary_table(resident_retention_summary_for_expiry_and_renewal_for_three_months,
                                                    resident_retention_summary_for_notice_and_mtm,
                                                    pdf)
    pdf = generate_leads_summary_table(leads_summary_for_last_three_weeks,
                                                          pdf)
    pdf = generate_maintenance_summary_table(maintenance_summary_for_last_three_weeks,
                                             pdf)
    pdf.output(property_name + '_table.pdf')

def generate_property_summary_table(property_name, property_summary: dict[date, PropertySummary], pdf: FPDF):
    # if today's day is sunday, then give full duration
    # calculate monday's date from date
    property_summary_sanitized = data_validator.sanitize_property_summary_dict(property_summary)
    property_summary_dates = list(property_summary_sanitized.keys())
    today_date = property_summary_dates[0]
    monday_date = today_date
    if today_date.weekday() == 6:
        monday_date = today_date - timedelta(days=6)

    one_week_ago_sunday_date = property_summary_dates[1]
    one_week_ago_monday_date = one_week_ago_sunday_date - timedelta(days=6)

    two_week_ago_sunday_date = property_summary_dates[2]
    two_week_ago_monday_date = two_week_ago_sunday_date - timedelta(days=6)

    property_summary_table_data = (
        ("Date", monday_date.strftime("%m/%d/%Y") + "-" + today_date.strftime("%m/%d/%Y"), one_week_ago_monday_date.strftime("%m/%d/%Y") + "-" + one_week_ago_sunday_date.strftime("%m/%d/%Y"), two_week_ago_monday_date.strftime("%m/%d/%Y") + "-" + two_week_ago_sunday_date.strftime("%m/%d/%Y")),
        ("Total Units", f"{property_summary_sanitized[today_date].total_units}", f"{property_summary_sanitized[one_week_ago_sunday_date].total_units}", f"{property_summary_sanitized[two_week_ago_sunday_date].total_units}"),
        ("Total Rentable Units", f"{property_summary_sanitized[today_date].total_rentable_units}",f"{property_summary_sanitized[one_week_ago_sunday_date].total_rentable_units}", f"{property_summary_sanitized[two_week_ago_sunday_date].total_rentable_units}"),
        ("Excluded/Downed Units", f"{property_summary_sanitized[today_date].excluded_units}", f"{property_summary_sanitized[one_week_ago_sunday_date].excluded_units}", f"{property_summary_sanitized[two_week_ago_sunday_date].excluded_units}"),
        ("Pre-leased Units", f"{property_summary_sanitized[today_date].preleased_units}", f"{property_summary_sanitized[one_week_ago_sunday_date].preleased_units}", f"{property_summary_sanitized[two_week_ago_sunday_date].preleased_units}"),
        ("Percentage Occupied", f"{property_summary_sanitized[today_date].occupied_units_percentage}", f"{property_summary_sanitized[one_week_ago_sunday_date].occupied_units_percentage}", f"{property_summary_sanitized[two_week_ago_sunday_date].occupied_units_percentage}"),
        ("Percentage Leased", f"{property_summary_sanitized[today_date].preleased_units_percentage}", f"{property_summary_sanitized[one_week_ago_sunday_date].preleased_units_percentage}", f"{property_summary_sanitized[two_week_ago_sunday_date].preleased_units_percentage}"),
        ("Evictions Filed", f"{property_summary_sanitized[today_date].evictions_filed}", f"{property_summary_sanitized[one_week_ago_sunday_date].evictions_filed}", f"{property_summary_sanitized[two_week_ago_sunday_date].evictions_filed}"),
        ("Evictions/Skips Occurred", f"{property_summary_sanitized[today_date].evictions_and_skips_occurred_for_current_month}", f"{property_summary_sanitized[one_week_ago_sunday_date].evictions_and_skips_occurred_for_current_month}", f"{property_summary_sanitized[two_week_ago_sunday_date].evictions_and_skips_occurred_for_current_month}"),
    )
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Summary for ' + property_name, align='C')
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 10, 'Property Summary', ln=True)
    pdf.ln(1)
    pdf.set_font("Times", size=11)
    with pdf.table() as table:
        for data_row in property_summary_table_data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln(5)
    return pdf

def generate_rent_summary_table(rent_summary: RentSummaryForCurrentAndLastTwoMonths, pdf: FPDF):
    rent_summary = data_validator.sanitize_rent_collection_summary(rent_summary)
    rent_summary_table_data = (
        ("Date", rent_summary.current_month_first_date + "-" + rent_summary.current_month_today_date,
         rent_summary.last_month_first_date + "-" + rent_summary.last_month_last_date,
         rent_summary.month_before_last_first_date + "-" + rent_summary.month_before_last_last_date),

        ("Rent billed", f"{rent_summary.current_month_total_rent_billed}",
         f"{rent_summary.last_month_total_rent_billed}",
         f"{rent_summary.month_before_last_total_rent_billed}"),

        ("Rent Collections", f"{rent_summary.current_month_total_rent_collected}",
         f"{rent_summary.last_month_total_rent_collected}",
         f"{rent_summary.month_before_last_total_rent_collected}"),

        ("Percentage Rent Collected", f"{rent_summary.current_month_total_rent_collected_percentage}",
         f"{rent_summary.last_month_total_rent_collected_percentage}",
         f"{rent_summary.month_before_last_total_rent_collected_percentage}"),
    )
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 10, 'Rent Collection Summary', ln=True)
    pdf.ln(3)
    pdf.set_font("Times", size=11)
    with pdf.table() as table:
        for data_row in rent_summary_table_data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln(5)
    return pdf

def generate_units_summary_table(units_summary: dict[date, UnitsSummary], pdf: FPDF):
    units_summary_sanitized = data_validator.sanitize_units_summary_dict(units_summary)
    units_summary_dates = list(units_summary_sanitized.keys())
    today_date = units_summary_dates[0]
    monday_date = today_date
    if today_date.weekday() == 6:
        monday_date = today_date - timedelta(days=6)

    one_week_ago_sunday_date = units_summary_dates[1]
    one_week_ago_monday_date = one_week_ago_sunday_date - timedelta(days=6)

    two_week_ago_sunday_date = units_summary_dates[2]
    two_week_ago_monday_date = two_week_ago_sunday_date - timedelta(days=6)

    # helpers method
    current_week_dates, last_week_dates, week_before_last_dates = helpers.generate_start_and_end_dates_for_three_weeks()

    units_summary_table_data = (
        ("Date", current_week_dates[0].strftime("%m/%d/%Y") + "-" + current_week_dates[1].strftime("%m/%d/%Y"),
         last_week_dates[0].strftime("%m/%d/%Y") + "-" + last_week_dates[1].strftime("%m/%d/%Y"),
         week_before_last_dates[0].strftime("%m/%d/%Y") + "-" + week_before_last_dates[1].strftime("%m/%d/%Y")),

        ("Occupied Units", f"{units_summary_sanitized[current_week_dates[1]].count_of_occupied_units}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_occupied_units}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_occupied_units}"),

        ("Notice Rented Units", f"{units_summary_sanitized[current_week_dates[1]].count_of_on_notice_rented_units}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_on_notice_rented_units}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_on_notice_rented_units}"),

        ("Notice Unrented Units", f"{units_summary_sanitized[current_week_dates[1]].count_of_on_notice_unrented_units}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_on_notice_unrented_units}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_on_notice_unrented_units}"),

        ("Vacant Units", f"{units_summary_sanitized[current_week_dates[1]].count_of_vacant_units}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_vacant_units}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_vacant_units}"),

        ("Vacant Rented Units", f"{units_summary_sanitized[current_week_dates[1]].count_of_vacant_rented_units}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_vacant_rented_units}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_vacant_rented_units}"),

        ("Vacant Unrented Units", f"{units_summary_sanitized[current_week_dates[1]].count_of_vacant_unrented_units}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_vacant_unrented_units}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_vacant_unrented_units}"),

        ("Total Move-ins", f"{units_summary_sanitized[current_week_dates[1]].count_of_total_move_ins}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_total_move_ins}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_total_move_ins}"),

        ("Total Move-out", f"{units_summary_sanitized[current_week_dates[1]].count_of_total_move_out}",
         f"{units_summary_sanitized[last_week_dates[1]].count_of_total_move_out}",
         f"{units_summary_sanitized[week_before_last_dates[1]].count_of_total_move_out}")
    )
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 10, 'Units Summary', ln=True)
    pdf.ln(3)
    pdf.set_font("Times", size=11)
    with pdf.table() as table:
        for data_row in units_summary_table_data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln(5)
    return pdf

def generate_resident_retention_summary_table(resident_retention_summary_for_expiry_and_renewal_for_three_months: ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths,
                                              resident_retention_summary_for_notice_and_mtm: ResidentRetentionSummaryForNoticeAndMTM,
                                              pdf: FPDF):
    resident_retention_summary_for_expiry_and_renewal_for_three_months = data_validator.sanitize_resident_retention_for_expiry_and_renewal_for_three_months_summary(resident_retention_summary_for_expiry_and_renewal_for_three_months)
    resident_retention_summary_for_notice_and_mtm = data_validator.sanitize_resident_retention_for_notice_and_mtm_summary(resident_retention_summary_for_notice_and_mtm)

    resident_retention_summary_table_data_for_expiry_and_renewal_for_three_months = (
        ("Date", f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_first_date}" + "-"
         + f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_last_date}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_month_first_date}" + "-"
         + f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_month_last_date}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_to_next_month_first_date}" + "-"
         + f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_to_next_month_last_date}"),

        ("Expiring Leases", f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_total_expiring_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_month_total_expiring_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_to_next_month_total_expiring_leases_count}"),

        ("Renewed Leases", f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_renewed_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_renewed_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_to_next_month_renewed_leases_count}"),

        ("Under Renewal Leases", f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_under_renewal_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_month_under_renewal_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_to_next_month_under_renewal_leases_count}"),

        ("Need Renewal Leases", f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_need_renewal_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_month_need_renewal_leases_count}",
         f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.next_to_next_month_need_renewal_leases_count}"),
    )

    resident_retention_summary_table_data_for_notice_and_mtm = (
        ("Date", f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_first_date}" + " - "
         + f"{resident_retention_summary_for_expiry_and_renewal_for_three_months.current_month_last_date}"),

        ("Notice Leases", f"{resident_retention_summary_for_notice_and_mtm.notice_non_renewed_leases_count}"),

        ("Notice (Eviction) Leases", f"{resident_retention_summary_for_notice_and_mtm.notice_eviction_leases_count}"),

        ("Month-to-month Leases", f"{resident_retention_summary_for_notice_and_mtm.need_renewal_mtm_leases_count}")
    )

    pdf.add_page()
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 10, 'Resident Retention Summary', ln=True)
    pdf.ln(1)
    pdf.set_font("Times", size=11)
    with pdf.table() as table:
        for data_row in resident_retention_summary_table_data_for_notice_and_mtm:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln(5)
    pdf.set_font("Times", size=11)
    with pdf.table() as table:
        for data_row in resident_retention_summary_table_data_for_expiry_and_renewal_for_three_months:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln(5)
    return pdf

def generate_leads_summary_table(leads_summary: LeadsSummaryForThreeWeeks, pdf: FPDF):
    leads_summary = sanitize_leads_summary(leads_summary)
    leads_summary_table_data = (
        ("Date", leads_summary.current_week_monday_date + " - " + leads_summary.current_week_end_date,
         leads_summary.last_week_monday_date + " - " + leads_summary.last_week_end_date,
         leads_summary.week_before_last_monday_date + " - " + leads_summary.week_before_last_end_date,),

        ("New Leads", f"{leads_summary.current_week_new_leads_count}",
         f"{leads_summary.last_week_new_leads_count}",
         f"{leads_summary.week_before_last_new_leads_count}"),

        ("Applications Started", f"{leads_summary.current_week_applications_started_count}",
         f"{leads_summary.last_week_applications_started_count}",
         f"{leads_summary.week_before_last_applications_started_count}"),

        ("Applications Completed", f"{leads_summary.current_week_applications_completed_count}",
         f"{leads_summary.last_week_applications_completed_count}",
         f"{leads_summary.week_before_last_applications_completed_count}"),

        ("Approved Applications", f"{leads_summary.current_week_approved_applications_count}",
         f"{leads_summary.last_week_approved_applications_count}",
         f"{leads_summary.week_before_last_approved_applications_count}"),

        ("Lease Signed", f"{leads_summary.current_week_lease_signed_count}",
         f"{leads_summary.last_week_lease_signed_count}",
         f"{leads_summary.week_before_last_lease_signed_count}"),

        ("Cancelled Applications", f"{leads_summary.current_week_cancelled_applications_count}",
         f"{leads_summary.last_week_cancelled_applications_count}",
         f"{leads_summary.week_before_last_cancelled_applications_count}"),
    )
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 10, 'Leads Summary', ln=True)
    pdf.ln(1)
    pdf.set_font("Times", size=11)
    with pdf.table() as table:
        for data_row in leads_summary_table_data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln(5)
    return pdf

def generate_maintenance_summary_table(maintenance_summary: MaintenanceSummaryForThreeWeeks, pdf: FPDF):
    maintenance_summary = data_validator.sanitize_maintenance_summary(maintenance_summary)
    maintenance_summary_table_data = (
        ("Date", maintenance_summary.current_week_monday_date + " - " + maintenance_summary.current_week_end_date,
         maintenance_summary.last_week_monday_date + " - " + maintenance_summary.last_week_sunday_date,
         maintenance_summary.week_before_last_monday_date + " - " + maintenance_summary.week_before_last_sunday_date),

        ("Open Work Orders", f"{maintenance_summary.current_week_open_work_orders_count}",
         f"{maintenance_summary.last_week_open_work_orders_count}",
         f"{maintenance_summary.week_before_last_open_work_orders_count}"),

        ("Completed Work Orders", f"{maintenance_summary.current_week_completed_work_orders_count}",
         f"{maintenance_summary.last_week_completed_work_orders_count}",
         f"{maintenance_summary.week_before_last_completed_work_orders_count}"),
    )
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 10, 'Maintenance Summary', ln=True)
    pdf.ln(1)
    pdf.set_font("Times", size=11)
    with pdf.table() as table:
        for data_row in maintenance_summary_table_data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln(5)
    return pdf