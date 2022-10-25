import datetime as dt
import unittest as t

import pydantic as pyd

import internal.inputs.carbonapi as CAPI
from .responses import *


class MockCarbonAPIHandler(CAPI.APIInterface):
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
        out = CAPI.FetchFromCarbonAPI(timestamp=self.testTime,
                                      handler=MockCarbonAPIHandler(response=APIResponse_National))

        self.assertFalse(out.error)
        self.assertEqual(
            dt.datetime(2019, 8, 25, 12, 30, tzinfo=dt.timezone.utc),
            out.data[0].start
        )
        self.assertEqual(
            APIResponse_National["data"][1]["intensity"]["actual"],
            out.data[1].intensity.actual
        )

    def testMapsRegionalDataToCarbonAPIResponsePayloadObject(self):
        out = CAPI.FetchFromCarbonAPI(timestamp=self.testTime,
                                      handler=MockCarbonAPIHandler(response=APIResponse_Regional))

        self.assertFalse(out.error)
        self.assertFalse(out.data[0].intensity)
        self.assertEqual(
            dt.datetime(2019, 8, 25, 12, 30, tzinfo=dt.timezone.utc),
            out.data[0].start
        )
        self.assertEqual(
            APIResponse_Regional["data"][0]["regions"][0]["shortname"],
            out.data[0].regions[0].shortname
        )
        self.assertEqual(
            APIResponse_Regional["data"][0]["regions"][0]["intensity"]["forecast"],
            out.data[0].regions[0].intensity.forecast
        )
        self.assertEqual(
            dt.datetime(2019, 8, 25, 13, 0, tzinfo=dt.timezone.utc),
            out.data[1].start
        )

    def testHandlesErrorResponse(self):
        out = CAPI.FetchFromCarbonAPI(timestamp=self.testTime, handler=MockCarbonAPIHandler(response=APIResponse_Error))

        self.assertFalse(out.data)

    def testErrorsOnReceiptOfBadData(self):
        out = CAPI.FetchFromCarbonAPI(timestamp=self.testTime,
                                      handler=MockCarbonAPIHandler(response=APIResponse_BadlyTyped))

        self.assertFalse(out.data)
        self.assertIn("validation error", out.error.message)
