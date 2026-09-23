# Get notification
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/find-event-notification`
---

# Get notification

## /calendars/:calendarId/notifications/:notificationId

Find Event notification by notificationId

## Requestâ

API VersionAvailable options2021-04-15

Calendar ID

Notification ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Notification ID

Notification recipient typeAvailable optionscontactguestassignedUseremailsphoneNumbersbusiness

Additional email addresses to receive notifications

Additional phone numbers to receive notifications

Notification channelAvailable optionsemailinAppsmswhatsapp

Notification typeAvailable optionsbookedconfirmationcancellationreminderfollowupreschedule

Whether the notification is active

Additional WhatsApp numbers to receive notifications

Template ID for the notification

Notification body content

Notification subject line

Time schedules after which follow-up notifications are sent

Time schedules before which reminder notifications are sent

Selected user IDs for the notification

Whether the notification is deleted

```json
{  "_id": "629a5d0a8c3f2b001f3d4e5a",  "receiverType": "contact",  "additionalEmailIds": [    "[email protected]",    "[email protected]"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

```json
{  "_id": "629a5d0a8c3f2b001f3d4e5a",  "receiverType": "contact",  "additionalEmailIds": [    "[email protected]",    "[email protected]"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```
