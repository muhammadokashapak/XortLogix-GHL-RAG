# Create Service Location
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-service-location`
---

# Create Service Location

## /calendars/services/locations

Create a new service location

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Location name

URL-friendly slug identifier

Phone number

Use a full street address when locationType is offline. Use a user-facing label when locationType is ask_booker.

URL of the cover image for this service location

Location typeAvailable optionsofflineask_booker

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Midtown Therapy Studio",  "slug": "midtown-therapy-studio",  "phone": "+1-212-555-0174",  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",  "locationType": "offline"}
```

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Midtown Therapy Studio",  "slug": "midtown-therapy-studio",  "phone": "+1-212-555-0174",  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",  "locationType": "offline"}
```

Service location created successfully

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
