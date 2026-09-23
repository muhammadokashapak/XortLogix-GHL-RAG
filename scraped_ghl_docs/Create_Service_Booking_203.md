# Create Service Booking
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-service-booking`
---

# Create Service Booking

## /calendars/services/bookings

Create a new service booking

## Requestâ

API VersionAvailable options2021-04-15

If true the time slot validation would be avoided for any booking creation/update (even the skipSchedulingNotice)Default value:false

If set to true, the minimum scheduling notice and date range would be ignoredDefault value:false

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Contact ID

Start Time

End Time

Timezone

Services

Service Location ID (If not provided, then the default service location will be used)

Meeting Location (If service location is an ask the booker, then the meeting location is required)

Service Booking Title

Status. (If not provided, the status configured in Service Global Settings will be used.)Available optionsconfirmednew

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "timezone": "America/New_York",  "services": [    {      "id": "a3b4c5d6e7f8901234567890",      "staffId": "8MkU36Wps2w5bRbuGtw3"    }  ],  "serviceLocationId": "65e5f6dfacf123513228d384",  "meetingLocation": "123 Main St, Anytown, USA",  "title": "Service Appointment",  "status": "confirmed"}
```

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "timezone": "America/New_York",  "services": [    {      "id": "a3b4c5d6e7f8901234567890",      "staffId": "8MkU36Wps2w5bRbuGtw3"    }  ],  "serviceLocationId": "65e5f6dfacf123513228d384",  "meetingLocation": "123 Main St, Anytown, USA",  "title": "Service Appointment",  "status": "confirmed"}
```

Booking created successfully

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

Optional informative or warning messages (e.g. meeting location ignored for non-ask-booker locations)

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```
