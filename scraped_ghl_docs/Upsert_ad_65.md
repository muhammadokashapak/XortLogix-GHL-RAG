# Upsert ad
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-upsert-ad`
---

# Upsert ad

## /ad-publishing/facebook/ads

Create or update a Facebook ad

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Ad identifier

Location identifier

Ad name

Single primary text. Normalised into primaryTexts when that array is empty, so send primaryTexts instead unless you have exactly one variant.

Ad-level headline for CAROUSEL ads â used for any card that does not set its own media[].headline. SINGLE (image and video) ads take their headline from the headlines array instead.

Single ad description. SINGLE (image and video) ads take their description from the descriptions array, and carousel cards from media[].description.

Ad image URL

Ad media typeAvailable optionsSINGLECAROUSEL

Media items (images or videos) attached to the ad creative

Enable multi-advertiser ads

Parent campaign ID

Parent ad set ID

Call-to-action button. Valid values depend on the parent campaign objective (and, for sales, the ad set conversionLocation) â OUTCOME_LEADS: APPLY_NOW, DOWNLOAD, GET_OFFER, GET_QUOTE, LEARN_MORE, SIGN_UP, SUBSCRIBE; OUTCOME_TRAFFIC: APPLY_NOW, BOOK_TRAVEL, BUY_NOW, CONTACT_US, GET_OFFER, GET_PROMOTIONS, GET_QUOTE, LEARN_MORE, NO_BUTTON, ORDER_NOW, SHOP_NOW, SIGN_UP, SUBSCRIBE; OUTCOME_ENGAGEMENT: APPLY_NOW, BOOK_TRAVEL, CONTACT_US, GET_PROMOTIONS, GET_QUOTE, INQUIRE_NOW, LEARN_MORE, MESSAGE_PAGE, ORDER_NOW, SEND_UPDATES, SHOP_NOW, SIGN_UP, SUBSCRIBE; OUTCOME_SALES with conversionLocation: messaging: APPLY_NOW, BOOK_TRAVEL, CONTACT_US, GET_QUOTE, LEARN_MORE, MESSAGE_PAGE, ORDER_NOW, PLAY_GAME, SHOP_NOW, SIGN_UP, SUBSCRIBE; OUTCOME_SALES with conversionLocation: website: APPLY_NOW, BOOK_TRAVEL, BUY_TICKETS, CONTACT_US, GET_OFFER, GET_QUOTE, GET_SHOWTIMES, LEARN_MORE, LISTEN_NOW, ORDER_NOW, PLAY_GAME, SHOP_NOW, SIGN_UP, SUBSCRIBE, WATCH_MORE. Note BOOK_TRAVEL is the "Book now" button. Not validated server-side, so values outside this set are forwarded to Facebook and may be rejected there.

Conversation form ID

Destination link URL

Destination form ID

Primary text variants. Used by every media type. Supply more than one to run Facebook text variations; with a single entry it becomes the ad message. Prefer this over the singular primaryText.

Headline variants. Applies to SINGLE (image and video) ads only â carousel ads take their per-card headline from media[].headline, falling back to the singular headline. Supply more than one to run Facebook text variations.

Description variants. Applies to SINGLE (image and video) ads only â carousel ads take their per-card description from media[].description. Supply more than one to run Facebook text variations.

```json
{  "id": "ad_123",  "locationId": "loc_abc123",  "name": "My Ad Creative",  "primaryText": "Check out our offer!",  "headline": "Great Deal",  "description": "Limited time offer",  "imageUrl": "https://example.com/img.jpg",  "mediaType": "SINGLE",  "media": [    {      "src": "https://example.com/image.jpg",      "thumbnailUrl": "https://example.com/thumb.jpg",      "selectedPoster": 0,      "type": "IMAGE",      "name": "ad_image.jpg"    }  ],  "multiAdvertiserAds": false,  "campaignId": "camp_123",  "adsetId": "adset_123",  "cta": "LEARN_MORE",  "conversationFormId": "conv_123",  "destinationLink": "https://example.com",  "destinationFormId": "form_123",  "primaryTexts": [    {      "text": "Automation Test Primary Text"    }  ],  "headlines": [    {      "text": "Automation Test Headline"    },    {      "text": "Automation Test Headline1"    }  ],  "descriptions": [    {      "text": "Automation Test Description"    }  ]}
```

```json
{  "id": "ad_123",  "locationId": "loc_abc123",  "name": "My Ad Creative",  "primaryText": "Check out our offer!",  "headline": "Great Deal",  "description": "Limited time offer",  "imageUrl": "https://example.com/img.jpg",  "mediaType": "SINGLE",  "media": [    {      "src": "https://example.com/image.jpg",      "thumbnailUrl": "https://example.com/thumb.jpg",      "selectedPoster": 0,      "type": "IMAGE",      "name": "ad_image.jpg"    }  ],  "multiAdvertiserAds": false,  "campaignId": "camp_123",  "adsetId": "adset_123",  "cta": "LEARN_MORE",  "conversationFormId": "conv_123",  "destinationLink": "https://example.com",  "destinationFormId": "form_123",  "primaryTexts": [    {      "text": "Automation Test Primary Text"    }  ],  "headlines": [    {      "text": "Automation Test Headline"    },    {      "text": "Automation Test Headline1"    }  ],  "descriptions": [    {      "text": "Automation Test Description"    }  ]}
```
