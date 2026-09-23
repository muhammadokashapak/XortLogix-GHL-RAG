# Create Association
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/create-association`
---

# Create Association

## /associations/

Allow you to create contact - contact , contact - custom objects associations, will add more in the future.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Association's Unique key

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

```json
{  "locationId": "string",  "key": "student_teacher",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact"}
```

```json
{  "locationId": "string",  "key": "student_teacher",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact"}
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
