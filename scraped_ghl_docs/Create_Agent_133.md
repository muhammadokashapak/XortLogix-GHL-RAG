# Create Agent
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/create-agent`
---

# Create Agent

## /agent-studio/agent

Creates a new agent with staging version. The agent will be created with an initial staging version that can later be promoted to production.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Name of the agent

Description of the agent

Agency ID

Author ID

Author name

Author email

Status of the agentAvailable optionsactiveinactivearchived

Version data for the agent including nodes, edges, and configuration

Nodes array (deprecated, prefer using version.nodes)

Edges array (deprecated, prefer using version.edges)

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Customer Support Agent",  "description": "AI agent specialized in handling customer inquiries and support tickets",  "agencyId": "gjL2sFNXJfJYa3d2OYSN",  "authorId": "usr_abc123def456",  "authorName": "John Doe",  "authorEmail": "[email protected]",  "status": "active",  "version": {    "versionName": "Version 1",    "description": "Initial version",    "nodes": [],    "edges": [],    "uiNodes": [],    "uiEdges": [],    "globalVariables": [],    "inputVariables": [],    "runtimeVariables": [],    "scopes": []  },  "nodes": [],  "edges": []}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Customer Support Agent",  "description": "AI agent specialized in handling customer inquiries and support tickets",  "agencyId": "gjL2sFNXJfJYa3d2OYSN",  "authorId": "usr_abc123def456",  "authorName": "John Doe",  "authorEmail": "[email protected]",  "status": "active",  "version": {    "versionName": "Version 1",    "description": "Initial version",    "nodes": [],    "edges": [],    "uiNodes": [],    "uiEdges": [],    "globalVariables": [],    "inputVariables": [],    "runtimeVariables": [],    "scopes": []  },  "nodes": [],  "edges": []}
```

Agent created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Created agent data with metadata

Created versions array (initial staging version)

```json
{  "success": true,  "message": "Agent created successfully with staging version.",  "agent": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "name": "Customer Support Agent",    "description": "AI agent specialized in handling customer inquiries and support tickets",    "locationId": "C2QujeCh8ZnC7al2InWR",    "agencyId": "gjL2sFNXJfJYa3d2OYSN",    "status": "active",    "authorId": "usr_abc123def456",    "folderId": "C2QujeCh8ZnC7al2InWR",    "folderName": null,    "createdAt": "2024-02-27T10:30:00.000Z",    "updatedAt": "2024-02-27T10:30:00.000Z"  },  "versions": [    {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v1",      "state": "staging",      "isPublished": false,      "version": 1,      "createdAt": "2024-02-27T10:30:00.000Z"    }  ]}
```

```json
{  "success": true,  "message": "Agent created successfully with staging version.",  "agent": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "name": "Customer Support Agent",    "description": "AI agent specialized in handling customer inquiries and support tickets",    "locationId": "C2QujeCh8ZnC7al2InWR",    "agencyId": "gjL2sFNXJfJYa3d2OYSN",    "status": "active",    "authorId": "usr_abc123def456",    "folderId": "C2QujeCh8ZnC7al2InWR",    "folderName": null,    "createdAt": "2024-02-27T10:30:00.000Z",    "updatedAt": "2024-02-27T10:30:00.000Z"  },  "versions": [    {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v1",      "state": "staging",      "isPublished": false,      "version": 1,      "createdAt": "2024-02-27T10:30:00.000Z"    }  ]}
```
