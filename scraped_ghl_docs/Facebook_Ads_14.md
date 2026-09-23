# Facebook Ads
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/facebook-ads`
---

Documentation for Ad-publishing API

## ðï¸Search targeting options

Search Facebook geo-locations and interests for ad targeting

## ðï¸Publish campaign

Publish a Facebook campaign and push it live to Facebook

## ðï¸Get conversion pixels

Retrieve Facebook conversion pixels for a location. For the FACEBOOK channel, without `limit` the response is `{ items, total }`; when `limit` is provided (max 100) the response is a paginated `{ items, paging }` envelope â pass `after` (from `paging.next`) to fetch the next batch. By default each item is returned in full; pass `projection` (comma-separated) to return only the requested fields, chosen from `createdAt`, `fbIsCrmPixel`, `fbPixelCode`, `fbPixelId`, `name`, `type` (any other value is rejected).

## ðï¸Upsert conversion pixel

Create or update a Facebook conversion pixel configuration

## ðï¸Get custom audiences

Retrieve Facebook custom audiences for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100) the response is a paginated `{ customAudiences, paging }` envelope; pass `after` (from `paging.next`) to fetch the next batch. By default each item is returned in full; pass `projection` (comma-separated, dot-notation for nested fields, e.g. ?projection=id,name,dataSource.type) to return only the requested fields â any value outside the known field set is rejected.

## ðï¸Delete custom audience

Delete a Facebook custom audience by ID

## ðï¸Update custom audience

Update name or description of a Facebook custom audience

## ðï¸Get custom audience by ID

Retrieve a specific Facebook custom audience by its ID

## ðï¸Add custom audience member

Add a member to a Facebook custom audience

## ðï¸Remove custom audience member

Remove a member from a Facebook custom audience

## ðï¸Batch update audience members

Add or remove members in bulk from a Facebook custom audience via CSV or smart lists

## ðï¸Get campaign with linked entities

Retrieve a Facebook campaign with its linked adsets and ads

## ðï¸Get entities

Retrieve Facebook campaigns, adsets, or ads based on entity type

## ðï¸Upsert campaign

Create or update a Facebook campaign

## ðï¸Upsert adset

Create or update a Facebook ad set

## ðï¸Upsert ad

Create or update a Facebook ad

## ðï¸Pause campaign

Pause a running Facebook campaign

## ðï¸Resume campaign

Resume a paused Facebook campaign

## ðï¸Duplicate campaign

Duplicate an existing Facebook campaign

## ðï¸Delete campaign

Delete a Facebook campaign by ID

## ðï¸Pause ad set

Pause a running Facebook ad set

## ðï¸Resume ad set

Resume a paused Facebook ad set

## ðï¸Duplicate ad set

Duplicate an existing Facebook ad set

## ðï¸Delete ad set

Delete a Facebook ad set by ID

## ðï¸Pause ad

Pause a running Facebook ad

## ðï¸Resume ad

Resume a paused Facebook ad

## ðï¸Duplicate ad

Duplicate an existing Facebook ad

## ðï¸Delete ad

Delete a Facebook ad by ID

## ðï¸Get campaign publishing progress

Returns Redis-backed publish progress for a campaign while it is publishing to Meta. Used by the validation funnel UI to poll step counts and completion state.
