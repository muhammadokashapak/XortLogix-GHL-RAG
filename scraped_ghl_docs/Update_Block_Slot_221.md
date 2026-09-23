# Update Block Slot
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/edit-block-slot`
---

# Update Block Slot

## /calendars/events/block-slots/:eventId

Update block slot by ID

## Requestâ

API VersionAvailable options2021-04-15

Event Id or Instance id. For recurring appointments send masterEventId to modify original series.

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Title

Either calendarId or assignedUserId can be set, not both.

Either calendarId or assignedUserId can be set, not both.

Location Id

Start Time

End Time

```json
{  "title": "Test Event",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

```json
{  "title": "Test Event",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Id

Location Id

Title

Start Time

End Time

Calendar id

Assigned User Id

```json
{  "id": "0TkCdp9PfvLeWKYRRvIz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "title": "My event",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "0007BWpSzSwfiuSl0tR2"}
```

```json
{  "id": "0TkCdp9PfvLeWKYRRvIz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "title": "My event",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "0007BWpSzSwfiuSl0tR2"}
```
