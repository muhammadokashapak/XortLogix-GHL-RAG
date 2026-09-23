# List Payouts
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/list-payouts`
---

# List Payouts

## /affiliate-manager/:locationId/payouts

Retrieve the list of payouts for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Payout status

query

Affiliate Id

Campaign Id

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Payout list

Pagination metadata

```json
{  "payouts": [    {      "_id": "65df04201e428a0c5ebb6571",      "locationId": "ve9EPM428h8vShlRW1KT",      "affiliateId": "65df04201e428a0c5ebb6572",      "campaignId": "65df04201e428a0c5ebb6573",      "currency": "USD",      "amount": 150,      "status": "pending",      "payoutMonth": "2024-06-01T00:00:00.000Z",      "dueAt": "2024-06-30T00:00:00.000Z",      "paidAt": "2024-06-30T00:00:00.000Z",      "paidMeta": {},      "paidMethod": "manual",      "altId": "alt_123",      "deleted": false,      "isMigrated": false,      "createdAt": "2024-06-16T00:00:00.000Z",      "updatedAt": "2024-06-17T00:00:00.000Z",      "campaign": "Summer Promo",      "affiliateName": "John Doe",      "affiliateEmail": "[email protected]",      "payoutMethod": "paypal",      "affiliate": {        "_id": "63d147176c5bbc30e9e091a4",        "firstName": "John",        "lastName": "Doe",        "phone": "+1 888 888-8888",        "deleted": false,        "locationId": "ve9EPM428h8vShlRW1KT",        "active": true,        "address": "123 Main St",        "avatar": "https://example.com/avatar.png",        "createdAt": "2024-06-16T00:00:00.000Z",        "createdBy": {},        "facebookUrl": "https://facebook.com/johndoe",        "instagramUrl": "https://instagram.com/johndoe",        "linkedInUrl": "https://linkedin.com/in/johndoe",        "twitterUrl": "https://twitter.com/johndoe",        "youtubeUrl": "https://youtube.com/channel",        "websiteUrl": "https://example.com",        "contactId": "ve9EPM428h8vShlRW1KT",        "campaignIds": [          "650173614761b33c46d33b19"        ],        "vatId": "VAT123",        "updatedAt": "2024-06-16T00:00:00.000Z",        "w8Form": "string",        "w9Form": "string",        "lastUpdatedBy": {},        "email": "[email protected]",        "revenue": 1250.5,        "customer": 15,        "lead": 5,        "droppedCustomer": 2,        "clickCount": 100,        "paid": 500,        "currency": "USD",        "owned": 750      }    }  ],  "meta": {    "count": 42  }}
```

```json
{  "payouts": [    {      "_id": "65df04201e428a0c5ebb6571",      "locationId": "ve9EPM428h8vShlRW1KT",      "affiliateId": "65df04201e428a0c5ebb6572",      "campaignId": "65df04201e428a0c5ebb6573",      "currency": "USD",      "amount": 150,      "status": "pending",      "payoutMonth": "2024-06-01T00:00:00.000Z",      "dueAt": "2024-06-30T00:00:00.000Z",      "paidAt": "2024-06-30T00:00:00.000Z",      "paidMeta": {},      "paidMethod": "manual",      "altId": "alt_123",      "deleted": false,      "isMigrated": false,      "createdAt": "2024-06-16T00:00:00.000Z",      "updatedAt": "2024-06-17T00:00:00.000Z",      "campaign": "Summer Promo",      "affiliateName": "John Doe",      "affiliateEmail": "[email protected]",      "payoutMethod": "paypal",      "affiliate": {        "_id": "63d147176c5bbc30e9e091a4",        "firstName": "John",        "lastName": "Doe",        "phone": "+1 888 888-8888",        "deleted": false,        "locationId": "ve9EPM428h8vShlRW1KT",        "active": true,        "address": "123 Main St",        "avatar": "https://example.com/avatar.png",        "createdAt": "2024-06-16T00:00:00.000Z",        "createdBy": {},        "facebookUrl": "https://facebook.com/johndoe",        "instagramUrl": "https://instagram.com/johndoe",        "linkedInUrl": "https://linkedin.com/in/johndoe",        "twitterUrl": "https://twitter.com/johndoe",        "youtubeUrl": "https://youtube.com/channel",        "websiteUrl": "https://example.com",        "contactId": "ve9EPM428h8vShlRW1KT",        "campaignIds": [          "650173614761b33c46d33b19"        ],        "vatId": "VAT123",        "updatedAt": "2024-06-16T00:00:00.000Z",        "w8Form": "string",        "w9Form": "string",        "lastUpdatedBy": {},        "email": "[email protected]",        "revenue": 1250.5,        "customer": 15,        "lead": 5,        "droppedCustomer": 2,        "clickCount": 100,        "paid": 500,        "currency": "USD",        "owned": 750      }    }  ],  "meta": {    "count": 42  }}
```
