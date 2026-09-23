# Create Calendar Resource
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-calendar-resource`
---

# Create Calendar Resource

## /calendars/resources/:resourceType

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Create calendar resource by resource type (Services V1)

## Requestâ

API VersionAvailable options2021-04-15

Calendar Resource TypeAvailable optionsequipmentsrooms

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Name of the calendar resource

Description of the calendar resource

Quantity of the equipment.

Quantity of the out of service equipment.

Capacity of the room.

Service calendar IDs to be mapped with the resource.

One room can be mapped with multiple service calendars.Possible values: <= 100

Possible values: <= 100

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "Projector",  "description": "Main conference room projector",  "quantity": 5,  "outOfService": 1,  "capacity": 20,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13"  ]}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "Projector",  "description": "Main conference room projector",  "quantity": 5,  "outOfService": 1,  "capacity": 20,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13"  ]}
```

Calendar resource created

* application/json

* SchemaExample (auto)
* Example (auto)

Location ID of the resource

Name of the resource

Type of the calendar resourceAvailable optionsequipmentsrooms

Whether the resource is active

Description of the resource

Quantity of the resource

Indicates if the resource is out of service

Capacity of the resource

Calendar IDs

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```
