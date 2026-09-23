# Update Appointment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/edit-appointment`
---

# Update Appointment

## /calendars/events/appointments/:eventId

Update appointment

## Requestâ

API VersionAvailable options2021-04-15

Event Id or Instance id. For recurring appointments send masterEventId to modify original series.

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

* If address is provided in the request body, the meetingLocationType defaults to custom.
* This value can be found in calendar.locationConfigurationsor calendar.teamMembers[].locationConfigurations
* false - If only meetingLocationId is provided
* true - If only meetingLocationType is provided

Title

Meeting location type.

* If address is provided in the request body, the meetingLocationType defaults to custom.

The unique identifier for the meeting location.

* This value can be found in calendar.locationConfigurationsor calendar.teamMembers[].locationConfigurations

Flag to override location config

* false - If only meetingLocationId is provided
* true - If only meetingLocationType is provided

Appointment statusAvailable optionsnewconfirmedcancelledshowednoshowinvalidcompletedactive

Assigned User Id

Appointment Description

Appointment Address

If set to true, the minimum scheduling notice and date range would be ignored

If set to false, the automations will not run. Defaults to trueDefault value: true

If true the time slot validation would be avoided for any appointment creation (even the ignoreDateRange)

RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. The rrule only be applied if ignoreFreeSlotValidation is true.

Calendar Id

Start Time

End Time

```json
{  "title": "Test Event",  "meetingLocationType": "custom",  "meetingLocationId": "custom_0",  "overrideLocationConfig": true,  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "description": "Booking a call to discuss the project",  "address": "Zoom",  "ignoreDateRange": false,  "toNotify": false,  "ignoreFreeSlotValidation": true,  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

```json
{  "title": "Test Event",  "meetingLocationType": "custom",  "meetingLocationId": "custom_0",  "overrideLocationConfig": true,  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "description": "Booking a call to discuss the project",  "address": "Zoom",  "ignoreDateRange": false,  "toNotify": false,  "ignoreFreeSlotValidation": true,  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Calendar Id

Location Id

Contact Id

Start Time

End Time

Title

Meeting Location TypeDefault value: default

Appointment statusAvailable optionsnewconfirmedcancelledshowednoshowinvalidactivecompleted

Assigned User Id

Appointment Address

true if the event is recurring otherwise false

RRULE as per the iCalendar (RFC 5545) specification for recurring events

Date Added

Date Updated

Id

```json
{  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "title": "Test Event",  "meetingLocationType": "custom",  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "address": "Zoom",  "isRecurring": "true",  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "dateAdded": "2021-06-23T03:30:00+05:30",  "dateUpdated": "2021-06-23T04:30:00+05:30",  "id": "0TkCdp9PfvLeWKYRRvIz"}
```

```json
{  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "title": "Test Event",  "meetingLocationType": "custom",  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "address": "Zoom",  "isRecurring": "true",  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "dateAdded": "2021-06-23T03:30:00+05:30",  "dateUpdated": "2021-06-23T04:30:00+05:30",  "id": "0TkCdp9PfvLeWKYRRvIz"}
```
