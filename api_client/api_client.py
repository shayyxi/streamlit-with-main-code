"""
API Client file, Calls Entrata APIs
"""
import calendar
import copy
import os
from datetime import datetime
import requests
from config import constants

def get_properties():
    """
    Get Properties method, call the get properties API to fetch the list of properties
    """
    headers = get_headers()
    try:
        response = requests.post(constants.PROPERTIES_ENDPOINT,
                                 json=constants.GET_PROPERTIES_DATA,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()

        print('Error in calling get properties endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def get_property_units(property_id):
    """
    Get Property units method, call the property units API to fetch the count of units
    """
    headers = get_headers()
    body = copy.deepcopy(constants.GET_PROPERTY_UNITS_DATA)
    body["method"]["params"]["propertyIds"] = property_id
    try:
        response = requests.post(constants.PROPERTY_UNITS_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get property units endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def get_units_availability_and_pricing(property_id):
    """
    Get Property units availability and pricing method,
    call the property units API to fetch the list of units and their details
    """
    headers = get_headers()
    body = copy.deepcopy(constants.GET_UNITS_AVAILABILITY_AND_PRICING_DATA)
    body["method"]["params"]["propertyId"] = property_id
    try:
        response = requests.post(constants.PROPERTY_UNITS_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling units availability and pricing endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def get_leases(property_id,
               lease_status_type_ids,
               set_move_out_date_for_current_month,
               set_move_in_date_for_current_month,
               till_today):
    """
    Get Leases method, call the leases API to fetch the list of leases and their details
    """
    headers = get_headers()
    if set_move_out_date_for_current_month and set_move_in_date_for_current_month:
        print('Error:', "can't set both move in and move out dates")
        return None
    body = copy.deepcopy(constants.GET_LEASES_DATA)
    body["method"]["params"]["propertyId"] = property_id
    if lease_status_type_ids is not None:
        body["method"]["params"]["leaseStatusTypeIds"] = lease_status_type_ids
    body["method"]["params"]["includeOtherIncomeLeases"] = 1
    if set_move_out_date_for_current_month:
        now = datetime.now()
        move_out_date_from = f"{now.month:02d}/01/{now.year}"
        if till_today:
            move_out_date_to = f"{now.month:02d}/{now.day:02d}/{now.year}"
        else:
            last_day = calendar.monthrange(now.year, now.month)[1]
            move_out_date_to = f"{now.month:02d}/{last_day:02d}/{now.year}"
        body["method"]["params"]["moveOutDateFrom"] = move_out_date_from
        body["method"]["params"]["moveOutDateTo"] = move_out_date_to
    if set_move_in_date_for_current_month:
        now = datetime.now()
        move_in_date_from = f"{now.month:02d}/01/{now.year}"
        if till_today:
            move_in_date_to = f"{now.month:02d}/{now.day:02d}/{now.year}"
        else:
            last_day = calendar.monthrange(now.year, now.month)[1]
            move_in_date_to = f"{now.month:02d}/{last_day:02d}/{now.year}"
        body["method"]["params"]["moveInDateFrom"] = move_in_date_from
        body["method"]["params"]["moveInDateTo"] = move_in_date_to
    try:
        response = requests.post(constants.LEASES_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get leases endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None
# adjust the dates for the transaction depending when the transactions are posted in the ledger
def get_lease_artransactions(property_id, from_date, to_date):
    """
    Get Leases Ar Transactions method,
    call the leases ar transactions API to fetch the transaction details of the leases
    """
    headers = get_headers()
    body = copy.deepcopy(constants.GET_LEASE_ARTRANSACTIONS_DATA)
    body["method"]["params"]["propertyId"] = property_id
    body["method"]["params"]["transactionFromDate"] = from_date
    body["method"]["params"]["transactionToDate"] = to_date
    body["method"]["params"]["includeOtherIncomeLeases"] = 1
    body["method"]["params"]["leaseStatusTypeIds"] = "4,5"
    try:
        response = requests.post(constants.LEASE_ARTRANSACTIONS_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get lease ar transactions endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

def get_leads(property_id, from_date, to_date):
    """
    Get Leads method,
    call the leads API to fetch the leads activity details
    """
    # from date, to date, should MM/DD/YYYY
    headers = get_headers()
    body = copy.deepcopy(constants.GET_LEADS_DATA)
    body["method"]["params"]["propertyId"] = property_id
    body["method"]["params"]["fromDate"] = from_date
    body["method"]["params"]["toDate"] = to_date
    try:
        response = requests.post(constants.LEADS_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get leads endpoint:', response.status_code)
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

def get_maintenance(property_id, from_date, to_date):
    """
    Get Maintenance Work Orders method,
    call the maintenance API to fetch the work order details,
    if the is_current_month is true, gives the data for current month
    else gives the data for previous three months
    """
    # from date, to date, should MM/DD/YYYY
    headers = get_headers()
    body = copy.deepcopy(constants.GET_MAINTENANCE_DATA)
    body["method"]["params"]["propertyId"] = property_id
    body["method"]["params"]["createdOnFromDate"] = from_date
    body["method"]["params"]["createdOnToDate"] = to_date
    body["method"]["params"]["workOrderTypeIds"] = "2" # only service request
    try:
        response = requests.post(constants.MAINTENANCE_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get maintenance endpoint:', response.status_code)
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

def get_leases_with_expiry_date_range(property_id, expiring_date_from, expiring_date_to):
    """
    Get Leases method, call the leases API to fetch the list of leases based on expiring date
    """
    headers = get_headers()
    body = copy.deepcopy(constants.GET_LEASES_DATA)
    body["method"]["params"]["propertyId"] = property_id
    body["method"]["params"]["leaseExpiringDateFrom"] = expiring_date_from
    body["method"]["params"]["leaseExpiringDateTo"] = expiring_date_to
    try:
        response = requests.post(constants.LEASES_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get leases endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

def get_expiring_leases_with_date_range(property_id, from_date, to_date):
    """
    Get expiring leases method, call the expiring leases API to fetch the list of expiring leases
    """
    headers = get_headers()
    body = copy.deepcopy(constants.GET_EXPIRING_LEASES_DATA)
    body["method"]["params"]["propertyId"] = property_id
    body["method"]["params"]["fromDate"] = from_date
    body["method"]["params"]["toDate"] = to_date
    try:
        response = requests.post(constants.LEASES_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get expiring leases endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

def get_leases_with_move_in_date_range(property_id, from_date, to_date):
    """
    Get Leases method, call the leases API to fetch the list of leases based on move in date range
    """
    headers = get_headers()
    body = copy.deepcopy(constants.GET_LEASES_DATA)
    body["method"]["params"]["propertyId"] = property_id
    body["method"]["params"]["moveInDateFrom"] = from_date
    body["method"]["params"]["moveInDateTo"] = to_date
    try:
        response = requests.post(constants.LEASES_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get leases endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

def get_leases_with_move_out_date_range(property_id, from_date, to_date):
    """
    Get leases method, call the leases API to fetch the list of leases based on moving out date range
    """
    headers = get_headers()
    body = copy.deepcopy(constants.GET_LEASES_DATA)
    body["method"]["params"]["propertyId"] = property_id
    body["method"]["params"]["moveOutDateFrom"] = from_date
    body["method"]["params"]["moveOutDateTo"] = to_date
    try:
        response = requests.post(constants.LEASES_ENDPOINT,
                                 json=body,
                                 headers=headers,
                                 timeout=60)
        if response.status_code == 200:
            return response.json()
        print('Error in calling get leases endpoint:', response.status_code)
        print(response.json())
        return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

def get_headers():
    api_key = os.getenv("API_KEY")
    headers = copy.deepcopy(constants.HEADERS)
    headers["X-Api-Key"] = api_key
    return headers