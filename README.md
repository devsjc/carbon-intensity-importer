# Carbon Intensity Importer

Data importer for the National Grid's Carbon Intensity API.

Links: https://carbonintensity.org.uk/

## Repository structure

The repository is modelled around the [hexagonal architecture pattern](https://github.com/devsjc/golang-project-structure/blob/main/alistair.cockburn.us/hexagonal-architecture), i.e. build upon ports and adaptors.

```yaml
carbon-intensity-importer:
  internal: # Source code
    inputs: # Folder for ports defining incoming data
      carbonapi: # Package for the Carbon API input
        - adaptor.py # Functions for modifying incoming data to the outgoing format
        - fetcher.py # Functions for fetching data over HTTP from the API endpoint
        - models.py # Class definitions for the structure of the incoming data
  - models.py # Class definitions for structure of the internal data
  - main.py # The entrypoint to the program
```

Here there is only one input and output, but by laying the project out in this manner it is easily extendable.

## Data Validation

Carbon Intensity Importer uses [pydantic](https://pydantic-docs.helpmanual.io/) to handle validation on the types of the incoming data. By handling type safety at the import level, we can ensure the outwritten data is clean and consistent. It would be a trivial exercise to export any error logs to a file for ease of retrying.

## Deployment

This could be happily packaged to a dockerfile and deployed as an airflow or kubernetes cron job, or even on a scheduled GitHub or GitLab CI pipeline.

