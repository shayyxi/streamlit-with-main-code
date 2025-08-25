from dataclasses import dataclass
from typing import Any, Optional, Union

@dataclass
class ApiResponsesForGeneratingPropertySummary:
    response_from_property_units_api: Optional[Any]
    response_from_units_availability_and_pricing_api: Optional[Any]
    response_from_leases_api_with_current_and_notice_type: Optional[Any]
    response_from_leases_api_with_notice_type: Optional[Any]
    response_from_leases_api_with_past_type: Optional[Any]

@dataclass
class ApiResponsesForGeneratingUnitsSummary:
    response_from_units_availability_and_pricing_api: Optional[Any]
    response_from_leases_api_with_move_in_date: Optional[Any]
    response_from_leases_api_with_move_out_date: Optional[Any]

@dataclass
class PropertySummary:
    total_units: Union[int, str, None]
    total_rentable_units: Union[int, str, None]
    excluded_units: Union[int, str, None]
    preleased_units: Union[int, str, None]
    occupied_units_percentage: Union[int, str, None]
    preleased_units_percentage: Union[int, str, None]
    evictions_filed: Union[int, str, None]
    evictions_and_skips_occurred_for_current_month: Union[int, str, None]

@dataclass
class UnitsSummary:
    count_of_occupied_units: Union[int, str, None]
    count_of_on_notice_rented_units: Union[int, str, None]
    count_of_on_notice_unrented_units: Union[int, str, None]
    count_of_vacant_units: Union[int, str, None]
    count_of_vacant_rented_units: Union[int, str, None]
    count_of_vacant_unrented_units: Union[int, str, None]
    count_of_total_move_ins: Union[int, str, None]
    count_of_total_move_out: Union[int, str, None]

@dataclass
class ResidentRetentionSummaryForNoticeAndMTM:
    notice_non_renewed_leases_count: Union[int, str, None]
    notice_eviction_leases_count: Union[int, str, None]
    need_renewal_mtm_leases_count: Union[int, str, None]

@dataclass
class ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths:
    current_month_first_date: Union[str, None]
    current_month_last_date: Union[int, str, None]
    current_month_total_expiring_leases_count: Union[int, str, None]
    current_month_renewed_leases_count: Union[int, str, None]
    current_month_under_renewal_leases_count: Union[int, str, None]
    current_month_need_renewal_leases_count: Union[int, str, None]

    next_month_first_date: Union[int, str, None]
    next_month_last_date: Union[int, str, None]
    next_month_total_expiring_leases_count: Union[int, str, None]
    next_month_renewed_leases_count: Union[int, str, None]
    next_month_under_renewal_leases_count: Union[int, str, None]
    next_month_need_renewal_leases_count: Union[int, str, None]

    next_to_next_month_first_date: Union[int, str, None]
    next_to_next_month_last_date: Union[int, str, None]
    next_to_next_month_total_expiring_leases_count: Union[int, str, None]
    next_to_next_month_renewed_leases_count: Union[int, str, None]
    next_to_next_month_under_renewal_leases_count: Union[int, str, None]
    next_to_next_month_need_renewal_leases_count: Union[int, str, None]

@dataclass
class RentSummaryForPersistence:
    total_rent_billed: Optional[int]

@dataclass
class RentSummaryForCurrentAndLastTwoMonths:
    current_month_first_date: Union[str, None]
    current_month_today_date: Union[str, None]
    current_month_total_rent_billed: Union[int, None]
    current_month_total_rent_collected: Union[int, None]
    current_month_total_rent_collected_percentage: Union[str, None]

    last_month_first_date: Union[str, None]
    last_month_last_date: Union[str, None]
    last_month_total_rent_billed: Union[int, None]
    last_month_total_rent_collected: Union[int, None]
    last_month_total_rent_collected_percentage: Union[str, None]

    month_before_last_first_date: Union[str, None]
    month_before_last_last_date: Union[str, None]
    month_before_last_total_rent_billed: Union[int, None]
    month_before_last_total_rent_collected: Union[int, None]
    month_before_last_total_rent_collected_percentage: Union[str, None]

@dataclass
class MaintenanceSummaryForThreeWeeks:
    current_week_monday_date: Union[str, None]
    current_week_end_date: Union[str, None]
    current_week_open_work_orders_count: Union[str, None]
    current_week_completed_work_orders_count: Union[str, None]
    last_week_monday_date: Union[str, None]
    last_week_sunday_date: Union[str, None]
    last_week_open_work_orders_count: Union[str, None]
    last_week_completed_work_orders_count: Union[str, None]
    week_before_last_monday_date: Union[str, None]
    week_before_last_sunday_date: Union[str, None]
    week_before_last_open_work_orders_count: Union[str, None]
    week_before_last_completed_work_orders_count: Union[str, None]

@dataclass
class LeadsSummaryForThreeWeeks:
    current_week_monday_date: Union[int, str, None]
    current_week_end_date: Union[int, str, None]
    current_week_new_leads_count: Union[int, str, None]
    current_week_applications_started_count: Union[int, str, None]
    current_week_applications_completed_count: Union[int, str, None]
    current_week_approved_applications_count: Union[int, str, None]
    current_week_lease_signed_count: Union[int, str, None]
    current_week_cancelled_applications_count: Union[int, str, None]

    last_week_monday_date: Union[int, str, None]
    last_week_end_date: Union[int, str, None]
    last_week_new_leads_count: Union[int, str, None]
    last_week_applications_started_count: Union[int, str, None]
    last_week_applications_completed_count: Union[int, str, None]
    last_week_approved_applications_count: Union[int, str, None]
    last_week_lease_signed_count: Union[int, str, None]
    last_week_cancelled_applications_count: Union[int, str, None]

    week_before_last_monday_date: Union[int, str, None]
    week_before_last_end_date: Union[int, str, None]
    week_before_last_new_leads_count: Union[int, str, None]
    week_before_last_applications_started_count: Union[int, str, None]
    week_before_last_applications_completed_count: Union[int, str, None]
    week_before_last_approved_applications_count: Union[int, str, None]
    week_before_last_lease_signed_count: Union[int, str, None]
    week_before_last_cancelled_applications_count: Union[int, str, None]