import datetime
import csv
import logging

import internal
import internal.inputs.carbonapi as CAPI

START = datetime.datetime(2018, 1, 1)
END = datetime.datetime.utcnow()
INCREMENT = datetime.timedelta(hours=48)


def main():
    # Set up logging
    logging.basicConfig(format='%(asctime)s %(message)s')

    dateCounter = START

    fieldnames = list(internal.CSVRow.schema()['properties'].keys())

    with open('out.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        while dateCounter < END:
            nationalPayload = CAPI.FetchFromCarbonAPI(timestamp=dateCounter)
            regionalPayload = CAPI.FetchFromCarbonAPI(timestamp=dateCounter, regional=True)
            data = CAPI.AdaptResponse(nationalPayload)
            data.extend(CAPI.AdaptResponse(regionalPayload))

            for row in data:
                writer.writerow(row.dict())

            dateCounter += INCREMENT


if __name__ == "__main__":
    main()
