# List Brand Voices
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/list-brand-voices-v-1`
---

# List Brand Voices

## /brand-boards/public/v1/locations/:locationId/voices

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Get list of brand voices for a location

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Number of brand voices to return. Defaults to 10, minimum is 1, maximum is 20Possible values: >= 1 and <= 20Default value:10

Possible values: >= 1 and <= 20Default value:10

Number of brand voices to skip for pagination. Defaults to 0, minimum is 0Possible values: >= 0Default value:0

Possible values: >= 0Default value:0

Search text for brand voice name

Whether to return deleted brand voices. Defaults to falseDefault value:false

Success

* application/json

* SchemaExample (auto)
* Example (auto)

List of brand voices

Total count of brand voices

Trace ID of request

```json
{  "items": [    {      "id": "507f1f77bcf86cd799439011",      "name": "My Brand Voice",      "isDefault": false,      "createdAt": "2024-01-05T12:00:00.000Z",      "updatedAt": "2024-01-05T12:00:00.000Z"    }  ],  "total": 25,  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "items": [    {      "id": "507f1f77bcf86cd799439011",      "name": "My Brand Voice",      "isDefault": false,      "createdAt": "2024-01-05T12:00:00.000Z",      "updatedAt": "2024-01-05T12:00:00.000Z"    }  ],  "total": 25,  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```
