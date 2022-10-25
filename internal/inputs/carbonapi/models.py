"""
Models for the fetching and handling of incoming data
from the Carbon Intensity API
"""

import datetime as dt

import pydantic as pyd


class Intensity(pyd.BaseModel):
    forecast: int
    actual: int | None
    index: str


class Region(pyd.BaseModel):
    regionid: int
    dnoregion: str
    shortname: str
    intensity: Intensity


class Data(pyd.BaseModel):
    start: dt.datetime = pyd.Field(alias='from')
    end: dt.datetime = pyd.Field(alias='to')
    intensity: Intensity | None
    regions: list[Region] | None


class Error(pyd.BaseModel):
    code: str
    message: str


class CarbonIntensityResponsePayload(pyd.BaseModel):
    """
    Incoming payload from Carbon Intensity API.
    """
    data: list[Data] | None
    error: Error | None


class APIInterface:
    """
    Generic interface for fetching API data, used for dependency injection
    """
    def fetchResponse(self, timestamp: dt.datetime, regional: bool) -> dict:
        """Get the Carbon Intensity API response as a dict"""
        pass

