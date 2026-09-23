# Upsert campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-upsert-campaign`
---

# Upsert campaign

## /ad-publishing/facebook/campaigns

Create or update a Facebook campaign

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Campaign identifier

Location identifier

Campaign name

Campaign objectiveAvailable optionsOUTCOME_LEADSOUTCOME_TRAFFICOUTCOME_ENGAGEMENTOUTCOME_SALES

Special ad categoriesAvailable optionsEMPLOYMENTCREDITFINANCIAL_PRODUCTS_SERVICESHOUSINGISSUES_ELECTIONS_POLITICSONLINE_GAMBLING_AND_GAMINGNONE

Campaign data source

User-provided overrides for custom_values merge tags used in ad copy

```json
{  "id": "camp_123",  "locationId": "loc_abc123",  "name": "Summer Campaign",  "objective": "OUTCOME_LEADS",  "specialAdCategories": [    "NONE"  ],  "source": "facebook",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```

```json
{  "id": "camp_123",  "locationId": "loc_abc123",  "name": "Summer Campaign",  "objective": "OUTCOME_LEADS",  "specialAdCategories": [    "NONE"  ],  "source": "facebook",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```
