# Upsert assets
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-assets`
---

# Upsert assets

## /ad-publishing/google/assets

Create or update Google Ads creative assets

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Asset type to create or updateAvailable optionsCALLSITELINK

Asset payload â shape depends on the type field: CallAssetPayload (CALL) or SitelinkAssetPayload (SITELINK)

```json
{  "locationId": "loc_abc123",  "type": "CALL",  "payload": {    "phoneNumber": "+14155551234",    "countryCode": "US"  }}
```

```json
{  "locationId": "loc_abc123",  "type": "CALL",  "payload": {    "phoneNumber": "+14155551234",    "countryCode": "US"  }}
```
