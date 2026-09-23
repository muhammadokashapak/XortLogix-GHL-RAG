# Get Free Slots
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-slots`
---

# Get Free Slots

## /calendars/:calendarId/free-slots

Get free slots for a calendar between a date range. Optionally a consumer can also request free slots in a particular timezone and also for a particular user.

## Requestâ

API VersionAvailable options2021-04-15

Calendar Id

Start Date (â ï¸ Important: Date range cannot be more than 31 days)

End Date (â ï¸ Important: Date range cannot be more than 31 days)

The timezone in which the free slots are returned

The user for whom the free slots are returned

The users for whom the free slots are returned

Availability map keyed by date (YYYY-MM-DD)

* application/json

* SchemaExample (auto)
* Example (auto)

```json
{  "2024-10-28": {    "slots": [      "2024-10-28T10:00:00-05:00",      "2024-10-28T11:00:00-05:00"    ]  },  "2024-10-29": {    "slots": [      "2024-10-29T10:00:00-05:00",      "2024-10-29T14:30:00-05:00"    ]  }}
```

```json
{  "2024-10-28": {    "slots": [      "2024-10-28T10:00:00-05:00",      "2024-10-28T11:00:00-05:00"    ]  },  "2024-10-29": {    "slots": [      "2024-10-29T10:00:00-05:00",      "2024-10-29T14:30:00-05:00"    ]  }}
```
