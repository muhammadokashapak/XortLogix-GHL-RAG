# Get Facebook pages
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-pages`
---

# Get Facebook pages

## /ad-publishing/facebook/pages

Retrieve Facebook pages for the connected account. Without limit the response is an array of pages (this array response will soon be deprecated â migrate to the paginated form). When limit is provided the response is a paginated { pages, paging } envelope; pass after (from paging.next) to fetch the next batch.

```json
{ pages, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Fetch existing pages flag

Page size for a paginated fetch (fetchExisting only, max 50). When set, the response is a { pages, paging } envelope instead of an array.

Opaque cursor for the next batch, taken from the previous response paging.next

An array of pages (default; will soon be deprecated â use limit to get the paginated { pages, paging } response), or a { pages, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookPagesDTO
* PaginatedFacebookPagesDTO
* Array [
* ]

* object[]PaginatedFacebookPagesDTO
* PaginatedFacebookPagesDTO

Facebook Page ID

Page name

Page category

Page profile picture URL

When the page was connected to the location

Whether the page is already connected to the location

Whether the Facebook Lead Ads TOS is accepted for the page

Whether this is the default connected page (only present when fetchExisting is false)

```json
[  {    "id": "1234567890",    "name": "Acme Marketing",    "category": "Marketing Agency",    "picture": "https://scontent.xx.fbcdn.net/...",    "createdOn": "2026-01-15T10:00:00.000Z",    "isConnected": false,    "tosAccepted": true,    "isDefault": false  }]
```

```json
[  {    "id": "1234567890",    "name": "Acme Marketing",    "category": "Marketing Agency",    "picture": "https://scontent.xx.fbcdn.net/...",    "createdOn": "2026-01-15T10:00:00.000Z",    "isConnected": false,    "tosAccepted": true,    "isDefault": false  }]
```
