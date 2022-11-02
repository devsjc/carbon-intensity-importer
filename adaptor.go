package main

// AdaptData converts a Data object to a list of CSVRow objects
func AdaptData(data Data) []CSVRow {
	var adaptedList []CSVRow

	if data.Regions != nil {
		// Convert each region's data
		for _, region := range *data.Regions {
			adaptedList = append(adaptedList, CSVRow{
				StartTimestampUTC: data.Start.Format(TimeFormat),
				EndTimestampUTC:   data.End.Format(TimeFormat),
				ForecastIntensity: region.Intensity.Forecast,
				ActualIntensity:   region.Intensity.Actual,
				Index:             region.Intensity.Index,
				Region:            region.Shortname,
			})
		}
	} else {
		// Convert single point of national data
		adaptedList = append(adaptedList, CSVRow{
			StartTimestampUTC: data.Start.Format(TimeFormat),
			EndTimestampUTC:   data.End.Format(TimeFormat),
			ForecastIntensity: data.Intensity.Forecast,
			ActualIntensity:   data.Intensity.Actual,
			Index:             data.Intensity.Index,
			Region:            "National",
		})
	}

	return adaptedList
}

// AdaptResponse takes each "data" entry in a response payload and converts them
// to either a single CSVRow entry in the national case or a list of CSVRow entries
// in the regional case. The resultant CSVRows are returned as a concatenated list.
//
// If there is no data to convert and/or an error in the data, an empty list is returned.
func AdaptResponse(response CarbonIntensityResponsePayload) []CSVRow {
	var out []CSVRow

	if response.Data != nil {
		for _, dataEntry := range *response.Data {
			out = append(out, AdaptData(dataEntry)...)
		}
	}

	return out
}
