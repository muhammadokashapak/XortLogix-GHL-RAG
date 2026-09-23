# Google Ads
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-ads`
---

Documentation for Ad-publishing API

## ðï¸Get conversions

Retrieve Google Ads conversion actions for a location. For AD_MANAGER, without `limit` the response is a plain array; when `limit` is provided (max 100, default 100) the response is a paginated `{ conversions, paging }` envelope â pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Upsert conversion

Create or update a Google Ads conversion action

## ðï¸Get conversion by ID

Retrieve a specific Google Ads conversion action by ID

## ðï¸Delete conversion

Delete a Google Ads conversion action by ID

## ðï¸Publish ad

Publish a Google ad and push it live

## ðï¸Search targeting options

Search Google geo-locations for ad targeting

## ðï¸Get keyword ideas

Retrieve keyword suggestions for Google Ads campaigns

## ðï¸Get assets

Retrieve Google Ads creative assets for a location. Without `limit` the response is a plain array of assets. When `limit` is provided (max 100, default 100) the response is a paginated `{ assets, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Upsert assets

Create or update Google Ads creative assets

## ðï¸Get entities

Retrieve Google campaigns, ad groups, or ads based on entity type

## ðï¸Get target interests

Retrieve affinity and in-market audience options for Google Ads targeting. Without `limit` the response is a plain array of root interests (each with a nested children tree). When `limit` is provided (max 100) the response is a paginated `{ targetInterests, paging }` envelope â a page counts root interests; pass `pageToken` (from `paging.next`) to fetch the next batch. By default each node is returned in full; pass `projection` (comma-separated, e.g. ?projection=name,userInterestId,children) to return only the requested fields â selecting `children` prunes the whole tree recursively with the same selection, and any value outside the known field set is rejected.

## ðï¸Get segments

Retrieve Google Ads audience segments for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100, default 100) the response is a paginated `{ segments, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Upsert segment

Create or update a Google Ads audience segment

## ðï¸Delete segment

Delete a Google Ads audience segment by ID

## ðï¸Get segment by ID

Retrieve a specific Google Ads audience segment by ID

## ðï¸Create offline user list job

Create a job to upload users to a Google customer match list

## ðï¸Upsert audience

Create or update a Google Ads combined audience

## ðï¸Get audiences

Retrieve Google Ads combined audiences for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100, default 100) the response is a paginated `{ audiences, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Get audience by ID

Retrieve a specific Google Ads combined audience by ID

## ðï¸Upsert Google campaign

Create or update a full Google Ads campaign structure

## ðï¸Get Google campaign by ID

Retrieve a specific Google Ads campaign by ID

## ðï¸Get conversion goals

Retrieve Google Ads conversion goals for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100, default 100) the response is a paginated `{ conversionGoals, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.
