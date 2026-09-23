# Create Business
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/create-business`
---

# Create Business

## /businesses/

Create Business

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

```json
{  "name": "Microsoft",  "locationId": "5DP4iH6HLkQsiKESj6rh",  "phone": "+18832327657",  "email": "[email protected]",  "website": "www.xyz.com",  "address": "street adress",  "city": "new york",  "postalCode": "12312312",  "state": "new york",  "country": "us",  "description": "business description"}
```

```json
{  "name": "Microsoft",  "locationId": "5DP4iH6HLkQsiKESj6rh",  "phone": "+18832327657",  "email": "[email protected]",  "website": "www.xyz.com",  "address": "street adress",  "city": "new york",  "postalCode": "12312312",  "state": "new york",  "country": "us",  "description": "business description"}
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
