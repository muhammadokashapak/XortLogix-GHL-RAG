# Get Service Location by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-location-by-id`
---

# Get Service Location by ID

## /calendars/services/locations/:serviceLocationId

Get service location by ID

## Requestâ

API VersionAvailable options2021-04-15

Unique Service Location ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Service Location ID

Location ID

Location name

Unique URL-friendly identifier for the service location

Whether location is activeDefault value: true

Whether location is private (not shown publicly)Default value: false

URL of the cover image displayed for this location

Location typeAvailable optionsofflineask_booker

Use a full street address when locationType is offline. Use a user-facing label when locationType is ask_booker.

Contact phone number for the service location

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```
