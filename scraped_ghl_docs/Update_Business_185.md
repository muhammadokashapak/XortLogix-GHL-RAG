# Update Business
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/update-business`
---

# Update Business

## /businesses/:businessId

Update Business

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

```json
{  "name": "Microsoft",  "phone": "+18832327657",  "email": "[email protected]",  "postalCode": "12312312",  "website": "www.xyz.com",  "address": "street adress",  "state": "new york",  "city": "new york",  "country": "us",  "description": "business description"}
```

```json
{  "name": "Microsoft",  "phone": "+18832327657",  "email": "[email protected]",  "postalCode": "12312312",  "website": "www.xyz.com",  "address": "street adress",  "state": "new york",  "city": "new york",  "country": "us",  "description": "business description"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Success Value

Business Response

```json
{  "success": true,  "buiseness": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```

```json
{  "success": true,  "buiseness": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```
