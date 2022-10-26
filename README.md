# Carbon Intensity Importer

[![Test Status](https://github.com/devsjc/carbon-intensity-importer/actions/workflows/test.yml/badge.svg)](https://github.com/devsjc/carbon-intensity-importer/actions/workflows/test.yml)

Data importer for the National Grid's Carbon Intensity API.

Pulls national and regional data from the API, and exports it in CSV format, found at out.csv.

Links: https://carbonintensity.org.uk/

## Repository structure

The repository is modelled around
the [hexagonal architecture pattern](https://github.com/devsjc/golang-project-structure/blob/main/alistair.cockburn.us/hexagonal-architecture)
, i.e. built upon ports and adaptors.

```yaml
carbon-intensity-importer:
  - .github: # Workflow definition files
  - internal: # Non-main source code
    - inputs: # Folder for ports defining incoming data
      - carbonapi: # Package for the Carbon API input
        - adaptor.py # Functions for modifying incoming data to the outgoing format
        - fetcher.py # Functions for fetching data over HTTP from the API endpoint
        - models.py # Class definitions for the structure of the incoming data
    - models.py # Class definitions for structure of the internal data
  - tests: # Unittests
  - main.py # The entrypoint to the program
  - requirements.txt # Conda environment definition file
```

Here there is only one input and output, but by laying the project out in this manner it is easily extendable.

## Output

A truncated output for a run with the current configuration can be found at `out.csv`. Since the importer is set to pull
both
regional and national data for every half an hour occurring from 2017 to now, the output csv is too large to upload to
GitHub, so the file that is
there is truncated to 50Mb. A full version of the file is produced as an artifact on the `run` workflow, as can be
accessed
here: https://github.com/devsjc/carbon-intensity-importer/actions/runs/3327927116.

## Data Validation and Contract

Carbon Intensity Importer uses [pydantic](https://pydantic-docs.helpmanual.io/) to handle validation on the types of the
incoming data. By handling type safety at the import level, we can ensure the outwritten data is clean and consistent.
It would be a trivial exercise to export any error logs to a file for ease of retrying.

The schema of the outgoing csv is defined in the
internal-level [models.py file](https://github.com/devsjc/carbon-intensity-importer/blob/main/internal/models.py), and
is as follows:

| Field             | Type   |
|-------------------|--------|
| StartTimestampUTC | string |
| EndTimestampUTC   | string |
| ForecastIntensity | int    |
| ActualIntensity   | int    |
| Region            | string |
| Index             | string |

## Deployment

This could be happily packaged to a dockerfile and deployed as an airflow or kubernetes cron job. In this instance I
have shown how it could even be instantiated and run using GitHub actions:
see [the run workflow](https://github.com/devsjc/carbon-intensity-importer/blob/main/.github/workflows/run.yml) and
the [last run instance](https://github.com/devsjc/carbon-intensity-importer/actions/runs/3327927116).
