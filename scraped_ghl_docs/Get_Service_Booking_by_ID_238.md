# Get Service Booking by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-booking-by-id`
---

# Get Service Booking by ID

## /calendars/services/bookings/:bookingId

Get a specific service booking by ID

## Requestâ

API VersionAvailable options2021-04-15

Unique Service Booking ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Booking ID

Location ID

Contact ID

Service Location ID

Service Booking Title

Start Time

End Time

Services

Timezone

Status

Tells if the booking is deleted

Date Added

Date Updated

Booking booked by metadata

Meeting Location (If service location is an ask the booker, then the meeting location is used for the booking)

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA"}
```

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA"}
```
