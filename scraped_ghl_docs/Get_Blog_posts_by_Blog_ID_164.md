# Get Blog posts by Blog ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/get-blog-post`
---

# Get Blog posts by Blog ID

## /blogs/posts/all

The "Get Blog posts by Blog ID" API allows you get blog posts for any given blog site using blog ID.Please use blogs/posts.readonly

## Requestâ

API VersionAvailable options2021-04-15

search for any post by name

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Object containing response data of blog posts

```json
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

```json
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```
