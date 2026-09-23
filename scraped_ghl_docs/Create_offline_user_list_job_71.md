# Create offline user list job
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-create-offline-user-list-job`
---

# Create offline user list job

## /ad-publishing/google/segments/offline-user-list-job

Create a job to upload users to a Google customer match list

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Smart list IDs

CSV file path

User list identifier

Dynamic list flag

```json
{  "locationId": "loc_abc123",  "smartListIds": [    "sl_123"  ],  "csvPath": "/uploads/users.csv",  "userListId": "ul_123",  "isDynamic": false}
```

```json
{  "locationId": "loc_abc123",  "smartListIds": [    "sl_123"  ],  "csvPath": "/uploads/users.csv",  "userListId": "ul_123",  "isDynamic": false}
```
