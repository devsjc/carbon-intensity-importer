"""
Functions for fetching data from the input
"""
import logging

import pydantic as pyd
import requests
import datetime as dt

from .models import CarbonIntensityResponsePayload, APIInterface, Error


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

        # choose fw48hr National or Regional endpoint
        if regional:
            url = f'{self.baseurl}/regional/intensity/{timestamp.isoformat(timespec="minutes")}/fw48h'
        else:
            url = f'{self.baseurl}/intensity/{timestamp.isoformat(timespec="minutes")}/fw48h'

        # fetch response
        response = requests.get(url)

        if not response.ok:
            logging.error(f"{response.status_code} error code received from GET {url}: {response.json()['error']}")

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

    # Validate the input by parsing to model class
    try:
        out = CarbonIntensityResponsePayload(**responseJson)
    except pyd.ValidationError as e:
        # Fail soft
        logging.error(f"Error parsing json response as struct: {str(e)}")
        out = CarbonIntensityResponsePayload(
            error=Error(
                code="409 Conflict",
                message=str(e)
            )
        )

    return out

