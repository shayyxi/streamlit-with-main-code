BASE_URL = "https://apis.entrata.com/ext/orgs/aamliving/v1"
HEADERS = {
    "Content-Type": "application/json",
    "X-Api-Key": ""
}
PROPERTIES_ENDPOINT = f"{BASE_URL}/properties"
PROPERTY_UNITS_ENDPOINT = f"{BASE_URL}/propertyunits"
LEASES_ENDPOINT = f"{BASE_URL}/leases"
LEASE_ARTRANSACTIONS_ENDPOINT = f"{BASE_URL}/artransactions"
LEADS_ENDPOINT = f"{BASE_URL}/leads"
MAINTENANCE_ENDPOINT = f"{BASE_URL}/maintenance"

LEASES_CURRENT_AND_NOTICE_TYPE_ID = "4,5"
LEASES_NOTICE_TYPE_ID = "5"
LEASES_PAST_TYPE_ID = "6"
UNIT_OCCUPIED_NOTICE_STATUS = ["Occupied", "On Notice"]
UNIT_OCCUPIED_STATUS = ["Occupied"]
UNIT_NOTICE_STATUS = ["On Notice"]
UNIT_VACANT_STATUS = ["Vacant"]

GET_PROPERTIES_DATA = {
    "auth": {
        "type": "apikey"
    },
    "requestId": "15",
    "method": {
        "name": "getProperties",
        "params": {
            "showAllStatus": "1"
        }
    }
}

GET_PROPERTY_UNITS_DATA = {
    "auth": {
        "type": "apikey"
    },
    "requestId": "15",
    "method": {
        "name": "getPropertyUnits",
        "params": {
            "propertyIds": ""
        }
    }
}

GET_UNITS_AVAILABILITY_AND_PRICING_DATA = {
    "auth": {
        "type": "apikey"
    },
    "requestId": "15",
    "method": {
        "name": "getUnitsAvailabilityAndPricing",
        "version": "r1",
        "params": {
            "propertyId": ""
        }
    }
}

GET_LEASES_DATA = {
    "auth": {
        "type": "apikey"
    },
    "requestId": "15",
    "method": {
        "name": "getLeases",
        "version": "r2",
        "params": {
            "propertyId": ""
        }
    }
}

GET_EXPIRING_LEASES_DATA = {
    "auth": {
        "type": "apikey"
    },
    "requestId": "15",
    "method": {
        "name": "getExpiringLeases",
        "params": {
            "propertyId": "",
            "fromDate": "",
            "toDate": "",
        }
    }
}

GET_LEASE_ARTRANSACTIONS_DATA = {
    "auth": {
        "type": "apikey"
    },
    "requestId": "15",
    "method": {
        "name": "getLeaseArTransactions",
        "version": "r1",
        "params": {
            "propertyId": "",
            "transactionFromDate": "",
            "transactionToDate": "",
        }
    }
}

GET_LEADS_DATA = {
    "auth": {
        "type": "apikey"
      },
      "requestId": "15",
      "method": {
        "name": "getLeads",
        "version": "r1",
        "params": {
          "propertyId": "",
          "fromDate": "",
          "toDate": ""
        }
    }
}

GET_MAINTENANCE_DATA = {
  "auth": {
    "type": "apikey"
  },
  "requestId": "15",
  "method": {
    "name": "getWorkOrders",
    "params": {
      "propertyId": "",
      "createdOnFromDate": "",
      "createdOnToDate": ""
    }
  }
}