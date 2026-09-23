# Set Default Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/set-default-brand-voice-v-1`
---

# Set Default Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices/:brandVoiceId/default

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Set a brand voice as the default for a location. The previous default will be unset.

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Brand voice ID

Success

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the operation was successful

Brand voice ID that was set as default

Trace ID of request

```json
{  "success": true,  "brandVoiceId": "507f1f77bcf86cd799439011",  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "success": true,  "brandVoiceId": "507f1f77bcf86cd799439011",  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```
