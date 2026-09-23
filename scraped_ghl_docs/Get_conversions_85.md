# Get conversions
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-conversions`
---

# Get conversions

## /ad-publishing/google/conversions

Retrieve Google Ads conversion actions for a location. For AD_MANAGER, without limit the response is a plain array; when limit is provided (max 100, default 100) the response is a paginated { conversions, paging } envelope â pass pageToken (from paging.next) to fetch the next batch.

```json
{ conversions, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Integration typeAvailable optionsAD_MANAGERAD_WORDS

Conversion action type to filter byAvailable optionsUPLOAD_CLICKSUPLOAD_CALLSWEBPAGELEAD_FORM_SUBMIT

Conversion action category to filter byAvailable optionsDEFAULTPAGE_VIEWPURCHASESIGNUPLEADDOWNLOADADD_TO_CARTBEGIN_CHECKOUTSUBSCRIBE_PAIDPHONE_CALL_LEADIMPORTED_LEADSUBMIT_LEAD_FORM

Filter start date

Filter end date

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { conversions, paging } envelope instead of a plain array. Applies to AD_MANAGER type only.

Opaque cursor for the next batch, taken from the previous response paging.next
