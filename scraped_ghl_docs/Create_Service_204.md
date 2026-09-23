# Create Service
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-service-catalog`
---

# Create Service

## /calendars/services/catalog

Create new service in a location.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Service name

Unique URL-friendly identifier

Assigned staff members (at least one required)

Service description

Service event color (hex)

Service cover image URL

Service category ID (uses default category if not provided)

Payment details (default amount is 0, currency configured in Service Global Settings is used.)

This controls the duration of the appointment

Duration unitAvailable optionsminshours

Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready

Pre-buffer unitAvailable optionsminshours

Post-buffer: Additional time that can be added after an appointment, allowing for extra time to wrap up

Post-buffer unitAvailable optionsminshours

Whether service is private (not shown publicly)

Custom form ID (will be used to display the custom form on the booking page, if only one service is selected)

Service variations (pass empty array for no variations)

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Hair Styling",  "slug": "hair-styling",  "staff": [    {      "id": "65e5f6dfacf123513228d384"    }  ],  "description": "Full hair styling session",  "eventColor": "#66C61C",  "coverImage": "https://example.com/cover.jpg",  "serviceCategoryId": "65e5f6dfacf123513228d381",  "payment": {    "amount": 50,    "deposit": 20,    "depositType": "amount"  },  "serviceDuration": 30,  "serviceDurationUnit": "mins",  "preBuffer": 10,  "preBufferUnit": "mins",  "postBuffer": 15,  "postBufferUnit": "mins",  "isPrivate": false,  "formId": "65e5f6dfacf123513228d390",  "variations": [    {      "name": "Standard Haircut",      "serviceDuration": 30,      "payment": {        "amount": 50      }    }  ]}
```

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Hair Styling",  "slug": "hair-styling",  "staff": [    {      "id": "65e5f6dfacf123513228d384"    }  ],  "description": "Full hair styling session",  "eventColor": "#66C61C",  "coverImage": "https://example.com/cover.jpg",  "serviceCategoryId": "65e5f6dfacf123513228d381",  "payment": {    "amount": 50,    "deposit": 20,    "depositType": "amount"  },  "serviceDuration": 30,  "serviceDurationUnit": "mins",  "preBuffer": 10,  "preBufferUnit": "mins",  "postBuffer": 15,  "postBufferUnit": "mins",  "isPrivate": false,  "formId": "65e5f6dfacf123513228d390",  "variations": [    {      "name": "Standard Haircut",      "serviceDuration": 30,      "payment": {        "amount": 50      }    }  ]}
```

Service created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Service details

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling"  }}
```

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling"  }}
```
