# Update event calendar availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/update-calendar-schedule`
---

# Update event calendar availability schedule

## /calendars/schedules/event-calendar/:calendarId

Update the availability schedule for a specific event calendar. Only provided fields will be updated. The calendar ID is provided in the path.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the event calendar

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Updated schedule rules defining when the schedule is active

Updated timezone for the schedule (IANA timezone identifier)Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "08:00",          "to": "18:00"        }      ]    }  ],  "timezone": "America/Los_Angeles"}
```

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "08:00",          "to": "18:00"        }      ]    }  ],  "timezone": "America/Los_Angeles"}
```

Schedule updated successfully for the event calendar

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
