import unittest as t

import internal.inputs.carbonapi as CAPI
from .responses import *


class TestAdaptData(t.TestCase):

    def testAdaptsNationalData(self):
        testData = CAPI.CarbonIntensityResponsePayload(**APIResponse_National).data[0]

        out = CAPI.AdaptData(testData)

        self.assertEqual("National", out[0].Region)
        self.assertEqual(1, len(out))
        self.assertEqual(testData.start.isoformat(timespec="minutes"), out[0].StartTimestampUTC)
        self.assertEqual(testData.intensity.forecast, out[0].ForecastIntensity)

    def testAdaptsRegionalData(self):
        testData = CAPI.CarbonIntensityResponsePayload(**APIResponse_Regional).data[0]

        out = CAPI.AdaptData(testData)

        self.assertEqual(18, len(out))
        self.assertEqual("North Scotland", out[0].Region)
        self.assertEqual("very low", out[0].Index)
        self.assertEqual(73, out[2].ForecastIntensity)


class TestAdaptResponse(t.TestCase):

    def testAdaptsNationalData(self):
        testData = CAPI.CarbonIntensityResponsePayload(**APIResponse_National)

        out = CAPI.AdaptResponse(testData)

        self.assertEqual(2, len(out))

    def testAdaptsRegionalData(self):
        testData = CAPI.CarbonIntensityResponsePayload(**APIResponse_Regional)

        out = CAPI.AdaptResponse(testData)

        self.assertEqual(36, len(out))
