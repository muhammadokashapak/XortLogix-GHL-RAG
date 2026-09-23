# Get all authors
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/get-all-blog-authors-by-location`
---

# Get all authors

## /blogs/authors

The "Get all authors" Api return the blog authors for a given location ID. Please use "blogs/author.readonly"

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Number of authors to show in the listing

Number of authors to skip in listing

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Array of authors

```json
{  "authors": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "name": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/post/technology"    }  ]}
```

```json
{  "authors": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "name": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/post/technology"    }  ]}
```
