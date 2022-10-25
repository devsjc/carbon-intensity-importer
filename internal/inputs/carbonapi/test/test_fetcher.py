import datetime as dt
import json
import unittest as t

import pydantic as pyd

from ..fetcher import FetchFromCarbonAPI
from ..models import APIInterface
from .responses import *


class MockCarbonAPIHandler(APIInterface):
    """
    Implement handler for mocking data fetching from endpoint.
    fetchResponse just returns whatever dict was passed to init.
    """

    response: dict

    def __init__(self, response: dict):
        self.response = response

    def fetchResponse(self, timestamp: dt.datetime, regional: bool) -> dict:
        return self.response


class TestFetchFromCarbonAPI(t.TestCase):
    testTime: dt.datetime = dt.datetime(2020, 7, 25)

    def testMapsNationalDataToCarbonAPIResponsePayloadObject(self):
        out = FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler(response=APIResponse_National))
        self.assertFalse(out.error)
        self.assertEqual(out.data[0].start, dt.datetime(2019, 8, 25, 12, 30, tzinfo=dt.timezone.utc))
        self.assertEqual(out.data[1].intensity.actual, APIResponse_National["data"][1]["intensity"]["actual"])

    def testMapsRegionalDataToCarbonAPIResponsePayloadObject(self):
        out = FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler(response=APIResponse_Regional))
        self.assertFalse(out.error)
        self.assertFalse(out.data[0].intensity)
        self.assertEqual(out.data[0].start, dt.datetime(2019, 8, 25, 12, 30, tzinfo=dt.timezone.utc))
        self.assertEqual(out.data[0].regions[0].shortname, APIResponse_Regional["data"][0]["regions"][0]["shortname"])
        self.assertEqual(out.data[0].regions[0].intensity.forecast,
                         APIResponse_Regional["data"][0]["regions"][0]["intensity"]["forecast"])
        self.assertEqual(out.data[1].start, dt.datetime(2019, 8, 25, 13, 0, tzinfo=dt.timezone.utc))

    def testHandlesErrorResponse(self):
        out = FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler(response=APIResponse_Error))
        self.assertFalse(out.data)

    def testErrorsOnReceiptOfBadData(self):
        with self.assertRaises(pyd.ValidationError):
            FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler(response=APIResponse_BadlyTyped))
