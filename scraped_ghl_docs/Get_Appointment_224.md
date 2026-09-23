# Get Appointment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-appointment`
---

# Get Appointment

## /calendars/events/appointments/:eventId

Get appointment by ID

## Requestâ

API VersionAvailable options2021-04-15

Event Id or Instance id. For recurring appointments send masterEventId to modify original series.

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Calendar event object

```json
{  "event": {    "id": "ocQHyuzHvysMo5N5VsXc",    "calendarId": "CVokAlI8fgw4WjWoC3IS",    "title": "Appointment with John"  }}
```

```json
{  "event": {    "id": "ocQHyuzHvysMo5N5VsXc",    "calendarId": "CVokAlI8fgw4WjWoC3IS",    "title": "Appointment with John"  }}
```
