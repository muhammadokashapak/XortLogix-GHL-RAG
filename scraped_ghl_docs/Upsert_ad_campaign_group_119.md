# Upsert ad campaign group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-upsert-campaign-group`
---

# Upsert ad campaign group

## /ad-publishing/linkedin/ads

Create or update a LinkedIn ad campaign group with campaigns and ads

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Internal ID

Location ID

Campaign group budget

Child ad campaigns

Ad budget optimization modeAvailable optionsMAXIMUM_DELIVERYCOST_CAP

Campaign group objectiveAvailable optionsLEAD_GENERATIONWEBSITE_VISIT

Campaign group name

LinkedIn campaign group resource ID

Publishing statusAvailable optionsDRAFTSCHEDULEDPUBLISHEDPUBLISHINGFAILEDIN_REVIEWPAUSEDARCHIVEDWITH_ISSUESREJECTED

LinkedIn ad account identifier

Whether the campaign group has unpublished changes

Additional metadata

LinkedIn API error message

User-provided overrides for custom_values merge tags used in ad copy

```json
{  "id": "cg_abc123",  "locationId": "loc_abc123",  "budget": {    "budgetType": "DAILY",    "amount": 10000  },  "adCampaigns": [    {      "name": "Campaign 1",      "publishingStatus": "PUBLISHED"    }  ],  "adBudgetOptimization": "MAXIMUM_DELIVERY",  "objectiveType": "LEAD_GENERATION",  "name": "Q1 Lead Gen",  "adCampaignGroupId": "123456789",  "publishingStatus": "PUBLISHED",  "linkedInAdAccountId": "12345678",  "unpublishedChanges": false,  "meta": {},  "linkedInError": "Budget below minimum",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```

```json
{  "id": "cg_abc123",  "locationId": "loc_abc123",  "budget": {    "budgetType": "DAILY",    "amount": 10000  },  "adCampaigns": [    {      "name": "Campaign 1",      "publishingStatus": "PUBLISHED"    }  ],  "adBudgetOptimization": "MAXIMUM_DELIVERY",  "objectiveType": "LEAD_GENERATION",  "name": "Q1 Lead Gen",  "adCampaignGroupId": "123456789",  "publishingStatus": "PUBLISHED",  "linkedInAdAccountId": "12345678",  "unpublishedChanges": false,  "meta": {},  "linkedInError": "Budget below minimum",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```
