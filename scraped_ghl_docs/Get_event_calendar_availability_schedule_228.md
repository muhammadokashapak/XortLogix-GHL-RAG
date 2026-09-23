# Get event calendar availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-calendar-schedule`
---

# Get event calendar availability schedule

## /calendars/schedules/event-calendar/:calendarId

Retrieve the availability schedule for a specific event calendar. Returns the schedule associated with the calendar ID provided in the path.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the event calendar

Schedule retrieved successfully for the event calendar

* application/json

* SchemaExample (auto)
* Example (auto)

The event calendar schedule

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```
