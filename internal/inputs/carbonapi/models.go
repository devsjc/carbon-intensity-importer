package carbonapi

import (
	"strings"
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
	Start     CustomTime `json:"from"`
	End       CustomTime `json:"to"`
	Intensity Intensity
	Regions   []Region
}

type Error struct {
	Code    string
	Message string
}

type CarbonIntensityResponsePayload struct {
	Data  []Data
	Error Error
}

type APIInterface interface {
	FetchResponse(t time.Time, regional bool) []byte
}

type CustomTime time.Time

func (ct *CustomTime) UnmarshalJSON(b []byte) (err error) {
	s := strings.Trim(string(b), `"`)
	nt, err := time.Parse(TimeFormat, s)
	*ct = CustomTime(nt)
	return
}

// String returns the time in the custom format
func (ct *CustomTime) String() string {
	t := time.Time(*ct)
	return t.Format(TimeFormat)
}
