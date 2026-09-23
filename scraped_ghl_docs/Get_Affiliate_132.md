# Get Affiliate
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/get-affiliate`
---

# Get Affiliate

## /affiliate-manager/:locationId/affiliates/:affiliateId

Retrieve a single affiliate by id for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Affiliate Id

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Affiliate id

Affiliate first name

Affiliate last name

Affiliate phone number

Whether the affiliate is deleted

Location id

Whether the affiliate is active

Affiliate address

Affiliate avatar URL

Created at timestamp

Created by audit info

Facebook URL

Instagram URL

LinkedIn URL

Twitter URL

YouTube URL

Website URL

Contact id associated with the affiliate

Campaign ids

VAT ID

Updated at timestamp

W8 form URL

W9 form URL

Last updated by audit info

Affiliate email

Affiliate revenue

Customer count

Lead count

Dropped customer count

Click count

Paid amount

Currency code

Owned amount

```json
{  "_id": "63d147176c5bbc30e9e091a4",  "firstName": "John",  "lastName": "Doe",  "phone": "+1 888 888-8888",  "deleted": false,  "locationId": "ve9EPM428h8vShlRW1KT",  "active": true,  "address": "123 Main St",  "avatar": "https://example.com/avatar.png",  "createdAt": "2024-06-16T00:00:00.000Z",  "createdBy": {},  "facebookUrl": "https://facebook.com/johndoe",  "instagramUrl": "https://instagram.com/johndoe",  "linkedInUrl": "https://linkedin.com/in/johndoe",  "twitterUrl": "https://twitter.com/johndoe",  "youtubeUrl": "https://youtube.com/channel",  "websiteUrl": "https://example.com",  "contactId": "ve9EPM428h8vShlRW1KT",  "campaignIds": [    "650173614761b33c46d33b19"  ],  "vatId": "VAT123",  "updatedAt": "2024-06-16T00:00:00.000Z",  "w8Form": "string",  "w9Form": "string",  "lastUpdatedBy": {},  "email": "[email protected]",  "revenue": 1250.5,  "customer": 15,  "lead": 5,  "droppedCustomer": 2,  "clickCount": 100,  "paid": 500,  "currency": "USD",  "owned": 750}
```

```json
{  "_id": "63d147176c5bbc30e9e091a4",  "firstName": "John",  "lastName": "Doe",  "phone": "+1 888 888-8888",  "deleted": false,  "locationId": "ve9EPM428h8vShlRW1KT",  "active": true,  "address": "123 Main St",  "avatar": "https://example.com/avatar.png",  "createdAt": "2024-06-16T00:00:00.000Z",  "createdBy": {},  "facebookUrl": "https://facebook.com/johndoe",  "instagramUrl": "https://instagram.com/johndoe",  "linkedInUrl": "https://linkedin.com/in/johndoe",  "twitterUrl": "https://twitter.com/johndoe",  "youtubeUrl": "https://youtube.com/channel",  "websiteUrl": "https://example.com",  "contactId": "ve9EPM428h8vShlRW1KT",  "campaignIds": [    "650173614761b33c46d33b19"  ],  "vatId": "VAT123",  "updatedAt": "2024-06-16T00:00:00.000Z",  "w8Form": "string",  "w9Form": "string",  "lastUpdatedBy": {},  "email": "[email protected]",  "revenue": 1250.5,  "customer": 15,  "lead": 5,  "droppedCustomer": 2,  "clickCount": 100,  "paid": 500,  "currency": "USD",  "owned": 750}
```
