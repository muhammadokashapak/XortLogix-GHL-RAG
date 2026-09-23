# Get Calendar Events
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-calendar-events`
---

# Get Calendar Events

## /calendars/events

Get Calendar Events

## Requestâ

API VersionAvailable options2021-04-15

Location Id

User Id - Owner of an appointment. Either of userId, groupId or calendarId is required

Either of calendarId, userId or groupId is required

Either of groupId, calendarId or userId is required

Start Time (in millis)

End Time (in millis)

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of calendar events

```json
{  "events": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "calendarId": "CVokAlI8fgw4WjWoC3IS",      "title": "Appointment with John"    }  ]}
```

```json
{  "events": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "calendarId": "CVokAlI8fgw4WjWoC3IS",      "title": "Appointment with John"    }  ]}
```
