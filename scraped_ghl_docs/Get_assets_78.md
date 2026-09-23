# Get assets
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-assets`
---

# Get assets

## /ad-publishing/google/assets

Retrieve Google Ads creative assets for a location. Without limit the response is a plain array of assets. When limit is provided (max 100, default 100) the response is a paginated { assets, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ assets, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Asset type to retrieveAvailable optionsCALLSITELINK

Asset identifier

Advertiser only flag

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { assets, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of assets (default), or a { assets, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleAssetsDTO
* PaginatedGoogleAssetsDTO
* Array [
* ]

* object[]PaginatedGoogleAssetsDTO
* PaginatedGoogleAssetsDTO

```json
[  {}]
```

```json
[  {}]
```
