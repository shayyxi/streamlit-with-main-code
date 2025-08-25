import datetime
from api_client import helpers

def test_get_previous_months_date_for_maintenance_data():
    date_str = "11/07/2025"
    dt = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    from_date, to_date = helpers.get_previous_months_date_for_maintenance_data(dt)
    assert from_date == "04/01/2025"
    assert to_date == "06/30/2025"

    date_str = "11/02/2025"
    dt = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    from_date, to_date = helpers.get_previous_months_date_for_maintenance_data(dt)
    assert from_date == "11/01/2024"
    assert to_date == "01/31/2025"

    date_str = "11/01/2025"
    dt = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    from_date, to_date = helpers.get_previous_months_date_for_maintenance_data(dt)
    assert from_date == "10/01/2024"
    assert to_date == "12/31/2024"