# Create lead form
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-create-lead-form`
---

# Create lead form

## /ad-publishing/linkedin/:accountId/form

Create a new LinkedIn lead gen form for an ad account

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Form owner

Creation locale

Form name

Form stateAvailable optionsPUBLISHED

Form content

Hidden fields

```json
{  "owner": {    "sponsoredAccount": "urn:li:sponsoredAccount:123456"  },  "creationLocale": {    "country": "US",    "language": "en"  },  "name": "Contact Us",  "state": "PUBLISHED",  "content": {    "questions": [],    "headline": {      "localized": {        "en_US": "Get in touch"      }    },    "postSubmissionInfo": {},    "legalInfo": {}  },  "hiddenFields": [    {      "name": "utm_source",      "value": "linkedin"    }  ]}
```

```json
{  "owner": {    "sponsoredAccount": "urn:li:sponsoredAccount:123456"  },  "creationLocale": {    "country": "US",    "language": "en"  },  "name": "Contact Us",  "state": "PUBLISHED",  "content": {    "questions": [],    "headline": {      "localized": {        "en_US": "Get in touch"      }    },    "postSubmissionInfo": {},    "legalInfo": {}  },  "hiddenFields": [    {      "name": "utm_source",      "value": "linkedin"    }  ]}
```
