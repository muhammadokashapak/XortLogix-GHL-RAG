# Get Notes
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-appointment-notes`
---

# Get Notes

## /calendars/appointments/:appointmentId/notes

Get Appointment Notes

## Requestâ

API VersionAvailable options2021-04-15

Appointment ID

Limit of notes to fetchPossible values: <= 20

Possible values: <= 20

Offset of notes to fetchPossible values: >= 0

Possible values: >= 0

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of appointment notes

Whether more notes are available

```json
{  "notes": [    {      "id": "HGPcayliwcdoUFzvbTok",      "body": "lorem ipsum",      "userId": "TUcmRxWrjqzJS8EjkxNK"    }  ],  "hasMore": true}
```

```json
{  "notes": [    {      "id": "HGPcayliwcdoUFzvbTok",      "body": "lorem ipsum",      "userId": "TUcmRxWrjqzJS8EjkxNK"    }  ],  "hasMore": true}
```
