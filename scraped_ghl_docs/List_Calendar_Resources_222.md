# List Calendar Resources
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/fetch-calendar-resources`
---

# List Calendar Resources

## /calendars/resources/:resourceType

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

List calendar resources by resource type and location ID (Services V1)

## Requestâ

API VersionAvailable options2021-04-15

Calendar Resource TypeAvailable optionsequipmentsrooms

Location ID

Maximum number of results

Number of results to skip

Calendar resources listed

* application/json

* SchemaExample (auto)
* Example (auto)

* Array [
* ]

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
[  {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "yoga room",    "resourceType": "rooms",    "isActive": true,    "description": "Spacious yoga studio",    "quantity": 3,    "outOfService": 0,    "capacity": 85,    "calendarIds": [      "Jsj0xnlDDjw0SuvX1J13",      "oCM5feFC86FAAbcO7lJK"    ]  }]
```

```json
[  {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "yoga room",    "resourceType": "rooms",    "isActive": true,    "description": "Spacious yoga studio",    "quantity": 3,    "outOfService": 0,    "capacity": 85,    "calendarIds": [      "Jsj0xnlDDjw0SuvX1J13",      "oCM5feFC86FAAbcO7lJK"    ]  }]
```
