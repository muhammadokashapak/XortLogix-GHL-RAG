# Update Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/update-brand-voice-v-1`
---

# Update Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices/:brandVoiceId

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Update a brand voice by ID

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Brand voice ID

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Name

Updated answers

```json
{  "name": "My Brand Voice",  "answers": {    "brandName": "Brand Name",    "toneOfVoice": "Friendly"  }}
```

```json
{  "name": "My Brand Voice",  "answers": {    "brandName": "Brand Name",    "toneOfVoice": "Friendly"  }}
```

Success

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
