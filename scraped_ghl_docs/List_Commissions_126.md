# List Commissions
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/list-commissions`
---

# List Commissions

## /affiliate-manager/:locationId/commissions

Retrieve the list of commissions for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Campaign Id

Affiliate Id

Status

Query

Maximum number of records to return. Maximum allowed value is 100.Default value:10

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Commission list

Pagination metadata

```json
{  "commissions": [    {      "_id": "6385d230f6d19db03eef6fb2",      "productId": "6385d230f6d19db03eef6fb2",      "productName": "Basic Plan",      "qty": 1,      "productCommission": 25,      "commissionAmount": 25,      "amount": 100,      "unitDiscount": 5,      "campaignName": "Summer Promo",      "commission": 25,      "commissionType": "percentage",      "transactionAt": "2024-06-16T00:00:00.000Z",      "transactionId": "txn_123",      "affiliateId": "6385d230f6d19db03eef6fb2",      "payoutId": "6385d230f6d19db03eef6fb2",      "status": "pending",      "currency": "USD",      "isTrial": false,      "customer": {        "_id": "6385d230f6d19db03eef6fb2",        "firstName": "John",        "lastName": "Doe",        "email": "[email protected]",        "type": "customer"      },      "createdAt": "2024-06-16T00:00:00.000Z",      "eventId": "evt_123",      "campaign": {        "id": "6385d230f6d19db03eef6fb2",        "name": "Summer Promo",        "liveMode": true      },      "affiliate": {        "_id": "6385d230f6d19db03eef6fb2",        "name": "John Doe",        "email": "[email protected]"      },      "dueAt": "2024-06-30T00:00:00.000Z",      "liveMode": true,      "tier": 1    }  ],  "meta": {    "count": 42  }}
```

```json
{  "commissions": [    {      "_id": "6385d230f6d19db03eef6fb2",      "productId": "6385d230f6d19db03eef6fb2",      "productName": "Basic Plan",      "qty": 1,      "productCommission": 25,      "commissionAmount": 25,      "amount": 100,      "unitDiscount": 5,      "campaignName": "Summer Promo",      "commission": 25,      "commissionType": "percentage",      "transactionAt": "2024-06-16T00:00:00.000Z",      "transactionId": "txn_123",      "affiliateId": "6385d230f6d19db03eef6fb2",      "payoutId": "6385d230f6d19db03eef6fb2",      "status": "pending",      "currency": "USD",      "isTrial": false,      "customer": {        "_id": "6385d230f6d19db03eef6fb2",        "firstName": "John",        "lastName": "Doe",        "email": "[email protected]",        "type": "customer"      },      "createdAt": "2024-06-16T00:00:00.000Z",      "eventId": "evt_123",      "campaign": {        "id": "6385d230f6d19db03eef6fb2",        "name": "Summer Promo",        "liveMode": true      },      "affiliate": {        "_id": "6385d230f6d19db03eef6fb2",        "name": "John Doe",        "email": "[email protected]"      },      "dueAt": "2024-06-30T00:00:00.000Z",      "liveMode": true,      "tier": 1    }  ],  "meta": {    "count": 42  }}
```
