# Private Integrations
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/PrivateIntegrationsToken`
---

Private Integrations allow you to build powerful custom integrations between your HighLevel account and any other third-party app.

If you are looking to integrate your HighLevel account with a third-party app, you have two options:

* Find and install the relevant app from the App Marketplace
* Build your own private integration by yourself or with the help of a developer using APIs.

Private Integrations help you achieve #2 securely.

Video Walkthrough

## Key Advantages of Private Integrationsâ

* Simple: Generate Private Integration tokens from your account settings and manage them with ease.
* Secure: You get to restrict the scopes/permissions that a developer can access on your account.

Private Integrations are available for both Agencies and Sub-Accounts.

## What's the difference between Private Integrations and API Keys?â

## What's the difference between Private Integrations and OAuth2 Access Tokens?â

Private Integrations, to put it simply, are static/fixed OAuth2 Access Tokens.

## How do I use Private Integrations?â

Private Integration tokens are used in the Authorization header, just like other Access Tokens.

Example:

```bash
curl --request GET \  --url https://services.leadconnectorhq.com/locations/ve9EPM428h8vShlRW1KT \  --header 'Accept: application/json' \  --header 'Authorization: Bearer <YOUR PRIVATE INTEGRATION TOKEN>' \  --header 'Version: 2021-07-28'
```

```bash
curl --request GET \  --url https://services.leadconnectorhq.com/locations/ve9EPM428h8vShlRW1KT \  --header 'Accept: application/json' \  --header 'Authorization: Bearer <YOUR PRIVATE INTEGRATION TOKEN>' \  --header 'Version: 2021-07-28'
```

## Testing a Private Integration with API Callsâ

Once your Private Integration is created, you may want to test it by pushing data to an API endpoint. Hereâs an example of how to test the integration by adding a new contact:

```json
curl --request POST \  --url https://services.leadconnectorhq.com/contacts/ \  --header 'Authorization: Bearer <YOUR PRIVATE INTEGRATION TOKEN>' \  --header 'Content-Type: application/json' \  --header 'Version: 2021-07-28' \  --data '{ "firstName": "John", "lastName": "Doe", "email": "[email protected]", "phone": "+1234567890", "locationId": "LOCATION_ID" }'
```

```json
curl --request POST \  --url https://services.leadconnectorhq.com/contacts/ \  --header 'Authorization: Bearer <YOUR PRIVATE INTEGRATION TOKEN>' \  --header 'Content-Type: application/json' \  --header 'Version: 2021-07-28' \  --data '{ "firstName": "John", "lastName": "Doe", "email": "[email protected]", "phone": "+1234567890", "locationId": "LOCATION_ID" }'
```

Make sure to:

* Replace LOCATION_ID with the actual sub-account ID.
* Replace Authorization value with your generated Private Integration token.

For a full list of available endpoints and testing capabilities, visit our official developer documentation.

## How do I manage Private Integrations?â

### Who can create Private Integrations?â

By default, all agency admins can create and manage Private Integrations. You can restrict this permission at a user level.

Navigate to:
Settings > Team > Edit the specific agency admin > Roles & Permissions, and enable/disable Private Integrations for the agency admin.

You may apply restrictions at two levels:

* Allow the agency admin to view and manage the agency's private integrations
* Allow the agency admin to view and manage the sub-accounts' private integrations

### Where can I find Private Integrations?â

You can find Private Integrations under agency settings.
If you don't find it under settings, please make sure that you have enabled the feature on Labs.

## How do I create a new Private Integration?â

Step 1: Click on "Create new Integration"
Step 2: Give your Private Integration a name and description to help you and your team identify what it's for.
Step 3: Select the scopes/permissions that you want the private integration to have access to on your agency account. Ensure that you are selecting only the required scopes for better data security.
Step 4: Copy the token generated and share it with your third-party app developer.

Note: Please ensure that you are sharing the token with trusted parties only. Do not share it publicly.
Don't forget to copy the token generated as you won't be able to do it again later.

## Best Practices to Maintain Security of My Private Integration Tokenâ

We recommend that you rotate your Private Integration tokens every 90 days.

### How to rotate your token:â

Step 1: Navigate to Private Integrations under settings, and click on the Private Integration you have created.
Step 2: Click on "Rotate and expire this token later".
Step 3: Click "Continue" in response to the warning message if you are sure that you want to proceed with rotation.
Step 4: Copy the new token and update it on your third-party app.

You will have a 7-day window where both the old and the new tokens will continue to work. After 7 days, the old token will expire.

During this window, you can:

* "Cancel rotation" if your developer needs more time.
* "Expire Now" if the third party app has been updated.

## What if my token has been compromised?â

Step 1: Navigate to Private Integrations under settings, and click on the Private Integration you have created.
Step 2: Click on "Rotate and expire this token now".
Step 3: Click "Continue" in response to the warning message if you are sure that you want to proceed with rotation.
Step 4: Copy the new token and update it on your third-party app.

Note: Don't forget to copy the token generated as you won't be able to do it again later.

## Can I edit the Private Integration permissions without updating the token?â

Yes, you can edit the Private Integration name, description and scopes/permissions any time after you've created it.

How:

* Navigate to Private Integrations under settings, and select "Edit" from the three-dot menu.
* Update the Private Integration name and description if required. Click on "Next".
* If required, update the scopes/permissions that you want the private integration to have access to on your account. Ensure that you are selecting only the required scopes for better data security. Click on "Update" to save the updates made.

Note: Updating the Private Integration details does not generate a new token. The existing token will continue to work.

## How do I delete the Private Integration once I no longer need it?â

You can delete the Private Integration once you are no longer using the third-party app.

To do so, navigate to Private Integrations under settings, and select "Delete" from the three-dot menu.
