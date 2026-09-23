# Update Calendar
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/update-calendar`
---

# Update Calendar

## /calendars/:calendarId

Update calendar by ID.

## Requestâ

API VersionAvailable options2021-04-15

Calendar Id

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

ð¨ Deprecated! Please use 'Calendar Notifications APIs' instead.

Group Id

Team members are required for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member.

Event type for round robin distributionAvailable optionsRoundRobin_OptimizeForAvailabilityRoundRobin_OptimizeForEqualDistribution

Calendar name

Calendar description

Calendar slug for URL

Widget slug

Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout.Available optionsdefaultclassic

Title for calendar events

Color for calendar events in hex formatDefault value: #039be5

Meeting location configuration for event calendar

This controls the duration of the meetingDefault value: 30

Unit for slot duration.Available optionsminshours

Unit for pre-buffer.Available optionsminshours

Slot interval reflects the amount of time the between booking slots that will be shown in the calendar.Default value: 30

Unit for slot interval.Available optionsminshours

Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up

Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready

Deprecated: use appointmentPerSlot instead. Maximum bookings per slot (per user)

Number of appointments that can be booked for a given day

Minimum scheduling notice for events

Unit for minimum scheduling noticeAvailable optionshoursdaysweeksmonthsmins

Minimum number of days/weeks/months for which to allow booking events

Unit for controlling the duration for which booking would be allowed forAvailable optionsdaysweeksmonths

While we will support this property for backward compatibility, it is recommended to use 'Availability' APIs instead.

Enable recurring appointments for the calendars. Please note that only one member should be added in the calendar to enable thisDefault value: false

Recurring appointment configuration

Form ID to be used for booking

Enable sticky contact assignment

Whether payment mode is live

Auto-confirm appointments

Send alert emails to assigned team member

Alert email address

Send Google invitation emails

Allow rescheduling of appointments

Allow cancellation of appointments

Assign contact to team member on booking

Skip assigning contact if contact already exists

Notes for the calendar

Facebook Pixel ID for tracking

Action after form submissionAvailable optionsRedirectURLThankYouMessage

Redirect URL after form submission

Thank you message displayed after form submission

While we will support this property for backward compatibility, it is not required anymore.Available options01

While we will support this property for backward compatibility, it is recommended to use 'Availability' APIs instead.

Type of guest allowedAvailable optionscount_onlycollect_detail

Consent label text

Calendar cover image URL

Look Busy Configuration

Whether the calendar is active

Maximum bookings per slot (per user)

Number of appointments that can be booked for a given day

```json
{  "groupId": "BqTwX8QFwXzpegMve9EQ",  "teamMembers": [    {      "userId": "ocQHyuzHvysMo5N5VsXc",      "priority": 0.5,      "isPrimary": true    }  ],  "eventType": "RoundRobin_OptimizeForAvailability",  "name": "test calendar",  "description": "this is used for testing",  "slug": "test1",  "widgetSlug": "test1",  "widgetType": "classic",  "eventTitle": "{{contact.name}}",  "eventColor": "#039BE5",  "locationConfigurations": [    {      "kind": "custom",      "location": "https://meet.google.com/abc-def"    }  ],  "slotDuration": 30,  "slotDurationUnit": "mins",  "preBufferUnit": "mins",  "slotInterval": 30,  "slotIntervalUnit": "mins",  "slotBuffer": 15,  "preBuffer": 10,  "appoinmentPerSlot": 1,  "appoinmentPerDay": 8,  "allowBookingAfter": 4,  "allowBookingAfterUnit": "days",  "allowBookingFor": 30,  "allowBookingForUnit": "days",  "enableRecurring": false,  "recurring": {    "freq": "WEEKLY",    "count": 4,    "bookingOption": "skip",    "bookingOverlapDefaultStatus": "confirmed"  },  "formId": "YlWd2wuCAZQzh2cH1fVZ",  "stickyContact": true,  "isLivePaymentMode": false,  "autoConfirm": true,  "shouldSendAlertEmailsToAssignedMember": false,  "alertEmail": "[email protected]",  "googleInvitationEmails": true,  "allowReschedule": true,  "allowCancellation": true,  "shouldAssignContactToTeamMember": true,  "shouldSkipAssigningContactForExisting": false,  "notes": "Please arrive 10 minutes early.",  "pixelId": "1234567890",  "formSubmitType": "ThankYouMessage",  "formSubmitRedirectURL": "https://example.com/thank-you",  "formSubmitThanksMessage": "Thank you for booking!",  "guestType": "count_only",  "consentLabel": "I confirm that I want to receive content from this company using any contact information I provide.",  "calendarCoverImage": "https://path-to-image.com",  "lookBusyConfig": {    "enabled": true,    "lookBusyPercentage": 50  },  "isActive": true,  "appointmentPerSlot": 1,  "appointmentPerDay": 8}
```

```json
{  "groupId": "BqTwX8QFwXzpegMve9EQ",  "teamMembers": [    {      "userId": "ocQHyuzHvysMo5N5VsXc",      "priority": 0.5,      "isPrimary": true    }  ],  "eventType": "RoundRobin_OptimizeForAvailability",  "name": "test calendar",  "description": "this is used for testing",  "slug": "test1",  "widgetSlug": "test1",  "widgetType": "classic",  "eventTitle": "{{contact.name}}",  "eventColor": "#039BE5",  "locationConfigurations": [    {      "kind": "custom",      "location": "https://meet.google.com/abc-def"    }  ],  "slotDuration": 30,  "slotDurationUnit": "mins",  "preBufferUnit": "mins",  "slotInterval": 30,  "slotIntervalUnit": "mins",  "slotBuffer": 15,  "preBuffer": 10,  "appoinmentPerSlot": 1,  "appoinmentPerDay": 8,  "allowBookingAfter": 4,  "allowBookingAfterUnit": "days",  "allowBookingFor": 30,  "allowBookingForUnit": "days",  "enableRecurring": false,  "recurring": {    "freq": "WEEKLY",    "count": 4,    "bookingOption": "skip",    "bookingOverlapDefaultStatus": "confirmed"  },  "formId": "YlWd2wuCAZQzh2cH1fVZ",  "stickyContact": true,  "isLivePaymentMode": false,  "autoConfirm": true,  "shouldSendAlertEmailsToAssignedMember": false,  "alertEmail": "[email protected]",  "googleInvitationEmails": true,  "allowReschedule": true,  "allowCancellation": true,  "shouldAssignContactToTeamMember": true,  "shouldSkipAssigningContactForExisting": false,  "notes": "Please arrive 10 minutes early.",  "pixelId": "1234567890",  "formSubmitType": "ThankYouMessage",  "formSubmitRedirectURL": "https://example.com/thank-you",  "formSubmitThanksMessage": "Thank you for booking!",  "guestType": "count_only",  "consentLabel": "I confirm that I want to receive content from this company using any contact information I provide.",  "calendarCoverImage": "https://path-to-image.com",  "lookBusyConfig": {    "enabled": true,    "lookBusyPercentage": 50  },  "isActive": true,  "appointmentPerSlot": 1,  "appointmentPerDay": 8}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Calendar details

```json
{  "calendar": {    "id": "0TkCdp9PfvLeWKYRRvIz",    "name": "test calendar",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```

```json
{  "calendar": {    "id": "0TkCdp9PfvLeWKYRRvIz",    "name": "test calendar",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```
