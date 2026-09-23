# Get conversion pixels
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-pixels`
---

# Get conversion pixels

## /ad-publishing/facebook/pixels

Retrieve Facebook conversion pixels for a location. For the FACEBOOK channel, without limit the response is { items, total }; when limit is provided (max 100) the response is a paginated { items, paging } envelope â pass after (from paging.next) to fetch the next batch. By default each item is returned in full; pass projection (comma-separated) to return only the requested fields, chosen from createdAt, fbIsCrmPixel, fbPixelCode, fbPixelId, name, type (any other value is rejected).

```json
{ items, total }
```

```json
{ items, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Channel typeAvailable optionsIGFACEBOOK

Facebook page ID

Instagram user ID

Page size for a paginated fetch (max 100, FACEBOOK channel only). When set, the response is a { items, paging } envelope instead of { items, total }.

Opaque cursor for the next batch, taken from the previous response paging.next

Fields to return on each item, comma-separated (e.g. ?projection=name,fbPixelId). When set, only the requested fields are returned. Selectable fields: createdAt, fbIsCrmPixel, fbPixelCode, fbPixelId, name, type â any other value is rejected. Omit the param entirely to receive the full item as-is.Available optionscreatedAtfbIsCrmPixelfbPixelCodefbPixelIdnametype

An { items, total } object (default), or an { items, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* objectPaginatedFacebookPixelsDTO
* PaginatedFacebookPixelsDTO

* objectPaginatedFacebookPixelsDTO
* PaginatedFacebookPixelsDTO

```json
{}
```

```json
{}
```
