# Get page lead forms
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-page-lead-forms`
---

# Get page lead forms

## /ad-publishing/facebook/page/:pageId/forms

Retrieve lead gen forms for a specific Facebook page (published + drafts), sorted newest-first by createdTime. By default each form is returned in full (including its questions) as a plain array; pass projection (comma-separated) to return only the requested fields â any value outside the known field set is rejected. Pass limit (max 100) for a { forms, paging } envelope; use after (from paging.next) to fetch the next batch.

```json
{ forms, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Facebook page identifier

Location identifier

Fields to return on each lead form, comma-separated (e.g. ?projection=name,id,pageId,status,isDraft,createdTime). When set, only the requested fields are returned; any other value is rejected. Omit to receive the full form (including questions) as-is.Available optionsidnamepageIdstatusisDraftcreatedTimelocalepagequestions

Page size for a paginated fetch (max 100). When set, the response is a { forms, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of lead forms (default), or a { forms, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookLeadFormsDTO
* PaginatedFacebookLeadFormsDTO
* Array [
* ]

* object[]PaginatedFacebookLeadFormsDTO
* PaginatedFacebookLeadFormsDTO

```json
[  {}]
```

```json
[  {}]
```
