# Get audiences
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-audiences`
---

# Get audiences

## /ad-publishing/google/audiences

Retrieve Google Ads combined audiences for a location. Without limit the response is a plain array. When limit is provided (max 100, default 100) the response is a paginated { audiences, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ audiences, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { audiences, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of audiences (default), or a { audiences, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleAudiencesDTO
* PaginatedGoogleAudiencesDTO
* Array [
* ]

* object[]PaginatedGoogleAudiencesDTO
* PaginatedGoogleAudiencesDTO

```json
[  {}]
```

```json
[  {}]
```
