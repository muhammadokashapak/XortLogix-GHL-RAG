# Get Service Bookings
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-bookings`
---

# Get Service Bookings

## /calendars/services/bookings

Retrieve service bookings for a location within a given date range, with an optional service location filter.

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Start Time (timestamp in milliseconds as string)

End Time (timestamp in milliseconds as string)

Timezone

Service Location ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Service Bookings

```json
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "title": "John Doe - Hair Styling",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "timezone": "America/New_York",      "status": "confirmed",      "deleted": false    }  ]}
```

```json
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "title": "John Doe - Hair Styling",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "timezone": "America/New_York",      "status": "confirmed",      "deleted": false    }  ]}
```
