# Changelog
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Changelog`
---

## 2026-08-18â

Knowledge Base

We have made changes to rename the Knowledge Base endpoint path prefix from /knowledge-base to /knowledge-bases. This change is backward compatible â both the existing /knowledge-base endpoints and the new /knowledge-bases endpoints continue to work, so no action is required. New integrations should use /knowledge-bases.

## 2026-08-13â

Ad Publishing

### GET /ad-publishing/facebook/ad-accountsâ

* â ï¸ the query request parameter type was restricted to a list of enum values
* added the new enum value AD_MANAGER to the query request parameter type
* added the new enum value INTEGRATION to the query request parameter type

### GET /ad-publishing/facebook/ad-accounts/{adAccountId}â

* â ï¸ deleted the query request parameter isDraft

### PUT /ad-publishing/facebook/adsâ

* added the new optional request property descriptions
* added the new optional request property headlines
* added the new optional request property primaryTexts

### GET /ad-publishing/facebook/campaigns/{campaignId}/publishing-progressâ

* â ï¸ deleted the query request parameter isDraft

### DELETE /ad-publishing/facebook/custom-audience/{audienceId}â

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/facebook/custom-audience/{audienceId}â

* â ï¸ deleted the query request parameter isDraft

### PUT /ad-publishing/facebook/custom-audience/{audienceId}/member/batchâ

* â ï¸ request property operationType was restricted to a list of enum values
* added the new ADD enum value to the request property operationType
* added the new REMOVE enum value to the request property operationType
* added the new REPLACE enum value to the request property operationType

### GET /ad-publishing/facebook/integrationâ

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/facebook/meâ

* â ï¸ deleted the query request parameter isDraft

### PUT /ad-publishing/facebook/page/defaultâ

* â ï¸ deleted the query request parameter isDraft

### POST /ad-publishing/facebook/page/{pageId}/formsâ

* â ï¸ request property greetingCard/allOf[#/components/schemas/GreetingCard]/style was restricted to a list of enum values
* â ï¸ request property thankYouPage/allOf[#/components/schemas/ThankYouPage]/buttonType was restricted to a list of enum values
* added the new CALL_BUSINESS enum value to the request property thankYouPage/allOf[#/components/schemas/ThankYouPage]/buttonType
* added the new DOWNLOAD enum value to the request property thankYouPage/allOf[#/components/schemas/ThankYouPage]/buttonType
* added the new LIST_STYLE enum value to the request property greetingCard/allOf[#/components/schemas/GreetingCard]/style
* added the new PARAGRAPH_STYLE enum value to the request property greetingCard/allOf[#/components/schemas/GreetingCard]/style
* added the new VIEW_WEBSITE enum value to the request property thankYouPage/allOf[#/components/schemas/ThankYouPage]/buttonType

### GET /ad-publishing/facebook/pixelsâ

* â ï¸ the query request parameter channel was restricted to a list of enum values
* added the new enum value FACEBOOK to the query request parameter channel
* added the new enum value IG to the query request parameter channel

### PUT /ad-publishing/facebook/pixelsâ

* â ï¸ request property type was restricted to a list of enum values
* added the new FUNNEL_EVENT enum value to the request property type
* added the new INSTAGRAM_DM enum value to the request property type
* added the new LEAD_EVENT enum value to the request property type

### GET /ad-publishing/facebook/targeting/searchâ

* â ï¸ the query request parameter type was restricted to a list of enum values
* added the new enum value geolocation to the query request parameter type
* added the new enum value interest to the query request parameter type
* added the new enum value language to the query request parameter type

### GET /ad-publishing/google/ad-accounts/{adAccountId}â

* â ï¸ deleted the query request parameter isDraft

### PUT /ad-publishing/google/adsâ

* â ï¸ request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum was restricted to a list of enum values
* â ï¸ request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/gender/items/enum was restricted to a list of enum values
* â ï¸ removed the enum value DISCOVERY of the request property advertisingChannelType
* â ï¸ removed the enum value DISPLAY of the request property advertisingChannelType
* â ï¸ removed the enum value HOTEL of the request property advertisingChannelType
* â ï¸ removed the enum value LOCAL of the request property advertisingChannelType
* â ï¸ removed the enum value MULTI_CHANNEL of the request property advertisingChannelType
* â ï¸ removed the enum value PERFORMANCE_MAX of the request property advertisingChannelType
* added the new AGE_RANGE_18_24 enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum
* added the new AGE_RANGE_25_34 enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum
* added the new AGE_RANGE_35_44 enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum
* added the new AGE_RANGE_45_54 enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum
* added the new AGE_RANGE_55_64 enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum
* added the new AGE_RANGE_65_UP enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum
* added the new AGE_RANGE_UNDETERMINED enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/ageRange/items/enum
* added the new FEMALE enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/gender/items/enum
* added the new MALE enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/gender/items/enum
* added the new UNDETERMINED enum value to the request property audience/allOf[#/components/schemas/GoogleCampaignAudienceDTO]/gender/items/enum

### GET /ad-publishing/google/ads/{adId}â

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/google/assetsâ

* â ï¸ removed the enum value IMAGE from the query request parameter type
* â ï¸ removed the enum value LEAD_FORM from the query request parameter type
* â ï¸ removed the enum value TEXT from the query request parameter type

### POST /ad-publishing/google/assetsâ

* â ï¸ removed the enum value LEAD_FORM of the request property type
* â ï¸ removed #/components/schemas/LeadFormAssetPayloadDTO from the payload request property oneOf list

### PUT /ad-publishing/google/audiencesâ

* â ï¸ added the new required request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/ageRanges/items/minAge
* â ï¸ added the new required request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/ageRanges/items/minAge
* â ï¸ request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/ was restricted to a list of enum values
* â ï¸ request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/ was restricted to a list of enum values
* â ï¸ request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/ was restricted to a list of enum values
* â ï¸ request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/ was restricted to a list of enum values
* â ï¸ the dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/ageRanges/items/ request property type changed from string to object
* â ï¸ the exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/ageRanges/items/ request property type changed from string to object
* added the new optional request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/ageRanges/items/maxAge
* added the new optional request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/ageRanges/items/maxAge
* added the new FEMALE enum value to the request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/
* added the new FEMALE enum value to the request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/
* added the new MALE enum value to the request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/
* added the new MALE enum value to the request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/
* added the new NOT_A_PARENT enum value to the request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/
* added the new NOT_A_PARENT enum value to the request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/
* added the new PARENT enum value to the request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/
* added the new PARENT enum value to the request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/
* added the new UNDETERMINED enum value to the request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/
* added the new UNDETERMINED enum value to the request property dimensions/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/
* added the new UNDETERMINED enum value to the request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/genders/items/
* added the new UNDETERMINED enum value to the request property exclusionDimension/allOf[#/components/schemas/AudienceDimensionDTO]/parentalStatuses/items/

### GET /ad-publishing/google/audiences/{audienceId}â

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/google/conversionsâ

* â ï¸ the query request parameter category was restricted to a list of enum values
* â ï¸ the query request parameter conversionType was restricted to a list of enum values
* added the new enum value ADD_TO_CART to the query request parameter category
* added the new enum value BEGIN_CHECKOUT to the query request parameter category
* added the new enum value BOOK_APPOINTMENT to the query request parameter category
* added the new enum value CONTACT to the query request parameter category
* added the new enum value CONVERTED_LEAD to the query request parameter category
* added the new enum value DEFAULT to the query request parameter category
* added the new enum value DOWNLOAD to the query request parameter category
* added the new enum value ENGAGEMENT to the query request parameter category
* added the new enum value GET_DIRECTIONS to the query request parameter category
* added the new enum value IMPORTED_LEAD to the query request parameter category
* added the new enum value LEAD to the query request parameter category
* added the new enum value LEAD_FORM_SUBMIT to the query request parameter conversionType
* added the new enum value OUTBOUND_CLICK to the query request parameter category
* added the new enum value PAGE_VIEW to the query request parameter category
* added the new enum value PHONE_CALL_LEAD to the query request parameter category
* added the new enum value PURCHASE to the query request parameter category
* added the new enum value QUALIFIED_LEAD to the query request parameter category
* added the new enum value REQUEST_QUOTE to the query request parameter category
* added the new enum value SIGNUP to the query request parameter category
* added the new enum value STORE_SALE to the query request parameter category
* added the new enum value STORE_VISIT to the query request parameter category
* added the new enum value SUBMIT_LEAD_FORM to the query request parameter category
* added the new enum value SUBSCRIBE_PAID to the query request parameter category
* added the new enum value UPLOAD_CALLS to the query request parameter conversionType
* added the new enum value UPLOAD_CLICKS to the query request parameter conversionType
* added the new enum value WEBPAGE to the query request parameter conversionType

### PUT /ad-publishing/google/conversionsâ

* â ï¸ request property category was restricted to a list of enum values
* â ï¸ removed the enum value LEAD_FORM_SUBMIT of the request property type
* â ï¸ removed the enum value UPLOAD_CALLS of the request property type
* â ï¸ removed the enum value WEBPAGE of the request property type
* added the new ADD_TO_CART enum value to the request property category
* added the new BEGIN_CHECKOUT enum value to the request property category
* added the new BOOK_APPOINTMENT enum value to the request property category
* added the new CONTACT enum value to the request property category
* added the new CONVERTED_LEAD enum value to the request property category
* added the new DEFAULT enum value to the request property category
* added the new DOWNLOAD enum value to the request property category
* added the new ENGAGEMENT enum value to the request property category
* added the new GET_DIRECTIONS enum value to the request property category
* added the new IMPORTED_LEAD enum value to the request property category
* added the new LEAD enum value to the request property category
* added the new OUTBOUND_CLICK enum value to the request property category
* added the new PAGE_VIEW enum value to the request property category
* added the new PHONE_CALL_LEAD enum value to the request property category
* added the new PURCHASE enum value to the request property category
* added the new QUALIFIED_LEAD enum value to the request property category
* added the new REQUEST_QUOTE enum value to the request property category
* added the new SIGNUP enum value to the request property category
* added the new STORE_SALE enum value to the request property category
* added the new STORE_VISIT enum value to the request property category
* added the new SUBMIT_LEAD_FORM enum value to the request property category
* added the new SUBSCRIBE_PAID enum value to the request property category

### DELETE /ad-publishing/google/conversions/{conversionId}â

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/google/conversions/{conversionId}â

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/google/integrationâ

* â ï¸ deleted the query request parameter isDraft

### POST /ad-publishing/google/keyword-ideasâ

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/google/meâ

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/google/segmentsâ

* â ï¸ the query request parameter type was restricted to a list of enum values
* added the new enum value ALL to the query request parameter type
* added the new enum value CUSTOM_SEGMENTS to the query request parameter type
* added the new enum value DATA_SEGMENTS to the query request parameter type

### GET /ad-publishing/google/targeting/searchâ

* â ï¸ the query request parameter type was restricted to a list of enum values
* added the new enum value geolocation to the query request parameter type
* added the new enum value language to the query request parameter type

### GET /ad-publishing/linkedin/ad-accountsâ

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/linkedin/ads/{adId}â

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/linkedin/integrationâ

* â ï¸ deleted the query request parameter isDraft

### GET /ad-publishing/linkedin/meâ

* â ï¸ deleted the query request parameter isDraft

### POST /ad-publishing/linkedin/{accountId}/formâ

* â ï¸ deleted the query request parameter isDraft

### PATCH /ad-publishing/linkedin/{adId}/statusâ

* â ï¸ deleted the query request parameter isDraft

## Componentsâ

* removed the schema CustomQuestionFieldDTO
* removed the schema GoogleDemographicTargetDTO
* removed the schema LeadFormAssetPayloadDTO
* removed the schema LeadFormFieldDTO

## 2026-08-12â

Knowledge Base

### GET /knowledge-bases/filesâ

* endpoint added

### POST /knowledge-bases/filesâ

* endpoint added

### DELETE /knowledge-bases/files/{fileId}â

* endpoint added

### GET /knowledge-bases/files/{fileId}â

* endpoint added

## 2026-08-06â

Saas Api

### GET /saas/locationsâ

* the query request parameter customerId became optional
* the query request parameter subscriptionId became optional
* added the media type application/json for the response with the status 200

## 2026-08-05â

Ad Publishing

### GET /ad-publishing/facebook/reporting/listâ

* â ï¸ the query request parameter listType was restricted to a list of enum values
* added the new enum value ads to the query request parameter listType
* added the new enum value adsets to the query request parameter listType
* added the new enum value campaigns to the query request parameter listType
* added the new enum value none to the query request parameter listType

### GET /ad-publishing/google/reporting/listâ

* â ï¸ the query request parameter listType was restricted to a list of enum values
* added the new enum value adGroups to the query request parameter listType
* added the new enum value ads to the query request parameter listType
* added the new enum value campaigns to the query request parameter listType
* added the new enum value keywords to the query request parameter listType

### GET /ad-publishing/linkedin/reporting/listâ

* â ï¸ the query request parameter listType was restricted to a list of enum values
* added the new enum value ads to the query request parameter listType
* added the new enum value campaignGroups to the query request parameter listType
* added the new enum value campaigns to the query request parameter listType

## 2026-08-03â

Contacts

## Componentsâ

* removed the schema ContactsMetaSchema
* removed the schema customFieldsInputArraySchema
* removed the schema customFieldsInputObjectSchema
* removed the schema customFieldsInputStringSchema
Ad Publishing

### GET /ad-publishing/facebook/conversation-formsâ

* â ï¸ deleted the query request parameter isDraft
* added the new optional query request parameter after
* added the new optional query request parameter limit
* added the media type application/json for the response with the status 200

### GET /ad-publishing/facebook/custom-audienceâ

* added the new optional query request parameter after
* added the new optional query request parameter limit
* added the new optional query request parameter projection
* added the media type application/json for the response with the status 200

### GET /ad-publishing/facebook/page/{pageId}/formsâ

* â ï¸ deleted the query request parameter isDraft
* added the new optional query request parameter after
* added the new optional query request parameter limit
* added the new optional query request parameter projection
* added the media type application/json for the response with the status 200

### GET /ad-publishing/facebook/pixelsâ

* added the new optional query request parameter after
* added the new optional query request parameter limit
* added the new optional query request parameter projection
* added the media type application/json for the response with the status 200

### GET /ad-publishing/google/assetsâ

* added the new optional query request parameter limit
* added the new optional query request parameter pageToken
* added the media type application/json for the response with the status 200

### GET /ad-publishing/google/audiencesâ

* â ï¸ deleted the query request parameter isDraft
* added the new optional query request parameter limit
* added the new optional query request parameter pageToken
* added the media type application/json for the response with the status 200

### GET /ad-publishing/google/conversion-goalsâ

* â ï¸ deleted the query request parameter isDraft
* added the new optional query request parameter limit
* added the new optional query request parameter pageToken
* added the media type application/json for the response with the status 200

### GET /ad-publishing/google/conversionsâ

* added the new optional query request parameter limit
* added the new optional query request parameter pageToken

### GET /ad-publishing/google/segmentsâ

* added the new optional query request parameter limit
* added the new optional query request parameter pageToken
* added the media type application/json for the response with the status 200

### GET /ad-publishing/google/target-interestsâ

* added the new optional query request parameter limit
* added the new optional query request parameter pageToken
* added the new optional query request parameter projection
* added the media type application/json for the response with the status 200

### GET /ad-publishing/linkedin/{accountId}/formsâ

* â ï¸ deleted the query request parameter isDraft
* added the new optional query request parameter limit
* added the new optional query request parameter pageToken
* added the new optional query request parameter projection
* added the media type application/json for the response with the status 200

## 2026-07-28â

Opportunities

### GET /opportunities/{id}â

* added #/components/schemas/GetOpportunityResponseSchema to the opportunity response property allOf list for the response status 200
* removed #/components/schemas/SearchOpportunitiesResponseSchema from the opportunity response property allOf list for the response status 200

## 2026-07-07â

Ad Publishing

### GET /ad-publishing/facebook/pagesâ

* added the new optional query request parameter after
* added the new optional query request parameter limit
* added the media type application/json for the response with the status 200

## 2026-06-26â

Opportunities

### POST /opportunities/pipelinesâ

* endpoint added

### DELETE /opportunities/pipelines/{pipelineId}â

* endpoint added

### GET /opportunities/pipelines/{pipelineId}â

* endpoint added

### PUT /opportunities/pipelines/{pipelineId}â

* endpoint added

## 2026-06-18â

Ad Publishing

### GET /ad-publishing/facebook/campaigns/{campaignId}/publishing-progressâ

Saas

### GET /saas/allow-attach-rebilling/{locationId}â

* endpoint added

## 2026-06-15â

Users

### GET /users/â

* â ï¸ added the new pipelines.create enum value to the users/items/scopes response property for the response status 200

### POST /users/â

* â ï¸ added the new pipelines.create enum value to the scopes response property for the response status 201
* added the new pipelines.create enum value to the request property scopes/items/
* added the new pipelines.create enum value to the request property scopesAssignedToOnly/items/

### GET /users/searchâ

* â ï¸ added the new pipelines.create enum value to the users/items/scopes response property for the response status 200

### POST /users/search/filter-by-emailâ

* â ï¸ added the new pipelines.create enum value to the users/items/scopes response property for the response status 200

### GET /users/{userId}â

* â ï¸ added the new pipelines.create enum value to the scopes response property for the response status 200

### PUT /users/{userId}â

* â ï¸ added the new pipelines.create enum value to the scopes response property for the response status 200
* added the new pipelines.create enum value to the request property scopes/items/
* added the new pipelines.create enum value to the request property scopesAssignedToOnly/items/

## 2026-06-12â

Ad Publishing

### GET /ad-publishing/facebook/reporting/listâ

* the query request parameter campaignId became optional

## 2026-04-28â

Users

### GET /users/â

* endpoint deprecated

## 2026-04-21â

Notes

### POST /notes/â

* endpoint added

### POST /notes/searchâ

* endpoint added

### DELETE /notes/{id}â

* endpoint added

### GET /notes/{id}â

* endpoint added

### PUT /notes/{id}â

* endpoint added

### PATCH /notes/{id}/attachmentsâ

* endpoint added

### PUT /notes/{id}/relationsâ

* endpoint added

### POST /notes/{id}/restoreâ

* endpoint added

## 2026-04-15â

Users

### GET /users/â

* â ï¸ added the new audit-logs.export enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new audit-logs.readonly enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.agency-subaccounts.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.billing.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.create enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.delete enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.details.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.export.list enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.features-limits.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.pause-resume enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new payments/settings.write enum value to the users/items/scopes response property for the response status 200

### POST /users/â

* â ï¸ added the new audit-logs.export enum value to the scopes response property for the response status 201
* â ï¸ added the new audit-logs.readonly enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.agency-subaccounts.manage enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.billing.manage enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.create enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.delete enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.details.manage enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.export.list enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.features-limits.manage enum value to the scopes response property for the response status 201
* â ï¸ added the new locations.pause-resume enum value to the scopes response property for the response status 201
* â ï¸ added the new payments/settings.write enum value to the scopes response property for the response status 201
* added the new optional request property twilioPhone
* added the new audit-logs.export enum value to the request property scopes/items/
* added the new audit-logs.export enum value to the request property scopesAssignedToOnly/items/
* added the new audit-logs.readonly enum value to the request property scopes/items/
* added the new audit-logs.readonly enum value to the request property scopesAssignedToOnly/items/
* added the new locations.agency-subaccounts.manage enum value to the request property scopes/items/
* added the new locations.agency-subaccounts.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.billing.manage enum value to the request property scopes/items/
* added the new locations.billing.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.create enum value to the request property scopes/items/
* added the new locations.create enum value to the request property scopesAssignedToOnly/items/
* added the new locations.delete enum value to the request property scopes/items/
* added the new locations.delete enum value to the request property scopesAssignedToOnly/items/
* added the new locations.details.manage enum value to the request property scopes/items/
* added the new locations.details.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.export.list enum value to the request property scopes/items/
* added the new locations.export.list enum value to the request property scopesAssignedToOnly/items/
* added the new locations.features-limits.manage enum value to the request property scopes/items/
* added the new locations.features-limits.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.pause-resume enum value to the request property scopes/items/
* added the new locations.pause-resume enum value to the request property scopesAssignedToOnly/items/
* added the new payments/settings.write enum value to the request property scopes/items/
* added the new payments/settings.write enum value to the request property scopesAssignedToOnly/items/

### GET /users/searchâ

* â ï¸ added the new audit-logs.export enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new audit-logs.readonly enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.agency-subaccounts.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.billing.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.create enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.delete enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.details.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.export.list enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.features-limits.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.pause-resume enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new payments/settings.write enum value to the users/items/scopes response property for the response status 200

### POST /users/search/filter-by-emailâ

* â ï¸ added the new audit-logs.export enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new audit-logs.readonly enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.agency-subaccounts.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.billing.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.create enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.delete enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.details.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.export.list enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.features-limits.manage enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new locations.pause-resume enum value to the users/items/scopes response property for the response status 200
* â ï¸ added the new payments/settings.write enum value to the users/items/scopes response property for the response status 200

### GET /users/{userId}â

* â ï¸ added the new audit-logs.export enum value to the scopes response property for the response status 200
* â ï¸ added the new audit-logs.readonly enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.agency-subaccounts.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.billing.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.create enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.delete enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.details.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.export.list enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.features-limits.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.pause-resume enum value to the scopes response property for the response status 200
* â ï¸ added the new payments/settings.write enum value to the scopes response property for the response status 200

### PUT /users/{userId}â

* â ï¸ added the new audit-logs.export enum value to the scopes response property for the response status 200
* â ï¸ added the new audit-logs.readonly enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.agency-subaccounts.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.billing.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.create enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.delete enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.details.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.export.list enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.features-limits.manage enum value to the scopes response property for the response status 200
* â ï¸ added the new locations.pause-resume enum value to the scopes response property for the response status 200
* â ï¸ added the new payments/settings.write enum value to the scopes response property for the response status 200
* added the new optional request property twilioPhone
* added the new audit-logs.export enum value to the request property scopes/items/
* added the new audit-logs.export enum value to the request property scopesAssignedToOnly/items/
* added the new audit-logs.readonly enum value to the request property scopes/items/
* added the new audit-logs.readonly enum value to the request property scopesAssignedToOnly/items/
* added the new locations.agency-subaccounts.manage enum value to the request property scopes/items/
* added the new locations.agency-subaccounts.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.billing.manage enum value to the request property scopes/items/
* added the new locations.billing.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.create enum value to the request property scopes/items/
* added the new locations.create enum value to the request property scopesAssignedToOnly/items/
* added the new locations.delete enum value to the request property scopes/items/
* added the new locations.delete enum value to the request property scopesAssignedToOnly/items/
* added the new locations.details.manage enum value to the request property scopes/items/
* added the new locations.details.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.export.list enum value to the request property scopes/items/
* added the new locations.export.list enum value to the request property scopesAssignedToOnly/items/
* added the new locations.features-limits.manage enum value to the request property scopes/items/
* added the new locations.features-limits.manage enum value to the request property scopesAssignedToOnly/items/
* added the new locations.pause-resume enum value to the request property scopes/items/
* added the new locations.pause-resume enum value to the request property scopesAssignedToOnly/items/
* added the new payments/settings.write enum value to the request property scopes/items/
* added the new payments/settings.write enum value to the request property scopesAssignedToOnly/items/

## 2026-04-14â

Marketplace

### GET /marketplace/app/{appId}/installationsâ

* added the optional property installationDetails/allOf[#/components/schemas/InstallerDetailsDTO]/companyPlan to the response with the 200 status
* response property installationDetails/allOf[#/components/schemas/InstallerDetailsDTO]/companyHighLevelPlan deprecated
