# Create page lead form
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-create-page-lead-form`
---

# Create page lead form

## /ad-publishing/facebook/page/:pageId/forms

Create a new lead gen form on a Facebook page

## Requestâ

API VersionAvailable options2021-04-15

Facebook page identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Lead form typeAvailable optionsMORE_VOLUMEHIGHER_INTENT

Lead form name

Location identifier

Greeting card config

List of questions displayed on the lead form. Required (non-empty) when isDraft is false or omitted; optional for drafts.

Question page headline

Privacy policy URL. Required when isDraft is false or omitted; optional for drafts.

Privacy policy text

Custom disclaimer config

Thank you page config. Required when isDraft is false or omitted; optional for drafts.

If the form is a draft, set to true

Draft form ID

Locale

```json
{  "type": "MORE_VOLUME",  "name": "Contact Form",  "locationId": "loc_abc123",  "greetingCard": {    "title": "Welcome!",    "style": "LIST_STYLE",    "content": [      "Learn more about our services"    ]  },  "questions": [    {      "key": "full_name",      "type": "FULL_NAME",      "options": []    },    {      "key": "email_address",      "type": "EMAIL",      "options": []    },    {      "key": "are_you_interested",      "label": "Are you interested?",      "type": "CUSTOM",      "options": [        {          "value": "Yes"        },        {          "value": "No"        }      ]    }  ],  "questionPageHeadline": "Tell us about yourself",  "privacyPolicyLink": "https://example.com/privacy",  "privacyPolicyText": "We respect your privacy",  "customDisclaimer": {    "title": "Terms & Conditions",    "body": "By submitting...",    "checkboxes": [      {        "isRequired": true,        "text": "I agree",        "key": "terms"      }    ]  },  "thankYouPage": {    "title": "Thank You!",    "body": "We will contact you soon",    "buttonText": "Visit Website",    "buttonType": "VIEW_WEBSITE",    "buttonLink": "https://example.com"  },  "isDraft": true,  "draftFormId": "1234567890",  "locale": "EN_US"}
```

```json
{  "type": "MORE_VOLUME",  "name": "Contact Form",  "locationId": "loc_abc123",  "greetingCard": {    "title": "Welcome!",    "style": "LIST_STYLE",    "content": [      "Learn more about our services"    ]  },  "questions": [    {      "key": "full_name",      "type": "FULL_NAME",      "options": []    },    {      "key": "email_address",      "type": "EMAIL",      "options": []    },    {      "key": "are_you_interested",      "label": "Are you interested?",      "type": "CUSTOM",      "options": [        {          "value": "Yes"        },        {          "value": "No"        }      ]    }  ],  "questionPageHeadline": "Tell us about yourself",  "privacyPolicyLink": "https://example.com/privacy",  "privacyPolicyText": "We respect your privacy",  "customDisclaimer": {    "title": "Terms & Conditions",    "body": "By submitting...",    "checkboxes": [      {        "isRequired": true,        "text": "I agree",        "key": "terms"      }    ]  },  "thankYouPage": {    "title": "Thank You!",    "body": "We will contact you soon",    "buttonText": "Visit Website",    "buttonType": "VIEW_WEBSITE",    "buttonLink": "https://example.com"  },  "isDraft": true,  "draftFormId": "1234567890",  "locale": "EN_US"}
```
