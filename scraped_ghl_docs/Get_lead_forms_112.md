# Get lead forms
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-lead-forms`
---

# Get lead forms

## /ad-publishing/linkedin/:accountId/forms

Retrieve LinkedIn lead gen forms for an ad account. By default each form is returned in full as a plain array; pass projection (comma-separated, dot-notation for nested fields) to return only the requested fields â any value outside the known field set is rejected. When limit is provided (max 100) the response is a paginated { leadForms, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ leadForms, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Account identifier

Location identifier

Fields to return on each lead form, comma-separated (e.g. ?projection=id,name,state,created,reviewInfo.reviewStatus). When set, only the requested fields are returned; any value outside the known field set is rejected. Nested fields use dot-notation (naming a parent like reviewInfo returns the whole object). Omit to receive the full form (including content.questions) as-is.Available optionsidnamestatecreatedlastModifiedversionIdcreationLocaleownerreviewInforeviewInfo.reviewStatusreviewInfo.rejectionReasonscontent

Page size for a paginated fetch (max 100). When set, the response is a { leadForms, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of lead forms (default), or a { leadForms, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedLinkedInLeadFormsDTO
* PaginatedLinkedInLeadFormsDTO
* Array [
* ]

* object[]PaginatedLinkedInLeadFormsDTO
* PaginatedLinkedInLeadFormsDTO

```json
[  {}]
```

```json
[  {}]
```
