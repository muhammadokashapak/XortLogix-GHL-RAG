# Create Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/create-brand-voice-v-1`
---

# Create Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Create a brand voice for a location

## Requestâ

API VersionAvailable options2021-04-15

Location ID

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Name

Creation type. "manual" creates with provided custom answers, "url" generates answers from a website, "description" generates answers from a text descriptionAvailable optionsmanualurldescription

Website URL to generate brand voice from. Required when type is "url"

Company description to generate brand voice from. Required when type is "description", optional when type is "url"

Brand voice answers. Required when type is "manual"

```json
{  "name": "My Brand Voice",  "type": "manual",  "url": "https://example.com",  "description": "We are a tech company focused on innovative solutions for small businesses",  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management"  }}
```

```json
{  "name": "My Brand Voice",  "type": "manual",  "url": "https://example.com",  "description": "We are a tech company focused on innovative solutions for small businesses",  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management"  }}
```

Created

* application/json

* SchemaExample (auto)
* Example (auto)

Brand voice ID

Brand voice name

Whether this is the default brand voice

Creation timestamp

Last update timestamp

Location ID

Whether the brand voice has been soft deleted

Brand voice answers

Trace ID of request

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```
