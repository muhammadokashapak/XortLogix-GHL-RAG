# Create conversation form
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-create-conversation-form`
---

# Create conversation form

## /ad-publishing/facebook/conversation-forms

Create a new Facebook conversation lead form

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Conversation form name

Welcome message text

Quick-reply questions shown in the welcome message of the conversation form

```json
{  "locationId": "loc_abc123",  "name": "Welcome Form",  "text": "Hi! How can we help?",  "questions": [    {      "question": "How can we help?",      "response": "Thanks for reaching out! A team member will assist you shortly."    },    {      "question": "I want to learn more",      "response": "Great! Here is a link to our services."    }  ]}
```

```json
{  "locationId": "loc_abc123",  "name": "Welcome Form",  "text": "Hi! How can we help?",  "questions": [    {      "question": "How can we help?",      "response": "Thanks for reaching out! A team member will assist you shortly."    },    {      "question": "I want to learn more",      "response": "Great! Here is a link to our services."    }  ]}
```
