# List Agents
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/get-agents`
---

# List Agents

## /agent-studio/agent

Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset. Optionally filter by isPublished=true to return only agents with a published production version.

## Requestâ

API VersionAvailable options2021-04-15

Optional filter to return only agents with a published production version

Agents retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

List of agents with metadata

Pagination metadata

```json
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

```json
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```
