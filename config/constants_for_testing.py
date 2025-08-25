from api_response_processor import data_classes

PROPERTY_UNITS_RESPONSE_JSON = {
    "response": {
        "requestId": "15",
        "code": 200,
        "result": {
            "properties": {
                "property": [
                    {
                        "propertyId": 100082999,
                        "propertyName": "4060 Preferred Place",
                        "currencyCode": "USD",
                        "buildingCount": 0,
                        "unitCount": 153,
                        "propertyAvailabilityURL": "https://4060preferredplace.com/dallas-dallas/4060-preferred-place-texas"
                    }
                ]
            }
        }
    }
}

EMPTY_RESPONSE_JSON = {}

BAD_RESPONSE_JSON = {
    "response": {
        "requestId": "15",
        "code": 200,
        "result": "No records found with mentioned preferences."
    }
}

UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_VACANT_STATUS = {
    "response": {
        "requestId": "15",
        "code": 200,
        "result": {
            "ILS_Units": {
                "Unit": {
                    "88942": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "Vacant",
                        }
                    },
                    "88943": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "Vacant",
                        }
                    },
                    "88944": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "Vacant",
                        }
                    },
                    "88945": {
                        "@attributes": {
                            "Availability": "Available",
                            "Status": "Vacant",
                        }
                    },
                    "88946": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "Vacant",
                        }
                    },
                    "88947": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "Vacant",
                        }
                    },
                    "88948": {
                        "@attributes": {
                            "Availability": "Available",
                            "Status": "Vacant",
                        }
                    },
                }
            }
        }
    }
}

UNITS_AVAILABILITY_AND_PRICING_RESPONSE_JSON_FOR_UNITS_SUMMARY_TESTING = {
    "response": {
        "requestId": "15",
        "code": 200,
        "result": {
            "Properties": {
        "Property": [
          {
            "Floorplans": {
              "Floorplan": [
                {
                  "Name": "A1",
                  "Comment": "One bedroom One Bath",
                  "UnitCount": "50",
                  "UnitsAvailable": "3"
                },
                {
                  "Name": "A2",
                  "Comment": "One bedroom One Bath",
                  "UnitCount": "50",
                  "UnitsAvailable": "3"
                },
                {
                  "Name": "A3",
                  "Comment": "One bedroom One Bath",
                  "UnitCount": "50",
                  "UnitsAvailable": "3"
                }
              ]
            }
          }
        ]
      },
            "ILS_Units": {
                "Unit": {
                    "88942": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "On Notice (Unavailable)",
                        }
                    },
                    "88943": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "On Notice (Unvailable)",
                        }
                    },
                    "88944": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "On Notice (Unavailable)",
                        }
                    },
                    "88945": {
                        "@attributes": {
                            "Availability": "Available",
                            "Status": "On Notice (Available)",
                        }
                    },
                    "88946": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "Occupied (Unavailable)",
                        }
                    },
                    "88947": {
                        "@attributes": {
                            "Availability": "Not Available",
                            "Status": "Occupied (Unavailable)",
                        }
                    },
                    "88948": {
                        "@attributes": {
                            "Availability": "Available",
                            "Status": "Occupied (Available)",
                        }
                    },
                }
            }
        }
    }
}

LEASES_RESPONSE_JSON = {
  "response": {
    "result": {
      "leases": {
        "lease": [
          {
            "id": "397346",
            "leaseStatusTypeId": "4",
            "propertyId": "100082999",
            "leaseSubStatus": "In Collections, Skip",
            "moveInDate": "08\/14\/2024",
            "propertyName": "4060 Preferred Place",
            "leaseIntervalStatus": "Current",
            "occupancyTypeId": "1",
            "occupancyType": "Conventional",
            "isMonthToMonth": 0,
            "leaseIntervalId": "300007",
            "floorPlanId": "24330",
            "floorPlanName": "B1",
            "paymentAllowanceType": "Allow All Payment Types",
            "isRenewalBlacklist": "Renewable",
            "customers": {
              "customer": [
                {
                  "id": 528368,
                  "customerType": "Primary",
                  "firstName": "Nancy",
                  "lastName": "Perez",
                  "middleName": "Kailene",
                  "nameFull": "Perez, Nancy",
                  "emailAddress": "nancykaiperez11@icloud.com",
                  "leaseCustomerStatus": "Current",
                  "relationshipName": "Primary",
                  "moveInDate": "08\/14\/2024",
                  "paymentAllowanceType": "Allow All Payment Types",
                  "addresses": {
                    "address": [
                      {
                        "addressType": "Primary",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      },
                      {
                        "addressType": "Current",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      }
                    ]
                  },
                  "phones": {
                    "phone": [
                      {
                        "phoneTypeName": "Primary",
                        "phoneType": "mobile",
                        "phoneNumber": "+1 9454445773",
                        "countryCode": 1
                      }
                    ]
                  }
                }
              ]
            },
            "unitId": "88816",
            "unitSpaces": {
              "unitSpace": [
                {
                  "unitSpaceId": 97264,
                  "unitSpace": "111"
                }
              ]
            },
            "scheduledCharges": {
              "scheduledCharge": [
                {
                  "id": "1165995",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29567",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Washer \/ Dryer Owned",
                  "amount": "50.00",
                  "chargeUsage": "Add-On",
                  "description": "Washer \/ Dryer Owned"
                },
                {
                  "id": "1164577",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "28479",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "Base Rent",
                  "chargeCode": "Rent",
                  "amount": "1470.00",
                  "chargeUsage": "Base",
                  "description": "Rent"
                },
                {
                  "id": "1244235",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29472",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Trash",
                  "amount": "11.00",
                  "chargeUsage": "Base",
                  "description": "Trash"
                },
                {
                  "id": "1244236",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29566",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Pest Control",
                  "amount": "5.00",
                  "chargeUsage": "Base",
                  "description": "Pest Control"
                }
              ]
            },
            "leaseIntervals": {
              "leaseInterval": [
                {
                  "id": 300007,
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "leaseIntervalTypeId": 1,
                  "leaseIntervalTypeName": "Application",
                  "leaseIntervalStatusTypeId": 4,
                  "leaseIntervalStatusTypeName": "Current",
                  "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                  "applicationId": "293292",
                  "intervalDateTime": "03\/21\/2025 14:53:57.725277 MDT",
                  "applications": {
                    "application": [
                      {
                        "id": "293292",
                        "leaseApprovedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseCompletedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseTerm": "12 months",
                        "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                        "leaseIntervalTypeId": 1,
                        "isActiveLeaseInterval": "t",
                        "propertyFloorPlanId": "24330",
                        "leaseStartDate": "08\/14\/2024",
                        "leaseEndDate": "08\/13\/2025"
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "id": "397346",
            "leaseStatusTypeId": "4",
            "propertyId": "100082999",
            "leaseSubStatus": "In Collections, Eviction",
            "moveInDate": "08\/14\/2024",
            "propertyName": "4060 Preferred Place",
            "leaseIntervalStatus": "Current",
            "occupancyTypeId": "1",
            "occupancyType": "Conventional",
            "isMonthToMonth": 0,
            "leaseIntervalId": "300007",
            "floorPlanId": "24330",
            "floorPlanName": "B1",
            "paymentAllowanceType": "Allow All Payment Types",
            "isRenewalBlacklist": "Renewable",
            "customers": {
              "customer": [
                {
                  "id": 528368,
                  "customerType": "Primary",
                  "firstName": "Nancy",
                  "lastName": "Perez",
                  "middleName": "Kailene",
                  "nameFull": "Perez, Nancy",
                  "emailAddress": "nancykaiperez11@icloud.com",
                  "leaseCustomerStatus": "Current",
                  "relationshipName": "Primary",
                  "moveInDate": "08\/14\/2024",
                  "paymentAllowanceType": "Allow All Payment Types",
                  "addresses": {
                    "address": [
                      {
                        "addressType": "Primary",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      },
                      {
                        "addressType": "Current",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      }
                    ]
                  },
                  "phones": {
                    "phone": [
                      {
                        "phoneTypeName": "Primary",
                        "phoneType": "mobile",
                        "phoneNumber": "+1 9454445773",
                        "countryCode": 1
                      }
                    ]
                  }
                }
              ]
            },
            "unitId": "88816",
            "unitSpaces": {
              "unitSpace": [
                {
                  "unitSpaceId": 97264,
                  "unitSpace": "111"
                }
              ]
            },
            "scheduledCharges": {
              "scheduledCharge": [
                {
                  "id": "1165995",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29567",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Washer \/ Dryer Owned",
                  "amount": "50.00",
                  "chargeUsage": "Add-On",
                  "description": "Washer \/ Dryer Owned"
                },
                {
                  "id": "1164577",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "28479",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "Base Rent",
                  "chargeCode": "Rent",
                  "amount": "1470.00",
                  "chargeUsage": "Base",
                  "description": "Rent"
                },
                {
                  "id": "1244235",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29472",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Trash",
                  "amount": "11.00",
                  "chargeUsage": "Base",
                  "description": "Trash"
                },
                {
                  "id": "1244236",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29566",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Pest Control",
                  "amount": "5.00",
                  "chargeUsage": "Base",
                  "description": "Pest Control"
                }
              ]
            },
            "leaseIntervals": {
              "leaseInterval": [
                {
                  "id": 300007,
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "leaseIntervalTypeId": 1,
                  "leaseIntervalTypeName": "Application",
                  "leaseIntervalStatusTypeId": 4,
                  "leaseIntervalStatusTypeName": "Current",
                  "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                  "applicationId": "293292",
                  "intervalDateTime": "03\/21\/2025 14:53:57.725277 MDT",
                  "applications": {
                    "application": [
                      {
                        "id": "293292",
                        "leaseApprovedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseCompletedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseTerm": "12 months",
                        "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                        "leaseIntervalTypeId": 1,
                        "isActiveLeaseInterval": "t",
                        "propertyFloorPlanId": "24330",
                        "leaseStartDate": "08\/14\/2024",
                        "leaseEndDate": "08\/13\/2025"
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "id": "397346",
            "leaseStatusTypeId": "4",
            "propertyId": "100082999",
            "leaseSubStatus": "Eviction, In collections",
            "moveInDate": "08\/14\/2024",
            "propertyName": "4060 Preferred Place",
            "leaseIntervalStatus": "Current",
            "occupancyTypeId": "1",
            "occupancyType": "Conventional",
            "isMonthToMonth": 0,
            "leaseIntervalId": "300007",
            "floorPlanId": "24330",
            "floorPlanName": "B1",
            "paymentAllowanceType": "Allow All Payment Types",
            "isRenewalBlacklist": "Renewable",
            "customers": {
              "customer": [
                {
                  "id": 528368,
                  "customerType": "Primary",
                  "firstName": "Nancy",
                  "lastName": "Perez",
                  "middleName": "Kailene",
                  "nameFull": "Perez, Nancy",
                  "emailAddress": "nancykaiperez11@icloud.com",
                  "leaseCustomerStatus": "Current",
                  "relationshipName": "Primary",
                  "moveInDate": "08\/14\/2024",
                  "paymentAllowanceType": "Allow All Payment Types",
                  "addresses": {
                    "address": [
                      {
                        "addressType": "Primary",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      },
                      {
                        "addressType": "Current",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      }
                    ]
                  },
                  "phones": {
                    "phone": [
                      {
                        "phoneTypeName": "Primary",
                        "phoneType": "mobile",
                        "phoneNumber": "+1 9454445773",
                        "countryCode": 1
                      }
                    ]
                  }
                }
              ]
            },
            "unitId": "88816",
            "unitSpaces": {
              "unitSpace": [
                {
                  "unitSpaceId": 97264,
                  "unitSpace": "111"
                }
              ]
            },
            "scheduledCharges": {
              "scheduledCharge": [
                {
                  "id": "1165995",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29567",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Washer \/ Dryer Owned",
                  "amount": "50.00",
                  "chargeUsage": "Add-On",
                  "description": "Washer \/ Dryer Owned"
                },
                {
                  "id": "1164577",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "28479",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "Base Rent",
                  "chargeCode": "Rent",
                  "amount": "1470.00",
                  "chargeUsage": "Base",
                  "description": "Rent"
                },
                {
                  "id": "1244235",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29472",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Trash",
                  "amount": "11.00",
                  "chargeUsage": "Base",
                  "description": "Trash"
                },
                {
                  "id": "1244236",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29566",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Pest Control",
                  "amount": "5.00",
                  "chargeUsage": "Base",
                  "description": "Pest Control"
                }
              ]
            },
            "leaseIntervals": {
              "leaseInterval": [
                {
                  "id": 300007,
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "leaseIntervalTypeId": 1,
                  "leaseIntervalTypeName": "Application",
                  "leaseIntervalStatusTypeId": 4,
                  "leaseIntervalStatusTypeName": "Current",
                  "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                  "applicationId": "293292",
                  "intervalDateTime": "03\/21\/2025 14:53:57.725277 MDT",
                  "applications": {
                    "application": [
                      {
                        "id": "293292",
                        "leaseApprovedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseCompletedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseTerm": "12 months",
                        "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                        "leaseIntervalTypeId": 1,
                        "isActiveLeaseInterval": "t",
                        "propertyFloorPlanId": "24330",
                        "leaseStartDate": "08\/14\/2024",
                        "leaseEndDate": "08\/13\/2025"
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "id": "397346",
            "leaseStatusTypeId": "4",
            "propertyId": "100082999",
            "leaseSubStatus": "Eviction",
            "moveInDate": "08\/14\/2024",
            "propertyName": "4060 Preferred Place",
            "leaseIntervalStatus": "Current",
            "occupancyTypeId": "1",
            "occupancyType": "Conventional",
            "isMonthToMonth": 0,
            "leaseIntervalId": "300007",
            "floorPlanId": "24330",
            "floorPlanName": "B1",
            "paymentAllowanceType": "Allow All Payment Types",
            "isRenewalBlacklist": "Renewable",
            "customers": {
              "customer": [
                {
                  "id": 528368,
                  "customerType": "Primary",
                  "firstName": "Nancy",
                  "lastName": "Perez",
                  "middleName": "Kailene",
                  "nameFull": "Perez, Nancy",
                  "emailAddress": "nancykaiperez11@icloud.com",
                  "leaseCustomerStatus": "Current",
                  "relationshipName": "Primary",
                  "moveInDate": "08\/14\/2024",
                  "paymentAllowanceType": "Allow All Payment Types",
                  "addresses": {
                    "address": [
                      {
                        "addressType": "Primary",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      },
                      {
                        "addressType": "Current",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      }
                    ]
                  },
                  "phones": {
                    "phone": [
                      {
                        "phoneTypeName": "Primary",
                        "phoneType": "mobile",
                        "phoneNumber": "+1 9454445773",
                        "countryCode": 1
                      }
                    ]
                  }
                }
              ]
            },
            "unitId": "88816",
            "unitSpaces": {
              "unitSpace": [
                {
                  "unitSpaceId": 97264,
                  "unitSpace": "111"
                }
              ]
            },
            "scheduledCharges": {
              "scheduledCharge": [
                {
                  "id": "1165995",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29567",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Washer \/ Dryer Owned",
                  "amount": "50.00",
                  "chargeUsage": "Add-On",
                  "description": "Washer \/ Dryer Owned"
                },
                {
                  "id": "1164577",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "28479",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "Base Rent",
                  "chargeCode": "Rent",
                  "amount": "1470.00",
                  "chargeUsage": "Base",
                  "description": "Rent"
                },
                {
                  "id": "1244235",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29472",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Trash",
                  "amount": "11.00",
                  "chargeUsage": "Base",
                  "description": "Trash"
                },
                {
                  "id": "1244236",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29566",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Pest Control",
                  "amount": "5.00",
                  "chargeUsage": "Base",
                  "description": "Pest Control"
                }
              ]
            },
            "leaseIntervals": {
              "leaseInterval": [
                {
                  "id": 300007,
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "leaseIntervalTypeId": 1,
                  "leaseIntervalTypeName": "Application",
                  "leaseIntervalStatusTypeId": 4,
                  "leaseIntervalStatusTypeName": "Current",
                  "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                  "applicationId": "293292",
                  "intervalDateTime": "03\/21\/2025 14:53:57.725277 MDT",
                  "applications": {
                    "application": [
                      {
                        "id": "293292",
                        "leaseApprovedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseCompletedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseTerm": "12 months",
                        "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                        "leaseIntervalTypeId": 1,
                        "isActiveLeaseInterval": "t",
                        "propertyFloorPlanId": "24330",
                        "leaseStartDate": "08\/14\/2024",
                        "leaseEndDate": "08\/13\/2025"
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "id": "397346",
            "leaseStatusTypeId": "4",
            "propertyId": "100082999",
            "leaseSubStatus": "Renewed",
            "moveInDate": "08\/14\/2024",
            "propertyName": "4060 Preferred Place",
            "leaseIntervalStatus": "Current",
            "occupancyTypeId": "1",
            "occupancyType": "Conventional",
            "isMonthToMonth": 0,
            "leaseIntervalId": "300007",
            "floorPlanId": "24330",
            "floorPlanName": "B1",
            "paymentAllowanceType": "Allow All Payment Types",
            "isRenewalBlacklist": "Renewable",
            "customers": {
              "customer": [
                {
                  "id": 528368,
                  "customerType": "Primary",
                  "firstName": "Nancy",
                  "lastName": "Perez",
                  "middleName": "Kailene",
                  "nameFull": "Perez, Nancy",
                  "emailAddress": "nancykaiperez11@icloud.com",
                  "leaseCustomerStatus": "Current",
                  "relationshipName": "Primary",
                  "moveInDate": "08\/14\/2024",
                  "paymentAllowanceType": "Allow All Payment Types",
                  "addresses": {
                    "address": [
                      {
                        "addressType": "Primary",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      },
                      {
                        "addressType": "Current",
                        "streetLine": "4060 PREFERRED PL APT 111",
                        "city": "DALLAS",
                        "state": "TX",
                        "postalCode": "75237",
                        "countryName": "US"
                      }
                    ]
                  },
                  "phones": {
                    "phone": [
                      {
                        "phoneTypeName": "Primary",
                        "phoneType": "mobile",
                        "phoneNumber": "+1 9454445773",
                        "countryCode": 1
                      }
                    ]
                  }
                }
              ]
            },
            "unitId": "88816",
            "unitSpaces": {
              "unitSpace": [
                {
                  "unitSpaceId": 97264,
                  "unitSpace": "111"
                }
              ]
            },
            "scheduledCharges": {
              "scheduledCharge": [
                {
                  "id": "1165995",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29567",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Washer \/ Dryer Owned",
                  "amount": "50.00",
                  "chargeUsage": "Add-On",
                  "description": "Washer \/ Dryer Owned"
                },
                {
                  "id": "1164577",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "28479",
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "chargeType": "Base Rent",
                  "chargeCode": "Rent",
                  "amount": "1470.00",
                  "chargeUsage": "Base",
                  "description": "Rent"
                },
                {
                  "id": "1244235",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29472",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Trash",
                  "amount": "11.00",
                  "chargeUsage": "Base",
                  "description": "Trash"
                },
                {
                  "id": "1244236",
                  "frequency": "Monthly",
                  "leaseIntervalId": "300007",
                  "chargeCodeId": "29566",
                  "startDate": "04\/01\/2025",
                  "endDate": "08\/13\/2025",
                  "chargeType": "other",
                  "chargeCode": "Pest Control",
                  "amount": "5.00",
                  "chargeUsage": "Base",
                  "description": "Pest Control"
                }
              ]
            },
            "leaseIntervals": {
              "leaseInterval": [
                {
                  "id": 300007,
                  "startDate": "08\/14\/2024",
                  "endDate": "08\/13\/2025",
                  "leaseIntervalTypeId": 1,
                  "leaseIntervalTypeName": "Application",
                  "leaseIntervalStatusTypeId": 4,
                  "leaseIntervalStatusTypeName": "Current",
                  "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                  "applicationId": "293292",
                  "intervalDateTime": "03\/21\/2025 14:53:57.725277 MDT",
                  "applications": {
                    "application": [
                      {
                        "id": "293292",
                        "leaseApprovedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseCompletedOn": "08\/13\/2024 00:00:00 MDT",
                        "leaseTerm": "12 months",
                        "applicationCompletedOn": "07\/15\/2024 00:00:00 MDT",
                        "leaseIntervalTypeId": 1,
                        "isActiveLeaseInterval": "t",
                        "propertyFloorPlanId": "24330",
                        "leaseStartDate": "08\/14\/2024",
                        "leaseEndDate": "08\/13\/2025"
                      }
                    ]
                  }
                }
              ]
            }
          }
        ]
      }
    }
  }
}

PROPERTIES_RESPONSE_JSON = {
"response": {
        "requestId": "15",
        "code": 200,
        "result": {
            "PhysicalProperty": {
                "Property": [
                    {
                    "MarketingName": "abc",
                    "PropertyID": 1234
                    },
                    {
                    "MarketingName": "def",
                    "PropertyID": 2345
                    },
                    {
                    "MarketingName": "ghi",
                    "PropertyID": 4567
                    },
                ]
            }
        }
    }
}

LEASE_ARTRANSACTIONS_RESPONSE_JSON = {
"response": {
        "requestId": "15",
        "code": 200,
        "result": {
            "leases": {
                "lease": [
                    {
                        "id": 397478,
                        "propertyId": 100082999,
                        "currencyCode": "USD",
                        "unitSpaceId": "97398",
                        "customers": {
                            "customer": [
                                {
                                    "id": 528493,
                                    "firstName": "Brittani",
                                    "lastName": "Mcleggan"
                                }
                            ]
                        },
                        "ledgers": {
                            "ledger": [
                                {
                                    "id": 8979,
                                    "name": "Resident",
                                    "balance": 1125.86,
                                    "pastDueBalance": 1090.86,
                                    "writeOff": 0,
                                    "transactions": {
                                        "transaction": [
                                            {
                                                "id": 33638608,
                                                "transactionTypeId": "2",
                                                "arCodeId": 28479,
                                                "arCodeName": "Rent",
                                                "leaseIntervalId": 444584,
                                                "description": "Posted from 07/31/2025 to 07/31/2025",
                                                "transactionDate": "06/30/2025",
                                                "postDate": "07/31/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/31/2025",
                                                "arTriggerId": 307,
                                                "balanceDue": 35,
                                                "amount": 35,
                                                "amountPaid": 0,
                                                "scheduledChargeId": 2122659
                                            },
                                            {
                                                "id": 33897329,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29471,
                                                "arCodeName": "Water/Sewer",
                                                "leaseIntervalId": 300146,
                                                "description": "Water From 05/14/2025 To 06/17/2025",
                                                "transactionDate": "07/01/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 501,
                                                "balanceDue": 17,
                                                "amount": 17,
                                                "amountPaid": 0
                                            },
                                            {
                                                "id": 33897306,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29471,
                                                "arCodeName": "Water/Sewer",
                                                "leaseIntervalId": 300146,
                                                "description": "Sewer From 05/14/2025 To 06/17/2025",
                                                "transactionDate": "07/01/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 504,
                                                "balanceDue": 10.55,
                                                "amount": 10.55,
                                                "amountPaid": 0
                                            },
                                            {
                                                "id": 33897281,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29564,
                                                "arCodeName": "Utility Billing Service",
                                                "leaseIntervalId": 300146,
                                                "description": "Stormwater Billing Fee",
                                                "transactionDate": "07/01/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 517,
                                                "balanceDue": 3,
                                                "amount": 3,
                                                "amountPaid": 0
                                            },
                                            {
                                                "id": 33897252,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29471,
                                                "arCodeName": "Water/Sewer",
                                                "leaseIntervalId": 300146,
                                                "description": "Stormwater From 05/14/2025 To 06/17/2025",
                                                "transactionDate": "07/01/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 517,
                                                "balanceDue": 2.62,
                                                "amount": 2.62,
                                                "amountPaid": 0
                                            },
                                            {
                                                "id": 33897224,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29564,
                                                "arCodeName": "Utility Billing Service",
                                                "leaseIntervalId": 300146,
                                                "description": "Gas Billing Fee",
                                                "transactionDate": "07/01/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 502,
                                                "balanceDue": 3,
                                                "amount": 3,
                                                "amountPaid": 0
                                            },
                                            {
                                                "id": 33897170,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29473,
                                                "arCodeName": "Gas",
                                                "leaseIntervalId": 300146,
                                                "description": "Gas From 05/08/2025 To 06/09/2025",
                                                "transactionDate": "07/01/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 502,
                                                "balanceDue": 17.69,
                                                "amount": 17.69,
                                                "amountPaid": 0
                                            },
                                            {
                                                "id": 33061178,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29472,
                                                "arCodeName": "Trash",
                                                "leaseIntervalId": 300146,
                                                "description": "Posted from 07/01/2025 to 07/30/2025",
                                                "transactionDate": "06/27/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 307,
                                                "balanceDue": 11,
                                                "amount": 11,
                                                "amountPaid": 0,
                                                "scheduledChargeId": 1246585
                                            },
                                            {
                                                "id": 33061177,
                                                "transactionTypeId": "2",
                                                "arCodeId": 28479,
                                                "arCodeName": "Rent",
                                                "leaseIntervalId": 300146,
                                                "description": "Posted from 07/01/2025 to 07/30/2025",
                                                "transactionDate": "06/27/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 307,
                                                "balanceDue": 1021,
                                                "amount": 1021,
                                                "amountPaid": 0,
                                                "scheduledChargeId": 1164923
                                            },
                                            {
                                                "id": 33061174,
                                                "transactionTypeId": "3",
                                                "arCodeId": 29566,
                                                "arCodeName": "Pest Control",
                                                "leaseIntervalId": 300146,
                                                "description": "Posted from 07/01/2025 to 07/30/2025",
                                                "transactionDate": "06/27/2025",
                                                "postDate": "07/01/2025",
                                                "postMonth": "07/01/2025",
                                                "isTemporary": 0,
                                                "dueDate": "07/01/2025",
                                                "arTriggerId": 307,
                                                "balanceDue": 5,
                                                "amount": 5,
                                                "amountPaid": 0,
                                                "scheduledChargeId": 1246586
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}

LEASES_RESPONSE_JSON_FOR_RESIDENT_RETENTION_SUMMARY = {
"response": {
    "result": {
      "leases": {
        "lease": [
            {
                "leaseSubStatus": "In Collections, Skip",
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseSubStatus": "Eviction",
                "leaseIntervalStatus": "Notice",
            },
            {
                "leaseSubStatus": "Eviction",
                "leaseIntervalStatus": "Notice",
            },
            {
                "leaseSubStatus": "Non renewal",
                "leaseIntervalStatus": "Notice",
            },
            {
                "leaseSubStatus": "Non renewal",
                "leaseIntervalStatus": "Notice",
            },
            {
                "leaseSubStatus": "Month To Month",
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseSubStatus": "Month To Month",
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseSubStatus": "Renewed",
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseSubStatus": "Renewed",
                "leaseIntervalStatus": "Current",
            },
        ]
      }
    }
  }
}

LEASES_RESPONSE_JSON_WITH_EXPIRY_DATE_FILTER = {
"response": {
    "result": {
      "leases": {
        "lease": [
            {
                "leaseIntervalStatus": "Current",
                "leaseSubStatus": "Renewed",
            },
            {
                "leaseIntervalStatus": "Current",
                "leaseSubStatus": "Renewed",
            },
            {
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseIntervalStatus": "Current",
            },
        ]
      }
    }
  }
}

EXPIRING_LEASES_RESPONSE_JSON = {
"response": {
    "result": {
      "Leases": {
        "Lease": [
            {
                "leaseIntervalStatus": "Current",
            },
            {
                "leaseIntervalStatus": "Current",
            },
        ]
      }
    }
  }
}

LEADS_RESPONSE_JSON = {
"response": {
    "result": {
       "prospects": [
                {
                    "prospect": [
                        {
                            "status": "Guest Card Completed",
                        },
                        {
                            "status": "Guest Card Cancelled",
                        },
                        {
                            "status": "Application Started",
                        },
                        {
                            "status": "Application Started",
                        },
                        {
                            "status": "Application Approved",
                        },
                        {
                            "status": "Application Cancelled",
                        },

                    ]
                }
        ]
    }
}
}

MAINTENANCE_RESPONSE_JSON = {
"response": {
        "requestId": "15",
        "code": 200,
        "result": {
            "workOrders": {
                "workOrder": [
                    {
                        "maintenanceStatus": "Completed"
                    },
                    {
                        "maintenanceStatus": "Completed"
                    },
                    {
                        "maintenanceStatus": "Completed"
                    },
                    {
                        "maintenanceStatus": "Completed"
                    },
                    {
                        "maintenanceStatus": "Open"
                    },
                    {
                        "maintenanceStatus": "Open"
                    },
                    {
                        "maintenanceStatus": "Open"
                    },
                    {
                        "maintenanceStatus": "Open"
                    }
                ]
            }
        }
}
}

db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "secret",
    "host": "localhost",
    "port": "5432"
}

fake_data_for_db = data_classes.PropertySummary(
        total_units=1,
        total_rentable_units=1,
        excluded_units=1,
        preleased_units=1,
        occupied_units_percentage=1,
        preleased_units_percentage=1,
        evictions_filed=1,
        evictions_and_skips_occurred_for_current_month=1
)