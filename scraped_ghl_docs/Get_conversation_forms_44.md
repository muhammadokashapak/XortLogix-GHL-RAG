# Get conversation forms
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-conversation-forms`
---

# Get conversation forms

## /ad-publishing/facebook/conversation-forms

Retrieve Facebook conversation lead forms for a location. Without limit the response is a plain array. When limit is provided (max 100) the response is a paginated { conversationForms, paging } envelope; pass after (from paging.next) to fetch the next batch.

```json
{ conversationForms, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Page size for a paginated fetch (max 100). When set, the response is a { conversationForms, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of conversation forms (default), or a { conversationForms, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookConversationFormsDTO
* PaginatedFacebookConversationFormsDTO
* Array [
* ]

* object[]PaginatedFacebookConversationFormsDTO
* PaginatedFacebookConversationFormsDTO

```json
[  {}]
```

```json
[  {}]
```
