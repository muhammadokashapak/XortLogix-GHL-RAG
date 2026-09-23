# Upsert segment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-segment`
---

# Upsert segment

## /ad-publishing/google/segments

Create or update a Google Ads audience segment

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Segment typeAvailable optionsCUSTOM_SEGMENTSWEBSITE_VISITORCUSTOMER_MATCHLOOKALIKE

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Segment name

Segment description

Segment members â keywords, URLs, or apps that define the custom segment

Segment status

Google custom-audience type, used only when the type query parameter is CUSTOM_SEGMENTS. Defaults to AUTO when omitted. This is NOT the same field as the type query parameter, which selects which kind of segment to upsert â settable values here are AUTO, INTEREST, PURCHASE_INTENT and SEARCH.

Segment identifier

Membership status

Rule-based user list config

Membership life span

Seed user list IDs

Country codes

Expansion levelAvailable optionsBALANCEDBROADNARROW

```json
{  "name": "My Segment",  "description": "Target audience segment",  "members": [    {      "memberType": "KEYWORD",      "keyword": "digital marketing"    },    {      "memberType": "URL",      "url": "https://example.com"    },    {      "memberType": "APP",      "app": "com.example.app"    }  ],  "status": "ENABLED",  "type": "AUTO",  "id": "seg_123",  "membershipStatus": "OPEN",  "ruleBasedUserList": {    "prepopulationStatus": "REQUESTED",    "flexibleRuleUserList": {      "inclusiveOperands": [],      "exclusiveOperands": []    }  },  "membershipLifeSpan": 30,  "seedUserListIds": [    "list_1"  ],  "countryCodes": [    "US",    "CA"  ],  "expansionLevel": "BALANCED"}
```

```json
{  "name": "My Segment",  "description": "Target audience segment",  "members": [    {      "memberType": "KEYWORD",      "keyword": "digital marketing"    },    {      "memberType": "URL",      "url": "https://example.com"    },    {      "memberType": "APP",      "app": "com.example.app"    }  ],  "status": "ENABLED",  "type": "AUTO",  "id": "seg_123",  "membershipStatus": "OPEN",  "ruleBasedUserList": {    "prepopulationStatus": "REQUESTED",    "flexibleRuleUserList": {      "inclusiveOperands": [],      "exclusiveOperands": []    }  },  "membershipLifeSpan": 30,  "seedUserListIds": [    "list_1"  ],  "countryCodes": [    "US",    "CA"  ],  "expansionLevel": "BALANCED"}
```
