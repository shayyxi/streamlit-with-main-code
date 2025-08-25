"""
API Response Processor for generating maintenance summary data
"""
from api_client import api_client
from api_response_processor import helpers, data_classes


def get_maintenance_summary(property_id):
    """
    method for calling the APIs, providing the API responses to process,
    and giving back the maintenance work order summary data
    """
    current_week, last_week, week_before_last = helpers.generate_start_and_end_dates_for_three_weeks()
    maintenance_api_response_for_current_week = api_client.get_maintenance(property_id,
                                                                           current_week[0].strftime("%m/%d/%Y"),
                                                                           current_week[1].strftime("%m/%d/%Y"))
    maintenance_api_response_for_last_week = api_client.get_maintenance(property_id,
                                                                        last_week[0].strftime("%m/%d/%Y"),
                                                                        last_week[1].strftime("%m/%d/%Y"))
    maintenance_api_response_for_week_before_last = api_client.get_maintenance(property_id,
                                                                               week_before_last[0].strftime("%m/%d/%Y"),
                                                                               week_before_last[1].strftime("%m/%d/%Y"))

    open_work_orders_for_current_week, completed_work_orders_for_current_week = generate_maintenance_summary(maintenance_api_response_for_current_week)
    open_work_orders_for_last_week, completed_work_orders_for_last_week = generate_maintenance_summary(maintenance_api_response_for_last_week)
    open_work_orders_for_week_before_last, completed_work_orders_for_week_before_last = generate_maintenance_summary(maintenance_api_response_for_week_before_last)
    maintenance_summary_for_three_weeks = data_classes.MaintenanceSummaryForThreeWeeks(
        current_week[0].strftime("%m/%d/%Y"),
        current_week[1].strftime("%m/%d/%Y"),
        open_work_orders_for_current_week,
        completed_work_orders_for_current_week,
        last_week[0].strftime("%m/%d/%Y"),
        last_week[1].strftime("%m/%d/%Y"),
        open_work_orders_for_last_week,
        completed_work_orders_for_last_week,
        week_before_last[0].strftime("%m/%d/%Y"),
        week_before_last[1].strftime("%m/%d/%Y"),
        open_work_orders_for_week_before_last,
        completed_work_orders_for_week_before_last,
    )
    print("Calculated the maintenance summary for " + f"{property_id}")
    return maintenance_summary_for_three_weeks

def generate_maintenance_summary(maintenance_api_response):
    """
    method for generating the maintenance summary data
    """
    work_orders = helpers.get_work_orders_from_maintenance_response_json(maintenance_api_response)
    if work_orders is None:
        return None, None
    open_work_orders = 0
    completed_work_orders = 0
    for work_order in work_orders:
        work_order_status = work_order["maintenanceStatus"]
        if work_order_status == "Open":
            open_work_orders += 1
        elif work_order_status == "Completed":
            completed_work_orders += 1
    return open_work_orders, completed_work_orders
