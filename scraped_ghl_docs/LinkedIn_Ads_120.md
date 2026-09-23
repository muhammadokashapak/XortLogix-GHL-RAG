# LinkedIn Ads
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/linked-in-ads`
---

Documentation for Ad-publishing API

## ðï¸Get ad campaign group

Retrieve a LinkedIn ad campaign group by ID

## ðï¸Publish ad campaign group

Publish a LinkedIn ad campaign group and push it live

## ðï¸Upsert ad campaign group

Create or update a LinkedIn ad campaign group with campaigns and ads

## ðï¸Search targeting options

Search LinkedIn targeting facets such as locations, industries, and job titles

## ðï¸Get lead forms

Retrieve LinkedIn lead gen forms for an ad account. By default each form is returned in full as a plain array; pass `projection` (comma-separated, dot-notation for nested fields) to return only the requested fields â any value outside the known field set is rejected. When `limit` is provided (max 100) the response is a paginated `{ leadForms, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Create lead form

Create a new LinkedIn lead gen form for an ad account

## ðï¸Update ad status

Pause or resume a LinkedIn ad, campaign, or ad group
