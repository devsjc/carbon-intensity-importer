import pydantic as pyd


class CSVRow(pyd.BaseModel):

    StartTimestampUTC: str
    EndTimestampUTC: str
    ForecastIntensity: int
    ActualIntensity: int | None
    Region: str = pyd.Field(default="National")
    Index: str
