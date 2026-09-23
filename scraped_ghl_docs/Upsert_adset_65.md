# Upsert adset
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-upsert-adset`
---

# Upsert adset

## /ad-publishing/facebook/adsets

Create or update a Facebook ad set

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Ad set identifier

Location identifier

Ad set name

Facebook page ID

Instagram actor ID

Messaging platformsAvailable optionsWHATSAPPMESSENGERINSTAGRAM_DIRECT

WhatsApp phone number

Targeting audience configuration including geo-locations, locales, placements, and custom audiences

Ad set budget config

Where the conversion happens. Valid values depend on the parent campaign objective â OUTCOME_LEADS: on_ad (instant form), website, website_and_lead_form; OUTCOME_SALES: website (pixel), messaging. Not validated server-side, so values outside this set are forwarded to Facebook and may be rejected there.

Facebook standard event optimised for. Only meaningful when conversionLocation is website (requires pixelId). Valid values depend on the parent campaign objective â OUTCOME_LEADS: COMPLETE_REGISTRATION, CONTACT, CONTENT_VIEW, FIND_LOCATION, LEAD, SCHEDULE, SEARCH, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE; OUTCOME_SALES: ADD_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, COMPLETE_REGISTRATION, CONTENT_VIEW, DONATE, INITIATED_CHECKOUT, PURCHASE, SEARCH, START_TRIAL, SUBSCRIBE. Not validated server-side, so values outside this set are forwarded to Facebook and may be rejected there.

Conversion pixel ID

Parent campaign ID

```json
{  "id": "adset_123",  "locationId": "loc_abc123",  "name": "Targeting Group A",  "pageId": "123456789",  "instagramActorId": "ig_123",  "messagingPlatforms": [    "WHATSAPP"  ],  "whatsappNumber": "+1234567890",  "audience": {    "geoLocations": [      {        "key": "US",        "name": "United States",        "type": "country",        "selectionType": "include"      }    ],    "ageMin": 18,    "ageMax": 65,    "genders": [      1,      2    ]  },  "budget": {    "budgetType": "DAILY",    "amount": 1000,    "scheduleStartDate": "2024-01-01",    "scheduleEndDate": "2024-01-31"  },  "conversionLocation": "website",  "customEventType": "PURCHASE",  "pixelId": "px_123",  "campaignId": "camp_123"}
```

```json
{  "id": "adset_123",  "locationId": "loc_abc123",  "name": "Targeting Group A",  "pageId": "123456789",  "instagramActorId": "ig_123",  "messagingPlatforms": [    "WHATSAPP"  ],  "whatsappNumber": "+1234567890",  "audience": {    "geoLocations": [      {        "key": "US",        "name": "United States",        "type": "country",        "selectionType": "include"      }    ],    "ageMin": 18,    "ageMax": 65,    "genders": [      1,      2    ]  },  "budget": {    "budgetType": "DAILY",    "amount": 1000,    "scheduleStartDate": "2024-01-01",    "scheduleEndDate": "2024-01-31"  },  "conversionLocation": "website",  "customEventType": "PURCHASE",  "pixelId": "px_123",  "campaignId": "camp_123"}
```
