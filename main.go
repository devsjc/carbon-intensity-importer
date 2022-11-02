package main

import (
	"encoding/csv"
	"log"
	"os"
	"time"
)

var (
	START = time.Date(2017, 1, 1, 0, 0, 0, 0, time.UTC)
	END   = time.Now().UTC()
)

func main() {

	f, err := os.Create("out.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// Write header to CSV
	csvWriter := csv.NewWriter(f)
	err = csvWriter.Write(CSVRow{}.GetHeaders())
	if err != nil {
		log.Fatal(err)
	}

	// Calculate loop variables
	_increment := time.Duration(48 * time.Hour)
	_delta := END.Sub(START)
	_numResponses := int(_delta / _increment)

	// Process national and regional data
	log.Printf("Pulling %s sets of National and Regional 48hr data.", _numResponses)
	dateCounter := START

	for i := 0; i < _numResponses; i++ {
		log.Printf("Processing response for %s ({%v}/{%v})", dateCounter.Format(TimeFormat), i, _numResponses)

		// Fetch data from API
		nationalPayload := FetchFromCarbonAPI(dateCounter, false, &CarbonApiHandler{})
		regionalPayload := FetchFromCarbonAPI(dateCounter, true, &CarbonApiHandler{})
		// Transform responses to output shape
		data := AdaptResponse(nationalPayload)
		data = append(data, AdaptResponse(regionalPayload)...)

		// Write rows to CSV
		for _, row := range data {
			err = csvWriter.Write(row.GetRow())
			log.Printf("Error writing row: %v", err)
		}

		dateCounter.Add(_increment)
	}

}
