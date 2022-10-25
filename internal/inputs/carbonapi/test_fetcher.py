import datetime as dt
import logging
import unittest as t

import pydantic as pyd

from .fetcher import FetchFromCarbonAPI
from .models import APIInterface


class MockCarbonAPIHandler_GoodNationalData(APIInterface):
    """
    Implement handler for mocking good data from national endpoint
    """
    def fetchResponse(self, timestamp: dt.datetime) -> dict:
        return {
            "data": [
                {
                    "from": timestamp.isoformat(timespec="minutes"),
                    "to": (timestamp + dt.timedelta(minutes=30)).isoformat(timespec="minutes"),
                    "intensity": {
                        "forecast": 180,
                        "actual": 188,
                        "index": "moderate"
                    }
                },
                {
                    "from": (timestamp + dt.timedelta(minutes=30)).isoformat(timespec="minutes"),
                    "to": (timestamp + dt.timedelta(minutes=60)).isoformat(timespec="minutes"),
                    "intensity": {
                        "forecast": 180,
                        "actual": 188,
                        "index": "moderate"
                    }
                },
            ]
        }


class MockCarbonAPIHandler_GoodRegionalData(APIInterface):
    """
    Implement handler for mocking good data from regional endpoint
    """
    def fetchResponse(self, timestamp: dt.datetime) -> dict:
        return {
            "data": [
                {
                    "from": timestamp.isoformat(timespec="minutes"),
                    "to": (timestamp + dt.timedelta(minutes=30)).isoformat(timespec="minutes"),
                    "regions": [
                        {
                            "regionid": 1,
                            "dnoregion": "Scottish Hydro Electric Power Distribution",
                            "shortname": "North Scotland",
                            "intensity": {
                                "forecast": 180,
                                "actual": 188,
                                "index": "moderate"
                            }
                        },
                        {
                            "regionid": 2,
                            "dnoregion": "SP Distribution",
                            "shortname": "South Scotland",
                            "intensity": {
                                "forecast": 180,
                                "actual": 188,
                                "index": "moderate"
                            }
                        }
                    ]
                },
                {
                    "from": (timestamp + dt.timedelta(minutes=30)).isoformat(timespec="minutes"),
                    "to": (timestamp + dt.timedelta(minutes=60)).isoformat(timespec="minutes"),
                    "regions": [
                        {
                            "regionid": 1,
                            "dnoregion": "Scottish Hydro Electric Power Distribution",
                            "shortname": "North Scotland",
                            "intensity": {
                                "forecast": 190,
                                "index": "moderate"
                            }
                        },
                        {
                            "regionid": 2,
                            "dnoregion": "SP Distribution",
                            "shortname": "South Scotland",
                            "intensity": {
                                "forecast": 190,
                                "index": "moderate"
                            }
                        }
                    ]
                },
            ]
        }


class MockCarbonAPIHandler_BadNationalData(APIInterface):
    """
    Implement handler for mocking bad data from national endpoint
    """
    def fetchResponse(self, timestamp: dt.datetime) -> dict:
        return {
            "data": [
                {
                    "from": "300BC",
                    "to": 2022,
                    "intensity": {
                        "forecast": "180",
                        "actual": "188",
                        "index": 1
                    }
                },
            ]
        }


class MockCarbonAPIHandler_ErrorData(APIInterface):
    """
    Implement handler for mocking error data
    """
    def fetchResponse(self, timestamp: dt.datetime) -> dict:
        logging.error(f'error fetching API data')
        return {
            "error": {
                "code": "400 Bad Request",
                "message": "Please enter a valid datetime in ISO8601 format YYYY-MM-DDThh:mmZ e.g. "
                           "/intensity/2017-08-25T15:30Z "
            }
        }


class TestFetchFromCarbonAPI(t.TestCase):
    testTime: dt.datetime = dt.datetime(2020, 7, 25)

    def testMapsNationalDataToCarbonAPIResponsePayloadObject(self):
        out = FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler_GoodNationalData())
        self.assertFalse(out.error)
        self.assertEqual(out.data[0].start, self.testTime)
        self.assertEqual(out.data[1].intensity.actual, 188)

    def testMapsRegionalDataToCarbonAPIResponsePayloadObject(self):
        out = FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler_GoodRegionalData())
        self.assertFalse(out.error)
        self.assertFalse(out.data[0].intensity)
        self.assertEqual(out.data[0].start, self.testTime)
        self.assertEqual(out.data[0].regions[0].shortname, "North Scotland")
        self.assertEqual(out.data[0].regions[0].intensity.actual, 188)
        self.assertEqual(out.data[1].start, self.testTime + dt.timedelta(minutes=30))

    def testHandlesErrorResponse(self):
        out = FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler_ErrorData())
        self.assertFalse(out.data)

    def testErrorsOnReceiptOfBadNationalData(self):
        with self.assertRaises(pyd.ValidationError):
            FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler_BadNationalData())
