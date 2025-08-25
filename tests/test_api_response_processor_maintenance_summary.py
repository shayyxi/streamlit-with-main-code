from api_response_processor import api_response_processor_maintenance_summary
from config import constants_for_testing

def test_generate_maintenance_summary():
    open_work_orders_count, completed_work_orders_count = api_response_processor_maintenance_summary.generate_maintenance_summary(
        constants_for_testing.MAINTENANCE_RESPONSE_JSON
    )
    assert open_work_orders_count == 4
    assert completed_work_orders_count == 4
    open_work_orders_count, completed_work_orders_count = api_response_processor_maintenance_summary.generate_maintenance_summary(
        constants_for_testing.BAD_RESPONSE_JSON
    )
    assert open_work_orders_count is None
    assert completed_work_orders_count is None
    open_work_orders_count, completed_work_orders_count = api_response_processor_maintenance_summary.generate_maintenance_summary(
        constants_for_testing.BAD_RESPONSE_JSON
    )
    assert open_work_orders_count is None
    assert completed_work_orders_count is None
    open_work_orders_count, completed_work_orders_count = api_response_processor_maintenance_summary.generate_maintenance_summary(
        constants_for_testing.EMPTY_RESPONSE_JSON
    )
    assert open_work_orders_count is None
    assert completed_work_orders_count is None