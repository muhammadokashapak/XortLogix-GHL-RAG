# Create event calendar availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-calendar-schedule`
---

# Create event calendar availability schedule

## /calendars/schedules/event-calendar/:calendarId

Create a new availability schedule specifically for an event calendar. The calendar ID is provided in the path, and schedule rules and timezone are provided in the request body.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the event calendar

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Schedule rules defining when the schedule is active

Timezone for the schedule (IANA timezone identifier)Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York"}
```

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York"}
```

Schedule created successfully for the event calendar

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
