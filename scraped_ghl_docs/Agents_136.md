# Agents
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/agents`
---

Documentation for Agent Studio APIs

## ðï¸Create Agent

Creates a new agent with staging version. The agent will be created with an initial staging version that can later be promoted to production.

## ðï¸List Agents

Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset. Optionally filter by isPublished=true to return only agents with a published production version.

## ðï¸Update Agent

Updates a specific agent version by versionId. Supports updating nodes, edges, variables, and configuration.

## ðï¸Update Agent Metadata

Updates agent metadata such as name, description, and status.

## ðï¸Delete Agent

Deletes an agent and all its versions.

## ðï¸Get Agent

Gets a specific agent by its ID for the specified location with all its versions. Returns complete agent metadata and all non-deleted versions (draft, staging, production). locationId is required parameter. The agent must have active status.

## ðï¸Promote to Production

Promotes a draft version to production.

## ðï¸Execute Agent

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body.

## ðï¸List Agents (Deprecated)

**Deprecated endpoint - use GET /agent instead.**

## ðï¸Get Agent (Deprecated)

**Deprecated endpoint - use GET /agent/:agentId instead.**

## ðï¸Execute Agent (Deprecated)

**Deprecated endpoint - use POST /agent/:agentId/execute instead.**
