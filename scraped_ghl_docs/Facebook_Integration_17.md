# Facebook Integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/facebook-integration`
---

Documentation for Ad-publishing API

## ðï¸Get current Facebook user

Retrieve the authenticated Facebook user profile for a location

## ðï¸Get Facebook pages

Retrieve Facebook pages for the connected account. Without `limit` the response is an array of pages (this array response will soon be deprecated â migrate to the paginated form). When `limit` is provided the response is a paginated `{ pages, paging }` envelope; pass `after` (from `paging.next`) to fetch the next batch.

## ðï¸Get Instagram accounts for page

Retrieve Instagram accounts linked to a specific Facebook page

## ðï¸Get page lead forms

Retrieve lead gen forms for a specific Facebook page (published + drafts), sorted newest-first by `createdTime`. By default each form is returned in full (including its `questions`) as a plain array; pass `projection` (comma-separated) to return only the requested fields â any value outside the known field set is rejected. Pass `limit` (max 100) for a `{ forms, paging }` envelope; use `after` (from `paging.next`) to fetch the next batch.

## ðï¸Create page lead form

Create a new lead gen form on a Facebook page

## ðï¸Get ad accounts

Retrieve Facebook ad accounts available for the connected user

## ðï¸Get ad account details

Retrieve details of a specific Facebook ad account

## ðï¸Delete ad account

Remove a Facebook ad account connection from a location

## ðï¸Get conversation forms

Retrieve Facebook conversation lead forms for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100) the response is a paginated `{ conversationForms, paging }` envelope; pass `after` (from `paging.next`) to fetch the next batch.

## ðï¸Create conversation form

Create a new Facebook conversation lead form

## ðï¸Create Facebook integration

Create a Facebook ad integration for a location with page and ad account

## ðï¸Get Facebook integration

Retrieve the Facebook ad integration details for a location

## ðï¸Delete Facebook integration

Remove the Facebook ad integration from a location

## ðï¸Delete page connection

Remove a Facebook page connection from a location

## ðï¸Set default page

Set the default Facebook page for a location

## ðï¸Get lead form by ID

Retrieve a specific Facebook lead form by its ID
