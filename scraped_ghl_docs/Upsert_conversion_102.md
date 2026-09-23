# Upsert conversion
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-conversion`
---

# Upsert conversion

## /ad-publishing/google/conversions

Create or update a Google Ads conversion action

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Conversion identifier

Conversion name

Conversion action type. Only UPLOAD_CLICKS is supported â the conversion list endpoint reads back UPLOAD_CLICKS actions only, so a conversion created with any other type would never be returned.Available optionsUPLOAD_CLICKS

Conversion action categoryAvailable optionsDEFAULTPAGE_VIEWPURCHASESIGNUPLEADDOWNLOADADD_TO_CARTBEGIN_CHECKOUTSUBSCRIBE_PAIDPHONE_CALL_LEADIMPORTED_LEADSUBMIT_LEAD_FORM

Value settings that control how monetary value is attributed to conversions

How conversions are counted per interactionAvailable optionsONE_PER_CLICKMANY_PER_CLICK

Attribution model used to credit conversionsAvailable optionsGOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVENGOOGLE_ADS_LAST_CLICK

Click-through conversion window in days

```json
{  "locationId": "loc_abc123",  "conversionId": "conv_456",  "name": "Purchase Conversion",  "type": "UPLOAD_CLICKS",  "category": "PURCHASE",  "valueSettings": {    "defaultValue": "10.00",    "defaultCurrencyCode": "USD",    "alwaysUseDefaultValue": false  },  "countingType": "ONE_PER_CLICK",  "attributionModel": "GOOGLE_ADS_LAST_CLICK",  "clickThroughWindow": 30}
```

```json
{  "locationId": "loc_abc123",  "conversionId": "conv_456",  "name": "Purchase Conversion",  "type": "UPLOAD_CLICKS",  "category": "PURCHASE",  "valueSettings": {    "defaultValue": "10.00",    "defaultCurrencyCode": "USD",    "alwaysUseDefaultValue": false  },  "countingType": "ONE_PER_CLICK",  "attributionModel": "GOOGLE_ADS_LAST_CLICK",  "clickThroughWindow": 30}
```
