# Update Group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/edit-group`
---

# Update Group

## /calendars/groups/:groupId

Update Group by group ID

## Requestâ

API VersionAvailable options2021-04-15

Group Id

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Group name

Group description

Group slug

```json
{  "name": "group a",  "description": "group description",  "slug": "15-mins"}
```

```json
{  "name": "group a",  "description": "group description",  "slug": "15-mins"}
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
