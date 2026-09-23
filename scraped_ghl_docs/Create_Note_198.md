# Create Note
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-appointment-note`
---

# Create Note

## /calendars/appointments/:appointmentId/notes

Create Note

## Requestâ

API VersionAvailable options2021-04-15

Appointment ID

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

User ID of the note author

Note bodyPossible values: <= 5000 characters

Possible values: <= 5000 characters

```json
{  "userId": "GCs5KuzPqTls7vWclkEV",  "body": "lorem ipsum"}
```

```json
{  "userId": "GCs5KuzPqTls7vWclkEV",  "body": "lorem ipsum"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

The created or updated note

```json
{  "note": {    "id": "HGPcayliwcdoUFzvbTok",    "body": "lorem ipsum",    "userId": "TUcmRxWrjqzJS8EjkxNK"  }}
```

```json
{  "note": {    "id": "HGPcayliwcdoUFzvbTok",    "body": "lorem ipsum",    "userId": "TUcmRxWrjqzJS8EjkxNK"  }}
```
