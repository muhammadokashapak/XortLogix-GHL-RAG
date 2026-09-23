# Upsert Google campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-campaign`
---

# Upsert Google campaign

## /ad-publishing/google/ads

Create or update a full Google Ads campaign structure

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Campaign identifier

Campaign name

Location identifier

Advertising channel. Only SEARCH and DEMAND_GEN campaigns can be built and published by this product; the other Google channels are readable on existing campaigns but cannot be created here.Available optionsSEARCHDEMAND_GEN

Channel sub typeAvailable optionsDEMAND_GEN

Goal typeAvailable optionsWEBSITE_TRAFFICLEAD

Campaign budget

Campaign audience targeting

Network settings

Bidding strategy config

Campaign assets

EU political ads flag

Campaign ad groups

Campaign goal config

Ad schedule rules

Publishing statusAvailable optionsDRAFTSCHEDULEDPUBLISHEDPUBLISHINGFAILEDIN_REVIEWPAUSEDARCHIVEDWITH_ISSUESREJECTED

Google Ad account identifier

Whether the campaign has unpublished changes

Maximum CPC bid in micros

Google Ads campaign resource ID

Traffic source

Advanced options

User-provided overrides for custom_values merge tags used in ad copy

```json
{  "id": "camp_abc123",  "name": "My Campaign",  "locationId": "loc_abc123",  "advertisingChannelType": "SEARCH",  "advertisingChannelSubType": "DEMAND_GEN",  "goalType": "WEBSITE_TRAFFIC",  "budget": {    "budgetType": "DAILY",    "amount": 5000,    "scheduleStartDate": "2024-01-01"  },  "audience": {    "geoLocations": [      {        "key": "geoTargetConstants/2840",        "name": "United States"      }    ]  },  "networkSettings": {    "targetSearchNetwork": true,    "targetContentNetwork": false  },  "biddingStrategy": {    "type": "MAXIMIZE_CONVERSIONS",    "value": 1000000  },  "assets": {    "calls": [],    "sitelinks": [],    "images": []  },  "isEuPoliticalAds": false,  "adGroups": [    {      "id": "ag_1",      "name": "Ad Group 1",      "adContent": []    }  ],  "campaignGoal": {    "type": "WEBSITE_TRAFFIC",    "isCustomConversionGoal": false  },  "adSchedule": [    {      "dayOfWeek": "MONDAY",      "from": "09:00",      "to": "17:00"    }  ],  "publishingStatus": "PUBLISHED",  "googleAdAccountId": "123-456-7890",  "unpublishedChanges": false,  "maximumCpc": 2000000,  "googleCampaignId": "customers/123/campaigns/456",  "source": "WEBSITE",  "advancedOptions": {    "source": "WEBSITE",    "postId": "post_abc123"  },  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```

```json
{  "id": "camp_abc123",  "name": "My Campaign",  "locationId": "loc_abc123",  "advertisingChannelType": "SEARCH",  "advertisingChannelSubType": "DEMAND_GEN",  "goalType": "WEBSITE_TRAFFIC",  "budget": {    "budgetType": "DAILY",    "amount": 5000,    "scheduleStartDate": "2024-01-01"  },  "audience": {    "geoLocations": [      {        "key": "geoTargetConstants/2840",        "name": "United States"      }    ]  },  "networkSettings": {    "targetSearchNetwork": true,    "targetContentNetwork": false  },  "biddingStrategy": {    "type": "MAXIMIZE_CONVERSIONS",    "value": 1000000  },  "assets": {    "calls": [],    "sitelinks": [],    "images": []  },  "isEuPoliticalAds": false,  "adGroups": [    {      "id": "ag_1",      "name": "Ad Group 1",      "adContent": []    }  ],  "campaignGoal": {    "type": "WEBSITE_TRAFFIC",    "isCustomConversionGoal": false  },  "adSchedule": [    {      "dayOfWeek": "MONDAY",      "from": "09:00",      "to": "17:00"    }  ],  "publishingStatus": "PUBLISHED",  "googleAdAccountId": "123-456-7890",  "unpublishedChanges": false,  "maximumCpc": 2000000,  "googleCampaignId": "customers/123/campaigns/456",  "source": "WEBSITE",  "advancedOptions": {    "source": "WEBSITE",    "postId": "post_abc123"  },  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```
