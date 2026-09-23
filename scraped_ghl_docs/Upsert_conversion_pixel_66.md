# Upsert conversion pixel
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-upsert-pixel`
---

# Upsert conversion pixel

## /ad-publishing/facebook/pixels

Create or update a Facebook conversion pixel configuration

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Conversion pixel ID

Pixel name

Instagram user ID

Pixel event typeAvailable optionsLEAD_EVENTFUNNEL_EVENTINSTAGRAM_DM

```json
{  "locationId": "loc_abc123",  "conversionPixelId": "px_123",  "name": "My Pixel",  "igUserId": "ig_user_123",  "type": "LEAD_EVENT"}
```

```json
{  "locationId": "loc_abc123",  "conversionPixelId": "px_123",  "name": "My Pixel",  "igUserId": "ig_user_123",  "type": "LEAD_EVENT"}
```
