# Create Calendar Group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-calendar-group`
---

# Create Calendar Group

## /calendars/groups

Create Calendar Group

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Group name

Group description

Group slug

Whether the group is active

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "group a",  "description": "group description",  "slug": "15-mins",  "isActive": true}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "group a",  "description": "group description",  "slug": "15-mins",  "isActive": true}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

The created group object

```json
{  "group": {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "group a",    "slug": "15-mins"  }}
```

```json
{  "group": {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "group a",    "slug": "15-mins"  }}
```
