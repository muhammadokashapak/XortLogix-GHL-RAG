# Create user availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-schedule`
---

# Create user availability schedule

## /calendars/schedules

Create new schedule with specified rules, timezone, location, user and calendar associations.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Schedule rules defining when the schedule is active

Timezone for the schedule (IANA timezone identifier)Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Location ID where this schedule applies

Human-readable name for the schedule

User ID associated with the schedule

Calendar IDs associated with the schedule

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York",  "locationId": "IkqiJlXJ7o9h61tCHHod",  "name": "Business Hours Schedule",  "userId": "IkqiJlXJ7o9h61tCHHod",  "calendarIds": [    "WvVX9LpvlBO6K506xLbp",    "XyZ8MnQrStUvWxYzAbCdEf"  ]}
```

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York",  "locationId": "IkqiJlXJ7o9h61tCHHod",  "name": "Business Hours Schedule",  "userId": "IkqiJlXJ7o9h61tCHHod",  "calendarIds": [    "WvVX9LpvlBO6K506xLbp",    "XyZ8MnQrStUvWxYzAbCdEf"  ]}
```

Schedule created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Schedule

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```
