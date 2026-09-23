# List Affiliates
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/list-affiliates`
---

# List Affiliates

## /affiliate-manager/:locationId/affiliates

Retrieve the list of affiliates for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Maximum number of records to return. Maximum allowed value is 100.Default value:10

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Affiliate list

Pagination metadata

```json
{  "affiliates": [    {      "_id": "63d147176c5bbc30e9e091a4",      "firstName": "John",      "lastName": "Doe",      "phone": "+1 888 888-8888",      "deleted": false,      "locationId": "ve9EPM428h8vShlRW1KT",      "active": true,      "address": "123 Main St",      "avatar": "https://example.com/avatar.png",      "createdAt": "2024-06-16T00:00:00.000Z",      "createdBy": {},      "facebookUrl": "https://facebook.com/johndoe",      "instagramUrl": "https://instagram.com/johndoe",      "linkedInUrl": "https://linkedin.com/in/johndoe",      "twitterUrl": "https://twitter.com/johndoe",      "youtubeUrl": "https://youtube.com/channel",      "websiteUrl": "https://example.com",      "contactId": "ve9EPM428h8vShlRW1KT",      "campaignIds": [        "650173614761b33c46d33b19"      ],      "vatId": "VAT123",      "updatedAt": "2024-06-16T00:00:00.000Z",      "w8Form": "string",      "w9Form": "string",      "lastUpdatedBy": {},      "email": "[email protected]",      "revenue": 1250.5,      "customer": 15,      "lead": 5,      "droppedCustomer": 2,      "clickCount": 100,      "paid": 500,      "currency": "USD",      "owned": 750    }  ],  "meta": {    "count": 42  }}
```

```json
{  "affiliates": [    {      "_id": "63d147176c5bbc30e9e091a4",      "firstName": "John",      "lastName": "Doe",      "phone": "+1 888 888-8888",      "deleted": false,      "locationId": "ve9EPM428h8vShlRW1KT",      "active": true,      "address": "123 Main St",      "avatar": "https://example.com/avatar.png",      "createdAt": "2024-06-16T00:00:00.000Z",      "createdBy": {},      "facebookUrl": "https://facebook.com/johndoe",      "instagramUrl": "https://instagram.com/johndoe",      "linkedInUrl": "https://linkedin.com/in/johndoe",      "twitterUrl": "https://twitter.com/johndoe",      "youtubeUrl": "https://youtube.com/channel",      "websiteUrl": "https://example.com",      "contactId": "ve9EPM428h8vShlRW1KT",      "campaignIds": [        "650173614761b33c46d33b19"      ],      "vatId": "VAT123",      "updatedAt": "2024-06-16T00:00:00.000Z",      "w8Form": "string",      "w9Form": "string",      "lastUpdatedBy": {},      "email": "[email protected]",      "revenue": 1250.5,      "customer": 15,      "lead": 5,      "droppedCustomer": 2,      "clickCount": 100,      "paid": 500,      "currency": "USD",      "owned": 750    }  ],  "meta": {    "count": 42  }}
```
