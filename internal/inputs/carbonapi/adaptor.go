package carbonapi

import (
	"carbon-intensity-importer/internal"
)

// AdaptData converts a Data object to a list of CSVRow objects
func AdaptData(data Data) []internal.CSVRow {
	var adaptedList []internal.CSVRow

	if len(data.Regions) != 0 {
		// Convert each region's data
		for _, region := range data.Regions {
			adaptedList = append(adaptedList, internal.CSVRow{
				StartTimestampUTC: data.Start.String(),
				EndTimestampUTC:   data.End.String(),
				ForecastIntensity: region.Intensity.Forecast,
				ActualIntensity:   region.Intensity.Actual,
				Index:             region.Intensity.Index,
				Region:            region.Shortname,
			})
		}
	} else {
		// Convert single point of national data
		adaptedList = append(adaptedList, internal.CSVRow{
			StartTimestampUTC: data.Start.String(),
			EndTimestampUTC:   data.End.String(),
			ForecastIntensity: data.Intensity.Forecast,
			ActualIntensity:   data.Intensity.Actual,
			Index:             data.Intensity.Index,
			Region:            "National",
		})
	}

	return adaptedList
}

// AdaptResponse takes each "data" entry in a response payload and converts them
// to either a single internal.CSVRow entry in the national case or a list of internal.CSVRow entries
// in the regional case. The resultant internal.CSVRows are returned as a concatenated list.
//
// If there is no data to convert and/or an error in the data, an empty list is returned.
func AdaptResponse(response CarbonIntensityResponsePayload) []internal.CSVRow {
	var out []internal.CSVRow

	if len(response.Data) != 0 {
		for _, dataEntry := range response.Data {
			out = append(out, AdaptData(dataEntry)...)
		}
	}

	return out
}
