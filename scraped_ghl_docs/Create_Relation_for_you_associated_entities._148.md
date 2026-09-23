# Create Relation for you associated entities.
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/create-relation`
---

# Create Relation for you associated entities.

## /associations/relations

Create Relation.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Your Sub Account's ID

Association's Id

First Record's Id. For instance, if you have an association between a contact and a custom object, and you specify the contact as the first object while creating the association, then your firstRecordId would be the contactId

Second Record's Id.For instance, if you have an association between a contact and a custom object, and you specify the custom object as the second entity while creating the association, then your secondRecordId would be the customObject record Id

```json
{  "locationId": "clF1LD04GTUKN3b3XuOj",  "associationId": "ve9EPM428h8vShlRW1KT",  "firstRecordId": "ve9EPM428h8vShlRW1KT",  "secondRecordId": "ve9EPM428h8vShlRW1KT"}
```

```json
{  "locationId": "clF1LD04GTUKN3b3XuOj",  "associationId": "ve9EPM428h8vShlRW1KT",  "firstRecordId": "ve9EPM428h8vShlRW1KT",  "secondRecordId": "ve9EPM428h8vShlRW1KT"}
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
