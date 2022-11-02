package internal

import "strconv"

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
