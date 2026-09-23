# Upsert audience
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-audience`
---

# Upsert audience

## /ad-publishing/google/audiences

Create or update a Google Ads combined audience

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Audience resource name

Audience name

Audience dimensions

Exclusion dimensions

```json
{  "locationId": "loc_abc123",  "resourceName": "customers/123/audiences/456",  "name": "My Audience",  "dimensions": {    "isAgeUnknown": false,    "ageRanges": [      {        "minAge": 25,        "maxAge": 34      }    ],    "genders": [      "MALE",      "FEMALE"    ]  },  "exclusionDimension": {    "genders": [      "UNDETERMINED"    ]  }}
```

```json
{  "locationId": "loc_abc123",  "resourceName": "customers/123/audiences/456",  "name": "My Audience",  "dimensions": {    "isAgeUnknown": false,    "ageRanges": [      {        "minAge": 25,        "maxAge": 34      }    ],    "genders": [      "MALE",      "FEMALE"    ]  },  "exclusionDimension": {    "genders": [      "UNDETERMINED"    ]  }}
```
