# Create notification
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-event-notification`
---

# Create notification

## /calendars/:calendarId/notifications

Create Calendar notifications, either one or multiple. All notification settings must be for single calendar only

## Requestâ

API VersionAvailable options2021-04-15

Calendar ID

* application/json

* BodyExample (auto)
* Example (auto)

### Body arrayrequired

* Array [
* ]

notification recipient typeAvailable optionscontactguestassignedUseremailsphoneNumbersbusiness

Notification channelAvailable optionsemailinAppsmswhatsapp

Notification typeAvailable optionsbookedconfirmationcancellationreminderfollowupreschedule

Is the notification activeDefault value: true

Template ID for email notification. Not necessary for in-App notification

Body  for email notification. Not necessary for in-App notification

Subject  for email notification. Not necessary for in-App notification

Specifies the time after which the follow-up notification should be sent. This is not required for other notification types.

Specifies the time before which the reminder notification should be sent. This is not required for other notification types.

Additional email addresses to receive notifications.

Additional phone numbers to receive notifications.

Selected users for in-App and business email notifications. Supports user IDs and special keyword "sub_account_admin"

from address for email notification

from name for email/sms notification

from number for sms notification

```json
[  {    "receiverType": "user",    "channel": "email",    "notificationType": "confirmation",    "isActive": true,    "templateId": "MwPcayliwcdoUFzvbTok",    "body": "Your appointment has been confirmed.",    "subject": "Appointment Confirmation",    "afterTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "beforeTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "additionalEmailIds": [      "[email protected]",      "[email protected]"    ],    "additionalPhoneNumbers": [      "+919876744444",      "+919876744445"    ],    "selectedUsers": [      "userId1",      "userId2",      "sub_account_admin"    ],    "fromAddress": "[email protected]",    "fromName": "Acme Scheduling",    "fromNumber": "+15551234567"  }]
```

```json
[  {    "receiverType": "user",    "channel": "email",    "notificationType": "confirmation",    "isActive": true,    "templateId": "MwPcayliwcdoUFzvbTok",    "body": "Your appointment has been confirmed.",    "subject": "Appointment Confirmation",    "afterTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "beforeTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "additionalEmailIds": [      "[email protected]",      "[email protected]"    ],    "additionalPhoneNumbers": [      "+919876744444",      "+919876744445"    ],    "selectedUsers": [      "userId1",      "userId2",      "sub_account_admin"    ],    "fromAddress": "[email protected]",    "fromName": "Acme Scheduling",    "fromNumber": "+15551234567"  }]
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

* Array [
* ]

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
[  {    "_id": "629a5d0a8c3f2b001f3d4e5a",    "receiverType": "contact",    "additionalEmailIds": [      "[email protected]",      "[email protected]"    ],    "additionalPhoneNumbers": [      "+919876744444",      "+919876744445"    ],    "channel": "email",    "notificationType": "confirmation",    "isActive": true,    "additionalWhatsappNumbers": [      "+919876744444",      "+919876744445"    ],    "templateId": "0as9d8as0d",    "body": "This is a test notification",    "subject": "Test Notification",    "afterTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "beforeTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "selectedUsers": [      "user1",      "user2"    ],    "deleted": false  }]
```

```json
[  {    "_id": "629a5d0a8c3f2b001f3d4e5a",    "receiverType": "contact",    "additionalEmailIds": [      "[email protected]",      "[email protected]"    ],    "additionalPhoneNumbers": [      "+919876744444",      "+919876744445"    ],    "channel": "email",    "notificationType": "confirmation",    "isActive": true,    "additionalWhatsappNumbers": [      "+919876744444",      "+919876744445"    ],    "templateId": "0as9d8as0d",    "body": "This is a test notification",    "subject": "Test Notification",    "afterTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "beforeTime": [      {        "timeOffset": 1,        "unit": "hours"      }    ],    "selectedUsers": [      "user1",      "user2"    ],    "deleted": false  }]
```
