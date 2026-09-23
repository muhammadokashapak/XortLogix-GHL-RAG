# Get target interests
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-target-interests`
---

# Get target interests

## /ad-publishing/google/target-interests

Retrieve affinity and in-market audience options for Google Ads targeting. Without limit the response is a plain array of root interests (each with a nested children tree). When limit is provided (max 100) the response is a paginated { targetInterests, paging } envelope â a page counts root interests; pass pageToken (from paging.next) to fetch the next batch. By default each node is returned in full; pass projection (comma-separated, e.g. ?projection=name,userInterestId,children) to return only the requested fields â selecting children prunes the whole tree recursively with the same selection, and any value outside the known field set is rejected.

```json
{ targetInterests, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Interest typeAvailable optionsAFFINITYIN_MARKET

Channel type

Page size for a paginated fetch (max 100). When set, the response is a { targetInterests, paging } envelope instead of a plain array. Counts root interests â each root includes its full children tree.

Opaque cursor for the next batch, taken from the previous response paging.next

Fields to return on each interest node, comma-separated (e.g. ?projection=name,userInterestId,children). When set, only the requested fields are returned. Selecting children prunes the whole tree recursively with the same selection; availabilities returns the whole array. Any value outside the known field set is rejected. Omit the param entirely to receive the full node as-is.Available optionsresourceNametaxonomyTypeuserInterestIdnameuserInterestParentavailabilitieschildren

A plain array of root interests (default), or a { targetInterests, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleTargetInterestsDTO
* PaginatedGoogleTargetInterestsDTO
* Array [
* ]

* object[]PaginatedGoogleTargetInterestsDTO
* PaginatedGoogleTargetInterestsDTO

```json
[  {}]
```

```json
[  {}]
```
