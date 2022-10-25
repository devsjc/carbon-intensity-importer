APIResponse_Error = {
    "error": {
        "code": "400 Bad Request",
        "message": "Please enter a valid datetime in ISO8601 format YYYY-MM-DDThh:mmZ e.g. /intensity/2017-08-25T15:30Z"
    }
}

APIResponse_National = {
    "data": [
        {
            "from": "2019-08-25T12:30Z",
            "to": "2019-08-25T13:00Z",
            "intensity": {
                "forecast": 183,
                "actual": 178,
                "index": "moderate"
            }
        },
        {
            "from": "2019-08-25T13:00Z",
            "to": "2019-08-25T13:30Z",
            "intensity": {
                "forecast": 178,
                "actual": 176,
                "index": "moderate"
            }
        },
    ]
}

APIResponse_Regional = {
    "data": [
        {
            "from": "2019-08-25T12:30Z",
            "to": "2019-08-25T13:00Z",
            "regions": [
                {
                    "regionid": 1,
                    "dnoregion": "Scottish Hydro Electric Power Distribution",
                    "shortname": "North Scotland",
                    "intensity": {
                        "forecast": 23,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 6.2
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 33.6
                        },
                        {
                            "fuel": "solar",
                            "perc": 0
                        },
                        {
                            "fuel": "wind",
                            "perc": 60.2
                        }
                    ]
                },
                {
                    "regionid": 2,
                    "dnoregion": "SP Distribution",
                    "shortname": "South Scotland",
                    "intensity": {
                        "forecast": 5,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 1.9
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 1.3
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 63
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.1
                        },
                        {
                            "fuel": "solar",
                            "perc": 11.2
                        },
                        {
                            "fuel": "wind",
                            "perc": 22.5
                        }
                    ]
                },
                {
                    "regionid": 3,
                    "dnoregion": "Electricity North West",
                    "shortname": "North West England",
                    "intensity": {
                        "forecast": 73,
                        "index": "low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 18.9
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 70.8
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 5
                        },
                        {
                            "fuel": "wind",
                            "perc": 5.3
                        }
                    ]
                },
                {
                    "regionid": 4,
                    "dnoregion": "NPG North East",
                    "shortname": "North East England",
                    "intensity": {
                        "forecast": 19,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 17.3
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 0
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 64.6
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 15.3
                        },
                        {
                            "fuel": "wind",
                            "perc": 2.8
                        }
                    ]
                },
                {
                    "regionid": 5,
                    "dnoregion": "NPG Yorkshire",
                    "shortname": "Yorkshire",
                    "intensity": {
                        "forecast": 276,
                        "index": "high"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 23.8
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 63.4
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 8.8
                        },
                        {
                            "fuel": "wind",
                            "perc": 4
                        }
                    ]
                },
                {
                    "regionid": 6,
                    "dnoregion": "SP Manweb",
                    "shortname": "North Wales and Merseyside",
                    "intensity": {
                        "forecast": 161,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0.3
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 41.9
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 5.4
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 6.4
                        },
                        {
                            "fuel": "solar",
                            "perc": 36
                        },
                        {
                            "fuel": "wind",
                            "perc": 10
                        }
                    ]
                },
                {
                    "regionid": 7,
                    "dnoregion": "WPD South Wales",
                    "shortname": "South Wales",
                    "intensity": {
                        "forecast": 297,
                        "index": "high"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 75.6
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 22
                        },
                        {
                            "fuel": "wind",
                            "perc": 2.4
                        }
                    ]
                },
                {
                    "regionid": 8,
                    "dnoregion": "WPD West Midlands",
                    "shortname": "West Midlands",
                    "intensity": {
                        "forecast": 144,
                        "index": "low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 2.4
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 36.1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 24.6
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 3.4
                        },
                        {
                            "fuel": "solar",
                            "perc": 23.3
                        },
                        {
                            "fuel": "wind",
                            "perc": 10.2
                        }
                    ]
                },
                {
                    "regionid": 9,
                    "dnoregion": "WPD East Midlands",
                    "shortname": "East Midlands",
                    "intensity": {
                        "forecast": 266,
                        "index": "high"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 67.8
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 28.8
                        },
                        {
                            "fuel": "wind",
                            "perc": 3.4
                        }
                    ]
                },
                {
                    "regionid": 10,
                    "dnoregion": "UKPN East",
                    "shortname": "East England",
                    "intensity": {
                        "forecast": 144,
                        "index": "low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 1.6
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0.3
                        },
                        {
                            "fuel": "gas",
                            "perc": 36.1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 12.3
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 44.6
                        },
                        {
                            "fuel": "wind",
                            "perc": 5.1
                        }
                    ]
                },
                {
                    "regionid": 11,
                    "dnoregion": "WPD South West",
                    "shortname": "South West England",
                    "intensity": {
                        "forecast": 58,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 17.6
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 22.5
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 59.1
                        },
                        {
                            "fuel": "wind",
                            "perc": 0.8
                        }
                    ]
                },
                {
                    "regionid": 12,
                    "dnoregion": "SSE South",
                    "shortname": "South England",
                    "intensity": {
                        "forecast": 176,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0.7
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 44.2
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 2.9
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.1
                        },
                        {
                            "fuel": "solar",
                            "perc": 50.3
                        },
                        {
                            "fuel": "wind",
                            "perc": 1.8
                        }
                    ]
                },
                {
                    "regionid": 13,
                    "dnoregion": "UKPN London",
                    "shortname": "London",
                    "intensity": {
                        "forecast": 197,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 4.8
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 25.2
                        },
                        {
                            "fuel": "gas",
                            "perc": 36.3
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 6.8
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.4
                        },
                        {
                            "fuel": "solar",
                            "perc": 23.9
                        },
                        {
                            "fuel": "wind",
                            "perc": 2.6
                        }
                    ]
                },
                {
                    "regionid": 14,
                    "dnoregion": "UKPN South East",
                    "shortname": "South East England",
                    "intensity": {
                        "forecast": 207,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 64.5
                        },
                        {
                            "fuel": "gas",
                            "perc": 21
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.2
                        },
                        {
                            "fuel": "solar",
                            "perc": 13.6
                        },
                        {
                            "fuel": "wind",
                            "perc": 0.7
                        }
                    ]
                },
                {
                    "regionid": 15,
                    "dnoregion": "England",
                    "shortname": "England",
                    "intensity": {
                        "forecast": 168,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 4.2
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 11
                        },
                        {
                            "fuel": "gas",
                            "perc": 36.1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 17.4
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.1
                        },
                        {
                            "fuel": "solar",
                            "perc": 28.3
                        },
                        {
                            "fuel": "wind",
                            "perc": 2.9
                        }
                    ]
                },
                {
                    "regionid": 16,
                    "dnoregion": "Scotland",
                    "shortname": "Scotland",
                    "intensity": {
                        "forecast": 5,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 1.4
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 48.2
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 8.6
                        },
                        {
                            "fuel": "solar",
                            "perc": 8.6
                        },
                        {
                            "fuel": "wind",
                            "perc": 32.2
                        }
                    ]
                },
                {
                    "regionid": 17,
                    "dnoregion": "Wales",
                    "shortname": "Wales",
                    "intensity": {
                        "forecast": 253,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 64.5
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 3.3
                        },
                        {
                            "fuel": "solar",
                            "perc": 26.3
                        },
                        {
                            "fuel": "wind",
                            "perc": 5.9
                        }
                    ]
                },
                {
                    "regionid": 18,
                    "dnoregion": "GB",
                    "shortname": "GB",
                    "intensity": {
                        "forecast": 178,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 3.6
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 9.1
                        },
                        {
                            "fuel": "gas",
                            "perc": 35.6
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 18.8
                        },
                        {
                            "fuel": "other",
                            "perc": 0.3
                        },
                        {
                            "fuel": "hydro",
                            "perc": 1
                        },
                        {
                            "fuel": "solar",
                            "perc": 25.8
                        },
                        {
                            "fuel": "wind",
                            "perc": 5.8
                        }
                    ]
                }
            ]
        },
        {
            "from": "2019-08-25T13:00Z",
            "to": "2019-08-25T13:30Z",
            "regions": [
                {
                    "regionid": 1,
                    "dnoregion": "Scottish Hydro Electric Power Distribution",
                    "shortname": "North Scotland",
                    "intensity": {
                        "forecast": 33,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 5.5
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 31.9
                        },
                        {
                            "fuel": "solar",
                            "perc": 0
                        },
                        {
                            "fuel": "wind",
                            "perc": 62.6
                        }
                    ]
                },
                {
                    "regionid": 2,
                    "dnoregion": "SP Distribution",
                    "shortname": "South Scotland",
                    "intensity": {
                        "forecast": 3,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 1.9
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 0
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 63.8
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.1
                        },
                        {
                            "fuel": "solar",
                            "perc": 10.6
                        },
                        {
                            "fuel": "wind",
                            "perc": 23.6
                        }
                    ]
                },
                {
                    "regionid": 3,
                    "dnoregion": "Electricity North West",
                    "shortname": "North West England",
                    "intensity": {
                        "forecast": 69,
                        "index": "low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 17.8
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 71.7
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 4.8
                        },
                        {
                            "fuel": "wind",
                            "perc": 5.7
                        }
                    ]
                },
                {
                    "regionid": 4,
                    "dnoregion": "NPG North East",
                    "shortname": "North East England",
                    "intensity": {
                        "forecast": 17,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 15.2
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 0
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 67.4
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 14.5
                        },
                        {
                            "fuel": "wind",
                            "perc": 2.9
                        }
                    ]
                },
                {
                    "regionid": 5,
                    "dnoregion": "NPG Yorkshire",
                    "shortname": "Yorkshire",
                    "intensity": {
                        "forecast": 269,
                        "index": "high"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 26.7
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 60.6
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 8.6
                        },
                        {
                            "fuel": "wind",
                            "perc": 4.1
                        }
                    ]
                },
                {
                    "regionid": 6,
                    "dnoregion": "SP Manweb",
                    "shortname": "North Wales and Merseyside",
                    "intensity": {
                        "forecast": 145,
                        "index": "low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0.5
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 37.4
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 8.2
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 5.7
                        },
                        {
                            "fuel": "solar",
                            "perc": 35.1
                        },
                        {
                            "fuel": "wind",
                            "perc": 13.1
                        }
                    ]
                },
                {
                    "regionid": 7,
                    "dnoregion": "WPD South Wales",
                    "shortname": "South Wales",
                    "intensity": {
                        "forecast": 295,
                        "index": "high"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 75.2
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 22.2
                        },
                        {
                            "fuel": "wind",
                            "perc": 2.6
                        }
                    ]
                },
                {
                    "regionid": 8,
                    "dnoregion": "WPD West Midlands",
                    "shortname": "West Midlands",
                    "intensity": {
                        "forecast": 137,
                        "index": "low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 3
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 35.1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 25
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 3.5
                        },
                        {
                            "fuel": "solar",
                            "perc": 22.3
                        },
                        {
                            "fuel": "wind",
                            "perc": 11.1
                        }
                    ]
                },
                {
                    "regionid": 9,
                    "dnoregion": "WPD East Midlands",
                    "shortname": "East Midlands",
                    "intensity": {
                        "forecast": 264,
                        "index": "high"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 66.9
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 29
                        },
                        {
                            "fuel": "wind",
                            "perc": 4.1
                        }
                    ]
                },
                {
                    "regionid": 10,
                    "dnoregion": "UKPN East",
                    "shortname": "East England",
                    "intensity": {
                        "forecast": 146,
                        "index": "low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 2.5
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 2.7
                        },
                        {
                            "fuel": "gas",
                            "perc": 34.7
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 10.1
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 43.8
                        },
                        {
                            "fuel": "wind",
                            "perc": 6.2
                        }
                    ]
                },
                {
                    "regionid": 11,
                    "dnoregion": "WPD South West",
                    "shortname": "South West England",
                    "intensity": {
                        "forecast": 28,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 7
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 24.2
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0
                        },
                        {
                            "fuel": "solar",
                            "perc": 67.9
                        },
                        {
                            "fuel": "wind",
                            "perc": 0.9
                        }
                    ]
                },
                {
                    "regionid": 12,
                    "dnoregion": "SSE South",
                    "shortname": "South England",
                    "intensity": {
                        "forecast": 182,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 1
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 46.1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 2.7
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.1
                        },
                        {
                            "fuel": "solar",
                            "perc": 48.1
                        },
                        {
                            "fuel": "wind",
                            "perc": 2
                        }
                    ]
                },
                {
                    "regionid": 13,
                    "dnoregion": "UKPN London",
                    "shortname": "London",
                    "intensity": {
                        "forecast": 198,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 4.2
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 37.3
                        },
                        {
                            "fuel": "gas",
                            "perc": 31.1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 4.4
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.4
                        },
                        {
                            "fuel": "solar",
                            "perc": 20.3
                        },
                        {
                            "fuel": "wind",
                            "perc": 2.3
                        }
                    ]
                },
                {
                    "regionid": 14,
                    "dnoregion": "UKPN South East",
                    "shortname": "South East England",
                    "intensity": {
                        "forecast": 208,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 64.5
                        },
                        {
                            "fuel": "gas",
                            "perc": 21.3
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.2
                        },
                        {
                            "fuel": "solar",
                            "perc": 13.2
                        },
                        {
                            "fuel": "wind",
                            "perc": 0.8
                        }
                    ]
                },
                {
                    "regionid": 15,
                    "dnoregion": "England",
                    "shortname": "England",
                    "intensity": {
                        "forecast": 166,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 4.5
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 10.9
                        },
                        {
                            "fuel": "gas",
                            "perc": 35.4
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 17.7
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 0.2
                        },
                        {
                            "fuel": "solar",
                            "perc": 27.7
                        },
                        {
                            "fuel": "wind",
                            "perc": 3.6
                        }
                    ]
                },
                {
                    "regionid": 16,
                    "dnoregion": "Scotland",
                    "shortname": "Scotland",
                    "intensity": {
                        "forecast": 12,
                        "index": "very low"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 1.4
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 1
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 47.2
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 8.6
                        },
                        {
                            "fuel": "solar",
                            "perc": 7.9
                        },
                        {
                            "fuel": "wind",
                            "perc": 33.9
                        }
                    ]
                },
                {
                    "regionid": 17,
                    "dnoregion": "Wales",
                    "shortname": "Wales",
                    "intensity": {
                        "forecast": 249,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 0
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 0
                        },
                        {
                            "fuel": "gas",
                            "perc": 63.9
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 0
                        },
                        {
                            "fuel": "other",
                            "perc": 0
                        },
                        {
                            "fuel": "hydro",
                            "perc": 2.4
                        },
                        {
                            "fuel": "solar",
                            "perc": 27
                        },
                        {
                            "fuel": "wind",
                            "perc": 6.7
                        }
                    ]
                },
                {
                    "regionid": 18,
                    "dnoregion": "GB",
                    "shortname": "GB",
                    "intensity": {
                        "forecast": 176,
                        "index": "moderate"
                    },
                    "generationmix": [
                        {
                            "fuel": "biomass",
                            "perc": 3.9
                        },
                        {
                            "fuel": "coal",
                            "perc": 0
                        },
                        {
                            "fuel": "imports",
                            "perc": 9.2
                        },
                        {
                            "fuel": "gas",
                            "perc": 35
                        },
                        {
                            "fuel": "nuclear",
                            "perc": 19
                        },
                        {
                            "fuel": "other",
                            "perc": 0.3
                        },
                        {
                            "fuel": "hydro",
                            "perc": 1
                        },
                        {
                            "fuel": "solar",
                            "perc": 25.2
                        },
                        {
                            "fuel": "wind",
                            "perc": 6.4
                        }
                    ]
                }
            ]
        },
    ]
}

APIResponse_BadlyTyped = {
    "data": [
        {
            "from": "25-08-2022T12:30Z",
            "to": "2019-08-25T13:00Z",
            "intensity": {
                "forecast": "183",
                "actual": 178,
                "index": "moderate"
            }
        },
        {
            "from": "2019-08-25T13:00Z",
            "to": "2019-08-25T13:30Z",
            "intensity": {
                "forecast": 178,
                "actual": "176",
                "index": 2,
            }
        },
    ]
}