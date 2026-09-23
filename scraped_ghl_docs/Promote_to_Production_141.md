# Promote to Production
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/promote-and-publish`
---

# Promote to Production

## /agent-studio/agent/versions/:versionId/publish

Promotes a draft version to production.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID for authorization

User ID performing the promotion action

User name performing the promotion action

User email performing the promotion action

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "userId": "usr_abc123def456",  "userName": "John Doe",  "userEmail": "[email protected]"}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "userId": "usr_abc123def456",  "userName": "John Doe",  "userEmail": "[email protected]"}
```

Version promoted and published successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Result data with production and new draft version details

```json
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "[email protected]"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

```json
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "[email protected]"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```
