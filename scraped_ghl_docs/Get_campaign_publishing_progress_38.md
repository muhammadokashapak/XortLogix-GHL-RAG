# Get campaign publishing progress
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-campaign-publishing-progress`
---

# Get campaign publishing progress

## /ad-publishing/facebook/campaigns/:campaignId/publishing-progress

Returns Redis-backed publish progress for a campaign while it is publishing to Meta. Used by the validation funnel UI to poll step counts and completion state.

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

Location identifier

Publishing progress for the campaign

* application/json

* SchemaExample (auto)
* Example (auto)

Campaign identifier

Current campaign publishing status in ad-publishingAvailable optionsDRAFTSCHEDULEDPUBLISHEDPUBLISHINGFAILEDIN_REVIEWPAUSEDARCHIVEDWITH_ISSUESREJECTED

Total publish steps tracked in Redis (campaign + ad sets + ads)

Number of publish steps completed so far

Whether publishing is finished (Redis complete/failed, processed >= total, or status is no longer PUBLISHING)

Whether publishing failed (Redis failed status or campaign FAILED)

```json
{  "campaignId": "507f1f77bcf86cd799439011",  "publishingStatus": "PUBLISHING",  "total": 5,  "processed": 2,  "isComplete": false,  "hasFailed": false}
```

```json
{  "campaignId": "507f1f77bcf86cd799439011",  "publishingStatus": "PUBLISHING",  "total": 5,  "processed": 2,  "isComplete": false,  "hasFailed": false}
```
