from metrics_persistence.metrics_persistence import MetricsPersistence
from config import constants_for_testing
from api_response_processor import data_classes
from freezegun import freeze_time

def test_create_table_if_not_exist(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mocker.patch("metrics_persistence.metrics_persistence.psycopg2.connect", return_value=mock_conn)
    MetricsPersistence(constants_for_testing.db_config)
    mock_conn.cursor.assert_called_once()
    assert mock_cursor.execute.call_count == 2
    mock_conn.commit.assert_called_once()

@freeze_time("2025-07-25")
def test_insert_property_metrics_if_day_is_friday(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mocker.patch("metrics_persistence.metrics_persistence.psycopg2.connect", return_value=mock_conn)
    persistence = MetricsPersistence(constants_for_testing.db_config)
    persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(
        property_id=1,
        data=constants_for_testing.fake_data_for_db,
        summary_table_name="property_summary"
    )
    assert mock_cursor.execute.called
    assert mock_conn.commit.called
    assert mock_cursor.execute.call_count == 3
    assert mock_conn.commit.call_count == 2

@freeze_time("2025-07-24")
def test_insert_property_metrics_if_day_is_not_friday(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mocker.patch("metrics_persistence.metrics_persistence.psycopg2.connect", return_value=mock_conn)
    persistence = MetricsPersistence(constants_for_testing.db_config)
    fake_data = data_classes.PropertySummary(
        total_units=1,
        total_rentable_units=1,
        excluded_units=1,
        preleased_units=1,
        occupied_units_percentage=1,
        preleased_units_percentage=1,
        evictions_filed=1,
        evictions_and_skips_occurred_for_current_month=1
    )
    persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(
        property_id=1,
        data=constants_for_testing.fake_data_for_db,
        summary_table_name="property_summary"
    )
    assert mock_cursor.execute.called
    assert mock_conn.commit.called
    assert mock_cursor.execute.call_count == 2
    assert mock_conn.commit.call_count == 1

@freeze_time("2025-07-24")
def test_insert_property_metrics_if_data_is_none(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mocker.patch("metrics_persistence.metrics_persistence.psycopg2.connect", return_value=mock_conn)
    persistence = MetricsPersistence(constants_for_testing.db_config)
    persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(
        property_id=1,
        data=None,
        summary_table_name="property_summary"
    )
    assert mock_cursor.execute.called
    assert mock_conn.commit.called
    assert mock_cursor.execute.call_count == 2
    assert mock_conn.commit.call_count == 1

@freeze_time("2025-07-24")
def test_insert_property_metrics_if_property_id_is_none(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mocker.patch("metrics_persistence.metrics_persistence.psycopg2.connect", return_value=mock_conn)
    persistence = MetricsPersistence(constants_for_testing.db_config)
    persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(
        property_id=None,
        data=constants_for_testing.fake_data_for_db,
        summary_table_name="property_summary"
    )
    assert mock_cursor.execute.called
    assert mock_conn.commit.called
    assert mock_cursor.execute.call_count == 2
    assert mock_conn.commit.call_count == 1

@freeze_time("2025-07-25")
def test_insert_property_metrics_if_summary_table_name_is_wrong(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mocker.patch("metrics_persistence.metrics_persistence.psycopg2.connect", return_value=mock_conn)
    persistence = MetricsPersistence(constants_for_testing.db_config)
    persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(
        property_id=123,
        data=constants_for_testing.fake_data_for_db,
        summary_table_name="somewhat"
    )
    assert mock_cursor.execute.called
    assert mock_conn.commit.called
    assert mock_cursor.execute.call_count == 2
    assert mock_conn.commit.call_count == 1
