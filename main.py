import datetime as dt
import csv
import logging
import sys

import internal
import internal.inputs.carbonapi as CAPI

START = dt.datetime(2021, 1, 1)
END = dt.datetime.utcnow()
INCREMENT = dt.timedelta(hours=48)
DELTA: dt.timedelta = END - START
NUM_RESPONSES: int = int(DELTA / INCREMENT)


def main():
    # Set up logging
    logging.basicConfig(
        stream=sys.stdout,
        format='%(asctime)s %(message)s',
        level=logging.DEBUG,
    )
    logging.debug("initializing main")

    dateCounter = START
    fieldnames = list(internal.CSVRow.schema()['properties'].keys())

    with open('out.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(NUM_RESPONSES):
            logging.debug(f"Processing response for {dateCounter.strftime('%Y-%m-%d')} ({i}/{NUM_RESPONSES})")
            nationalPayload = CAPI.FetchFromCarbonAPI(timestamp=dateCounter)
            regionalPayload = CAPI.FetchFromCarbonAPI(timestamp=dateCounter, regional=True)
            data = CAPI.AdaptResponse(nationalPayload)
            data.extend(CAPI.AdaptResponse(regionalPayload))

            for row in data:
                writer.writerow(row.dict())

            dateCounter += INCREMENT


if __name__ == "__main__":
    main()
