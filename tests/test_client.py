from api_client import api_client
import requests

def test_get_properties_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_properties()
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_properties_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_properties()
    assert result is None

def test_get_property_units_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_property_units("123")
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_property_units_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_property_units("123")
    assert result is None

def test_get_units_availability_and_pricing_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_units_availability_and_pricing("123")
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_units_availability_and_pricing_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_units_availability_and_pricing("123")
    assert result is None

def test_get_leases_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_leases("123", "4,5", None, None, None)
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_leases_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_leases("123", "4,5", None, None, None)
    assert result is None

def test_get_leases_set_both_move_in_and_out_time(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_leases("123", "4,5", True, True, True)
    assert result == None

def test_get_lease_artransactions_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_lease_artransactions("123", "123", "123")
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_lease_artransactions_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_lease_artransactions("123", "123", "123")
    assert result is None

def test_get_leads_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_leads("123", "1234", "1234")
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_leads_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_leads("123", "1234", "1234")
    assert result is None

def test_get_maintenance_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_maintenance("123", "1234", "1234")
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_maintenance_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_maintenance("123", "1234", "1234")
    assert result is None

def test_get_leases_with_expiry_date_filter_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_leases_with_expiry_date_range("123", "1234", "1234")
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_leases_with_expiry_date_filter_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_leases_with_expiry_date_range("123", "123", "123")
    assert result is None

def test_get_expiring_leases_with_date_range_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": "some_property_data"}
    mock_response.status_code = 200
    mocker.patch("api_client.api_client.requests.post", return_value=mock_response)
    result = api_client.get_leases_with_expiry_date_range("123", "1234", "1234")
    assert result == {"data": "some_property_data"}
    assert mock_response.status_code == 200

def test_get_expiring_leases_with_date_range_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 500
    mocker.patch("api_client.api_client.requests.post", side_effect=requests.exceptions.RequestException("API failure"))
    result = api_client.get_leases_with_expiry_date_range("123", "123", "123")
    assert result is None