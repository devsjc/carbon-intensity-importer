"""
Functions for fetching data from the input
"""
import logging

import requests
import datetime as dt

from .models import CarbonIntensityResponsePayload, APIInterface


class CarbonAPIHandler(APIInterface):
    """
    Implements a handler to fetch the data from the Carbon API
    """
    baseurl = "https://api.carbonintensity.org.uk"

    def fetchResponse(self, timestamp: dt.datetime, regional: bool) -> dict:
        """
        fetchResponse gets a list of Carbon Intensity Data from the Carbon Intensity API
        starting at the input timestamp and ending 48 hours afterwards. The data is split
        into 30 minute segments. Regional data can be specified to be fetched via the
        regional parameter..
        """

        if regional:
            url = f'{self.baseurl}/regional/intensity/{timestamp.isoformat(timespec="minutes")}/fw48h'
        else:
            url = f'{self.baseurl}/intensity/{timestamp.isoformat(timespec="minutes")}/fw48h'

        response = requests.get(url)
        if not response.ok:
            logging.error(f'error fetching API data: {response.text}')
            return {}
        return response.json()


def FetchFromCarbonAPI(
        timestamp: dt.datetime,
        regional: bool = False,
        handler: APIInterface = CarbonAPIHandler()) -> CarbonIntensityResponsePayload:
    """
    FetchFromCarbonAPI calls the fetchResponse method on the input API handler,
    and converts the output dict to a CarbonIntensityResponsePayload object.
    """
    responseJson = handler.fetchResponse(timestamp=timestamp, regional=regional)
    return CarbonIntensityResponsePayload(**responseJson)

