# Get all categories
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/get-all-categories-by-location`
---

# Get all categories

## /blogs/categories

The "Get all categories" Api return the blog categoies for a given location ID. Please use "blogs/category.readonly"

## Requestâ

API VersionAvailable options2021-04-15

Number of categories to show in the listing

Number of categories to skip in listing

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Array of categories

```json
{  "categories": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "label": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/doc/category/agency-growth",      "urlSlug": "agency-growth"    }  ]}
```

```json
{  "categories": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "label": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/doc/category/agency-growth",      "urlSlug": "agency-growth"    }  ]}
```
