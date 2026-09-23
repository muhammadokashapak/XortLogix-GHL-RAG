# Get custom audiences
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-custom-audiences`
---

# Get custom audiences

## /ad-publishing/facebook/custom-audience

Retrieve Facebook custom audiences for a location. Without limit the response is a plain array. When limit is provided (max 100) the response is a paginated { customAudiences, paging } envelope; pass after (from paging.next) to fetch the next batch. By default each item is returned in full; pass projection (comma-separated, dot-notation for nested fields, e.g. ?projection=id,name,dataSource.type) to return only the requested fields â any value outside the known field set is rejected.

```json
{ customAudiences, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Audience list typeAvailable optionslookalikecustomall

Audience data sourceAvailable optionsad_managerintegration

Ad account identifier

Page size for a paginated fetch (max 100). When set, the response is a { customAudiences, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

Fields to return on each item, comma-separated (e.g. ?projection=id,name,dataSource.type). When set, only the requested fields are returned. Nested fields use dot-notation; naming a parent (e.g. dataSource) returns the whole nested object. Any value outside the known field set is rejected. Omit the param entirely to receive the full item as-is.Available optionsidnamedescriptionapproximateCountLowerBoundapproximateCountUpperBoundsubtypetimeCreatedtimeUpdateddataSourcedataSource.typedataSource.subTypedataSource.creationParams

A plain array of custom audiences (default), or a { customAudiences, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookCustomAudiencesDTO
* PaginatedFacebookCustomAudiencesDTO
* Array [
* ]

* object[]PaginatedFacebookCustomAudiencesDTO
* PaginatedFacebookCustomAudiencesDTO

```json
[  {}]
```

```json
[  {}]
```
