"""
Adaptors for converting from input data to internal data
"""
import logging

from .models import CarbonIntensityResponsePayload, Data
import internal


def AdaptData(data: Data) -> list[internal.CSVRow]:
    """
    AdaptData converts a Data object to a list of CSVRow objects
    """
    adaptedList: list[internal.CSVRow] = []

    if data.regions:
        # convert each region's data
        for region in data.regions:
            adaptedList.append(internal.CSVRow(
                StartTimestampUTC=data.start.isoformat(timespec='minutes'),
                EndTimestampUTC=data.end.isoformat(timespec='minutes'),
                ForecastIntensity=region.intensity.forecast,
                ActualIntensity=region.intensity.actual,
                Index=region.intensity.index,
                Region=region.shortname,
            ))
    else:
        # convert single point of national data
        adaptedList.append(internal.CSVRow(
            StartTimestampUTC=data.start.isoformat(timespec='minutes'),
            EndTimestampUTC=data.end.isoformat(timespec='minutes'),
            ForecastIntensity=data.intensity.forecast,
            ActualIntensity=data.intensity.actual,
            Index=data.intensity.index,
        ))

    return adaptedList


def AdaptResponse(response: CarbonIntensityResponsePayload) -> list[internal.CSVRow]:
    """
    AdaptResponse takes each "data" entry in a response payload and converts them
    to either a single CSVRow entry in the national case or a list of CSVRow entries
    in the regional case. The resultant CSVRows are returned as a concatenated list.

    If there is no data to convert and/or an error in the data, an empty list is returned.
    """
    out: list[internal.CSVRow] = []

    if response.data:
        for dataEntry in response.data:
            out.extend(AdaptData(data=dataEntry))
    return out
