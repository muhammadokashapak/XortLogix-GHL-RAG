# Update ad status
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-update-ad-status`
---

# Update ad status

## /ad-publishing/linkedin/:adId/status

Pause or resume a LinkedIn ad, campaign, or ad group

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

Location identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Update operationAvailable optionsPAUSEDARCHIVEDRESUME

Ad object typeAvailable optionsadGroupadCampaignad

```json
{  "operationType": "PAUSED",  "type": "adCampaign"}
```

```json
{  "operationType": "PAUSED",  "type": "adCampaign"}
```
