# Get association by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/get-association-by-id`
---

# Get association by ID

## /associations/:associationId

Using this api you can get SYSTEM_DEFINED / USER_DEFINED association by id

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```
