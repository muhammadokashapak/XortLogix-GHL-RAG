# Create a new brand board
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/create-brand-board`
---

# Create a new brand board

## /brand-boards/

Creates a new brand board with logos, colors, and fonts

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID where the brand board will be created

Name of the brand board

Array of logos for the brand board

Array of colors for the brand board

Array of fonts for the brand board

Set as the default brand board for this location

Source brand board ID to copy from (creates a new brand board based on this template)

Parent folder ID in media library for organizing brand boards

Source type indicating how the brand board was createdAvailable optionstemplateblanksnapshoturl

Website URL to extract design kit from (colors, fonts, logos)

```json
{  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": true,  "brandBoardId": "507f1f77bcf86cd799439011",  "parentId": "507f1f77bcf86cd799439011",  "type": "blank",  "url": "https://example.com"}
```

```json
{  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": true,  "brandBoardId": "507f1f77bcf86cd799439011",  "parentId": "507f1f77bcf86cd799439011",  "type": "blank",  "url": "https://example.com"}
```

Created

* application/json

* SchemaExample (auto)
* Example (auto)

Brand board ID

Location ID

Brand board name

Array of logos

Array of brand colors

Array of brand fonts

Whether this is the default brand board for the location

Whether the brand board has been soft deleted

Parent folder ID in media library

Media library folder ID for this brand board

Original brand board ID if cloned from snapshot

Metadata about the brand board

Assets that used fallbacks/defaults (only returned when creating from URL)

Creation timestamp

Last update timestamp

```json
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "missingAssets": {    "logos": [      "Footer"    ],    "fonts": [      "Arial"    ],    "colors": []  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

```json
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "missingAssets": {    "logos": [      "Footer"    ],    "fonts": [      "Arial"    ],    "colors": []  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```
