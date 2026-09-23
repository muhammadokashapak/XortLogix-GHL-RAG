# List user availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-all-schedules`
---

# List user availability schedule

## /calendars/schedules/search

Retrieve user availability schedules based on various filters including location, calendar, and user. Supports pagination.

## Requestâ

API VersionAvailable options2021-04-15

Location ID to filter schedules by

User ID to filter schedules by specific user

Calendar ID for filtering schedules by specific calendar

Number of items to skip for paginationPossible values: >= 0Default value:0

Possible values: >= 0Default value:0

Maximum number of items to return (max 500)Possible values: >= 1 and <= 500Default value:50

Possible values: >= 1 and <= 500Default value:50

Schedules retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Array of schedules

```json
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "ocQHyuzHvysMo5N5VsXc"    }  ]}
```

```json
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "ocQHyuzHvysMo5N5VsXc"    }  ]}
```
