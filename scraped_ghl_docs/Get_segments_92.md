# Get segments
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-segments`
---

# Get segments

## /ad-publishing/google/segments

Retrieve Google Ads audience segments for a location. Without limit the response is a plain array. When limit is provided (max 100, default 100) the response is a paginated { segments, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ segments, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Segment typeAvailable optionsCUSTOM_SEGMENTSDATA_SEGMENTSALL

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { segments, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of segments (default), or a { segments, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleSegmentsDTO
* PaginatedGoogleSegmentsDTO
* Array [
* ]

* object[]PaginatedGoogleSegmentsDTO
* PaginatedGoogleSegmentsDTO

```json
[  {}]
```

```json
[  {}]
```
