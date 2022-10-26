import datetime as dt
import csv
import logging
import sys

import internal
import internal.inputs.carbonapi as CAPI

# These could be set by env vars or program inputs
START = dt.datetime(2017, 1, 1)
END = dt.datetime.utcnow()


def main():

    # Set up logging
    logging.basicConfig(
        stream=sys.stdout,
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
    )

    with open('out.csv', 'w') as f:

        # Write header to CSV
        fieldnames = list(internal.CSVRow.schema()['properties'].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # Calculate loop variables
        _increment = dt.timedelta(hours=48)
        _delta: dt.timedelta = END - START
        _num_responses: int = int(_delta / _increment)

        # Process National and Regional Data
        logging.info(f"Pulling {_num_responses} sets of National and Regional 48hr data.")
        dateCounter = START

        for i in range(_num_responses):
            logging.debug(f"Processing response for {dateCounter.strftime('%Y-%m-%d')} ({i}/{_num_responses})")

            # Fetch data from API
            nationalPayload = CAPI.FetchFromCarbonAPI(timestamp=dateCounter)
            regionalPayload = CAPI.FetchFromCarbonAPI(timestamp=dateCounter, regional=True)
            # Transform responses to output shape
            data = CAPI.AdaptResponse(nationalPayload)
            data.extend(CAPI.AdaptResponse(regionalPayload))

            # Write rows to CSV
            for row in data:
                writer.writerow(row.dict())

            dateCounter += _increment


if __name__ == "__main__":
    main()
