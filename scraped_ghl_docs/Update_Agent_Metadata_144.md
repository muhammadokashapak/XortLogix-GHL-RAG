# Update Agent Metadata
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/update-agent-metadata`
---

# Update Agent Metadata

## /agent-studio/agent/:agentId

Updates agent metadata such as name, description, and status.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID for authorization (cannot be updated)

Name of the agent

Description of the agent

Status of the agentAvailable optionsactiveinactivearchived

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Updated Customer Support Agent",  "description": "Updated AI agent with enhanced customer support capabilities",  "status": "active"}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Updated Customer Support Agent",  "description": "Updated AI agent with enhanced customer support capabilities",  "status": "active"}
```

Agent metadata updated successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Updated agent or version data

```json
{  "success": true,  "message": "Agent updated successfully",  "data": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "versionId": "v1a2b3c4d5e6f7g8h9i0",    "name": "Updated Customer Support Agent",    "description": "Updated AI agent with enhanced customer support capabilities",    "status": "active",    "updatedAt": "2024-02-27T11:45:00.000Z"  }}
```

```json
{  "success": true,  "message": "Agent updated successfully",  "data": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "versionId": "v1a2b3c4d5e6f7g8h9i0",    "name": "Updated Customer Support Agent",    "description": "Updated AI agent with enhanced customer support capabilities",    "status": "active",    "updatedAt": "2024-02-27T11:45:00.000Z"  }}
```
