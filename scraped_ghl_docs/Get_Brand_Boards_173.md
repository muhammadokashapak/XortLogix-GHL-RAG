# Get Brand Boards
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/get-brand-boards-by-location`
---

# Get Brand Boards

## /brand-boards/:locationId

Retrieves all Brand Boards for a specific location

## Requestâ

API VersionAvailable options2021-04-15

Location ID where the brand boards exist

Maximum number of brand boards to returnDefault value:10

Number of brand boards to skip for paginationDefault value:0

Search term to filter brand boards by nameDefault value:

Include deleted brand boards in resultsDefault value:false

Success

* application/json

* SchemaExample (auto)
* Example (auto)

Array of brand boards for the location

Total number of brand boards matching the query

```json
{  "brandBoards": [    {      "_id": "507f1f77bcf86cd799439011",      "name": "My Brand Board",      "updatedAt": "2024-01-05T12:00:00.000Z",      "default": true,      "meta": {        "updatedBy": "user_abc123",        "lastAction": "UPDATE",        "sourceType": "blank"      }    }  ],  "totalCount": 42}
```

```json
{  "brandBoards": [    {      "_id": "507f1f77bcf86cd799439011",      "name": "My Brand Board",      "updatedAt": "2024-01-05T12:00:00.000Z",      "default": true,      "meta": {        "updatedBy": "user_abc123",        "lastAction": "UPDATE",        "sourceType": "blank"      }    }  ],  "totalCount": 42}
```
