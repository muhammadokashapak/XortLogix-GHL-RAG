# Update Association By Id
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/update-association`
---

# Update Association By Id

## /associations/:associationId

Update Association , Allows you to update labels of an associations. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

```json
{  "firstObjectLabel": "student",  "secondObjectLabel": "tutor"}
```

```json
{  "firstObjectLabel": "student",  "secondObjectLabel": "tutor"}
```

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
