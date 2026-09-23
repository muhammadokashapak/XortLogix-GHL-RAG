# Batch update audience members
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-batch-update-audience-members`
---

# Batch update audience members

## /ad-publishing/facebook/custom-audience/:audienceId/member/batch

Add or remove members in bulk from a Facebook custom audience via CSV or smart lists

## Requestâ

API VersionAvailable options2021-04-15

Custom audience identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

CSV file path

Batch operation typeAvailable optionsADDREMOVEREPLACE

Smartlist IDs array

Dynamic audience flag

```json
{  "locationId": "loc_abc123",  "csvPath": "/uploads/audience.csv",  "operationType": "ADD",  "smartlistIds": [    "list_1",    "list_2"  ],  "dynamicAudience": "true"}
```

```json
{  "locationId": "loc_abc123",  "csvPath": "/uploads/audience.csv",  "operationType": "ADD",  "smartlistIds": [    "list_1",    "list_2"  ],  "dynamicAudience": "true"}
```
