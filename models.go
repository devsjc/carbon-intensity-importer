package main

import (
	"strconv"
	"time"
)

const (
	TimeFormat = "2006-01-02T15:04Z"
)

type Intensity struct {
	Forecast int
	Actual   *int
	Index    string
}

type Region struct {
	RegionID  int
	DNORegion string
	Shortname string
	Intensity Intensity
}

type Data struct {
	Start     time.Time
	End       time.Time
	Intensity *Intensity
	Regions   *[]Region
}

type Error struct {
	Code    string
	Message string
}

type CarbonIntensityResponsePayload struct {
	Data  *[]Data
	Error *Error
}

type APIInterface interface {
	FetchResponse(t time.Time, regional bool) []byte
}

type CSVRow struct {
	StartTimestampUTC string
	EndTimestampUTC   string
	ForecastIntensity int
	ActualIntensity   *int
	Region            string
	Index             string
}

func (CSVRow) GetHeaders() []string {
	return []string{"StartTimestampUTC", "EndTimestampUTC", "ForecastIntensity", "ActualIntensity", "Region", "Index"}
}

func (c CSVRow) GetRow() []string {
	actualIntensity := ""
	if c.ActualIntensity != nil {
		actualIntensity = strconv.Itoa(*c.ActualIntensity)
	}
	return []string{c.StartTimestampUTC, c.EndTimestampUTC, strconv.Itoa(c.ForecastIntensity), actualIntensity, c.Region, c.Index}
}
