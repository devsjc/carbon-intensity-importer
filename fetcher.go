package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"time"
)

const (
	baseUrl = "https://api.carbonintensity.org.uk"
)

type CarbonApiHandler struct{}

// FetchResponse gets a list of Carbon Intensity Data from the Carbon Intensity API
// starting at the input timestamp and ending 48 hours afterwards. The data is split
// into 30 minute segments. Regional data can be specified to be fetched via the
// regional parameter.
func (*CarbonApiHandler) FetchResponse(t time.Time, regional bool) []byte {

	// Choose fw48hr National or Regional endpoint
	url := ""
	if regional {
		url = fmt.Sprintf("%s/regional/intensity/%s/fw48h", baseUrl, t.Format(TimeFormat))
	} else {
		url = fmt.Sprintf("%s/intensity/%s/fw48h", baseUrl, t.Format(TimeFormat))
	}

	// Fetch response
	resp, err := http.Get(url)

	if err != nil || resp.StatusCode < 400 {
		log.Print(err)
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Print(err)
	}

	return body
}

// FetchFromCarbonAPI calls the fetchResponse method on the input API handler,
// and converts the output dict to a CarbonIntensityResponsePayload object.
func FetchFromCarbonAPI(t time.Time, regional bool, handler APIInterface) (payload CarbonIntensityResponsePayload) {
	responseBytes := handler.FetchResponse(t, regional)

	err := json.Unmarshal(responseBytes, &payload)
	if err != nil {
		log.Print(err)
		payload.Error = &Error{
			Code:    "409 Conflict",
			Message: err.Error(),
		}
	}

	return payload
}
