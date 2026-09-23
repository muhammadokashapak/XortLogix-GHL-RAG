# Update Agent
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/update-agent-version`
---

# Update Agent

## /agent-studio/agent/versions/:versionId

Updates a specific agent version by versionId. Supports updating nodes, edges, variables, and configuration.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID for authorization

Version name

Description of the version

Complete array of nodes for the agent workflow. Provide all nodes including unchanged ones.

Complete array of edges connecting the nodes. Provide all edges including unchanged ones.

Global variables accessible throughout the agent workflow

Input variables required from user at execution time

Runtime variables generated during agent execution

Global configuration including prompts and settings

User ID performing the update

User name performing the update

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "versionName": "Customer Support Agent v2",  "description": "Updated version with improved customer handling logic",  "nodes": [    {      "nodeId": "node_1",      "nodeName": "Start",      "type": "start",      "isStartNode": true    },    {      "nodeId": "node_2",      "nodeName": "LLM Node",      "type": "llm",      "nodeConfig": {        "prompt": "How can I help you?",        "llmProvider": "openai",        "llmModel": "gpt-4"      }    }  ],  "edges": [    {      "startNode": "node_1",      "endNode": "node_2"    }  ],  "globalVariables": [    {      "key": "apiKey",      "type": "string",      "value": "your-api-key"    }  ],  "inputVariables": [    {      "key": "customerName",      "type": "string",      "description": "Customer name for personalization"    }  ],  "runtimeVariables": [    {      "key": "sessionId",      "type": "string",      "description": "Current session identifier"    }  ],  "globalConfig": {    "globalPrompt": {      "currentPrompt": "You are a helpful customer support assistant.",      "history": []    }  },  "userId": "usr_abc123def456",  "userName": "John Doe"}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "versionName": "Customer Support Agent v2",  "description": "Updated version with improved customer handling logic",  "nodes": [    {      "nodeId": "node_1",      "nodeName": "Start",      "type": "start",      "isStartNode": true    },    {      "nodeId": "node_2",      "nodeName": "LLM Node",      "type": "llm",      "nodeConfig": {        "prompt": "How can I help you?",        "llmProvider": "openai",        "llmModel": "gpt-4"      }    }  ],  "edges": [    {      "startNode": "node_1",      "endNode": "node_2"    }  ],  "globalVariables": [    {      "key": "apiKey",      "type": "string",      "value": "your-api-key"    }  ],  "inputVariables": [    {      "key": "customerName",      "type": "string",      "description": "Customer name for personalization"    }  ],  "runtimeVariables": [    {      "key": "sessionId",      "type": "string",      "description": "Current session identifier"    }  ],  "globalConfig": {    "globalPrompt": {      "currentPrompt": "You are a helpful customer support assistant.",      "history": []    }  },  "userId": "usr_abc123def456",  "userName": "John Doe"}
```

Version updated successfully

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
