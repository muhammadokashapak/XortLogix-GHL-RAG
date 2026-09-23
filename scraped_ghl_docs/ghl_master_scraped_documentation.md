# GoHighLevel Master Complete API & Developer Documentation

Generated on: 2026-08-22 00:04:30
Total Pages Scraped: 248

================================================================================

# HighLevel API Documentation - Developer Portal
**Source URL:** `https://marketplace.gohighlevel.com/docs`
---

## Comprehensive API Coverage

Access all HighLevel platform features through our REST API.Perfect for building integrations, automating workflows, and creating custom applications.

### ð¢ CRM & Contacts

Manage contacts, leads, and customer data with full CRUD operations, tagging, and custom fields.

### ð¬ Conversations

Handle SMS, email, and call communications. Send messages, manage threads, and track conversations.

### ð Calendar & Events

Schedule appointments, manage calendar events, and handle booking workflows programmatically.

### ð¯ Opportunities

Track sales pipeline, manage deals, and automate opportunity workflows with our sales API.

### ð³ Payments

Process payments, manage subscriptions, and handle transaction data through our payment API.

### ð Webhooks

Real-time notifications for 50+ events. Stay updated with instant webhook callbacks.

## Quick Start Guide

* Choose Integration Type - Marketplace app or Private integrationSet Up Authentication - OAuth 2.0 or Private Integration TokenMake Your First API Call - Test with our interactive documentationBuild & Deploy - Use our SDKs and code examples
* Set Up Authentication - OAuth 2.0 or Private Integration TokenMake Your First API Call - Test with our interactive documentationBuild & Deploy - Use our SDKs and code examples
* Make Your First API Call - Test with our interactive documentationBuild & Deploy - Use our SDKs and code examples
* Build & Deploy - Use our SDKs and code examples

### Example API Request

```bash
curl -X GET \
  https://services.leadconnectorhq.com/contacts/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

## Developer Resources

#### ð API Reference

Complete endpoint documentation with request/response examples

#### ð Authentication

OAuth 2.0 and Private Integration setup guides

#### â¡ Webhooks

Real-time event notifications and webhook setup

#### ðª Marketplace

Build and distribute apps in the HighLevel marketplace


================================================================================

# 70 docs tagged with "Webhook Events"
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/tags/webhook-events`
---

## App

Called whenever an app is installed


================================================================================

# One doc tagged with "Country"
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/tags/country`
---

## Country List

Select country code whenever a contact will create or update with country field


================================================================================

# Developer's Glossary of Terms
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/DeveloperGlossary`
---

* Developer's Marketplace: The Developer's Marketplace is a platform within HighLevel that allows developers to build and integrate their applications and tools using the HighLevel API. HighLevel Developer Documentation
* API (Application Programming Interface): An API is a set of rules and protocols that allows different software applications to communicate with each other. In the Developer's Marketplace context, the HighLevel API enables developers to access and interact with HighLevel's features and data.
* Access Token: An Access Token is a credential an app uses to access protected resources for a user or account. In the Developer's Marketplace, developers obtain an Access Token through the OAuth process, which allows their app to make authenticated API requests to HighLevel. The Access Token is usually included in the Authorization header of API requests.
* AppID: The unique identifier for your marketplace application. You can find it below the app name.
* Conversation Provider ID: The unique identifier for the type of provider a user installs. You can find it under the name of the conversation provider if you have created one for your app.
* Refresh Token: A Refresh Token is a credential that can be used to obtain a new Access Token without requiring the user to reauthorize the app. It provides a longer-lasting authorization mechanism and helps maintain continuous access to HighLevel resources. When an Access Token expires, the Refresh Token can be used to obtain a new one.
* OAuth (Open Authorization): OAuth is an industry-standard protocol that enables secure app authorization and authentication. It allows users to grant permission to apps to access their HighLevel data without sharing their login credentials. OAuth involves an authorization process where users are redirected to HighLevel to authenticate and grant access to the app. OAuth 2.0 Introduction
* Redirect URI: A Redirect URI is the URL that HighLevel will send users after authorizing the app's access. During the OAuth process, users are redirected to the app with an authorization code or access token appended to the Redirect URI after granting permission. OAuth 2.0 Redirect URI
* Authorization Code: In the OAuth process, an Authorization Code is a short-lived credential obtained after a user successfully authorizes an app. The app exchanges this code for an Access Token and Refresh Token. OAuth 2.0 Authorization Code Grant
* Scopes: Scopes define the specific permissions and access rights an app requires to interact with HighLevel. When creating an app, developers specify the necessary scopes that align with their app's functionalities. Scopes can include reading, writing, or managing permissions for different resources within HighLevel. OAuth 2.0 Scopes and this resource is for HighLevel's OAuth Scopes.
* Endpoint: An endpoint is a specific URL or URI representing an API resource or functionality. HighLevel's API exposes various endpoints that developers can access to perform specific actions or retrieve specific data.
* Status Code: A status code is a three-digit number returned by the server to indicate the outcome of an HTTP request. Common status codes include 200 (OK), 400 (Bad Request), 401 (Unauthorized), and 422 (Unprocessable Entity). HTTP Status Codes
* Distribution Type: Distribution Type refers to how an app is distributed or made available to HighLevel users. It can be either Agency or Sub Account. Agency distribution allows the app to be used by all locations within an agency account, while Sub Account distribution limits usage to specific sub-accounts or individual locations.
* Location ID: Location ID is a unique identifier assigned to a specific location within a HighLevel account. It is used to differentiate and manage access at the location level.
* Company ID: Company ID is a unique identifier assigned to a HighLevel company or account. It helps differentiate and manage access at the company level.
* Live Server: Live Server refers to the actual production environment where the app interacts with HighLevel's API and real user data. It is the server where the app is deployed and accessible by users.
* SDK (Software Development Kit): An SDK is a set of tools, libraries, and documentation developers use to build applications for a specific platform or framework. HighLevel provides an SDK that facilitates the integration of custom apps with its API.
* Authorization Header: The Authorization Header is an HTTP header that includes authentication credentials in API requests, such as an Access Token. It typically takes the form "Authorization: Bearer Access-Token". Understand the Authorization Header
* API Key: An API Key is a unique identifier or code provided to developers granting API access. It serves as a form of authentication when making API requests.
* Callback URL: A Callback URL is where an app expects to receive callbacks or responses. In the Developer's Marketplace context, the Callback URL is the endpoint that receives the authorization code or access token after the user grants permission during the OAuth process. Learn more about Callback URLs
* JSON (JavaScript Object Notation): JSON is a lightweight data-interchange format that is easy for humans to read and write and for machines to parse and generate. It is commonly used for structuring data in API requests and responses. Introduction to JSON
* Parameters: Parameters are additional values included in an API request to provide specific instructions or filter the desired data. Parameters can be used to specify search criteria, sorting preferences, or pagination options. Understanding API Parameters
* Pagination: Pagination is dividing a large data set into smaller, more manageable parts called pages. API responses often include pagination information, such as the number of items per page and the total number of pages, allowing developers to retrieve data incrementally. Implementing Pagination
* Rate Limiting: Rate Limiting is a mechanism APIs use to restrict client or user's requests within a specific period. It helps maintain API performance and prevent abuse.
* Webhooks: Webhooks are HTTP callbacks or notifications sent from one application to another when a specific event or trigger occurs. In the Developer's Marketplace context, developers can configure webhooks to receive real-time updates or data from HighLevel, such as new leads or contact information.
* Event: An Event refers to a specific occurrence or action within an application or system. In the context of webhooks, events are triggers that prompt sending a webhook notification.
* Request: A request is a communication made by an app to the HighLevel API. It includes the HTTP method (e.g., GET, POST), the URL or endpoint, headers, and required parameters or data. HTTP Request Methods
* Response: A response is the server's reply to a request made by an app. It contains the requested data, an acknowledgment of the action performed, and an appropriate status code. HTTP Response Status Codes
* GET: GET is an HTTP method to retrieve server data. It is commonly used for fetching resources or information from APIs. GET method in HTTP
* POST: POST is an HTTP method to submit data to a server. It is typically used for creating new resources or sending data to be processed by APIs. POST method in HTTP
* PUT: PUT is an HTTP method to update or replace existing data on a server. It replaces the entire resource with the new data provided in the request. PUT method in HTTP
* DELETE: DELETE is an HTTP method that removes or deletes a resource from a server. It instructs the server to delete the specified resource. DELETE method in HTTP
* Front-End Development: Front-End Development involves building the user-facing components of a software application. It typically includes HTML, CSS, and JavaScript developers to create interactive and visually appealing interfaces.
* Back-End Development: Back-End Development focuses on the server-side components of a software application. It involves implementing the logic, data storage, and processing necessary to support the application's functionality.

Developer's Marketplace: The Developer's Marketplace is a platform within HighLevel that allows developers to build and integrate their applications and tools using the HighLevel API. HighLevel Developer Documentation

API (Application Programming Interface): An API is a set of rules and protocols that allows different software applications to communicate with each other. In the Developer's Marketplace context, the HighLevel API enables developers to access and interact with HighLevel's features and data.

Access Token: An Access Token is a credential an app uses to access protected resources for a user or account. In the Developer's Marketplace, developers obtain an Access Token through the OAuth process, which allows their app to make authenticated API requests to HighLevel. The Access Token is usually included in the Authorization header of API requests.

AppID: The unique identifier for your marketplace application. You can find it below the app name.

Conversation Provider ID: The unique identifier for the type of provider a user installs. You can find it under the name of the conversation provider if you have created one for your app.

Refresh Token: A Refresh Token is a credential that can be used to obtain a new Access Token without requiring the user to reauthorize the app. It provides a longer-lasting authorization mechanism and helps maintain continuous access to HighLevel resources. When an Access Token expires, the Refresh Token can be used to obtain a new one.

OAuth (Open Authorization): OAuth is an industry-standard protocol that enables secure app authorization and authentication. It allows users to grant permission to apps to access their HighLevel data without sharing their login credentials. OAuth involves an authorization process where users are redirected to HighLevel to authenticate and grant access to the app. OAuth 2.0 Introduction

Redirect URI: A Redirect URI is the URL that HighLevel will send users after authorizing the app's access. During the OAuth process, users are redirected to the app with an authorization code or access token appended to the Redirect URI after granting permission. OAuth 2.0 Redirect URI

Authorization Code: In the OAuth process, an Authorization Code is a short-lived credential obtained after a user successfully authorizes an app. The app exchanges this code for an Access Token and Refresh Token. OAuth 2.0 Authorization Code Grant

Scopes: Scopes define the specific permissions and access rights an app requires to interact with HighLevel. When creating an app, developers specify the necessary scopes that align with their app's functionalities. Scopes can include reading, writing, or managing permissions for different resources within HighLevel. OAuth 2.0 Scopes and this resource is for HighLevel's OAuth Scopes.

Endpoint: An endpoint is a specific URL or URI representing an API resource or functionality. HighLevel's API exposes various endpoints that developers can access to perform specific actions or retrieve specific data.

Status Code: A status code is a three-digit number returned by the server to indicate the outcome of an HTTP request. Common status codes include 200 (OK), 400 (Bad Request), 401 (Unauthorized), and 422 (Unprocessable Entity). HTTP Status Codes

Distribution Type: Distribution Type refers to how an app is distributed or made available to HighLevel users. It can be either Agency or Sub Account. Agency distribution allows the app to be used by all locations within an agency account, while Sub Account distribution limits usage to specific sub-accounts or individual locations.

Location ID: Location ID is a unique identifier assigned to a specific location within a HighLevel account. It is used to differentiate and manage access at the location level.

Company ID: Company ID is a unique identifier assigned to a HighLevel company or account. It helps differentiate and manage access at the company level.

Live Server: Live Server refers to the actual production environment where the app interacts with HighLevel's API and real user data. It is the server where the app is deployed and accessible by users.

SDK (Software Development Kit): An SDK is a set of tools, libraries, and documentation developers use to build applications for a specific platform or framework. HighLevel provides an SDK that facilitates the integration of custom apps with its API.

Authorization Header: The Authorization Header is an HTTP header that includes authentication credentials in API requests, such as an Access Token. It typically takes the form "Authorization: Bearer Access-Token". Understand the Authorization Header

API Key: An API Key is a unique identifier or code provided to developers granting API access. It serves as a form of authentication when making API requests.

Callback URL: A Callback URL is where an app expects to receive callbacks or responses. In the Developer's Marketplace context, the Callback URL is the endpoint that receives the authorization code or access token after the user grants permission during the OAuth process. Learn more about Callback URLs

JSON (JavaScript Object Notation): JSON is a lightweight data-interchange format that is easy for humans to read and write and for machines to parse and generate. It is commonly used for structuring data in API requests and responses. Introduction to JSON

Parameters: Parameters are additional values included in an API request to provide specific instructions or filter the desired data. Parameters can be used to specify search criteria, sorting preferences, or pagination options. Understanding API Parameters

Pagination: Pagination is dividing a large data set into smaller, more manageable parts called pages. API responses often include pagination information, such as the number of items per page and the total number of pages, allowing developers to retrieve data incrementally. Implementing Pagination

Rate Limiting: Rate Limiting is a mechanism APIs use to restrict client or user's requests within a specific period. It helps maintain API performance and prevent abuse.

Webhooks: Webhooks are HTTP callbacks or notifications sent from one application to another when a specific event or trigger occurs. In the Developer's Marketplace context, developers can configure webhooks to receive real-time updates or data from HighLevel, such as new leads or contact information.

Event: An Event refers to a specific occurrence or action within an application or system. In the context of webhooks, events are triggers that prompt sending a webhook notification.

Request: A request is a communication made by an app to the HighLevel API. It includes the HTTP method (e.g., GET, POST), the URL or endpoint, headers, and required parameters or data. HTTP Request Methods

Response: A response is the server's reply to a request made by an app. It contains the requested data, an acknowledgment of the action performed, and an appropriate status code. HTTP Response Status Codes

GET: GET is an HTTP method to retrieve server data. It is commonly used for fetching resources or information from APIs. GET method in HTTP

POST: POST is an HTTP method to submit data to a server. It is typically used for creating new resources or sending data to be processed by APIs. POST method in HTTP

PUT: PUT is an HTTP method to update or replace existing data on a server. It replaces the entire resource with the new data provided in the request. PUT method in HTTP

DELETE: DELETE is an HTTP method that removes or deletes a resource from a server. It instructs the server to delete the specified resource. DELETE method in HTTP

Front-End Development: Front-End Development involves building the user-facing components of a software application. It typically includes HTML, CSS, and JavaScript developers to create interactive and visually appealing interfaces.

Back-End Development: Back-End Development focuses on the server-side components of a software application. It involves implementing the logic, data storage, and processing necessary to support the application's functionality.


================================================================================

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


================================================================================

# Authorization
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/authorization_doc`
---

Authorization is the process of granting or denying access to resources based on a user's verified identity and permissions. It determines what a user can do within a system after they have been authenticated (proven their identity). Essentially, it's about verifying that a user has the right to access specific resources or perform certain actions.

## HighLevel currently supports two types of authorization:â

* Private Integration Token
* OAuth 2.0 Flow

### When should I use a Private Integration Token?â

You should use a Private Integration Token if:

* Your use case involves accessing our API endpoints for internal purposes.
* If you don't need webhooks or custom design or pages.
* If you need to access only 1 sub-account at a time.

#### Example use cases:â

* Internal data synchronization
* Custom reporting dashboards
* Automated tasks within your own system

### When should I use OAuth 2.0 Flow?â

You should use OAuth 2.0 Flow if:

* You're developing a full-scale integration intended for public use.
* Your integration requires features like webhooks and custom modules.
* You need advanced security features and standardized authorization management.

#### Example use cases:â

* Third-party applications
* Creating custom conversation providers/custom workflow actions and triggers, etc.
* Services requiring secure user authorization


================================================================================

# One doc tagged with "OAuth 2.0"
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/tags/o-auth-2-0`
---

## **Scopes**

Here is a list of the scopes you require to access the API Endpoints and Webhook Events.


================================================================================

# 7 docs tagged with "Webhook Response"
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/tags/webhook-response`
---

## Association Created

Overview


================================================================================

# Access Token Generation: Agency vs. Sub-Account Scenarios
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/AccessTokenUseCase`
---

The type of Access Token that is generated depends on who is installing the app (an agency or a sub-account) and the app's distribution settings. Understanding these scenarios is crucial for developers to ensure their app correctly authenticates and functions as expected. Below, we'll outline the different contexts that determine whether an Agency-level or Sub-Account (Location-level) Access Token is issued.


================================================================================

# OAuth 2.0
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/OAuth2.0`
---

OAuth 2.0 is a standard protocol that authorizes a client application (like a third-party app) to access specific resources on behalf of a user, without sharing the userâs password. Itâs widely used for APIs that need secure, delegated access.

HighLevel supports the Authorization Code Grant flow with v2 APIs. Below is the step-by-step procedure to understand and use the OAuth 2.0 flow.

## 1. Register an OAuth Appâ

* Go to the Marketplace and sign up for a developer account.
* Go to My Apps, click Create App.
* Fill in the following details:

APP Name: Suitable name for the app.
APP Type: Private or Public.

Private Apps: For personal/internal use, not listed in the Marketplace.
Public Apps: Visible and installable by all users once approved.

Note: We recommend starting with your app set to Private. This allows you to develop and thoroughly test its functionality in a controlled environment. Once you're confident the app is stable and complete, you can switch it to Public for broader installation and use by other accounts.
Target User: This allows you to define who your app is intended for â in other words, who will actually be using it.
For the vast majority of apps (approximately 95%), the ideal choice is "Sub-account" (recommended).
Who can install: Who should be able to view and install the app from the Marketplace UI?
The recommended setting is âBoth Agency & Sub-accountâ to ensure maximum visibility and adoption of your app.
However, if youâre building a fully white-labeled SaaS feature intended to be exclusively discovered and installed by agencies for use within their sub-accounts, you may choose to limit visibility to Agencies only.
Listing Type: White-label recommended for marketing agencies.
* APP Name: Suitable name for the app.
* APP Type: Private or Public.

Private Apps: For personal/internal use, not listed in the Marketplace.
Public Apps: Visible and installable by all users once approved.

Note: We recommend starting with your app set to Private. This allows you to develop and thoroughly test its functionality in a controlled environment. Once you're confident the app is stable and complete, you can switch it to Public for broader installation and use by other accounts.
* Private Apps: For personal/internal use, not listed in the Marketplace.
* Public Apps: Visible and installable by all users once approved.
* Target User: This allows you to define who your app is intended for â in other words, who will actually be using it.
For the vast majority of apps (approximately 95%), the ideal choice is "Sub-account" (recommended).
* Who can install: Who should be able to view and install the app from the Marketplace UI?
The recommended setting is âBoth Agency & Sub-accountâ to ensure maximum visibility and adoption of your app.
However, if youâre building a fully white-labeled SaaS feature intended to be exclusively discovered and installed by agencies for use within their sub-accounts, you may choose to limit visibility to Agencies only.
* Listing Type: White-label recommended for marketing agencies.

* APP Name: Suitable name for the app.
* APP Type: Private or Public.

Private Apps: For personal/internal use, not listed in the Marketplace.
Public Apps: Visible and installable by all users once approved.

Note: We recommend starting with your app set to Private. This allows you to develop and thoroughly test its functionality in a controlled environment. Once you're confident the app is stable and complete, you can switch it to Public for broader installation and use by other accounts.
* Private Apps: For personal/internal use, not listed in the Marketplace.
* Public Apps: Visible and installable by all users once approved.
* Target User: This allows you to define who your app is intended for â in other words, who will actually be using it.
For the vast majority of apps (approximately 95%), the ideal choice is "Sub-account" (recommended).
* Who can install: Who should be able to view and install the app from the Marketplace UI?
The recommended setting is âBoth Agency & Sub-accountâ to ensure maximum visibility and adoption of your app.
However, if youâre building a fully white-labeled SaaS feature intended to be exclusively discovered and installed by agencies for use within their sub-accounts, you may choose to limit visibility to Agencies only.
* Listing Type: White-label recommended for marketing agencies.

* Private Apps: For personal/internal use, not listed in the Marketplace.
* Public Apps: Visible and installable by all users once approved.

* After creating the APP you will be taken to the Profile section where you will need to add the details related to your APP. For eg; APP Logo, category, Company Name, APP Description, preview images etc.
* After completing the profile details, please click on the Advanced Settings drop down available in the left pane and go to the auth section.
* The Auth page will appear as shown in the screenshot below. This is where youâll configure essential settings for your appâs OAuth integration, including scopes, redirect URLs, and client credentials.

* Scopes: Scopes define the level of access your app will have â what data it can read or what actions it can perform on behalf of the user. Click Here to find all the available Scopes.

Itâs best practice to request the minimum number of scopes necessary for your app to function.
Click on the "Select Scope" dropdown and choose the relevant scopes based on your appâs functionality.
* Itâs best practice to request the minimum number of scopes necessary for your app to function.
* Click on the "Select Scope" dropdown and choose the relevant scopes based on your appâs functionality.
* Redirect URL: A Redirect URL (also known as a Callback URL) is the destination where the authorization server will send the authorization code after the user installs the app.

Enter your redirect URL in the Redirect URL field.
Click the "Add" button to save it.
* Enter your redirect URL in the Redirect URL field.
* Click the "Add" button to save it.
* Client Keys (ID & Secret): In the Client Keys section:

Click the "Add" button.
Provide a name for your client key pair.
Upon saving, your Client ID and Client Secret will be generated.
* Click the "Add" button.
* Provide a name for your client key pair.
* Upon saving, your Client ID and Client Secret will be generated.

Scopes: Scopes define the level of access your app will have â what data it can read or what actions it can perform on behalf of the user. Click Here to find all the available Scopes.

* Itâs best practice to request the minimum number of scopes necessary for your app to function.
* Click on the "Select Scope" dropdown and choose the relevant scopes based on your appâs functionality.

Redirect URL: A Redirect URL (also known as a Callback URL) is the destination where the authorization server will send the authorization code after the user installs the app.

* Enter your redirect URL in the Redirect URL field.
* Click the "Add" button to save it.

Client Keys (ID & Secret): In the Client Keys section:

* Click the "Add" button.
* Provide a name for your client key pair.
* Upon saving, your Client ID and Client Secret will be generated.

These credentials are used to identify and authenticate your application with the OAuth server during token exchange.

Important: Be sure to copy and securely store your Client Secret immediately. After clicking "OK", you will not be able to view or copy the secret again from the UI.

## 2. Add the App to Your Desired Locationâ

* Have the location/agency admin visit your Installation URL.
* Select the location to connect.
* Redirected to your Redirect URL with an Authorization Code.
* Exchange the code for an Access Token via the OAuth 2.0 Get Access Token API.
* Use the Access Token to call APIs.

## 3. Get the Installation URLâ

Inside your APP Auth Pane available inside the Advanced Settings Section you will be able to see the Install Link at the top of the Page.

Click on the Show button and you will be able to see the Installation URLs which you will be using to install the APP.

Depending on your usecase and account setup you can either use the standard or the whitelabel version of the Installation URL.

Refer to the below steps to install the APP:

* Copy the Installation URL and open it in your browser.
* In case you are not logged in to your GHL account it will ask you to login to your account.

* In case you are logged in it will show a page showcasing the accounts.

* Select the account you want to install the APP in.
* When a user grants access, their browser is redirected to the specified redirect URI, and the Authorization Code is passed inside the code query parameter.

```bash
https://myapp.com/oauth/callback/highlevel?code=7676cjcbdc6t76cdcbkjcd09821jknnkj
```

```bash
https://myapp.com/oauth/callback/highlevel?code=7676cjcbdc6t76cdcbkjcd09821jknnkj
```

This URL demonstrates a typical OAuth callback scenario for a HighLevel integration. The code parameter included in the query string is essential for completing the authorization flow.

## 4. Listening to Webhook Eventsâ

The HighLevel Marketplace App allows you to listen to various webhook events, enabling real-time updates and integrations based on user actions.

To set up webhook listeners:

* Navigate to your app in the Marketplace dashboard.
* Click on the "Advanced Settings" dropdown in the left-hand panel.
* Go to the "Webhooks" section.
* In the input box at the top, enter your webhook URL.
* Use the toggle switches next to each event to subscribe to the events you wish to listen for.

For a full list of supported webhook events and example payloads, please refer to the documentation: Webhook Events & Payloads

### Important: App Install Webhookâ

One of the most critical webhook events is the App Install event. This event provides essential details whenever your app is installed by a user. If a webhook URL is configured for your app, this event is subscribed to by default.

Hereâs a sample payload for the App Install event:

```json
{  "type": "INSTALL",  "appId": "665c6bb13d4e5364bdec0e2f",  "versionId": "665c6bb13d4e5364bdec0e2f",  "installType": "Location",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "companyName": "Marketplace and Integrations Prod Agency",  "isWhitelabelCompany": true,  "whitelabelDetails": {    "logoUrl": "https://...gif",    "domain": "rajender.dentistsnear.me"  },  "timestamp": "2025-06-25T06:57:06.225Z",  "webhookId": "1a533f85-1f1e-4886-891e-ee0cf4666e90"}
```

```json
{  "type": "INSTALL",  "appId": "665c6bb13d4e5364bdec0e2f",  "versionId": "665c6bb13d4e5364bdec0e2f",  "installType": "Location",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "companyName": "Marketplace and Integrations Prod Agency",  "isWhitelabelCompany": true,  "whitelabelDetails": {    "logoUrl": "https://...gif",    "domain": "rajender.dentistsnear.me"  },  "timestamp": "2025-06-25T06:57:06.225Z",  "webhookId": "1a533f85-1f1e-4886-891e-ee0cf4666e90"}
```

## 5. Exchange Authorization Code for Access Tokenâ

Once you have received the Authorization code on your redirect URl you are expected to use Get Access Token API endpoint to generate the Acces Token which you can then use to run the API endpoints.

Sample Payload:

```json
curl -X POST "https://services.leadconnectorhq.com/oauth/token" \  -H "Accept: application/json" \  -H "Content-Type: application/json" \  -d '{    "client_id": "665c6bb13d4e5364bdec0e2f-mawqjyjd",    "client_secret": "74032272-7f45-4e07-8717-5e1ddbfe3de0",    "grant_type": "authorization_code",    "code": "363fe3f086e2db02bb9c34722902d21f76c9b217",    "user_type": "Company",    "redirect_uri": "https://myapp.com/oauth/callback/highlevel"  }'
```

```json
curl -X POST "https://services.leadconnectorhq.com/oauth/token" \  -H "Accept: application/json" \  -H "Content-Type: application/json" \  -d '{    "client_id": "665c6bb13d4e5364bdec0e2f-mawqjyjd",    "client_secret": "74032272-7f45-4e07-8717-5e1ddbfe3de0",    "grant_type": "authorization_code",    "code": "363fe3f086e2db02bb9c34722902d21f76c9b217",    "user_type": "Company",    "redirect_uri": "https://myapp.com/oauth/callback/highlevel"  }'
```

Sample Response:

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb20",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21w",  "scope": "calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "refreshTokenId": "685a9cc9f7434ae2fc66c31d",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb20",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21w",  "scope": "calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "refreshTokenId": "685a9cc9f7434ae2fc66c31d",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```

## 6. Refresh Token Usageâ

As shown in the previous response, the Access Token expires after 86,399 seconds, which is approximately 24 hours. This means you'll need to regenerate a new Access Token once it expires to continue making API requests.

However, regenerating an Access Token using the authorization code requires repeating the entire installation process, which can be time-consuming. To simplify this, we also provide a Refresh Token along with the Access Token.

The Refresh Token is valid for up to one year, or until it is used. Once you use a Refresh Token to obtain a new Access Token, the original Refresh Token becomes invalid, and the response will include a new Refresh Token along with the new Access Token.
If left unused, the Refresh Token will remain valid for one year.

To generate a new Access Token using your existing Refresh Token, use the following API endpoint: Get Access Token

* Access Tokens expire after ~24 hours.
* Refresh Tokens are valid for 1 year or until used.
* Use Refresh Token to obtain a new Access Token without reinstallation.

Sample Payload:

```bash
curl --request POST \  --url https://services.leadconnectorhq.com/oauth/token \  --header 'Accept: application/json' \  --header 'Content-Type: application/x-www-form-urlencoded' \  --data client_id=665c6bb13d4e5364bdece2f-mawqjyjd \  --data client_secret=74032272-7f45-4e7-8717-5e1ddbfe3de0 \  --data grant_type=refresh_token \  --data refresh_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.dCiY5HiwOaxk8Cz6pQ0KstyeRu5fhPo \  --data user_type=Company \  --data redirect_uri=https://myapp.com/oauth/callback/highlevel
```

```bash
curl --request POST \  --url https://services.leadconnectorhq.com/oauth/token \  --header 'Accept: application/json' \  --header 'Content-Type: application/x-www-form-urlencoded' \  --data client_id=665c6bb13d4e5364bdece2f-mawqjyjd \  --data client_secret=74032272-7f45-4e7-8717-5e1ddbfe3de0 \  --data grant_type=refresh_token \  --data refresh_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.dCiY5HiwOaxk8Cz6pQ0KstyeRu5fhPo \  --data user_type=Company \  --data redirect_uri=https://myapp.com/oauth/callback/highlevel
```

Sample Response:

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21QU_Dcpo6oL_t8NN350g",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.sDO9cDrBHKShX173dwDZyxh4a6U",  "scope": "businesses.readonly businesses.write companies.readonly calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "refreshTokenId": "685b558f21fa7b18e3d09a",  "userType": "Company",  "companyId": "GNb7aIvrQFVb9wNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRih7dS9gJ3W8a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21QU_Dcpo6oL_t8NN350g",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.sDO9cDrBHKShX173dwDZyxh4a6U",  "scope": "businesses.readonly businesses.write companies.readonly calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "refreshTokenId": "685b558f21fa7b18e3d09a",  "userType": "Company",  "companyId": "GNb7aIvrQFVb9wNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRih7dS9gJ3W8a"}
```

## 7. Types of Access Tokenâ

In HighLevel we have 2 types of Access Token depending on the type of APP you have installed and who has installed the APP.

* Access Token with User Type as Agency: This Type of Access Token will be utilized to run the APIs related to the Agency Functionalities. For eg; Create Sub-Account API.

Sample Response:

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21QU_Dcpo6oL_t8NN350g",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.sDO9cDrBHKShX173dwDZyxh4a6U",  "scope": "businesses.readonly businesses.write companies.readonly calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "refreshTokenId": "685ba558f21fa7b18e3d09a",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9wNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJ3W8a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21QU_Dcpo6oL_t8NN350g",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.sDO9cDrBHKShX173dwDZyxh4a6U",  "scope": "businesses.readonly businesses.write companies.readonly calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "refreshTokenId": "685ba558f21fa7b18e3d09a",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9wNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJ3W8a"}
```

* Access Token with User Type as Location: This Type of Access Token will be utilized to run the APIs related to the Sub-Account or Location Functionalities. For eg; Create Contact API.

Sample Response:

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2ODViZDRiNW",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3",  "scope": "calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iNl5K",  "locationId": "HjiMUOsCCHCjtxEf8PR",  "userId": "Rg6BRRiHh7dS9gy3W8a",  "traceId": "8f712294-b015-42a-8c69-7fcb960560aa"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2ODViZDRiNW",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3",  "scope": "calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iNl5K",  "locationId": "HjiMUOsCCHCjtxEf8PR",  "userId": "Rg6BRRiHh7dS9gy3W8a",  "traceId": "8f712294-b015-42a-8c69-7fcb960560aa"}
```

## 8. Create Sub-Account Token from Agency Tokenâ

Suppose you have an Agency-level Access Token but want to run API endpoints specific to a Sub-Account (Location). In that case, you can use the Agency-level Access Token to generate a Sub-Account/Location-level Access Token via the Get Location Access Token from Agency Token API endpoint.

Sample Payload:

```json
curl -L "https://services.leadconnectorhq.com/oauth/locationToken" \  -H "Content-Type: application/json" \  -H "Accept: application/json" \  -H "Version: 2021-07-28" \  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJD" \  -d '{    "companyId": "GNb7aIv4rQFV9iwNl5K",    "locationId": "HjiMUOsCCHCjtxEf8PR"  }'
```

```json
curl -L "https://services.leadconnectorhq.com/oauth/locationToken" \  -H "Content-Type: application/json" \  -H "Accept: application/json" \  -H "Version: 2021-07-28" \  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJD" \  -d '{    "companyId": "GNb7aIv4rQFV9iwNl5K",    "locationId": "HjiMUOsCCHCjtxEf8PR"  }'
```

Sample Response:

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2ODViZDRiNW",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3",  "scope": "calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iNl5K",  "locationId": "HjiMUOsCCHCjtxEf8PR",  "userId": "Rg6BRRiHh7dS9gy3W8a",  "traceId": "8f712294-b015-42a-8c69-7fcb960560aa"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2ODViZDRiNW",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3",  "scope": "calendars.readonly calendars/events.readonly calendars.write calendars/events.write calendars/groups.readonly calendars/groups.write calendars/resources.readonly calendars/resources.write",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iNl5K",  "locationId": "HjiMUOsCCHCjtxEf8PR",  "userId": "Rg6BRRiHh7dS9gy3W8a",  "traceId": "8f712294-b015-42a-8c69-7fcb960560aa"}
```


================================================================================

# Handling Access Tokens for Apps with Target User: Agency
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/TargetUserAgency`
---

This guide explains how the installation flow works for the Agency targeted APPs , how to obtain the access token.

## Overviewâ

For apps whose Target User is set as Agency, the app will only be visible to the Agency Admin/Owner, and only they can install it.

## Installation Flowâ

* Install the app on your Agency account.
* After installation, the redirect URL will be triggered from our end, and the authorization code will be shared.
* Use this authorization code to exchange for an Access Token using the Get Access Token API endpoint.

* Note: The Access Token generated will be of user type company(Agency Level Token).

#### Sample Requestâ

```bash
curl -X POST   https://services.leadconnectorhq.com/oauth/token  -H 'Accept: application/json'   -H 'Content-Type: application/x-www-form-urlencoded'   -d 'client_id=68a2fd84fab6670f45220ebf-megyp358'   -d 'client_secret=673011da-b03a-4768-bbff-0f45821cd6fe'   -d 'grant_type=authorization_code'   -d 'code=16d0b6ceb51350ba437870074ad25bc65e8c1d8d'   -d 'user_type=Company'
```

```bash
curl -X POST   https://services.leadconnectorhq.com/oauth/token  -H 'Accept: application/json'   -H 'Content-Type: application/x-www-form-urlencoded'   -d 'client_id=68a2fd84fab6670f45220ebf-megyp358'   -d 'client_secret=673011da-b03a-4768-bbff-0f45821cd6fe'   -d 'grant_type=authorization_code'   -d 'code=16d0b6ceb51350ba437870074ad25bc65e8c1d8d'   -d 'user_type=Company'
```

#### Sample Responseâ

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21wYW55IiwiYXV0aENsYQ",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21wYW55IiwiYXV0aEN",  "scope": "locations.write",  "refreshTokenId": "68a2feef89153fe9b8d196bc",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": false,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21wYW55IiwiYXV0aENsYQ",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJDb21wYW55IiwiYXV0aEN",  "scope": "locations.write",  "refreshTokenId": "68a2feef89153fe9b8d196bc",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": false,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```


================================================================================

# Facebook Ads
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/facebook-ads`
---

Documentation for Ad-publishing API

## ðï¸Search targeting options

Search Facebook geo-locations and interests for ad targeting

## ðï¸Publish campaign

Publish a Facebook campaign and push it live to Facebook

## ðï¸Get conversion pixels

Retrieve Facebook conversion pixels for a location. For the FACEBOOK channel, without `limit` the response is `{ items, total }`; when `limit` is provided (max 100) the response is a paginated `{ items, paging }` envelope â pass `after` (from `paging.next`) to fetch the next batch. By default each item is returned in full; pass `projection` (comma-separated) to return only the requested fields, chosen from `createdAt`, `fbIsCrmPixel`, `fbPixelCode`, `fbPixelId`, `name`, `type` (any other value is rejected).

## ðï¸Upsert conversion pixel

Create or update a Facebook conversion pixel configuration

## ðï¸Get custom audiences

Retrieve Facebook custom audiences for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100) the response is a paginated `{ customAudiences, paging }` envelope; pass `after` (from `paging.next`) to fetch the next batch. By default each item is returned in full; pass `projection` (comma-separated, dot-notation for nested fields, e.g. ?projection=id,name,dataSource.type) to return only the requested fields â any value outside the known field set is rejected.

## ðï¸Delete custom audience

Delete a Facebook custom audience by ID

## ðï¸Update custom audience

Update name or description of a Facebook custom audience

## ðï¸Get custom audience by ID

Retrieve a specific Facebook custom audience by its ID

## ðï¸Add custom audience member

Add a member to a Facebook custom audience

## ðï¸Remove custom audience member

Remove a member from a Facebook custom audience

## ðï¸Batch update audience members

Add or remove members in bulk from a Facebook custom audience via CSV or smart lists

## ðï¸Get campaign with linked entities

Retrieve a Facebook campaign with its linked adsets and ads

## ðï¸Get entities

Retrieve Facebook campaigns, adsets, or ads based on entity type

## ðï¸Upsert campaign

Create or update a Facebook campaign

## ðï¸Upsert adset

Create or update a Facebook ad set

## ðï¸Upsert ad

Create or update a Facebook ad

## ðï¸Pause campaign

Pause a running Facebook campaign

## ðï¸Resume campaign

Resume a paused Facebook campaign

## ðï¸Duplicate campaign

Duplicate an existing Facebook campaign

## ðï¸Delete campaign

Delete a Facebook campaign by ID

## ðï¸Pause ad set

Pause a running Facebook ad set

## ðï¸Resume ad set

Resume a paused Facebook ad set

## ðï¸Duplicate ad set

Duplicate an existing Facebook ad set

## ðï¸Delete ad set

Delete a Facebook ad set by ID

## ðï¸Pause ad

Pause a running Facebook ad

## ðï¸Resume ad

Resume a paused Facebook ad

## ðï¸Duplicate ad

Duplicate an existing Facebook ad

## ðï¸Delete ad

Delete a Facebook ad by ID

## ðï¸Get campaign publishing progress

Returns Redis-backed publish progress for a campaign while it is publishing to Meta. Used by the validation funnel UI to poll step counts and completion state.


================================================================================

# Webhook
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/category/webhook`
---

## ðï¸AppInstall

Called whenever an app is installed

## ðï¸AppointmentCreate

Called whenever an appointment is created

## ðï¸AppointmentDelete

Called whenever an appointment is deleted

## ðï¸AppointmentUpdate

Called whenever an appointment is updated

## ðï¸AppUninstall

Called whenever an app is uninstalled

## ðï¸AppPaymentStatus

Called whenever the payment status of a paid app subscription changes â for example when a recurring payment fails during dunning, or when a previously failed payment is successfully recovered.

## ðï¸AppUpdate

Called whenever an app is updated to a new version

## ðï¸AssociationCreate

Overview

## ðï¸AssociationDelete

Overview

## ðï¸AssociationUpdate

Overview

## ðï¸CampaignStatusUpdate

Called whenever a campaign status is updated

## ðï¸ContactCreate

Called whenever a contact is created

## ðï¸ContactUpdate

Called whenever the specific fields in contact is updated

## ðï¸ContactDelete

Called whenever a contact is deleted

## ðï¸ContactUpdate

Called whenever the specific fields in contact is updated

## ðï¸ContactDndUpdate

Called whenever a contact's dnd field is updated

## ðï¸ContactTagUpdate

Called whenever a contact's tag field is updated

## ðï¸ConversationUnreadWebhook

Called whenever a conversations unread status is updated

## ðï¸ConversationUpdate

Called whenever a live chat conversation is merged into another conversation due to contact identification (e.g. a visitor provides their email or phone number matching an existing contact).

## ðï¸ExternalAuthConnected

Called whenever external authentication (OAuth2 or Basic) is connected successfully for an app/location/company.

## ðï¸SupportTicketCreate

Called whenever a new support ticket is created for an app.

## ðï¸SupportTicketUpdate

Called whenever a support ticket is updated â for example when its status changes, a reply is added to the conversation, or its details are edited.

## ðï¸SupportTicketDelete

Called whenever a support ticket is deleted.

## ðï¸InboundMessage

Called whenever a contact sends a message to the user.

## ðï¸InvoiceCreate

Called whenever an invoice is created

## ðï¸InvoiceDelete

Called whenever an invoice is deleted

## ðï¸InvoicePaid

Called whenever an invoice is paid

## ðï¸InvoicePartiallyPaid

Called whenever an invoice is partially paid

## ðï¸InvoiceSent

Called whenever an invoice is sent

## ðï¸InvoiceUpdate

Called whenever an invoice is updated

## ðï¸InvoiceVoid

Called whenever an invoice is marked as void

## ðï¸KnowledgeBaseCreate

Called whenever a knowledge base is created

## ðï¸KnowledgeBaseUpdate

Called whenever a knowledge base name/description is updated

## ðï¸KnowledgeBaseDelete

Called whenever a knowledge base is deleted

## ðï¸KnowledgeBaseFileChange

Called whenever a knowledge base file asset is created, updated or deleted

## ðï¸KnowledgeBaseFaqChange

Called whenever a knowledge base FAQ asset is created, updated or deleted

## ðï¸KnowledgeBaseRichTextChange

Called whenever a knowledge base rich text asset is created, updated or deleted

## ðï¸KnowledgeBaseTableFileChange

Called whenever a knowledge base table file asset is created, updated or deleted

## ðï¸KnowledgeBaseTrainedUrlChange

Called whenever a knowledge base trained URL asset is created, updated or deleted

## ðï¸LCEmailStats

Called whenever an email is sent, gives the statistics of the said email.

## ðï¸LocationCreate

Called whenever a location is created.

## ðï¸LocationUpdate

Called whenever a location is updated.

## ðï¸NoteCreate

Called whenever a note is created

## ðï¸NoteDelete

Called whenever a note is deleted

## ðï¸NoteUpdate

Called whenever a note is updated

## ðï¸ObjectSchemaCreate

Overview

## ðï¸ObjectSchemaUpdate

Overview

## ðï¸OpportunityAssignedToUpdate

Called whenever an opportunity's AssignedTo field is updated

## ðï¸OpportunityCreate

Called whenever an opportunity is created

## ðï¸OpportunityDelete

Called whenever an opportunity is deleted

## ðï¸OpportunityMonetaryValueUpdate

Called whenever an opportunity's monetary value field is updated

## ðï¸OpportunityStageUpdate

Called whenever an opportunity's stage field is updated

## ðï¸OpportunityStatusUpdate

Called whenever an opportunity's status field is updated

## ðï¸OpportunityUpdate

Called whenever an opportunity is updated

## ðï¸OrderCreate

Called whenever an order is created

## ðï¸OrderStatusUpdate

Called whenever an order's status field updated

## ðï¸OutboundMessage

Called whenever a user sends a message to a contact.

## ðï¸PlanChange

Called whenever user changes the plan for a paid app.

## ðï¸PriceCreate

Called whenever a price is created

## ðï¸PriceDelete

Called whenever a price is deleted

## ðï¸PriceUpdate

Called whenever a price is updated

## ðï¸ProductCreate

Called whenever a product is created

## ðï¸ProductDelete

Called whenever a product is deleted

## ðï¸ProductUpdate

Called whenever a product is updated

## ðï¸ProviderOutboundMessage

Called whenever a user sends a message to a contact and has a custom provider as the default channel in the settings.

## ðï¸RecordCreate

Overview

## ðï¸RecordDelete

Overview

## ðï¸RecordUpdate

Overview

## ðï¸RelationCreate

Overview

## ðï¸RelationDelete

Overview

## ðï¸SaaSPlanCreate

Overview

## ðï¸TaskComplete

Called whenever a task is completed

## ðï¸TaskCreate

Called whenever a task is created

## ðï¸TaskDelete

Called whenever a task is deleted

## ðï¸UserCreate

Called whenever a user is created

## ðï¸VoiceAiCallEnd

Called whenever a Voice AI call ends for a sub-account.

## ðï¸UserDelete

Called whenever a user is deleted

## ðï¸UserUpdate

Called whenever a user is updated


================================================================================

# Ad Manager API
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/ad-manager-api`
---

# Ad Manager API

Documentation for Ad-publishing API

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# Facebook Reporting
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/facebook-reporting`
---

Documentation for Ad-publishing API

## ðï¸Get reporting data

Retrieve aggregated Facebook ad reporting metrics for a location

## ðï¸Get campaign reporting

Retrieve reporting metrics for a specific Facebook campaign

## ðï¸Get reporting list

Retrieve a list of Facebook campaigns, adsets, or ads with reporting data


================================================================================

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


================================================================================

# Handling Access Tokens for Apps with Target User: Sub-Account
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/TargetUserSubAccount`
---

This document explains how to manage Access Tokens when your appâs Target User is set to Sub-Account.

## Installation Optionsâ

When you set the target user to Sub-Account during app creation, you can configure who can install the app. The type of token generated depends on the option chosen and who installs the app.

## Who can install the APP: Agency Onlyâ

* The app will be visible only to Agency Admins/Owners.
* Only Agency Admin/Owner can install the app.

#### Installation Flowâ

* Install the app on your account.
* After installation, the redirect URL will be triggered and an authorization code will be shared.
* Use this code to exchange for an Access Token via the Get Access Token API.

â ï¸ Note: The Access Token generated here will be of type Company (Agency-level).

#### Sample Requestâ

```bash
curl --request POST   --url https://services.leadconnectorhq.com/oauth/token   --header 'Accept: application/json'   --header 'Content-Type: application/x-www-form-urlencoded'   --data-urlencode client_id=68a32958b5154ca8bbdc4d40-meh5chaj   --data-urlencode client_secret=a5949eb7-4d46-4bfd-95c1-e338d4952e6b   --data-urlencode grant_type=authorization_code   --data-urlencode code=059ff0439402599b0ecb45388a9d4b9fc2d17123   --data-urlencode user_type=Company
```

```bash
curl --request POST   --url https://services.leadconnectorhq.com/oauth/token   --header 'Accept: application/json'   --header 'Content-Type: application/x-www-form-urlencoded'   --data-urlencode client_id=68a32958b5154ca8bbdc4d40-meh5chaj   --data-urlencode client_secret=a5949eb7-4d46-4bfd-95c1-e338d4952e6b   --data-urlencode grant_type=authorization_code   --data-urlencode code=059ff0439402599b0ecb45388a9d4b9fc2d17123   --data-urlencode user_type=Company
```

#### Sample Responseâ

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "scope": "businesses.readonly",  "refreshTokenId": "68a32a7fb5154c26d5dd218c",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "scope": "businesses.readonly",  "refreshTokenId": "68a32a7fb5154c26d5dd218c",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```

* To access Sub-Accountâspecific API endpoints, the Agency-level Access Token must first be exchanged for a Sub-Account (Location-level) Access Token. This exchange can be performed using the Get Location Access Token from Agency Token API.

Note: You can configure a webhook URL for your app, and the App Install event will automatically be subscribed by default.

When the APP is installed this event will be triggered, this webhook provides details such as the locationId where the app has been installed. You can use the locationId along with your Agency-level Access Token to exchange it for a Sub-Account (Location-level) Access Token.

#### Sample App Install Event Payloadâ

```json
{  "type": "INSTALL",  "appId": "665c6bb13d4e5364bdec0e2f",  "versionId": "665c6bb13d4e5364bdec0e2f",  "installType": "Location",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "companyName": "Marketplace and Integrations Prod Agency",  "isWhitelabelCompany": true,  "whitelabelDetails": {    "logoUrl": "https://...gif",    "domain": "rajender.dentistsnear.me"  },  "timestamp": "2025-06-25T06:57:06.225Z",  "webhookId": "1a533f85-1f1e-4886-891e-ee0cf4666e90"}
```

```json
{  "type": "INSTALL",  "appId": "665c6bb13d4e5364bdec0e2f",  "versionId": "665c6bb13d4e5364bdec0e2f",  "installType": "Location",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "companyName": "Marketplace and Integrations Prod Agency",  "isWhitelabelCompany": true,  "whitelabelDetails": {    "logoUrl": "https://...gif",    "domain": "rajender.dentistsnear.me"  },  "timestamp": "2025-06-25T06:57:06.225Z",  "webhookId": "1a533f85-1f1e-4886-891e-ee0cf4666e90"}
```

#### Sample Request for Get Location Access Token from Agency Tokenâ

```json
curl -L 'https://services.leadconnectorhq.com/oauth/locationToken'   -H 'Content-Type: application/x-www-form-urlencoded'   -H 'Accept: application/json'   -H 'Version: 2021-07-28'   -H 'Authorization: Bearer {AGENCY_ACCESS_TOKEN}'   -d 'companyId=GNb7aIv4rQFVb9iwNl5K'   -d 'locationId=HjiMUOsCCHCjtxzEf8PR'
```

```json
curl -L 'https://services.leadconnectorhq.com/oauth/locationToken'   -H 'Content-Type: application/x-www-form-urlencoded'   -H 'Accept: application/json'   -H 'Version: 2021-07-28'   -H 'Authorization: Bearer {AGENCY_ACCESS_TOKEN}'   -d 'companyId=GNb7aIv4rQFVb9iwNl5K'   -d 'locationId=HjiMUOsCCHCjtxzEf8PR'
```

#### Sample Responseâ

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2OGEzMmRhNjlkN2EzY2E5NT",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2NhdGlvbiIsImF",  "scope": "businesses.readonly oauth.write oauth.readonly",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "traceId": "8cf33664-9f4f-4392-adf6-71b8bed2592a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2OGEzMmRhNjlkN2EzY2E5NT",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2NhdGlvbiIsImF",  "scope": "businesses.readonly oauth.write oauth.readonly",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "traceId": "8cf33664-9f4f-4392-adf6-71b8bed2592a"}
```

## Who can install the APP: Everyoneâ

This type of app can be installed by both Agency users and Sub-Account users. The type of Access Token generated will depend on who performs the installation.

### Scenario 1: Agency User installs the appâ

In this case, the Access Token generated will be of type Company (Agency-level). To access Sub-Account resources, you must exchange this token for a Location-level token using the Get Location Access Token from Agency Token API endpoint.

#### Installation Flowâ

* Install the app on your account.
* After installation, the redirect URL will be triggered and an authorization code will be shared.
* Use this code to exchange for an Access Token via the Get Access Token API.

â ï¸ Note: The Access Token generated here will be of type Company (Agency-level).

#### Sample Requestâ

```bash
curl --request POST   --url https://services.leadconnectorhq.com/oauth/token   --header 'Accept: application/json'   --header 'Content-Type: application/x-www-form-urlencoded'   --data-urlencode client_id=68a32958b5154ca8bbdc4d40-meh5chaj   --data-urlencode client_secret=a5949eb7-4d46-4bfd-95c1-e338d4952e6b   --data-urlencode grant_type=authorization_code   --data-urlencode code=059ff0439402599b0ecb45388a9d4b9fc2d17123   --data-urlencode user_type=Company
```

```bash
curl --request POST   --url https://services.leadconnectorhq.com/oauth/token   --header 'Accept: application/json'   --header 'Content-Type: application/x-www-form-urlencoded'   --data-urlencode client_id=68a32958b5154ca8bbdc4d40-meh5chaj   --data-urlencode client_secret=a5949eb7-4d46-4bfd-95c1-e338d4952e6b   --data-urlencode grant_type=authorization_code   --data-urlencode code=059ff0439402599b0ecb45388a9d4b9fc2d17123   --data-urlencode user_type=Company
```

#### Sample Responseâ

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "scope": "businesses.readonly",  "refreshTokenId": "68a32a7fb5154c26d5dd218c",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  "scope": "businesses.readonly",  "refreshTokenId": "68a32a7fb5154c26d5dd218c",  "userType": "Company",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "isBulkInstallation": true,  "userId": "Rg6BRRiHh7dS9gJy3W8a"}
```

* To access Sub-Accountâspecific API endpoints, the Agency-level Access Token must first be exchanged for a Sub-Account (Location-level) Access Token. This exchange can be performed using the Get Location Access Token from Agency Token API.

Note: You can configure a webhook URL for your app, and the App Install event will automatically be subscribed by default.

When the APP is installed this event will be triggered, this webhook provides details such as the locationId where the app has been installed. You can use the locationId along with your Agency-level Access Token to exchange it for a Sub-Account (Location-level) Access Token.

#### Sample App Install Event Payloadâ

```json
{  "type": "INSTALL",  "appId": "665c6bb13d4e5364bdec0e2f",  "versionId": "665c6bb13d4e5364bdec0e2f",  "installType": "Location",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "companyName": "Marketplace and Integrations Prod Agency",  "isWhitelabelCompany": true,  "whitelabelDetails": {    "logoUrl": "https://...gif",    "domain": "rajender.dentistsnear.me"  },  "timestamp": "2025-06-25T06:57:06.225Z",  "webhookId": "1a533f85-1f1e-4886-891e-ee0cf4666e90"}
```

```json
{  "type": "INSTALL",  "appId": "665c6bb13d4e5364bdec0e2f",  "versionId": "665c6bb13d4e5364bdec0e2f",  "installType": "Location",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "companyName": "Marketplace and Integrations Prod Agency",  "isWhitelabelCompany": true,  "whitelabelDetails": {    "logoUrl": "https://...gif",    "domain": "rajender.dentistsnear.me"  },  "timestamp": "2025-06-25T06:57:06.225Z",  "webhookId": "1a533f85-1f1e-4886-891e-ee0cf4666e90"}
```

#### Sample Request for Get Location Access Token from Agency Tokenâ

```json
curl -L 'https://services.leadconnectorhq.com/oauth/locationToken'   -H 'Content-Type: application/x-www-form-urlencoded'   -H 'Accept: application/json'   -H 'Version: 2021-07-28'   -H 'Authorization: Bearer {AGENCY_ACCESS_TOKEN}'   -d 'companyId=GNb7aIv4rQFVb9iwNl5K'   -d 'locationId=HjiMUOsCCHCjtxzEf8PR'
```

```json
curl -L 'https://services.leadconnectorhq.com/oauth/locationToken'   -H 'Content-Type: application/x-www-form-urlencoded'   -H 'Accept: application/json'   -H 'Version: 2021-07-28'   -H 'Authorization: Bearer {AGENCY_ACCESS_TOKEN}'   -d 'companyId=GNb7aIv4rQFVb9iwNl5K'   -d 'locationId=HjiMUOsCCHCjtxzEf8PR'
```

#### Sample Responseâ

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2OGEzMmRhNjlkN2EzY2E5NT",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2NhdGlvbiIsImF",  "scope": "businesses.readonly oauth.write oauth.readonly",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "traceId": "8cf33664-9f4f-4392-adf6-71b8bed2592a"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2OGEzMmRhNjlkN2EzY2E5NT",  "token_type": "Bearer",  "expires_in": 86400,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2NhdGlvbiIsImF",  "scope": "businesses.readonly oauth.write oauth.readonly",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "userId": "Rg6BRRiHh7dS9gJy3W8a",  "traceId": "8cf33664-9f4f-4392-adf6-71b8bed2592a"}
```

### Scenario 2: Sub-Account User installs the appâ

In this case, the Access Token generated will be of type Location (Sub-Account level).

#### Installation Flowâ

* Install the app on your account.
* After installation, the redirect URL will be triggered and an authorization code will be shared.
* Use this code to exchange for an Access Token via the Get Access Token API.

#### Sample Requestâ

```bash
curl --request POST \  --url https://services.leadconnectorhq.com/oauth/token \  --header 'Accept: application/json' \  --header 'Content-Type: application/x-www-form-urlencoded' \  --data-urlencode client_id=68a42f3c2a64bb65c985c618-mei99elp \  --data-urlencode client_secret=86f9901c-b57d-4395-a406-ff178cd8a57d \  --data-urlencode grant_type=authorization_code \  --data-urlencode code=4a1a74401abd1b46d923543c4a366eb3f21b5cbf \  --data-urlencode user_type=Location
```

```bash
curl --request POST \  --url https://services.leadconnectorhq.com/oauth/token \  --header 'Accept: application/json' \  --header 'Content-Type: application/x-www-form-urlencoded' \  --data-urlencode client_id=68a42f3c2a64bb65c985c618-mei99elp \  --data-urlencode client_secret=86f9901c-b57d-4395-a406-ff178cd8a57d \  --data-urlencode grant_type=authorization_code \  --data-urlencode code=4a1a74401abd1b46d923543c4a366eb3f21b5cbf \  --data-urlencode user_type=Location
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2NhdGlvbiIsImF1dGhDbGFzc0lkIjoiSGppTVVPc0NDSENqdHh6RWY4UFIiLCJzb3VyY2UiOiJJTl",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2N",  "scope": "businesses.readonly",  "refreshTokenId": "68a4332c2a64bbc7a1888971",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "isBulkInstallation": false,  "userId": "57n5nmVqHA1ghBM8UKhU"}
```

```json
{  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2NhdGlvbiIsImF1dGhDbGFzc0lkIjoiSGppTVVPc0NDSENqdHh6RWY4UFIiLCJzb3VyY2UiOiJJTl",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2N",  "scope": "businesses.readonly",  "refreshTokenId": "68a4332c2a64bbc7a1888971",  "userType": "Location",  "companyId": "GNb7aIv4rQFVb9iwNl5K",  "locationId": "HjiMUOsCCHCjtxzEf8PR",  "isBulkInstallation": false,  "userId": "57n5nmVqHA1ghBM8UKhU"}
```

## Summaryâ

* Agency-only installation: If âWho can install the appâ is set to Agency only, the generated token will be of type Company (Agency-level). To run APIs and perform actions at the Sub-Account level, this token must be exchanged for a Location-level token.
* Everyone installation:  If âWho can install the appâ is set to Everyone, there are two possible scenarios:

Agency User Installs the APP â The generated token will be of type Company (Agency-level). To run APIs and perform actions at the Sub-Account level, this token must be exchanged for a Location-level token.
Sub-Account User Installs the APP â The generated token will be of type Location. This token can be used directly to call APIs and perform tasks without further exchange.
* Agency User Installs the APP â The generated token will be of type Company (Agency-level). To run APIs and perform actions at the Sub-Account level, this token must be exchanged for a Location-level token.
* Sub-Account User Installs the APP â The generated token will be of type Location. This token can be used directly to call APIs and perform tasks without further exchange.

* Agency User Installs the APP â The generated token will be of type Company (Agency-level). To run APIs and perform actions at the Sub-Account level, this token must be exchanged for a Location-level token.
* Sub-Account User Installs the APP â The generated token will be of type Location. This token can be used directly to call APIs and perform tasks without further exchange.


================================================================================

# Facebook Integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/facebook-integration`
---

Documentation for Ad-publishing API

## ðï¸Get current Facebook user

Retrieve the authenticated Facebook user profile for a location

## ðï¸Get Facebook pages

Retrieve Facebook pages for the connected account. Without `limit` the response is an array of pages (this array response will soon be deprecated â migrate to the paginated form). When `limit` is provided the response is a paginated `{ pages, paging }` envelope; pass `after` (from `paging.next`) to fetch the next batch.

## ðï¸Get Instagram accounts for page

Retrieve Instagram accounts linked to a specific Facebook page

## ðï¸Get page lead forms

Retrieve lead gen forms for a specific Facebook page (published + drafts), sorted newest-first by `createdTime`. By default each form is returned in full (including its `questions`) as a plain array; pass `projection` (comma-separated) to return only the requested fields â any value outside the known field set is rejected. Pass `limit` (max 100) for a `{ forms, paging }` envelope; use `after` (from `paging.next`) to fetch the next batch.

## ðï¸Create page lead form

Create a new lead gen form on a Facebook page

## ðï¸Get ad accounts

Retrieve Facebook ad accounts available for the connected user

## ðï¸Get ad account details

Retrieve details of a specific Facebook ad account

## ðï¸Delete ad account

Remove a Facebook ad account connection from a location

## ðï¸Get conversation forms

Retrieve Facebook conversation lead forms for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100) the response is a paginated `{ conversationForms, paging }` envelope; pass `after` (from `paging.next`) to fetch the next batch.

## ðï¸Create conversation form

Create a new Facebook conversation lead form

## ðï¸Create Facebook integration

Create a Facebook ad integration for a location with page and ad account

## ðï¸Get Facebook integration

Retrieve the Facebook ad integration details for a location

## ðï¸Delete Facebook integration

Remove the Facebook ad integration from a location

## ðï¸Delete page connection

Remove a Facebook page connection from a location

## ðï¸Set default page

Set the default Facebook page for a location

## ðï¸Get lead form by ID

Retrieve a specific Facebook lead form by its ID


================================================================================

# **Scopes**
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/Authorization/Scopes`
---

Here is a list of the scopes you require to access the API Endpoints and Webhook Events.


================================================================================

# Create conversation form
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-create-conversation-form`
---

# Create conversation form

## /ad-publishing/facebook/conversation-forms

Create a new Facebook conversation lead form

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Conversation form name

Welcome message text

Quick-reply questions shown in the welcome message of the conversation form

```json
{  "locationId": "loc_abc123",  "name": "Welcome Form",  "text": "Hi! How can we help?",  "questions": [    {      "question": "How can we help?",      "response": "Thanks for reaching out! A team member will assist you shortly."    },    {      "question": "I want to learn more",      "response": "Great! Here is a link to our services."    }  ]}
```

```json
{  "locationId": "loc_abc123",  "name": "Welcome Form",  "text": "Hi! How can we help?",  "questions": [    {      "question": "How can we help?",      "response": "Thanks for reaching out! A team member will assist you shortly."    },    {      "question": "I want to learn more",      "response": "Great! Here is a link to our services."    }  ]}
```


================================================================================

# Add custom audience member
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-add-custom-audience-member`
---

# Add custom audience member

## /ad-publishing/facebook/custom-audience/:audienceId/member

Add a member to a Facebook custom audience

## Requestâ

API VersionAvailable options2021-04-15

Custom audience identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Contact identifier

Facebook ad account ID

```json
{  "locationId": "loc_abc123",  "contactId": "contact_123",  "fbAdAccountId": "act_123456"}
```

```json
{  "locationId": "loc_abc123",  "contactId": "contact_123",  "fbAdAccountId": "act_123456"}
```


================================================================================

# Batch update audience members
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-batch-update-audience-members`
---

# Batch update audience members

## /ad-publishing/facebook/custom-audience/:audienceId/member/batch

Add or remove members in bulk from a Facebook custom audience via CSV or smart lists

## Requestâ

API VersionAvailable options2021-04-15

Custom audience identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

CSV file path

Batch operation typeAvailable optionsADDREMOVEREPLACE

Smartlist IDs array

Dynamic audience flag

```json
{  "locationId": "loc_abc123",  "csvPath": "/uploads/audience.csv",  "operationType": "ADD",  "smartlistIds": [    "list_1",    "list_2"  ],  "dynamicAudience": "true"}
```

```json
{  "locationId": "loc_abc123",  "csvPath": "/uploads/audience.csv",  "operationType": "ADD",  "smartlistIds": [    "list_1",    "list_2"  ],  "dynamicAudience": "true"}
```


================================================================================

# Create Facebook integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-create-integration`
---

# Create Facebook integration

## /ad-publishing/facebook/integration

Create a Facebook ad integration for a location with page and ad account

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Facebook page ID

Ad account identifier

```json
{  "locationId": "loc_abc123",  "pageId": "123456789",  "adAccountId": "act_123456"}
```

```json
{  "locationId": "loc_abc123",  "pageId": "123456789",  "adAccountId": "act_123456"}
```


================================================================================

# Delete ad account
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-delete-ad-account`
---

# Delete ad account

## /ad-publishing/facebook/ad-accounts/:adAccountId

Remove a Facebook ad account connection from a location

## Requestâ

API VersionAvailable options2021-04-15

Ad account identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Delete custom audience
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-delete-custom-audience`
---

# Delete custom audience

## /ad-publishing/facebook/custom-audience/:audienceId

Delete a Facebook custom audience by ID

## Requestâ

API VersionAvailable options2021-04-15

Custom audience identifier

Location identifier


================================================================================

# Delete ad
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-delete-ad`
---

# Delete ad

## /ad-publishing/facebook/ads/:adId

Delete a Facebook ad by ID

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Duplicate ad
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-duplicate-ad`
---

# Duplicate ad

## /ad-publishing/facebook/ads/:adId/duplicate

Duplicate an existing Facebook ad

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Delete page connection
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-delete-page`
---

# Delete page connection

## /ad-publishing/facebook/page

Remove a Facebook page connection from a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Facebook page ID


================================================================================

# Get ad account details
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-ad-account`
---

# Get ad account details

## /ad-publishing/facebook/ad-accounts/:adAccountId

Retrieve details of a specific Facebook ad account

## Requestâ

API VersionAvailable options2021-04-15

Ad account identifier

Location identifier


================================================================================

# Duplicate ad set
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-duplicate-adset`
---

# Duplicate ad set

## /ad-publishing/facebook/adsets/:adSetId/duplicate

Duplicate an existing Facebook ad set

## Requestâ

API VersionAvailable options2021-04-15

Ad set identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Duplicate campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-duplicate-campaign`
---

# Duplicate campaign

## /ad-publishing/facebook/campaigns/:campaignId/duplicate

Duplicate an existing Facebook campaign

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Create page lead form
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-create-page-lead-form`
---

# Create page lead form

## /ad-publishing/facebook/page/:pageId/forms

Create a new lead gen form on a Facebook page

## Requestâ

API VersionAvailable options2021-04-15

Facebook page identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Lead form typeAvailable optionsMORE_VOLUMEHIGHER_INTENT

Lead form name

Location identifier

Greeting card config

List of questions displayed on the lead form. Required (non-empty) when isDraft is false or omitted; optional for drafts.

Question page headline

Privacy policy URL. Required when isDraft is false or omitted; optional for drafts.

Privacy policy text

Custom disclaimer config

Thank you page config. Required when isDraft is false or omitted; optional for drafts.

If the form is a draft, set to true

Draft form ID

Locale

```json
{  "type": "MORE_VOLUME",  "name": "Contact Form",  "locationId": "loc_abc123",  "greetingCard": {    "title": "Welcome!",    "style": "LIST_STYLE",    "content": [      "Learn more about our services"    ]  },  "questions": [    {      "key": "full_name",      "type": "FULL_NAME",      "options": []    },    {      "key": "email_address",      "type": "EMAIL",      "options": []    },    {      "key": "are_you_interested",      "label": "Are you interested?",      "type": "CUSTOM",      "options": [        {          "value": "Yes"        },        {          "value": "No"        }      ]    }  ],  "questionPageHeadline": "Tell us about yourself",  "privacyPolicyLink": "https://example.com/privacy",  "privacyPolicyText": "We respect your privacy",  "customDisclaimer": {    "title": "Terms & Conditions",    "body": "By submitting...",    "checkboxes": [      {        "isRequired": true,        "text": "I agree",        "key": "terms"      }    ]  },  "thankYouPage": {    "title": "Thank You!",    "body": "We will contact you soon",    "buttonText": "Visit Website",    "buttonType": "VIEW_WEBSITE",    "buttonLink": "https://example.com"  },  "isDraft": true,  "draftFormId": "1234567890",  "locale": "EN_US"}
```

```json
{  "type": "MORE_VOLUME",  "name": "Contact Form",  "locationId": "loc_abc123",  "greetingCard": {    "title": "Welcome!",    "style": "LIST_STYLE",    "content": [      "Learn more about our services"    ]  },  "questions": [    {      "key": "full_name",      "type": "FULL_NAME",      "options": []    },    {      "key": "email_address",      "type": "EMAIL",      "options": []    },    {      "key": "are_you_interested",      "label": "Are you interested?",      "type": "CUSTOM",      "options": [        {          "value": "Yes"        },        {          "value": "No"        }      ]    }  ],  "questionPageHeadline": "Tell us about yourself",  "privacyPolicyLink": "https://example.com/privacy",  "privacyPolicyText": "We respect your privacy",  "customDisclaimer": {    "title": "Terms & Conditions",    "body": "By submitting...",    "checkboxes": [      {        "isRequired": true,        "text": "I agree",        "key": "terms"      }    ]  },  "thankYouPage": {    "title": "Thank You!",    "body": "We will contact you soon",    "buttonText": "Visit Website",    "buttonType": "VIEW_WEBSITE",    "buttonLink": "https://example.com"  },  "isDraft": true,  "draftFormId": "1234567890",  "locale": "EN_US"}
```


================================================================================

# Delete Facebook integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-delete-integration`
---

# Delete Facebook integration

## /ad-publishing/facebook/integration

Remove the Facebook ad integration from a location

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Delete ad set
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-delete-adset`
---

# Delete ad set

## /ad-publishing/facebook/adsets/:adSetId

Delete a Facebook ad set by ID

## Requestâ

API VersionAvailable options2021-04-15

Ad set identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Delete campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-delete-campaign`
---

# Delete campaign

## /ad-publishing/facebook/campaigns/:campaignId

Delete a Facebook campaign by ID

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

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


================================================================================

# Get ad accounts
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-ad-accounts`
---

# Get ad accounts

## /ad-publishing/facebook/ad-accounts

Retrieve Facebook ad accounts available for the connected user

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Account source typeAvailable optionsINTEGRATIONAD_MANAGER

Pagination cursor

Fetch all accounts

Results page limit


================================================================================

# Get campaign reporting
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-campaign-reporting`
---

# Get campaign reporting

## /ad-publishing/facebook/reporting/campaign/:campaignId

Retrieve reporting metrics for a specific Facebook campaign

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

Location identifier

Report start date (YYYY-MM-DD)

Report end date (YYYY-MM-DD)


================================================================================

# Get campaign with linked entities
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-campaign`
---

# Get campaign with linked entities

## /ad-publishing/facebook/campaign/:campaignId

Retrieve a Facebook campaign with its linked adsets and ads

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

Location identifier

Comma-separated field names

Campaign data source


================================================================================

# Get custom audience by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-custom-audience-by-id`
---

# Get custom audience by ID

## /ad-publishing/facebook/custom-audience/:audienceId

Retrieve a specific Facebook custom audience by its ID

## Requestâ

API VersionAvailable options2021-04-15

Custom audience identifier

Location identifier


================================================================================

# Get conversation forms
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-conversation-forms`
---

# Get conversation forms

## /ad-publishing/facebook/conversation-forms

Retrieve Facebook conversation lead forms for a location. Without limit the response is a plain array. When limit is provided (max 100) the response is a paginated { conversationForms, paging } envelope; pass after (from paging.next) to fetch the next batch.

```json
{ conversationForms, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Page size for a paginated fetch (max 100). When set, the response is a { conversationForms, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of conversation forms (default), or a { conversationForms, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookConversationFormsDTO
* PaginatedFacebookConversationFormsDTO
* Array [
* ]

* object[]PaginatedFacebookConversationFormsDTO
* PaginatedFacebookConversationFormsDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Get current Facebook user
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-current-user`
---

# Get current Facebook user

## /ad-publishing/facebook/me

Retrieve the authenticated Facebook user profile for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier


================================================================================

# Get Facebook integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-integration`
---

# Get Facebook integration

## /ad-publishing/facebook/integration

Retrieve the Facebook ad integration details for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier


================================================================================

# Get entities
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-entity`
---

# Get entities

## /ad-publishing/facebook/entity

Retrieve Facebook campaigns, adsets, or ads based on entity type

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Integration source typeAvailable optionsAD_MANAGERINTEGRATION

Pagination cursor

Fetch all entities

Campaign identifier

Ad set identifier

Entity type to fetchAvailable optionsCAMPAIGNADSETAD

Search identifier

Selected ad account ID


================================================================================

# Get custom audiences
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-custom-audiences`
---

# Get custom audiences

## /ad-publishing/facebook/custom-audience

Retrieve Facebook custom audiences for a location. Without limit the response is a plain array. When limit is provided (max 100) the response is a paginated { customAudiences, paging } envelope; pass after (from paging.next) to fetch the next batch. By default each item is returned in full; pass projection (comma-separated, dot-notation for nested fields, e.g. ?projection=id,name,dataSource.type) to return only the requested fields â any value outside the known field set is rejected.

```json
{ customAudiences, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Audience list typeAvailable optionslookalikecustomall

Audience data sourceAvailable optionsad_managerintegration

Ad account identifier

Page size for a paginated fetch (max 100). When set, the response is a { customAudiences, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

Fields to return on each item, comma-separated (e.g. ?projection=id,name,dataSource.type). When set, only the requested fields are returned. Nested fields use dot-notation; naming a parent (e.g. dataSource) returns the whole nested object. Any value outside the known field set is rejected. Omit the param entirely to receive the full item as-is.Available optionsidnamedescriptionapproximateCountLowerBoundapproximateCountUpperBoundsubtypetimeCreatedtimeUpdateddataSourcedataSource.typedataSource.subTypedataSource.creationParams

A plain array of custom audiences (default), or a { customAudiences, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookCustomAudiencesDTO
* PaginatedFacebookCustomAudiencesDTO
* Array [
* ]

* object[]PaginatedFacebookCustomAudiencesDTO
* PaginatedFacebookCustomAudiencesDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Get lead form by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-lead-form`
---

# Get lead form by ID

## /ad-publishing/facebook/lead-form/:leadFormId

Retrieve a specific Facebook lead form by its ID

## Requestâ

API VersionAvailable options2021-04-15

Lead form identifier

Location identifier

Fetch the unpublished draft of this lead form instead of the published form


================================================================================

# Get Facebook pages
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-pages`
---

# Get Facebook pages

## /ad-publishing/facebook/pages

Retrieve Facebook pages for the connected account. Without limit the response is an array of pages (this array response will soon be deprecated â migrate to the paginated form). When limit is provided the response is a paginated { pages, paging } envelope; pass after (from paging.next) to fetch the next batch.

```json
{ pages, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Fetch existing pages flag

Page size for a paginated fetch (fetchExisting only, max 50). When set, the response is a { pages, paging } envelope instead of an array.

Opaque cursor for the next batch, taken from the previous response paging.next

An array of pages (default; will soon be deprecated â use limit to get the paginated { pages, paging } response), or a { pages, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookPagesDTO
* PaginatedFacebookPagesDTO
* Array [
* ]

* object[]PaginatedFacebookPagesDTO
* PaginatedFacebookPagesDTO

Facebook Page ID

Page name

Page category

Page profile picture URL

When the page was connected to the location

Whether the page is already connected to the location

Whether the Facebook Lead Ads TOS is accepted for the page

Whether this is the default connected page (only present when fetchExisting is false)

```json
[  {    "id": "1234567890",    "name": "Acme Marketing",    "category": "Marketing Agency",    "picture": "https://scontent.xx.fbcdn.net/...",    "createdOn": "2026-01-15T10:00:00.000Z",    "isConnected": false,    "tosAccepted": true,    "isDefault": false  }]
```

```json
[  {    "id": "1234567890",    "name": "Acme Marketing",    "category": "Marketing Agency",    "picture": "https://scontent.xx.fbcdn.net/...",    "createdOn": "2026-01-15T10:00:00.000Z",    "isConnected": false,    "tosAccepted": true,    "isDefault": false  }]
```


================================================================================

# Get reporting data
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-reporting`
---

# Get reporting data

## /ad-publishing/facebook/reporting

Retrieve aggregated Facebook ad reporting metrics for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Reporting fields. Pass as comma-separated values on the wire (e.g. ?fields=impressions,clicks).Available optionsimpressionsclicksspendcpccost_per_conversionconversionsresultscost_per_resultcpmreachfrequencyctr

Time grouping intervalAvailable optionsdayweekmonth

Report start date (YYYY-MM-DD)

Report end date (YYYY-MM-DD)

Integration source typeAvailable optionsAD_MANAGERINTEGRATION


================================================================================

# Get Instagram accounts for page
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-instagram-accounts`
---

# Get Instagram accounts for page

## /ad-publishing/facebook/page/:pageId/instagram

Retrieve Instagram accounts linked to a specific Facebook page

## Requestâ

API VersionAvailable options2021-04-15

Facebook page identifier

Location identifier

Integration typeAvailable optionsINTEGRATIONAD_MANAGER


================================================================================

# Get conversion pixels
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-pixels`
---

# Get conversion pixels

## /ad-publishing/facebook/pixels

Retrieve Facebook conversion pixels for a location. For the FACEBOOK channel, without limit the response is { items, total }; when limit is provided (max 100) the response is a paginated { items, paging } envelope â pass after (from paging.next) to fetch the next batch. By default each item is returned in full; pass projection (comma-separated) to return only the requested fields, chosen from createdAt, fbIsCrmPixel, fbPixelCode, fbPixelId, name, type (any other value is rejected).

```json
{ items, total }
```

```json
{ items, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Channel typeAvailable optionsIGFACEBOOK

Facebook page ID

Instagram user ID

Page size for a paginated fetch (max 100, FACEBOOK channel only). When set, the response is a { items, paging } envelope instead of { items, total }.

Opaque cursor for the next batch, taken from the previous response paging.next

Fields to return on each item, comma-separated (e.g. ?projection=name,fbPixelId). When set, only the requested fields are returned. Selectable fields: createdAt, fbIsCrmPixel, fbPixelCode, fbPixelId, name, type â any other value is rejected. Omit the param entirely to receive the full item as-is.Available optionscreatedAtfbIsCrmPixelfbPixelCodefbPixelIdnametype

An { items, total } object (default), or an { items, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* objectPaginatedFacebookPixelsDTO
* PaginatedFacebookPixelsDTO

* objectPaginatedFacebookPixelsDTO
* PaginatedFacebookPixelsDTO

```json
{}
```

```json
{}
```


================================================================================

# Get page lead forms
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-page-lead-forms`
---

# Get page lead forms

## /ad-publishing/facebook/page/:pageId/forms

Retrieve lead gen forms for a specific Facebook page (published + drafts), sorted newest-first by createdTime. By default each form is returned in full (including its questions) as a plain array; pass projection (comma-separated) to return only the requested fields â any value outside the known field set is rejected. Pass limit (max 100) for a { forms, paging } envelope; use after (from paging.next) to fetch the next batch.

```json
{ forms, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Facebook page identifier

Location identifier

Fields to return on each lead form, comma-separated (e.g. ?projection=name,id,pageId,status,isDraft,createdTime). When set, only the requested fields are returned; any other value is rejected. Omit to receive the full form (including questions) as-is.Available optionsidnamepageIdstatusisDraftcreatedTimelocalepagequestions

Page size for a paginated fetch (max 100). When set, the response is a { forms, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of lead forms (default), or a { forms, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedFacebookLeadFormsDTO
* PaginatedFacebookLeadFormsDTO
* Array [
* ]

* object[]PaginatedFacebookLeadFormsDTO
* PaginatedFacebookLeadFormsDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Pause ad set
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-pause-adset`
---

# Pause ad set

## /ad-publishing/facebook/adsets/:adSetId/pause

Pause a running Facebook ad set

## Requestâ

API VersionAvailable options2021-04-15

Ad set identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Pause ad
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-pause-ad`
---

# Pause ad

## /ad-publishing/facebook/ads/:adId/pause

Pause a running Facebook ad

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Get reporting list
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-get-reporting-list`
---

# Get reporting list

## /ad-publishing/facebook/reporting/list

Retrieve a list of Facebook campaigns, adsets, or ads with reporting data

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Reporting list typeAvailable optionsadsadsetscampaignsnone

Report start date (YYYY-MM-DD)

Report end date (YYYY-MM-DD)

Campaign identifier (required when listType is adsets or ads)

Integration source typeAvailable optionsAD_MANAGERINTEGRATION


================================================================================

# Remove custom audience member
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-remove-custom-audience-member`
---

# Remove custom audience member

## /ad-publishing/facebook/custom-audience/:audienceId/member

Remove a member from a Facebook custom audience

## Requestâ

API VersionAvailable options2021-04-15

Custom audience identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Contact identifier

Facebook ad account ID

```json
{  "locationId": "loc_abc123",  "contactId": "contact_123",  "fbAdAccountId": "act_123456"}
```

```json
{  "locationId": "loc_abc123",  "contactId": "contact_123",  "fbAdAccountId": "act_123456"}
```


================================================================================

# Pause campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-pause-campaign`
---

# Pause campaign

## /ad-publishing/facebook/campaigns/:campaignId/pause

Pause a running Facebook campaign

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Resume ad
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-resume-ad`
---

# Resume ad

## /ad-publishing/facebook/ads/:adId/resume

Resume a paused Facebook ad

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Resume ad set
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-resume-adset`
---

# Resume ad set

## /ad-publishing/facebook/adsets/:adSetId/resume

Resume a paused Facebook ad set

## Requestâ

API VersionAvailable options2021-04-15

Ad set identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Resume campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-resume-campaign`
---

# Resume campaign

## /ad-publishing/facebook/campaigns/:campaignId/resume

Resume a paused Facebook campaign

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Upsert adset
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-upsert-adset`
---

# Upsert adset

## /ad-publishing/facebook/adsets

Create or update a Facebook ad set

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Ad set identifier

Location identifier

Ad set name

Facebook page ID

Instagram actor ID

Messaging platformsAvailable optionsWHATSAPPMESSENGERINSTAGRAM_DIRECT

WhatsApp phone number

Targeting audience configuration including geo-locations, locales, placements, and custom audiences

Ad set budget config

Where the conversion happens. Valid values depend on the parent campaign objective â OUTCOME_LEADS: on_ad (instant form), website, website_and_lead_form; OUTCOME_SALES: website (pixel), messaging. Not validated server-side, so values outside this set are forwarded to Facebook and may be rejected there.

Facebook standard event optimised for. Only meaningful when conversionLocation is website (requires pixelId). Valid values depend on the parent campaign objective â OUTCOME_LEADS: COMPLETE_REGISTRATION, CONTACT, CONTENT_VIEW, FIND_LOCATION, LEAD, SCHEDULE, SEARCH, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE; OUTCOME_SALES: ADD_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, COMPLETE_REGISTRATION, CONTENT_VIEW, DONATE, INITIATED_CHECKOUT, PURCHASE, SEARCH, START_TRIAL, SUBSCRIBE. Not validated server-side, so values outside this set are forwarded to Facebook and may be rejected there.

Conversion pixel ID

Parent campaign ID

```json
{  "id": "adset_123",  "locationId": "loc_abc123",  "name": "Targeting Group A",  "pageId": "123456789",  "instagramActorId": "ig_123",  "messagingPlatforms": [    "WHATSAPP"  ],  "whatsappNumber": "+1234567890",  "audience": {    "geoLocations": [      {        "key": "US",        "name": "United States",        "type": "country",        "selectionType": "include"      }    ],    "ageMin": 18,    "ageMax": 65,    "genders": [      1,      2    ]  },  "budget": {    "budgetType": "DAILY",    "amount": 1000,    "scheduleStartDate": "2024-01-01",    "scheduleEndDate": "2024-01-31"  },  "conversionLocation": "website",  "customEventType": "PURCHASE",  "pixelId": "px_123",  "campaignId": "camp_123"}
```

```json
{  "id": "adset_123",  "locationId": "loc_abc123",  "name": "Targeting Group A",  "pageId": "123456789",  "instagramActorId": "ig_123",  "messagingPlatforms": [    "WHATSAPP"  ],  "whatsappNumber": "+1234567890",  "audience": {    "geoLocations": [      {        "key": "US",        "name": "United States",        "type": "country",        "selectionType": "include"      }    ],    "ageMin": 18,    "ageMax": 65,    "genders": [      1,      2    ]  },  "budget": {    "budgetType": "DAILY",    "amount": 1000,    "scheduleStartDate": "2024-01-01",    "scheduleEndDate": "2024-01-31"  },  "conversionLocation": "website",  "customEventType": "PURCHASE",  "pixelId": "px_123",  "campaignId": "camp_123"}
```


================================================================================

# Publish campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-publish-campaign`
---

# Publish campaign

## /ad-publishing/facebook/campaigns/:campaignId/publish

Publish a Facebook campaign and push it live to Facebook

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "loc_abc123"}
```

```json
{  "locationId": "loc_abc123"}
```


================================================================================

# Set default page
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-set-default-page`
---

# Set default page

## /ad-publishing/facebook/page/default

Set the default Facebook page for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Facebook page identifier

```json
{  "pageId": "103456789012345"}
```

```json
{  "pageId": "103456789012345"}
```


================================================================================

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


================================================================================

# Upsert campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-upsert-campaign`
---

# Upsert campaign

## /ad-publishing/facebook/campaigns

Create or update a Facebook campaign

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Campaign identifier

Location identifier

Campaign name

Campaign objectiveAvailable optionsOUTCOME_LEADSOUTCOME_TRAFFICOUTCOME_ENGAGEMENTOUTCOME_SALES

Special ad categoriesAvailable optionsEMPLOYMENTCREDITFINANCIAL_PRODUCTS_SERVICESHOUSINGISSUES_ELECTIONS_POLITICSONLINE_GAMBLING_AND_GAMINGNONE

Campaign data source

User-provided overrides for custom_values merge tags used in ad copy

```json
{  "id": "camp_123",  "locationId": "loc_abc123",  "name": "Summer Campaign",  "objective": "OUTCOME_LEADS",  "specialAdCategories": [    "NONE"  ],  "source": "facebook",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```

```json
{  "id": "camp_123",  "locationId": "loc_abc123",  "name": "Summer Campaign",  "objective": "OUTCOME_LEADS",  "specialAdCategories": [    "NONE"  ],  "source": "facebook",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```


================================================================================

# Update custom audience
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-update-custom-audience`
---

# Update custom audience

## /ad-publishing/facebook/custom-audience/:audienceId

Update name or description of a Facebook custom audience

## Requestâ

API VersionAvailable options2021-04-15

Custom audience identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Audience name

Audience description

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe",  "name": "My Custom Audience",  "description": "Lookalike audience from website visitors"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe",  "name": "My Custom Audience",  "description": "Lookalike audience from website visitors"}
```


================================================================================

# Upsert conversion pixel
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-upsert-pixel`
---

# Upsert conversion pixel

## /ad-publishing/facebook/pixels

Create or update a Facebook conversion pixel configuration

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Conversion pixel ID

Pixel name

Instagram user ID

Pixel event typeAvailable optionsLEAD_EVENTFUNNEL_EVENTINSTAGRAM_DM

```json
{  "locationId": "loc_abc123",  "conversionPixelId": "px_123",  "name": "My Pixel",  "igUserId": "ig_user_123",  "type": "LEAD_EVENT"}
```

```json
{  "locationId": "loc_abc123",  "conversionPixelId": "px_123",  "name": "My Pixel",  "igUserId": "ig_user_123",  "type": "LEAD_EVENT"}
```


================================================================================

# Google Ads
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-ads`
---

Documentation for Ad-publishing API

## ðï¸Get conversions

Retrieve Google Ads conversion actions for a location. For AD_MANAGER, without `limit` the response is a plain array; when `limit` is provided (max 100, default 100) the response is a paginated `{ conversions, paging }` envelope â pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Upsert conversion

Create or update a Google Ads conversion action

## ðï¸Get conversion by ID

Retrieve a specific Google Ads conversion action by ID

## ðï¸Delete conversion

Delete a Google Ads conversion action by ID

## ðï¸Publish ad

Publish a Google ad and push it live

## ðï¸Search targeting options

Search Google geo-locations for ad targeting

## ðï¸Get keyword ideas

Retrieve keyword suggestions for Google Ads campaigns

## ðï¸Get assets

Retrieve Google Ads creative assets for a location. Without `limit` the response is a plain array of assets. When `limit` is provided (max 100, default 100) the response is a paginated `{ assets, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Upsert assets

Create or update Google Ads creative assets

## ðï¸Get entities

Retrieve Google campaigns, ad groups, or ads based on entity type

## ðï¸Get target interests

Retrieve affinity and in-market audience options for Google Ads targeting. Without `limit` the response is a plain array of root interests (each with a nested children tree). When `limit` is provided (max 100) the response is a paginated `{ targetInterests, paging }` envelope â a page counts root interests; pass `pageToken` (from `paging.next`) to fetch the next batch. By default each node is returned in full; pass `projection` (comma-separated, e.g. ?projection=name,userInterestId,children) to return only the requested fields â selecting `children` prunes the whole tree recursively with the same selection, and any value outside the known field set is rejected.

## ðï¸Get segments

Retrieve Google Ads audience segments for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100, default 100) the response is a paginated `{ segments, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Upsert segment

Create or update a Google Ads audience segment

## ðï¸Delete segment

Delete a Google Ads audience segment by ID

## ðï¸Get segment by ID

Retrieve a specific Google Ads audience segment by ID

## ðï¸Create offline user list job

Create a job to upload users to a Google customer match list

## ðï¸Upsert audience

Create or update a Google Ads combined audience

## ðï¸Get audiences

Retrieve Google Ads combined audiences for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100, default 100) the response is a paginated `{ audiences, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Get audience by ID

Retrieve a specific Google Ads combined audience by ID

## ðï¸Upsert Google campaign

Create or update a full Google Ads campaign structure

## ðï¸Get Google campaign by ID

Retrieve a specific Google Ads campaign by ID

## ðï¸Get conversion goals

Retrieve Google Ads conversion goals for a location. Without `limit` the response is a plain array. When `limit` is provided (max 100, default 100) the response is a paginated `{ conversionGoals, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.


================================================================================

# Search targeting options
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/fb-search-targeting`
---

# Search targeting options

## /ad-publishing/facebook/targeting/search

Search Facebook geo-locations and interests for ad targeting

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Targeting search typeAvailable optionsgeolocationinterestlanguage

Search query string

Specific search subtype


================================================================================

# Create offline user list job
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-create-offline-user-list-job`
---

# Create offline user list job

## /ad-publishing/google/segments/offline-user-list-job

Create a job to upload users to a Google customer match list

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Smart list IDs

CSV file path

User list identifier

Dynamic list flag

```json
{  "locationId": "loc_abc123",  "smartListIds": [    "sl_123"  ],  "csvPath": "/uploads/users.csv",  "userListId": "ul_123",  "isDynamic": false}
```

```json
{  "locationId": "loc_abc123",  "smartListIds": [    "sl_123"  ],  "csvPath": "/uploads/users.csv",  "userListId": "ul_123",  "isDynamic": false}
```


================================================================================

# Delete ad account
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-delete-ad-account`
---

# Delete ad account

## /ad-publishing/google/ad-accounts/:adAccountId

Remove a Google Ads account connection from a location

## Requestâ

API VersionAvailable options2021-04-15

Ad account identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Create Google integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-create-integration`
---

# Create Google integration

## /ad-publishing/google/integration

Create a Google Ads integration for a location

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Ad account identifier

MCC identifier

```json
{  "locationId": "loc_abc123",  "adAccountId": "123-456-7890",  "mccId": "987-654-3210"}
```

```json
{  "locationId": "loc_abc123",  "adAccountId": "123-456-7890",  "mccId": "987-654-3210"}
```


================================================================================

# Delete segment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-delete-segment`
---

# Delete segment

## /ad-publishing/google/segments/:segmentId

Delete a Google Ads audience segment by ID

## Requestâ

API VersionAvailable options2021-04-15

Segment identifier

Location identifier

Segment typeAvailable optionsCUSTOM_SEGMENTSDATA_SEGMENTS


================================================================================

# Get Google ad accounts
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-ad-accounts`
---

# Get Google ad accounts

## /ad-publishing/google/ad-accounts

Retrieve Google Ads accounts available for the connected user

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Account typeAvailable optionsINTEGRATIONAD_MANAGER


================================================================================

# Get ad account details
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-ad-account-details`
---

# Get ad account details

## /ad-publishing/google/ad-accounts/:adAccountId

Retrieve details of a specific Google Ads account

## Requestâ

API VersionAvailable options2021-04-15

Ad account identifier

Location identifier


================================================================================

# Delete conversion
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-delete-conversion`
---

# Delete conversion

## /ad-publishing/google/conversions/:conversionId

Delete a Google Ads conversion action by ID

## Requestâ

API VersionAvailable options2021-04-15

Conversion identifier

Location identifier


================================================================================

# Get assets
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-assets`
---

# Get assets

## /ad-publishing/google/assets

Retrieve Google Ads creative assets for a location. Without limit the response is a plain array of assets. When limit is provided (max 100, default 100) the response is a paginated { assets, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ assets, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Asset type to retrieveAvailable optionsCALLSITELINK

Asset identifier

Advertiser only flag

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { assets, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of assets (default), or a { assets, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleAssetsDTO
* PaginatedGoogleAssetsDTO
* Array [
* ]

* object[]PaginatedGoogleAssetsDTO
* PaginatedGoogleAssetsDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Get audience by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-audience-by-id`
---

# Get audience by ID

## /ad-publishing/google/audiences/:audienceId

Retrieve a specific Google Ads combined audience by ID

## Requestâ

API VersionAvailable options2021-04-15

Audience identifier

Location identifier


================================================================================

# Get conversion by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-conversion-by-id`
---

# Get conversion by ID

## /ad-publishing/google/conversions/:conversionId

Retrieve a specific Google Ads conversion action by ID

## Requestâ

API VersionAvailable options2021-04-15

Conversion identifier

Location identifier


================================================================================

# Get campaign reporting
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-campaign-reporting`
---

# Get campaign reporting

## /ad-publishing/google/reporting/campaign/:campaignId

Retrieve reporting metrics for a specific Google campaign

## Requestâ

API VersionAvailable options2021-04-15

Campaign identifier

Location identifier

Report start date

Report end date


================================================================================

# Get Google campaign by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-campaign-by-id`
---

# Get Google campaign by ID

## /ad-publishing/google/ads/:adId

Retrieve a specific Google Ads campaign by ID

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

Location identifier


================================================================================

# Get current Google user
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-current-user`
---

# Get current Google user

## /ad-publishing/google/me

Retrieve the authenticated Google user info for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier


================================================================================

# Get conversion goals
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-conversion-goals`
---

# Get conversion goals

## /ad-publishing/google/conversion-goals

Retrieve Google Ads conversion goals for a location. Without limit the response is a plain array. When limit is provided (max 100, default 100) the response is a paginated { conversionGoals, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ conversionGoals, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { conversionGoals, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of conversion goals (default), or a { conversionGoals, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleConversionGoalsDTO
* PaginatedGoogleConversionGoalsDTO
* Array [
* ]

* object[]PaginatedGoogleConversionGoalsDTO
* PaginatedGoogleConversionGoalsDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Get audiences
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-audiences`
---

# Get audiences

## /ad-publishing/google/audiences

Retrieve Google Ads combined audiences for a location. Without limit the response is a plain array. When limit is provided (max 100, default 100) the response is a paginated { audiences, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ audiences, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { audiences, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of audiences (default), or a { audiences, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleAudiencesDTO
* PaginatedGoogleAudiencesDTO
* Array [
* ]

* object[]PaginatedGoogleAudiencesDTO
* PaginatedGoogleAudiencesDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Get Google integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-integration`
---

# Get Google integration

## /ad-publishing/google/integration

Retrieve the Google Ads integration details for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier


================================================================================

# Get entities
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-entity`
---

# Get entities

## /ad-publishing/google/entity

Retrieve Google campaigns, ad groups, or ads based on entity type

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Integration typeAvailable optionsAD_MANAGERINTEGRATION

Campaign identifier

Ad group identifier

Entity typeAvailable optionsCAMPAIGNADGROUPAD

Comma-separated Google Ads IDs to filter by

Filter start date

Filter end date

Selected ad account ID


================================================================================

# Get reporting data
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-reporting`
---

# Get reporting data

## /ad-publishing/google/reporting

Retrieve aggregated Google Ads reporting metrics for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Reporting fields. Pass as comma-separated values on the wire (e.g. ?fields=impressions,clicks).Available optionsimpressionsclickscost_microsaverage_cpcconversionsaverage_cpmcost_per_conversionctr

Group by periodAvailable optionsdateweekmonth

Report start date

Report end date

Integration typeAvailable optionsAD_MANAGERINTEGRATION


================================================================================

# Get reporting list
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-reporting-list`
---

# Get reporting list

## /ad-publishing/google/reporting/list

Retrieve a list of Google campaigns or ad groups with reporting data

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Report list typeAvailable optionscampaignsadsadGroupskeywords

Report start date

Report end date

Campaign identifier (required when listType is adGroups, ads, or keywords)

Integration typeAvailable optionsAD_MANAGERINTEGRATION


================================================================================

# Get conversions
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-conversions`
---

# Get conversions

## /ad-publishing/google/conversions

Retrieve Google Ads conversion actions for a location. For AD_MANAGER, without limit the response is a plain array; when limit is provided (max 100, default 100) the response is a paginated { conversions, paging } envelope â pass pageToken (from paging.next) to fetch the next batch.

```json
{ conversions, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Integration typeAvailable optionsAD_MANAGERAD_WORDS

Conversion action type to filter byAvailable optionsUPLOAD_CLICKSUPLOAD_CALLSWEBPAGELEAD_FORM_SUBMIT

Conversion action category to filter byAvailable optionsDEFAULTPAGE_VIEWPURCHASESIGNUPLEADDOWNLOADADD_TO_CARTBEGIN_CHECKOUTSUBSCRIBE_PAIDPHONE_CALL_LEADIMPORTED_LEADSUBMIT_LEAD_FORM

Filter start date

Filter end date

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { conversions, paging } envelope instead of a plain array. Applies to AD_MANAGER type only.

Opaque cursor for the next batch, taken from the previous response paging.next


================================================================================

# Get segment by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-segment-by-id`
---

# Get segment by ID

## /ad-publishing/google/segments/:segmentId

Retrieve a specific Google Ads audience segment by ID

## Requestâ

API VersionAvailable options2021-04-15

Segment identifier

Location identifier

Segment typeAvailable optionsCUSTOM_SEGMENTSDATA_SEGMENTS


================================================================================

# Get target interests
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-target-interests`
---

# Get target interests

## /ad-publishing/google/target-interests

Retrieve affinity and in-market audience options for Google Ads targeting. Without limit the response is a plain array of root interests (each with a nested children tree). When limit is provided (max 100) the response is a paginated { targetInterests, paging } envelope â a page counts root interests; pass pageToken (from paging.next) to fetch the next batch. By default each node is returned in full; pass projection (comma-separated, e.g. ?projection=name,userInterestId,children) to return only the requested fields â selecting children prunes the whole tree recursively with the same selection, and any value outside the known field set is rejected.

```json
{ targetInterests, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Interest typeAvailable optionsAFFINITYIN_MARKET

Channel type

Page size for a paginated fetch (max 100). When set, the response is a { targetInterests, paging } envelope instead of a plain array. Counts root interests â each root includes its full children tree.

Opaque cursor for the next batch, taken from the previous response paging.next

Fields to return on each interest node, comma-separated (e.g. ?projection=name,userInterestId,children). When set, only the requested fields are returned. Selecting children prunes the whole tree recursively with the same selection; availabilities returns the whole array. Any value outside the known field set is rejected. Omit the param entirely to receive the full node as-is.Available optionsresourceNametaxonomyTypeuserInterestIdnameuserInterestParentavailabilitieschildren

A plain array of root interests (default), or a { targetInterests, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleTargetInterestsDTO
* PaginatedGoogleTargetInterestsDTO
* Array [
* ]

* object[]PaginatedGoogleTargetInterestsDTO
* PaginatedGoogleTargetInterestsDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Publish ad
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-publish-ad`
---

# Publish ad

## /ad-publishing/google/ads/:adId/publish

Publish a Google ad and push it live

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Google Integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-integration`
---

Documentation for Ad-publishing API

## ðï¸Get Google integration

Retrieve the Google Ads integration details for a location

## ðï¸Create Google integration

Create a Google Ads integration for a location

## ðï¸Get current Google user

Retrieve the authenticated Google user info for a location

## ðï¸Get Google ad accounts

Retrieve Google Ads accounts available for the connected user

## ðï¸Get ad account details

Retrieve details of a specific Google Ads account

## ðï¸Delete ad account

Remove a Google Ads account connection from a location


================================================================================

# Get segments
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-segments`
---

# Get segments

## /ad-publishing/google/segments

Retrieve Google Ads audience segments for a location. Without limit the response is a plain array. When limit is provided (max 100, default 100) the response is a paginated { segments, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ segments, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Segment typeAvailable optionsCUSTOM_SEGMENTSDATA_SEGMENTSALL

Page size for a paginated fetch (max 100, defaults to 100). When set, the response is a { segments, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of segments (default), or a { segments, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedGoogleSegmentsDTO
* PaginatedGoogleSegmentsDTO
* Array [
* ]

* object[]PaginatedGoogleSegmentsDTO
* PaginatedGoogleSegmentsDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Get keyword ideas
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-get-keyword-ideas`
---

# Get keyword ideas

## /ad-publishing/google/keyword-ideas

Retrieve keyword suggestions for Google Ads campaigns

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Target URL

Language code

Target locations

Seed keywords

```json
{  "url": "https://example.com",  "languageCode": "en",  "locations": [    "US",    "CA"  ],  "keywords": [    "marketing"  ]}
```

```json
{  "url": "https://example.com",  "languageCode": "en",  "locations": [    "US",    "CA"  ],  "keywords": [    "marketing"  ]}
```


================================================================================

# Google Reporting
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-reporting`
---

Documentation for Ad-publishing API

## ðï¸Get reporting data

Retrieve aggregated Google Ads reporting metrics for a location

## ðï¸Get reporting list

Retrieve a list of Google campaigns or ad groups with reporting data

## ðï¸Get campaign reporting

Retrieve reporting metrics for a specific Google campaign


================================================================================

# Search targeting options
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-search-targeting`
---

# Search targeting options

## /ad-publishing/google/targeting/search

Search Google geo-locations for ad targeting

## Requestâ

API VersionAvailable options2021-04-15

Search typeAvailable optionsgeolocationlanguage

Search query

Location identifier


================================================================================

# Upsert audience
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-audience`
---

# Upsert audience

## /ad-publishing/google/audiences

Create or update a Google Ads combined audience

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Audience resource name

Audience name

Audience dimensions

Exclusion dimensions

```json
{  "locationId": "loc_abc123",  "resourceName": "customers/123/audiences/456",  "name": "My Audience",  "dimensions": {    "isAgeUnknown": false,    "ageRanges": [      {        "minAge": 25,        "maxAge": 34      }    ],    "genders": [      "MALE",      "FEMALE"    ]  },  "exclusionDimension": {    "genders": [      "UNDETERMINED"    ]  }}
```

```json
{  "locationId": "loc_abc123",  "resourceName": "customers/123/audiences/456",  "name": "My Audience",  "dimensions": {    "isAgeUnknown": false,    "ageRanges": [      {        "minAge": 25,        "maxAge": 34      }    ],    "genders": [      "MALE",      "FEMALE"    ]  },  "exclusionDimension": {    "genders": [      "UNDETERMINED"    ]  }}
```


================================================================================

# Upsert conversion
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-conversion`
---

# Upsert conversion

## /ad-publishing/google/conversions

Create or update a Google Ads conversion action

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Conversion identifier

Conversion name

Conversion action type. Only UPLOAD_CLICKS is supported â the conversion list endpoint reads back UPLOAD_CLICKS actions only, so a conversion created with any other type would never be returned.Available optionsUPLOAD_CLICKS

Conversion action categoryAvailable optionsDEFAULTPAGE_VIEWPURCHASESIGNUPLEADDOWNLOADADD_TO_CARTBEGIN_CHECKOUTSUBSCRIBE_PAIDPHONE_CALL_LEADIMPORTED_LEADSUBMIT_LEAD_FORM

Value settings that control how monetary value is attributed to conversions

How conversions are counted per interactionAvailable optionsONE_PER_CLICKMANY_PER_CLICK

Attribution model used to credit conversionsAvailable optionsGOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVENGOOGLE_ADS_LAST_CLICK

Click-through conversion window in days

```json
{  "locationId": "loc_abc123",  "conversionId": "conv_456",  "name": "Purchase Conversion",  "type": "UPLOAD_CLICKS",  "category": "PURCHASE",  "valueSettings": {    "defaultValue": "10.00",    "defaultCurrencyCode": "USD",    "alwaysUseDefaultValue": false  },  "countingType": "ONE_PER_CLICK",  "attributionModel": "GOOGLE_ADS_LAST_CLICK",  "clickThroughWindow": 30}
```

```json
{  "locationId": "loc_abc123",  "conversionId": "conv_456",  "name": "Purchase Conversion",  "type": "UPLOAD_CLICKS",  "category": "PURCHASE",  "valueSettings": {    "defaultValue": "10.00",    "defaultCurrencyCode": "USD",    "alwaysUseDefaultValue": false  },  "countingType": "ONE_PER_CLICK",  "attributionModel": "GOOGLE_ADS_LAST_CLICK",  "clickThroughWindow": 30}
```


================================================================================

# Upsert assets
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-assets`
---

# Upsert assets

## /ad-publishing/google/assets

Create or update Google Ads creative assets

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Asset type to create or updateAvailable optionsCALLSITELINK

Asset payload â shape depends on the type field: CallAssetPayload (CALL) or SitelinkAssetPayload (SITELINK)

```json
{  "locationId": "loc_abc123",  "type": "CALL",  "payload": {    "phoneNumber": "+14155551234",    "countryCode": "US"  }}
```

```json
{  "locationId": "loc_abc123",  "type": "CALL",  "payload": {    "phoneNumber": "+14155551234",    "countryCode": "US"  }}
```


================================================================================

# Upsert segment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-segment`
---

# Upsert segment

## /ad-publishing/google/segments

Create or update a Google Ads audience segment

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Segment typeAvailable optionsCUSTOM_SEGMENTSWEBSITE_VISITORCUSTOMER_MATCHLOOKALIKE

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Segment name

Segment description

Segment members â keywords, URLs, or apps that define the custom segment

Segment status

Google custom-audience type, used only when the type query parameter is CUSTOM_SEGMENTS. Defaults to AUTO when omitted. This is NOT the same field as the type query parameter, which selects which kind of segment to upsert â settable values here are AUTO, INTEREST, PURCHASE_INTENT and SEARCH.

Segment identifier

Membership status

Rule-based user list config

Membership life span

Seed user list IDs

Country codes

Expansion levelAvailable optionsBALANCEDBROADNARROW

```json
{  "name": "My Segment",  "description": "Target audience segment",  "members": [    {      "memberType": "KEYWORD",      "keyword": "digital marketing"    },    {      "memberType": "URL",      "url": "https://example.com"    },    {      "memberType": "APP",      "app": "com.example.app"    }  ],  "status": "ENABLED",  "type": "AUTO",  "id": "seg_123",  "membershipStatus": "OPEN",  "ruleBasedUserList": {    "prepopulationStatus": "REQUESTED",    "flexibleRuleUserList": {      "inclusiveOperands": [],      "exclusiveOperands": []    }  },  "membershipLifeSpan": 30,  "seedUserListIds": [    "list_1"  ],  "countryCodes": [    "US",    "CA"  ],  "expansionLevel": "BALANCED"}
```

```json
{  "name": "My Segment",  "description": "Target audience segment",  "members": [    {      "memberType": "KEYWORD",      "keyword": "digital marketing"    },    {      "memberType": "URL",      "url": "https://example.com"    },    {      "memberType": "APP",      "app": "com.example.app"    }  ],  "status": "ENABLED",  "type": "AUTO",  "id": "seg_123",  "membershipStatus": "OPEN",  "ruleBasedUserList": {    "prepopulationStatus": "REQUESTED",    "flexibleRuleUserList": {      "inclusiveOperands": [],      "exclusiveOperands": []    }  },  "membershipLifeSpan": 30,  "seedUserListIds": [    "list_1"  ],  "countryCodes": [    "US",    "CA"  ],  "expansionLevel": "BALANCED"}
```


================================================================================

# Create lead form
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-create-lead-form`
---

# Create lead form

## /ad-publishing/linkedin/:accountId/form

Create a new LinkedIn lead gen form for an ad account

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Form owner

Creation locale

Form name

Form stateAvailable optionsPUBLISHED

Form content

Hidden fields

```json
{  "owner": {    "sponsoredAccount": "urn:li:sponsoredAccount:123456"  },  "creationLocale": {    "country": "US",    "language": "en"  },  "name": "Contact Us",  "state": "PUBLISHED",  "content": {    "questions": [],    "headline": {      "localized": {        "en_US": "Get in touch"      }    },    "postSubmissionInfo": {},    "legalInfo": {}  },  "hiddenFields": [    {      "name": "utm_source",      "value": "linkedin"    }  ]}
```

```json
{  "owner": {    "sponsoredAccount": "urn:li:sponsoredAccount:123456"  },  "creationLocale": {    "country": "US",    "language": "en"  },  "name": "Contact Us",  "state": "PUBLISHED",  "content": {    "questions": [],    "headline": {      "localized": {        "en_US": "Get in touch"      }    },    "postSubmissionInfo": {},    "legalInfo": {}  },  "hiddenFields": [    {      "name": "utm_source",      "value": "linkedin"    }  ]}
```


================================================================================

# Get ad account details
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-ad-account-details`
---

# Get ad account details

## /ad-publishing/linkedin/ad-account

Retrieve details of a specific LinkedIn ad account

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Ad account identifier


================================================================================

# Get LinkedIn ad accounts
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-ad-accounts`
---

# Get LinkedIn ad accounts

## /ad-publishing/linkedin/ad-accounts

Retrieve LinkedIn Ads accounts available for the connected user

## Requestâ

API VersionAvailable options2021-04-15

Location identifier


================================================================================

# Upsert Google campaign
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/google-upsert-campaign`
---

# Upsert Google campaign

## /ad-publishing/google/ads

Create or update a full Google Ads campaign structure

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Campaign identifier

Campaign name

Location identifier

Advertising channel. Only SEARCH and DEMAND_GEN campaigns can be built and published by this product; the other Google channels are readable on existing campaigns but cannot be created here.Available optionsSEARCHDEMAND_GEN

Channel sub typeAvailable optionsDEMAND_GEN

Goal typeAvailable optionsWEBSITE_TRAFFICLEAD

Campaign budget

Campaign audience targeting

Network settings

Bidding strategy config

Campaign assets

EU political ads flag

Campaign ad groups

Campaign goal config

Ad schedule rules

Publishing statusAvailable optionsDRAFTSCHEDULEDPUBLISHEDPUBLISHINGFAILEDIN_REVIEWPAUSEDARCHIVEDWITH_ISSUESREJECTED

Google Ad account identifier

Whether the campaign has unpublished changes

Maximum CPC bid in micros

Google Ads campaign resource ID

Traffic source

Advanced options

User-provided overrides for custom_values merge tags used in ad copy

```json
{  "id": "camp_abc123",  "name": "My Campaign",  "locationId": "loc_abc123",  "advertisingChannelType": "SEARCH",  "advertisingChannelSubType": "DEMAND_GEN",  "goalType": "WEBSITE_TRAFFIC",  "budget": {    "budgetType": "DAILY",    "amount": 5000,    "scheduleStartDate": "2024-01-01"  },  "audience": {    "geoLocations": [      {        "key": "geoTargetConstants/2840",        "name": "United States"      }    ]  },  "networkSettings": {    "targetSearchNetwork": true,    "targetContentNetwork": false  },  "biddingStrategy": {    "type": "MAXIMIZE_CONVERSIONS",    "value": 1000000  },  "assets": {    "calls": [],    "sitelinks": [],    "images": []  },  "isEuPoliticalAds": false,  "adGroups": [    {      "id": "ag_1",      "name": "Ad Group 1",      "adContent": []    }  ],  "campaignGoal": {    "type": "WEBSITE_TRAFFIC",    "isCustomConversionGoal": false  },  "adSchedule": [    {      "dayOfWeek": "MONDAY",      "from": "09:00",      "to": "17:00"    }  ],  "publishingStatus": "PUBLISHED",  "googleAdAccountId": "123-456-7890",  "unpublishedChanges": false,  "maximumCpc": 2000000,  "googleCampaignId": "customers/123/campaigns/456",  "source": "WEBSITE",  "advancedOptions": {    "source": "WEBSITE",    "postId": "post_abc123"  },  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```

```json
{  "id": "camp_abc123",  "name": "My Campaign",  "locationId": "loc_abc123",  "advertisingChannelType": "SEARCH",  "advertisingChannelSubType": "DEMAND_GEN",  "goalType": "WEBSITE_TRAFFIC",  "budget": {    "budgetType": "DAILY",    "amount": 5000,    "scheduleStartDate": "2024-01-01"  },  "audience": {    "geoLocations": [      {        "key": "geoTargetConstants/2840",        "name": "United States"      }    ]  },  "networkSettings": {    "targetSearchNetwork": true,    "targetContentNetwork": false  },  "biddingStrategy": {    "type": "MAXIMIZE_CONVERSIONS",    "value": 1000000  },  "assets": {    "calls": [],    "sitelinks": [],    "images": []  },  "isEuPoliticalAds": false,  "adGroups": [    {      "id": "ag_1",      "name": "Ad Group 1",      "adContent": []    }  ],  "campaignGoal": {    "type": "WEBSITE_TRAFFIC",    "isCustomConversionGoal": false  },  "adSchedule": [    {      "dayOfWeek": "MONDAY",      "from": "09:00",      "to": "17:00"    }  ],  "publishingStatus": "PUBLISHED",  "googleAdAccountId": "123-456-7890",  "unpublishedChanges": false,  "maximumCpc": 2000000,  "googleCampaignId": "customers/123/campaigns/456",  "source": "WEBSITE",  "advancedOptions": {    "source": "WEBSITE",    "postId": "post_abc123"  },  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```


================================================================================

# Get ad analytics
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-ad-analytics`
---

# Get ad analytics

## /ad-publishing/linkedin/reporting

Retrieve LinkedIn Ads analytics data with configurable pivot and time grouping

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Analytics pivot typeAvailable optionsACCOUNTCAMPAIGNCAMPAIGN_GROUPCREATIVE

Time granularity for analyticsAvailable optionsdaymonthyear

Start date in yyyy-mm-dd format

End date in yyyy-mm-dd format

Comma-separated list of entity URNs

Reporting fields. Pass as comma-separated values on the wire (e.g. ?fields=impressions,clicks).Available optionsclicksoneClickLeadscostInLocalCurrencyimpressionscostInUsdctrcpccpmcplexternalWebsitePostClickConversionsconversionRate


================================================================================

# Create LinkedIn integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-create-integration`
---

# Create LinkedIn integration

## /ad-publishing/linkedin/integration

Create a LinkedIn Ads integration for a location with ad account details

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

Ad account identifier

Ad account name

Currency code

Organization identifier

```json
{  "locationId": "loc_123",  "adAccountId": "12345678",  "adAccountName": "My Ad Account",  "currencyCode": "USD",  "organizationId": "12345678"}
```

```json
{  "locationId": "loc_123",  "adAccountId": "12345678",  "adAccountName": "My Ad Account",  "currencyCode": "USD",  "organizationId": "12345678"}
```


================================================================================

# Delete ad account
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-delete-ad-account`
---

# Delete ad account

## /ad-publishing/linkedin/ad-account

Remove a LinkedIn ad account connection from a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Ad account identifier


================================================================================

# Get ad campaign group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-campaign-group`
---

# Get ad campaign group

## /ad-publishing/linkedin/ads/:adId

Retrieve a LinkedIn ad campaign group by ID

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

Location identifier


================================================================================

# Get campaign group reporting
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-campaign-group-reporting`
---

# Get campaign group reporting

## /ad-publishing/linkedin/reporting/campaign-group/:campaignGroupId

Retrieve reporting metrics for a specific LinkedIn campaign group

## Requestâ

API VersionAvailable options2021-04-15

Campaign group identifier

Location ID

Start date in yyyy-mm-dd format

End date in yyyy-mm-dd format

Reporting fields. Pass as comma-separated values on the wire (e.g. ?fields=impressions,clicks).Available optionsclicksoneClickLeadscostInLocalCurrencyimpressionscostInUsdctrcpccpmcplexternalWebsitePostClickConversionsconversionRate

Campaign group ID


================================================================================

# Publish ad campaign group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-publish-campaign-group`
---

# Publish ad campaign group

## /ad-publishing/linkedin/ads/:adId/publish

Publish a LinkedIn ad campaign group and push it live

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location identifier

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```

```json
{  "locationId": "HChooFuiyPpVYzeJ4HMe"}
```


================================================================================

# Get reporting list
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-reporting-list`
---

# Get reporting list

## /ad-publishing/linkedin/reporting/list

Retrieve a list of LinkedIn campaigns or campaign groups with reporting data

## Requestâ

API VersionAvailable options2021-04-15

Location ID

List typeAvailable optionscampaignGroupscampaignsads

Campaign ID

Campaign group ID

Start date in yyyy-mm-dd format

End date in yyyy-mm-dd format

Reporting fields. Pass as comma-separated values on the wire (e.g. ?fields=impressions,clicks).Available optionsclicksoneClickLeadscostInLocalCurrencyimpressionscostInUsdctrcpccpmcplexternalWebsitePostClickConversionsconversionRate


================================================================================

# Get LinkedIn integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-integration`
---

# Get LinkedIn integration

## /ad-publishing/linkedin/integration

Retrieve the LinkedIn Ads integration details for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier


================================================================================

# Get current LinkedIn user
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-current-user`
---

# Get current LinkedIn user

## /ad-publishing/linkedin/me

Retrieve the authenticated LinkedIn user info for a location

## Requestâ

API VersionAvailable options2021-04-15

Location identifier


================================================================================

# LinkedIn Integration
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/linked-in-integration`
---

Documentation for Ad-publishing API

## ðï¸Get LinkedIn integration

Retrieve the LinkedIn Ads integration details for a location

## ðï¸Create LinkedIn integration

Create a LinkedIn Ads integration for a location with ad account details

## ðï¸Get LinkedIn ad accounts

Retrieve LinkedIn Ads accounts available for the connected user

## ðï¸Get ad account details

Retrieve details of a specific LinkedIn ad account

## ðï¸Delete ad account

Remove a LinkedIn ad account connection from a location

## ðï¸Get current LinkedIn user

Retrieve the authenticated LinkedIn user info for a location


================================================================================

# Search targeting options
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-search-targeting`
---

# Search targeting options

## /ad-publishing/linkedin/targeting/search

Search LinkedIn targeting facets such as locations, industries, and job titles

## Requestâ

API VersionAvailable options2021-04-15

Location identifier

Targeting facet

Search query

Query parameter


================================================================================

# LinkedIn Ads
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/linked-in-ads`
---

Documentation for Ad-publishing API

## ðï¸Get ad campaign group

Retrieve a LinkedIn ad campaign group by ID

## ðï¸Publish ad campaign group

Publish a LinkedIn ad campaign group and push it live

## ðï¸Upsert ad campaign group

Create or update a LinkedIn ad campaign group with campaigns and ads

## ðï¸Search targeting options

Search LinkedIn targeting facets such as locations, industries, and job titles

## ðï¸Get lead forms

Retrieve LinkedIn lead gen forms for an ad account. By default each form is returned in full as a plain array; pass `projection` (comma-separated, dot-notation for nested fields) to return only the requested fields â any value outside the known field set is rejected. When `limit` is provided (max 100) the response is a paginated `{ leadForms, paging }` envelope; pass `pageToken` (from `paging.next`) to fetch the next batch.

## ðï¸Create lead form

Create a new LinkedIn lead gen form for an ad account

## ðï¸Update ad status

Pause or resume a LinkedIn ad, campaign, or ad group


================================================================================

# LinkedIn Reporting
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/linked-in-reporting`
---

Documentation for Ad-publishing API

## ðï¸Get ad analytics

Retrieve LinkedIn Ads analytics data with configurable pivot and time grouping

## ðï¸Get reporting list

Retrieve a list of LinkedIn campaigns or campaign groups with reporting data

## ðï¸Get campaign group reporting

Retrieve reporting metrics for a specific LinkedIn campaign group


================================================================================

# Upsert ad campaign group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-upsert-campaign-group`
---

# Upsert ad campaign group

## /ad-publishing/linkedin/ads

Create or update a LinkedIn ad campaign group with campaigns and ads

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Internal ID

Location ID

Campaign group budget

Child ad campaigns

Ad budget optimization modeAvailable optionsMAXIMUM_DELIVERYCOST_CAP

Campaign group objectiveAvailable optionsLEAD_GENERATIONWEBSITE_VISIT

Campaign group name

LinkedIn campaign group resource ID

Publishing statusAvailable optionsDRAFTSCHEDULEDPUBLISHEDPUBLISHINGFAILEDIN_REVIEWPAUSEDARCHIVEDWITH_ISSUESREJECTED

LinkedIn ad account identifier

Whether the campaign group has unpublished changes

Additional metadata

LinkedIn API error message

User-provided overrides for custom_values merge tags used in ad copy

```json
{  "id": "cg_abc123",  "locationId": "loc_abc123",  "budget": {    "budgetType": "DAILY",    "amount": 10000  },  "adCampaigns": [    {      "name": "Campaign 1",      "publishingStatus": "PUBLISHED"    }  ],  "adBudgetOptimization": "MAXIMUM_DELIVERY",  "objectiveType": "LEAD_GENERATION",  "name": "Q1 Lead Gen",  "adCampaignGroupId": "123456789",  "publishingStatus": "PUBLISHED",  "linkedInAdAccountId": "12345678",  "unpublishedChanges": false,  "meta": {},  "linkedInError": "Budget below minimum",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```

```json
{  "id": "cg_abc123",  "locationId": "loc_abc123",  "budget": {    "budgetType": "DAILY",    "amount": 10000  },  "adCampaigns": [    {      "name": "Campaign 1",      "publishingStatus": "PUBLISHED"    }  ],  "adBudgetOptimization": "MAXIMUM_DELIVERY",  "objectiveType": "LEAD_GENERATION",  "name": "Q1 Lead Gen",  "adCampaignGroupId": "123456789",  "publishingStatus": "PUBLISHED",  "linkedInAdAccountId": "12345678",  "unpublishedChanges": false,  "meta": {},  "linkedInError": "Budget below minimum",  "customValueMappings": {    "{{ custom_values.pet_name }}": "Fluffy"  }}
```


================================================================================

# Get lead forms
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-get-lead-forms`
---

# Get lead forms

## /ad-publishing/linkedin/:accountId/forms

Retrieve LinkedIn lead gen forms for an ad account. By default each form is returned in full as a plain array; pass projection (comma-separated, dot-notation for nested fields) to return only the requested fields â any value outside the known field set is rejected. When limit is provided (max 100) the response is a paginated { leadForms, paging } envelope; pass pageToken (from paging.next) to fetch the next batch.

```json
{ leadForms, paging }
```

## Requestâ

API VersionAvailable options2021-04-15

Account identifier

Location identifier

Fields to return on each lead form, comma-separated (e.g. ?projection=id,name,state,created,reviewInfo.reviewStatus). When set, only the requested fields are returned; any value outside the known field set is rejected. Nested fields use dot-notation (naming a parent like reviewInfo returns the whole object). Omit to receive the full form (including content.questions) as-is.Available optionsidnamestatecreatedlastModifiedversionIdcreationLocaleownerreviewInforeviewInfo.reviewStatusreviewInfo.rejectionReasonscontent

Page size for a paginated fetch (max 100). When set, the response is a { leadForms, paging } envelope instead of a plain array.

Opaque cursor for the next batch, taken from the previous response paging.next

A plain array of lead forms (default), or a { leadForms, paging } envelope when limit is provided

* application/json

* SchemaExample (auto)
* Example (auto)

* object[]PaginatedLinkedInLeadFormsDTO
* PaginatedLinkedInLeadFormsDTO
* Array [
* ]

* object[]PaginatedLinkedInLeadFormsDTO
* PaginatedLinkedInLeadFormsDTO

```json
[  {}]
```

```json
[  {}]
```


================================================================================

# Update ad status
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/ad-publishing/li-update-ad-status`
---

# Update ad status

## /ad-publishing/linkedin/:adId/status

Pause or resume a LinkedIn ad, campaign, or ad group

## Requestâ

API VersionAvailable options2021-04-15

Ad identifier

Location identifier

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Update operationAvailable optionsPAUSEDARCHIVEDRESUME

Ad object typeAvailable optionsadGroupadCampaignad

```json
{  "operationType": "PAUSED",  "type": "adCampaign"}
```

```json
{  "operationType": "PAUSED",  "type": "adCampaign"}
```


================================================================================

# Affiliates
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/affiliates`
---

Documentation for Affiliate Manager API

## ðï¸List Affiliates

Retrieve the list of affiliates for a location.

## ðï¸Get Affiliate

Retrieve a single affiliate by id for a location.


================================================================================

# Commissions
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/commissions`
---

Documentation for Affiliate Manager API

## ðï¸List Commissions

Retrieve the list of commissions for a location.


================================================================================

# List Affiliates
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/list-affiliates`
---

# List Affiliates

## /affiliate-manager/:locationId/affiliates

Retrieve the list of affiliates for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Maximum number of records to return. Maximum allowed value is 100.Default value:10

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Affiliate list

Pagination metadata

```json
{  "affiliates": [    {      "_id": "63d147176c5bbc30e9e091a4",      "firstName": "John",      "lastName": "Doe",      "phone": "+1 888 888-8888",      "deleted": false,      "locationId": "ve9EPM428h8vShlRW1KT",      "active": true,      "address": "123 Main St",      "avatar": "https://example.com/avatar.png",      "createdAt": "2024-06-16T00:00:00.000Z",      "createdBy": {},      "facebookUrl": "https://facebook.com/johndoe",      "instagramUrl": "https://instagram.com/johndoe",      "linkedInUrl": "https://linkedin.com/in/johndoe",      "twitterUrl": "https://twitter.com/johndoe",      "youtubeUrl": "https://youtube.com/channel",      "websiteUrl": "https://example.com",      "contactId": "ve9EPM428h8vShlRW1KT",      "campaignIds": [        "650173614761b33c46d33b19"      ],      "vatId": "VAT123",      "updatedAt": "2024-06-16T00:00:00.000Z",      "w8Form": "string",      "w9Form": "string",      "lastUpdatedBy": {},      "email": "[email protected]",      "revenue": 1250.5,      "customer": 15,      "lead": 5,      "droppedCustomer": 2,      "clickCount": 100,      "paid": 500,      "currency": "USD",      "owned": 750    }  ],  "meta": {    "count": 42  }}
```

```json
{  "affiliates": [    {      "_id": "63d147176c5bbc30e9e091a4",      "firstName": "John",      "lastName": "Doe",      "phone": "+1 888 888-8888",      "deleted": false,      "locationId": "ve9EPM428h8vShlRW1KT",      "active": true,      "address": "123 Main St",      "avatar": "https://example.com/avatar.png",      "createdAt": "2024-06-16T00:00:00.000Z",      "createdBy": {},      "facebookUrl": "https://facebook.com/johndoe",      "instagramUrl": "https://instagram.com/johndoe",      "linkedInUrl": "https://linkedin.com/in/johndoe",      "twitterUrl": "https://twitter.com/johndoe",      "youtubeUrl": "https://youtube.com/channel",      "websiteUrl": "https://example.com",      "contactId": "ve9EPM428h8vShlRW1KT",      "campaignIds": [        "650173614761b33c46d33b19"      ],      "vatId": "VAT123",      "updatedAt": "2024-06-16T00:00:00.000Z",      "w8Form": "string",      "w9Form": "string",      "lastUpdatedBy": {},      "email": "[email protected]",      "revenue": 1250.5,      "customer": 15,      "lead": 5,      "droppedCustomer": 2,      "clickCount": 100,      "paid": 500,      "currency": "USD",      "owned": 750    }  ],  "meta": {    "count": 42  }}
```


================================================================================

# List Commissions
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/list-commissions`
---

# List Commissions

## /affiliate-manager/:locationId/commissions

Retrieve the list of commissions for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Campaign Id

Affiliate Id

Status

Query

Maximum number of records to return. Maximum allowed value is 100.Default value:10

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Commission list

Pagination metadata

```json
{  "commissions": [    {      "_id": "6385d230f6d19db03eef6fb2",      "productId": "6385d230f6d19db03eef6fb2",      "productName": "Basic Plan",      "qty": 1,      "productCommission": 25,      "commissionAmount": 25,      "amount": 100,      "unitDiscount": 5,      "campaignName": "Summer Promo",      "commission": 25,      "commissionType": "percentage",      "transactionAt": "2024-06-16T00:00:00.000Z",      "transactionId": "txn_123",      "affiliateId": "6385d230f6d19db03eef6fb2",      "payoutId": "6385d230f6d19db03eef6fb2",      "status": "pending",      "currency": "USD",      "isTrial": false,      "customer": {        "_id": "6385d230f6d19db03eef6fb2",        "firstName": "John",        "lastName": "Doe",        "email": "[email protected]",        "type": "customer"      },      "createdAt": "2024-06-16T00:00:00.000Z",      "eventId": "evt_123",      "campaign": {        "id": "6385d230f6d19db03eef6fb2",        "name": "Summer Promo",        "liveMode": true      },      "affiliate": {        "_id": "6385d230f6d19db03eef6fb2",        "name": "John Doe",        "email": "[email protected]"      },      "dueAt": "2024-06-30T00:00:00.000Z",      "liveMode": true,      "tier": 1    }  ],  "meta": {    "count": 42  }}
```

```json
{  "commissions": [    {      "_id": "6385d230f6d19db03eef6fb2",      "productId": "6385d230f6d19db03eef6fb2",      "productName": "Basic Plan",      "qty": 1,      "productCommission": 25,      "commissionAmount": 25,      "amount": 100,      "unitDiscount": 5,      "campaignName": "Summer Promo",      "commission": 25,      "commissionType": "percentage",      "transactionAt": "2024-06-16T00:00:00.000Z",      "transactionId": "txn_123",      "affiliateId": "6385d230f6d19db03eef6fb2",      "payoutId": "6385d230f6d19db03eef6fb2",      "status": "pending",      "currency": "USD",      "isTrial": false,      "customer": {        "_id": "6385d230f6d19db03eef6fb2",        "firstName": "John",        "lastName": "Doe",        "email": "[email protected]",        "type": "customer"      },      "createdAt": "2024-06-16T00:00:00.000Z",      "eventId": "evt_123",      "campaign": {        "id": "6385d230f6d19db03eef6fb2",        "name": "Summer Promo",        "liveMode": true      },      "affiliate": {        "_id": "6385d230f6d19db03eef6fb2",        "name": "John Doe",        "email": "[email protected]"      },      "dueAt": "2024-06-30T00:00:00.000Z",      "liveMode": true,      "tier": 1    }  ],  "meta": {    "count": 42  }}
```


================================================================================

# Payouts
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/payouts`
---

Documentation for Affiliate Manager API

## ðï¸List Payouts

Retrieve the list of payouts for a location.


================================================================================

# Affiliate Manager API
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/affiliate-manager-api`
---

# Affiliate Manager API

Documentation for Affiliate Manager API

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# Agent Studio APIs
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/agent-studio-apis`
---

# Agent Studio APIs

Documentation for Agent Studio APIs

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# List Payouts
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/list-payouts`
---

# List Payouts

## /affiliate-manager/:locationId/payouts

Retrieve the list of payouts for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Payout status

query

Affiliate Id

Campaign Id

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Payout list

Pagination metadata

```json
{  "payouts": [    {      "_id": "65df04201e428a0c5ebb6571",      "locationId": "ve9EPM428h8vShlRW1KT",      "affiliateId": "65df04201e428a0c5ebb6572",      "campaignId": "65df04201e428a0c5ebb6573",      "currency": "USD",      "amount": 150,      "status": "pending",      "payoutMonth": "2024-06-01T00:00:00.000Z",      "dueAt": "2024-06-30T00:00:00.000Z",      "paidAt": "2024-06-30T00:00:00.000Z",      "paidMeta": {},      "paidMethod": "manual",      "altId": "alt_123",      "deleted": false,      "isMigrated": false,      "createdAt": "2024-06-16T00:00:00.000Z",      "updatedAt": "2024-06-17T00:00:00.000Z",      "campaign": "Summer Promo",      "affiliateName": "John Doe",      "affiliateEmail": "[email protected]",      "payoutMethod": "paypal",      "affiliate": {        "_id": "63d147176c5bbc30e9e091a4",        "firstName": "John",        "lastName": "Doe",        "phone": "+1 888 888-8888",        "deleted": false,        "locationId": "ve9EPM428h8vShlRW1KT",        "active": true,        "address": "123 Main St",        "avatar": "https://example.com/avatar.png",        "createdAt": "2024-06-16T00:00:00.000Z",        "createdBy": {},        "facebookUrl": "https://facebook.com/johndoe",        "instagramUrl": "https://instagram.com/johndoe",        "linkedInUrl": "https://linkedin.com/in/johndoe",        "twitterUrl": "https://twitter.com/johndoe",        "youtubeUrl": "https://youtube.com/channel",        "websiteUrl": "https://example.com",        "contactId": "ve9EPM428h8vShlRW1KT",        "campaignIds": [          "650173614761b33c46d33b19"        ],        "vatId": "VAT123",        "updatedAt": "2024-06-16T00:00:00.000Z",        "w8Form": "string",        "w9Form": "string",        "lastUpdatedBy": {},        "email": "[email protected]",        "revenue": 1250.5,        "customer": 15,        "lead": 5,        "droppedCustomer": 2,        "clickCount": 100,        "paid": 500,        "currency": "USD",        "owned": 750      }    }  ],  "meta": {    "count": 42  }}
```

```json
{  "payouts": [    {      "_id": "65df04201e428a0c5ebb6571",      "locationId": "ve9EPM428h8vShlRW1KT",      "affiliateId": "65df04201e428a0c5ebb6572",      "campaignId": "65df04201e428a0c5ebb6573",      "currency": "USD",      "amount": 150,      "status": "pending",      "payoutMonth": "2024-06-01T00:00:00.000Z",      "dueAt": "2024-06-30T00:00:00.000Z",      "paidAt": "2024-06-30T00:00:00.000Z",      "paidMeta": {},      "paidMethod": "manual",      "altId": "alt_123",      "deleted": false,      "isMigrated": false,      "createdAt": "2024-06-16T00:00:00.000Z",      "updatedAt": "2024-06-17T00:00:00.000Z",      "campaign": "Summer Promo",      "affiliateName": "John Doe",      "affiliateEmail": "[email protected]",      "payoutMethod": "paypal",      "affiliate": {        "_id": "63d147176c5bbc30e9e091a4",        "firstName": "John",        "lastName": "Doe",        "phone": "+1 888 888-8888",        "deleted": false,        "locationId": "ve9EPM428h8vShlRW1KT",        "active": true,        "address": "123 Main St",        "avatar": "https://example.com/avatar.png",        "createdAt": "2024-06-16T00:00:00.000Z",        "createdBy": {},        "facebookUrl": "https://facebook.com/johndoe",        "instagramUrl": "https://instagram.com/johndoe",        "linkedInUrl": "https://linkedin.com/in/johndoe",        "twitterUrl": "https://twitter.com/johndoe",        "youtubeUrl": "https://youtube.com/channel",        "websiteUrl": "https://example.com",        "contactId": "ve9EPM428h8vShlRW1KT",        "campaignIds": [          "650173614761b33c46d33b19"        ],        "vatId": "VAT123",        "updatedAt": "2024-06-16T00:00:00.000Z",        "w8Form": "string",        "w9Form": "string",        "lastUpdatedBy": {},        "email": "[email protected]",        "revenue": 1250.5,        "customer": 15,        "lead": 5,        "droppedCustomer": 2,        "clickCount": 100,        "paid": 500,        "currency": "USD",        "owned": 750      }    }  ],  "meta": {    "count": 42  }}
```


================================================================================

# Delete Agent
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/delete-agent`
---

# Delete Agent

## /agent-studio/agent/:agentId

Deletes an agent and all its versions.

## Requestâ

API VersionAvailable options2021-04-15

Agent deleted successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Deleted agent ID

```json
{  "success": true,  "message": "Agent deleted successfully",  "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2"}
```

```json
{  "success": true,  "message": "Agent deleted successfully",  "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2"}
```


================================================================================

# Get Affiliate
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/affiliate-manager/get-affiliate`
---

# Get Affiliate

## /affiliate-manager/:locationId/affiliates/:affiliateId

Retrieve a single affiliate by id for a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Affiliate Id

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Affiliate id

Affiliate first name

Affiliate last name

Affiliate phone number

Whether the affiliate is deleted

Location id

Whether the affiliate is active

Affiliate address

Affiliate avatar URL

Created at timestamp

Created by audit info

Facebook URL

Instagram URL

LinkedIn URL

Twitter URL

YouTube URL

Website URL

Contact id associated with the affiliate

Campaign ids

VAT ID

Updated at timestamp

W8 form URL

W9 form URL

Last updated by audit info

Affiliate email

Affiliate revenue

Customer count

Lead count

Dropped customer count

Click count

Paid amount

Currency code

Owned amount

```json
{  "_id": "63d147176c5bbc30e9e091a4",  "firstName": "John",  "lastName": "Doe",  "phone": "+1 888 888-8888",  "deleted": false,  "locationId": "ve9EPM428h8vShlRW1KT",  "active": true,  "address": "123 Main St",  "avatar": "https://example.com/avatar.png",  "createdAt": "2024-06-16T00:00:00.000Z",  "createdBy": {},  "facebookUrl": "https://facebook.com/johndoe",  "instagramUrl": "https://instagram.com/johndoe",  "linkedInUrl": "https://linkedin.com/in/johndoe",  "twitterUrl": "https://twitter.com/johndoe",  "youtubeUrl": "https://youtube.com/channel",  "websiteUrl": "https://example.com",  "contactId": "ve9EPM428h8vShlRW1KT",  "campaignIds": [    "650173614761b33c46d33b19"  ],  "vatId": "VAT123",  "updatedAt": "2024-06-16T00:00:00.000Z",  "w8Form": "string",  "w9Form": "string",  "lastUpdatedBy": {},  "email": "[email protected]",  "revenue": 1250.5,  "customer": 15,  "lead": 5,  "droppedCustomer": 2,  "clickCount": 100,  "paid": 500,  "currency": "USD",  "owned": 750}
```

```json
{  "_id": "63d147176c5bbc30e9e091a4",  "firstName": "John",  "lastName": "Doe",  "phone": "+1 888 888-8888",  "deleted": false,  "locationId": "ve9EPM428h8vShlRW1KT",  "active": true,  "address": "123 Main St",  "avatar": "https://example.com/avatar.png",  "createdAt": "2024-06-16T00:00:00.000Z",  "createdBy": {},  "facebookUrl": "https://facebook.com/johndoe",  "instagramUrl": "https://instagram.com/johndoe",  "linkedInUrl": "https://linkedin.com/in/johndoe",  "twitterUrl": "https://twitter.com/johndoe",  "youtubeUrl": "https://youtube.com/channel",  "websiteUrl": "https://example.com",  "contactId": "ve9EPM428h8vShlRW1KT",  "campaignIds": [    "650173614761b33c46d33b19"  ],  "vatId": "VAT123",  "updatedAt": "2024-06-16T00:00:00.000Z",  "w8Form": "string",  "w9Form": "string",  "lastUpdatedBy": {},  "email": "[email protected]",  "revenue": 1250.5,  "customer": 15,  "lead": 5,  "droppedCustomer": 2,  "clickCount": 100,  "paid": 500,  "currency": "USD",  "owned": 750}
```


================================================================================

# Create Agent
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/create-agent`
---

# Create Agent

## /agent-studio/agent

Creates a new agent with staging version. The agent will be created with an initial staging version that can later be promoted to production.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Name of the agent

Description of the agent

Agency ID

Author ID

Author name

Author email

Status of the agentAvailable optionsactiveinactivearchived

Version data for the agent including nodes, edges, and configuration

Nodes array (deprecated, prefer using version.nodes)

Edges array (deprecated, prefer using version.edges)

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Customer Support Agent",  "description": "AI agent specialized in handling customer inquiries and support tickets",  "agencyId": "gjL2sFNXJfJYa3d2OYSN",  "authorId": "usr_abc123def456",  "authorName": "John Doe",  "authorEmail": "[email protected]",  "status": "active",  "version": {    "versionName": "Version 1",    "description": "Initial version",    "nodes": [],    "edges": [],    "uiNodes": [],    "uiEdges": [],    "globalVariables": [],    "inputVariables": [],    "runtimeVariables": [],    "scopes": []  },  "nodes": [],  "edges": []}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Customer Support Agent",  "description": "AI agent specialized in handling customer inquiries and support tickets",  "agencyId": "gjL2sFNXJfJYa3d2OYSN",  "authorId": "usr_abc123def456",  "authorName": "John Doe",  "authorEmail": "[email protected]",  "status": "active",  "version": {    "versionName": "Version 1",    "description": "Initial version",    "nodes": [],    "edges": [],    "uiNodes": [],    "uiEdges": [],    "globalVariables": [],    "inputVariables": [],    "runtimeVariables": [],    "scopes": []  },  "nodes": [],  "edges": []}
```

Agent created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Created agent data with metadata

Created versions array (initial staging version)

```json
{  "success": true,  "message": "Agent created successfully with staging version.",  "agent": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "name": "Customer Support Agent",    "description": "AI agent specialized in handling customer inquiries and support tickets",    "locationId": "C2QujeCh8ZnC7al2InWR",    "agencyId": "gjL2sFNXJfJYa3d2OYSN",    "status": "active",    "authorId": "usr_abc123def456",    "folderId": "C2QujeCh8ZnC7al2InWR",    "folderName": null,    "createdAt": "2024-02-27T10:30:00.000Z",    "updatedAt": "2024-02-27T10:30:00.000Z"  },  "versions": [    {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v1",      "state": "staging",      "isPublished": false,      "version": 1,      "createdAt": "2024-02-27T10:30:00.000Z"    }  ]}
```

```json
{  "success": true,  "message": "Agent created successfully with staging version.",  "agent": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "name": "Customer Support Agent",    "description": "AI agent specialized in handling customer inquiries and support tickets",    "locationId": "C2QujeCh8ZnC7al2InWR",    "agencyId": "gjL2sFNXJfJYa3d2OYSN",    "status": "active",    "authorId": "usr_abc123def456",    "folderId": "C2QujeCh8ZnC7al2InWR",    "folderName": null,    "createdAt": "2024-02-27T10:30:00.000Z",    "updatedAt": "2024-02-27T10:30:00.000Z"  },  "versions": [    {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v1",      "state": "staging",      "isPublished": false,      "version": 1,      "createdAt": "2024-02-27T10:30:00.000Z"    }  ]}
```


================================================================================

# Execute Agent
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/execute-agent`
---

# Execute Agent

## /agent-studio/agent/:agentId/execute

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body.

Session Management:

* For the first message in a new session, do not include the executionId in the request payload.
* The API will return an executionId along with the agent response, which uniquely identifies this conversation session.
* To continue the conversation within the same session, include the executionId from the previous response in subsequent requests. This allows the agent to maintain conversation context and history across multiple interactions.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Message to send to the agent

Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Omit this field for the first message in a new session. Include the executionId returned from the previous response to maintain context in subsequent messages.

Input variables to pass to the agent. These should match the input variables defined in the agent configuration.

Published version ID to execute. If not provided, the latest published production version will be used.

Attachments for the message

Location ID

Contact ID to associate with this execution. When provided, contact data will be hydrated and made available to the agent.

```json
{  "message": "How can you help me with my marketing?",  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "inputVariables": {    "customerName": "John Doe",    "orderNumber": "ORD-12345"  },  "versionId": "b2b1c1d2-3e4f-5a6b-7c8d-9e0f1a2b3c4d",  "attachments": [    {      "type": "image",      "imageUrl": "https://example.com/image.png"    }  ],  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "cid_abc123def456"}
```

```json
{  "message": "How can you help me with my marketing?",  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "inputVariables": {    "customerName": "John Doe",    "orderNumber": "ORD-12345"  },  "versionId": "b2b1c1d2-3e4f-5a6b-7c8d-9e0f1a2b3c4d",  "attachments": [    {      "type": "image",      "imageUrl": "https://example.com/image.png"    }  ],  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "cid_abc123def456"}
```

Agent executed successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Use this ID in subsequent requests to continue the conversation.

Unique identifier for a single interaction cycle, consisting of one user input and the corresponding agent response. Each message exchange generates a new interactionId.

Agent response text

Response type

Expected input type for next interaction

When end node is added in the graph, this will be true if the agent reached the end node in the graph

Execution status

Whether flow was switched

Response attachments

Generated outputs

```json
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

```json
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```


================================================================================

# Execute Agent (Deprecated)
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/execute-agent-deprecated`
---

# Execute Agent (Deprecated)

## /agent-studio/public-api/agents/:agentId/execute

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Deprecated endpoint - use POST /agent/:agentId/execute instead.

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body.

Session Management:

* For the first message in a new session, do not include the executionId in the request payload.
* The API will return an executionId along with the agent response, which uniquely identifies this conversation session.
* To continue the conversation within the same session, include the executionId from the previous response in subsequent requests.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Message to send to the agent

Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Omit this field for the first message in a new session. Include the executionId returned from the previous response to maintain context in subsequent messages.

Input variables to pass to the agent. These should match the input variables defined in the agent configuration.

Published version ID to execute. If not provided, the latest published production version will be used.

Attachments for the message

Location ID

Contact ID to associate with this execution. When provided, contact data will be hydrated and made available to the agent.

```json
{  "message": "How can you help me with my marketing?",  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "inputVariables": {    "customerName": "John Doe",    "orderNumber": "ORD-12345"  },  "versionId": "b2b1c1d2-3e4f-5a6b-7c8d-9e0f1a2b3c4d",  "attachments": [    {      "type": "image",      "imageUrl": "https://example.com/image.png"    }  ],  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "cid_abc123def456"}
```

```json
{  "message": "How can you help me with my marketing?",  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "inputVariables": {    "customerName": "John Doe",    "orderNumber": "ORD-12345"  },  "versionId": "b2b1c1d2-3e4f-5a6b-7c8d-9e0f1a2b3c4d",  "attachments": [    {      "type": "image",      "imageUrl": "https://example.com/image.png"    }  ],  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "cid_abc123def456"}
```

Agent executed successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Use this ID in subsequent requests to continue the conversation.

Unique identifier for a single interaction cycle, consisting of one user input and the corresponding agent response. Each message exchange generates a new interactionId.

Agent response text

Response type

Expected input type for next interaction

When end node is added in the graph, this will be true if the agent reached the end node in the graph

Execution status

Whether flow was switched

Response attachments

Generated outputs

```json
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

```json
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```


================================================================================

# Agents
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/agents`
---

Documentation for Agent Studio APIs

## ðï¸Create Agent

Creates a new agent with staging version. The agent will be created with an initial staging version that can later be promoted to production.

## ðï¸List Agents

Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset. Optionally filter by isPublished=true to return only agents with a published production version.

## ðï¸Update Agent

Updates a specific agent version by versionId. Supports updating nodes, edges, variables, and configuration.

## ðï¸Update Agent Metadata

Updates agent metadata such as name, description, and status.

## ðï¸Delete Agent

Deletes an agent and all its versions.

## ðï¸Get Agent

Gets a specific agent by its ID for the specified location with all its versions. Returns complete agent metadata and all non-deleted versions (draft, staging, production). locationId is required parameter. The agent must have active status.

## ðï¸Promote to Production

Promotes a draft version to production.

## ðï¸Execute Agent

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body.

## ðï¸List Agents (Deprecated)

**Deprecated endpoint - use GET /agent instead.**

## ðï¸Get Agent (Deprecated)

**Deprecated endpoint - use GET /agent/:agentId instead.**

## ðï¸Execute Agent (Deprecated)

**Deprecated endpoint - use POST /agent/:agentId/execute instead.**


================================================================================

# Get Agent (Deprecated)
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/get-agent-by-id-deprecated`
---

# Get Agent (Deprecated)

## /agent-studio/public-api/agents/:agentId

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Deprecated endpoint - use GET /agent/:agentId instead.

Gets a specific agent by its ID for the specified location with all its versions. locationId is required parameter. The agent must have active status.

## Requestâ

API VersionAvailable options2021-04-15

Agent retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Agent metadata with all active versions

Request trace ID for debugging

```json
{  "success": true,  "message": "Agent retrieved successfully",  "agent": {    "id": "d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd",    "agentId": "AgfS2JXWsSN8aXb5c4d2",    "name": "Customer Support Agent",    "description": "AI agent for customer support",    "agencyId": "5DP4iH6HLkQsiKESj6rh",    "locationId": "C2QujeCh8ZnC7al2InWR",    "productSlug": "agent_studio",    "productId": "agent_studio",    "authorId": "usr_123",    "status": "active",    "folderId": "vEoIigWSAw1BQA9DEchD",    "folderName": "Default Agents",    "createdAt": "2026-03-06T10:37:01.013Z",    "updatedAt": "2026-03-06T10:37:01.014Z",    "deleted": false,    "productionVersion": {      "versionId": "Ver1K8sSF2nC7al5InWz",      "versionName": "Content Creation Agent v1",      "isPublished": true,      "inputVariables": [],      "updatedAt": "2026-03-02T06:53:40.570Z"    },    "versions": [      {        "id": "3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3",        "versionId": "Ver1K8sSF2nC7al5InWz",        "agentId": "AgfS2JXWsSN8aXb5c4d2",        "agencyId": "5DP4iH6HLkQsiKESj6rh",        "locationId": "C2QujeCh8ZnC7al2InWR",        "versionName": "v1",        "description": "AI agent for customer support",        "state": "staging",        "isPublished": false,        "scopes": [],        "nodes": [],        "edges": [],        "uiNodes": [],        "uiEdges": [],        "globalVariables": [],        "inputVariables": [],        "runtimeVariables": [],        "viewport": {          "x": 0,          "y": 0,          "zoom": 1        },        "globalConfig": {},        "createdAt": "2026-03-06T10:37:01.079Z",        "updatedAt": "2026-03-06T10:37:01.079Z",        "deleted": false,        "storedInBucket": true,        "bucketFilePath": "agent-definitions/5DP4iH6HLkQsiKESj6rh/vEoIigWSAw1BQA9DEchD/d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd/3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3.json"      }    ]  },  "traceId": "22dbda99-13d3-4b4d-a30e-c468334e2178"}
```

```json
{  "success": true,  "message": "Agent retrieved successfully",  "agent": {    "id": "d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd",    "agentId": "AgfS2JXWsSN8aXb5c4d2",    "name": "Customer Support Agent",    "description": "AI agent for customer support",    "agencyId": "5DP4iH6HLkQsiKESj6rh",    "locationId": "C2QujeCh8ZnC7al2InWR",    "productSlug": "agent_studio",    "productId": "agent_studio",    "authorId": "usr_123",    "status": "active",    "folderId": "vEoIigWSAw1BQA9DEchD",    "folderName": "Default Agents",    "createdAt": "2026-03-06T10:37:01.013Z",    "updatedAt": "2026-03-06T10:37:01.014Z",    "deleted": false,    "productionVersion": {      "versionId": "Ver1K8sSF2nC7al5InWz",      "versionName": "Content Creation Agent v1",      "isPublished": true,      "inputVariables": [],      "updatedAt": "2026-03-02T06:53:40.570Z"    },    "versions": [      {        "id": "3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3",        "versionId": "Ver1K8sSF2nC7al5InWz",        "agentId": "AgfS2JXWsSN8aXb5c4d2",        "agencyId": "5DP4iH6HLkQsiKESj6rh",        "locationId": "C2QujeCh8ZnC7al2InWR",        "versionName": "v1",        "description": "AI agent for customer support",        "state": "staging",        "isPublished": false,        "scopes": [],        "nodes": [],        "edges": [],        "uiNodes": [],        "uiEdges": [],        "globalVariables": [],        "inputVariables": [],        "runtimeVariables": [],        "viewport": {          "x": 0,          "y": 0,          "zoom": 1        },        "globalConfig": {},        "createdAt": "2026-03-06T10:37:01.079Z",        "updatedAt": "2026-03-06T10:37:01.079Z",        "deleted": false,        "storedInBucket": true,        "bucketFilePath": "agent-definitions/5DP4iH6HLkQsiKESj6rh/vEoIigWSAw1BQA9DEchD/d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd/3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3.json"      }    ]  },  "traceId": "22dbda99-13d3-4b4d-a30e-c468334e2178"}
```


================================================================================

# Get Agent
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/get-agent-by-id`
---

# Get Agent

## /agent-studio/agent/:agentId

Gets a specific agent by its ID for the specified location with all its versions. Returns complete agent metadata and all non-deleted versions (draft, staging, production). locationId is required parameter. The agent must have active status.

## Requestâ

API VersionAvailable options2021-04-15

Agent retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Agent metadata with all active versions

Request trace ID for debugging

```json
{  "success": true,  "message": "Agent retrieved successfully",  "agent": {    "id": "d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd",    "agentId": "AgfS2JXWsSN8aXb5c4d2",    "name": "Customer Support Agent",    "description": "AI agent for customer support",    "agencyId": "5DP4iH6HLkQsiKESj6rh",    "locationId": "C2QujeCh8ZnC7al2InWR",    "productSlug": "agent_studio",    "productId": "agent_studio",    "authorId": "usr_123",    "status": "active",    "folderId": "vEoIigWSAw1BQA9DEchD",    "folderName": "Default Agents",    "createdAt": "2026-03-06T10:37:01.013Z",    "updatedAt": "2026-03-06T10:37:01.014Z",    "deleted": false,    "productionVersion": {      "versionId": "Ver1K8sSF2nC7al5InWz",      "versionName": "Content Creation Agent v1",      "isPublished": true,      "inputVariables": [],      "updatedAt": "2026-03-02T06:53:40.570Z"    },    "versions": [      {        "id": "3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3",        "versionId": "Ver1K8sSF2nC7al5InWz",        "agentId": "AgfS2JXWsSN8aXb5c4d2",        "agencyId": "5DP4iH6HLkQsiKESj6rh",        "locationId": "C2QujeCh8ZnC7al2InWR",        "versionName": "v1",        "description": "AI agent for customer support",        "state": "staging",        "isPublished": false,        "scopes": [],        "nodes": [],        "edges": [],        "uiNodes": [],        "uiEdges": [],        "globalVariables": [],        "inputVariables": [],        "runtimeVariables": [],        "viewport": {          "x": 0,          "y": 0,          "zoom": 1        },        "globalConfig": {},        "createdAt": "2026-03-06T10:37:01.079Z",        "updatedAt": "2026-03-06T10:37:01.079Z",        "deleted": false,        "storedInBucket": true,        "bucketFilePath": "agent-definitions/5DP4iH6HLkQsiKESj6rh/vEoIigWSAw1BQA9DEchD/d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd/3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3.json"      }    ]  },  "traceId": "22dbda99-13d3-4b4d-a30e-c468334e2178"}
```

```json
{  "success": true,  "message": "Agent retrieved successfully",  "agent": {    "id": "d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd",    "agentId": "AgfS2JXWsSN8aXb5c4d2",    "name": "Customer Support Agent",    "description": "AI agent for customer support",    "agencyId": "5DP4iH6HLkQsiKESj6rh",    "locationId": "C2QujeCh8ZnC7al2InWR",    "productSlug": "agent_studio",    "productId": "agent_studio",    "authorId": "usr_123",    "status": "active",    "folderId": "vEoIigWSAw1BQA9DEchD",    "folderName": "Default Agents",    "createdAt": "2026-03-06T10:37:01.013Z",    "updatedAt": "2026-03-06T10:37:01.014Z",    "deleted": false,    "productionVersion": {      "versionId": "Ver1K8sSF2nC7al5InWz",      "versionName": "Content Creation Agent v1",      "isPublished": true,      "inputVariables": [],      "updatedAt": "2026-03-02T06:53:40.570Z"    },    "versions": [      {        "id": "3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3",        "versionId": "Ver1K8sSF2nC7al5InWz",        "agentId": "AgfS2JXWsSN8aXb5c4d2",        "agencyId": "5DP4iH6HLkQsiKESj6rh",        "locationId": "C2QujeCh8ZnC7al2InWR",        "versionName": "v1",        "description": "AI agent for customer support",        "state": "staging",        "isPublished": false,        "scopes": [],        "nodes": [],        "edges": [],        "uiNodes": [],        "uiEdges": [],        "globalVariables": [],        "inputVariables": [],        "runtimeVariables": [],        "viewport": {          "x": 0,          "y": 0,          "zoom": 1        },        "globalConfig": {},        "createdAt": "2026-03-06T10:37:01.079Z",        "updatedAt": "2026-03-06T10:37:01.079Z",        "deleted": false,        "storedInBucket": true,        "bucketFilePath": "agent-definitions/5DP4iH6HLkQsiKESj6rh/vEoIigWSAw1BQA9DEchD/d6a6792d-0d50-4e8f-9c3b-ecd8096d0bdd/3f9d9ab7-5ca4-4e64-8472-eab9e77a0fe3.json"      }    ]  },  "traceId": "22dbda99-13d3-4b4d-a30e-c468334e2178"}
```


================================================================================

# Update Agent
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/update-agent-version`
---

# Update Agent

## /agent-studio/agent/versions/:versionId

Updates a specific agent version by versionId. Supports updating nodes, edges, variables, and configuration.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID for authorization

Version name

Description of the version

Complete array of nodes for the agent workflow. Provide all nodes including unchanged ones.

Complete array of edges connecting the nodes. Provide all edges including unchanged ones.

Global variables accessible throughout the agent workflow

Input variables required from user at execution time

Runtime variables generated during agent execution

Global configuration including prompts and settings

User ID performing the update

User name performing the update

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "versionName": "Customer Support Agent v2",  "description": "Updated version with improved customer handling logic",  "nodes": [    {      "nodeId": "node_1",      "nodeName": "Start",      "type": "start",      "isStartNode": true    },    {      "nodeId": "node_2",      "nodeName": "LLM Node",      "type": "llm",      "nodeConfig": {        "prompt": "How can I help you?",        "llmProvider": "openai",        "llmModel": "gpt-4"      }    }  ],  "edges": [    {      "startNode": "node_1",      "endNode": "node_2"    }  ],  "globalVariables": [    {      "key": "apiKey",      "type": "string",      "value": "your-api-key"    }  ],  "inputVariables": [    {      "key": "customerName",      "type": "string",      "description": "Customer name for personalization"    }  ],  "runtimeVariables": [    {      "key": "sessionId",      "type": "string",      "description": "Current session identifier"    }  ],  "globalConfig": {    "globalPrompt": {      "currentPrompt": "You are a helpful customer support assistant.",      "history": []    }  },  "userId": "usr_abc123def456",  "userName": "John Doe"}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "versionName": "Customer Support Agent v2",  "description": "Updated version with improved customer handling logic",  "nodes": [    {      "nodeId": "node_1",      "nodeName": "Start",      "type": "start",      "isStartNode": true    },    {      "nodeId": "node_2",      "nodeName": "LLM Node",      "type": "llm",      "nodeConfig": {        "prompt": "How can I help you?",        "llmProvider": "openai",        "llmModel": "gpt-4"      }    }  ],  "edges": [    {      "startNode": "node_1",      "endNode": "node_2"    }  ],  "globalVariables": [    {      "key": "apiKey",      "type": "string",      "value": "your-api-key"    }  ],  "inputVariables": [    {      "key": "customerName",      "type": "string",      "description": "Customer name for personalization"    }  ],  "runtimeVariables": [    {      "key": "sessionId",      "type": "string",      "description": "Current session identifier"    }  ],  "globalConfig": {    "globalPrompt": {      "currentPrompt": "You are a helpful customer support assistant.",      "history": []    }  },  "userId": "usr_abc123def456",  "userName": "John Doe"}
```

Version updated successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Updated agent or version data

```json
{  "success": true,  "message": "Agent updated successfully",  "data": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "versionId": "v1a2b3c4d5e6f7g8h9i0",    "name": "Updated Customer Support Agent",    "description": "Updated AI agent with enhanced customer support capabilities",    "status": "active",    "updatedAt": "2024-02-27T11:45:00.000Z"  }}
```

```json
{  "success": true,  "message": "Agent updated successfully",  "data": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "versionId": "v1a2b3c4d5e6f7g8h9i0",    "name": "Updated Customer Support Agent",    "description": "Updated AI agent with enhanced customer support capabilities",    "status": "active",    "updatedAt": "2024-02-27T11:45:00.000Z"  }}
```


================================================================================

# List Agents (Deprecated)
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/get-agents-deprecated`
---

# List Agents (Deprecated)

## /agent-studio/public-api/agents

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Deprecated endpoint - use GET /agent instead.

Lists all active agents that have a published production version for the specified location. locationId is required parameter. Supports pagination using limit and offset.

## Requestâ

API VersionAvailable options2021-04-15

Agents retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

List of agents with metadata

Pagination metadata

```json
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

```json
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```


================================================================================

# Promote to Production
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/promote-and-publish`
---

# Promote to Production

## /agent-studio/agent/versions/:versionId/publish

Promotes a draft version to production.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID for authorization

User ID performing the promotion action

User name performing the promotion action

User email performing the promotion action

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "userId": "usr_abc123def456",  "userName": "John Doe",  "userEmail": "[email protected]"}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "userId": "usr_abc123def456",  "userName": "John Doe",  "userEmail": "[email protected]"}
```

Version promoted and published successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Result data with production and new draft version details

```json
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "[email protected]"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

```json
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "[email protected]"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```


================================================================================

# Associations
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/associations`
---

Documentation for Associations API

## ðï¸Get association key by key name

Using this api you can get standard / user defined association by key

## ðï¸Get association by object keys

Get association by object keys like contacts, custom objects and opportunities. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## ðï¸Update Association By Id

Update Association , Allows you to update labels of an associations. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## ðï¸Delete Association

Delete USER_DEFINED Association By Id, deleting an association will also all the relations for that association

## ðï¸Get association by ID

Using this api you can get SYSTEM_DEFINED / USER_DEFINED association by id

## ðï¸Create Association

Allow you to create contact - contact , contact - custom objects associations, will add more in the future.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## ðï¸Get all associations for a sub-account / location

Get all Associations


================================================================================

# Create Association
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/create-association`
---

# Create Association

## /associations/

Allow you to create contact - contact , contact - custom objects associations, will add more in the future.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Association's Unique key

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

```json
{  "locationId": "string",  "key": "student_teacher",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact"}
```

```json
{  "locationId": "string",  "key": "student_teacher",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Update Agent Metadata
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/update-agent-metadata`
---

# Update Agent Metadata

## /agent-studio/agent/:agentId

Updates agent metadata such as name, description, and status.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID for authorization (cannot be updated)

Name of the agent

Description of the agent

Status of the agentAvailable optionsactiveinactivearchived

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Updated Customer Support Agent",  "description": "Updated AI agent with enhanced customer support capabilities",  "status": "active"}
```

```json
{  "locationId": "C2QujeCh8ZnC7al2InWR",  "name": "Updated Customer Support Agent",  "description": "Updated AI agent with enhanced customer support capabilities",  "status": "active"}
```

Agent metadata updated successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

Updated agent or version data

```json
{  "success": true,  "message": "Agent updated successfully",  "data": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "versionId": "v1a2b3c4d5e6f7g8h9i0",    "name": "Updated Customer Support Agent",    "description": "Updated AI agent with enhanced customer support capabilities",    "status": "active",    "updatedAt": "2024-02-27T11:45:00.000Z"  }}
```

```json
{  "success": true,  "message": "Agent updated successfully",  "data": {    "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",    "versionId": "v1a2b3c4d5e6f7g8h9i0",    "name": "Updated Customer Support Agent",    "description": "Updated AI agent with enhanced customer support capabilities",    "status": "active",    "updatedAt": "2024-02-27T11:45:00.000Z"  }}
```


================================================================================

# Associations API
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/associations-api`
---

# Associations API

Documentation for Associations API

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# List Agents
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/agent-studio/get-agents`
---

# List Agents

## /agent-studio/agent

Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset. Optionally filter by isPublished=true to return only agents with a published production version.

## Requestâ

API VersionAvailable options2021-04-15

Optional filter to return only agents with a published production version

Agents retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success status

Response message

List of agents with metadata

Pagination metadata

```json
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

```json
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```


================================================================================

# Delete Association
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/delete-association`
---

# Delete Association

## /associations/:associationId

Delete USER_DEFINED Association By Id, deleting an association will also all the relations for that association

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Deletion status

Association Id

```json
{  "deleted": true,  "id": "6d6f6e676f5f6576656e7473",  "message": "Association deleted successfully"}
```

```json
{  "deleted": true,  "id": "6d6f6e676f5f6576656e7473",  "message": "Association deleted successfully"}
```


================================================================================

# Create Relation for you associated entities.
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/create-relation`
---

# Create Relation for you associated entities.

## /associations/relations

Create Relation.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Your Sub Account's ID

Association's Id

First Record's Id. For instance, if you have an association between a contact and a custom object, and you specify the contact as the first object while creating the association, then your firstRecordId would be the contactId

Second Record's Id.For instance, if you have an association between a contact and a custom object, and you specify the custom object as the second entity while creating the association, then your secondRecordId would be the customObject record Id

```json
{  "locationId": "clF1LD04GTUKN3b3XuOj",  "associationId": "ve9EPM428h8vShlRW1KT",  "firstRecordId": "ve9EPM428h8vShlRW1KT",  "secondRecordId": "ve9EPM428h8vShlRW1KT"}
```

```json
{  "locationId": "clF1LD04GTUKN3b3XuOj",  "associationId": "ve9EPM428h8vShlRW1KT",  "firstRecordId": "ve9EPM428h8vShlRW1KT",  "secondRecordId": "ve9EPM428h8vShlRW1KT"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Get all associations for a sub-account / location
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/find-associations`
---

# Get all associations for a sub-account / location

## /associations/

Get all Associations

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Get association by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/get-association-by-id`
---

# Get association by ID

## /associations/:associationId

Using this api you can get SYSTEM_DEFINED / USER_DEFINED association by id

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Get association key by key name
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/get-association-key-by-key-name`
---

# Get association key by key name

## /associations/key/:key_name

Using this api you can get standard / user defined association by key

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Get association by object keys
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/get-association-by-object-keys`
---

# Get association by object keys

## /associations/objectKey/:objectKey

Get association by object keys like contacts, custom objects and opportunities. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Delete Relation
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/delete-relation`
---

# Delete Relation

## /associations/relations/:relationId

Delete Relation

## Requestâ

API VersionAvailable options2021-04-15

Your Sub Account's ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Blogs API
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/blogs-api`
---

# Blogs API

Documentation for Blog public API

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# Update Association By Id
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/update-association`
---

# Update Association By Id

## /associations/:associationId

Update Association , Allows you to update labels of an associations. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

```json
{  "firstObjectLabel": "student",  "secondObjectLabel": "tutor"}
```

```json
{  "firstObjectLabel": "student",  "secondObjectLabel": "tutor"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Get all relations By record Id
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/get-relations-by-record-id`
---

# Get all relations By record Id

## /associations/relations/:recordId

Get all relations by record Id

## Requestâ

API VersionAvailable options2021-04-15

Your Sub Account's ID

Association Ids

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

First Objects Association Label (custom_objects.children)

First Objects Association Label (custom_objects.children)

First Objects Key

Second Object Association Label (contact)

Second Objects Key

Association Type can be USER_DEFINED or SYSTEM_DEFINED

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```

```json
{  "locationId": "string",  "id": "ve9EPM428h8vShlRW1KT",  "key": "student",  "firstObjectLabel": "student",  "firstObjectKey": "custom_objects.children",  "secondObjectLabel": "Teacher",  "secondObjectKey": "contact",  "associationType": "USER_DEFINED"}
```


================================================================================

# Create Blog Post
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/create-blog-post`
---

# Create Blog Post

## /blogs/posts

The "Create Blog Post" API allows you create blog post for any given blog site. Please use blogs/post.write

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

You can find the blog id from blog site dashboard link

This needs to be array of category ids, which you can get from the category get api call.

This needs to be author id, which you can get from the author get api call.

Provide ISO timestamp

```json
{  "title": "Your blog title",  "locationId": "Location ID",  "blogId": "Blog ID",  "imageUrl": "Image URl",  "description": "A short description",  "rawHTML": "<h1>Your blog content</h1>",  "status": "This can be PUBLISHED OR SCHEDULED OR ARCHIVED OR DRAFT",  "imageAltText": "Alt text for your blog image",  "categories": [    "9c48df2694a849b6089f9d0d3513efe",    "6683abde331c041f32c07aee"  ],  "tags": [    "blog",    "seo"  ],  "author": "6683abde331c041f32c07aea",  "urlSlug": "any-blog-post-url",  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",  "publishedAt": "2025-02-05T18:30:47.000Z"}
```

```json
{  "title": "Your blog title",  "locationId": "Location ID",  "blogId": "Blog ID",  "imageUrl": "Image URl",  "description": "A short description",  "rawHTML": "<h1>Your blog content</h1>",  "status": "This can be PUBLISHED OR SCHEDULED OR ARCHIVED OR DRAFT",  "imageAltText": "Alt text for your blog image",  "categories": [    "9c48df2694a849b6089f9d0d3513efe",    "6683abde331c041f32c07aee"  ],  "tags": [    "blog",    "seo"  ],  "author": "6683abde331c041f32c07aea",  "urlSlug": "any-blog-post-url",  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",  "publishedAt": "2025-02-05T18:30:47.000Z"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Object containing response data of blog post create.

```json
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

```json
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```


================================================================================

# Get all authors
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/get-all-blog-authors-by-location`
---

# Get all authors

## /blogs/authors

The "Get all authors" Api return the blog authors for a given location ID. Please use "blogs/author.readonly"

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Number of authors to show in the listing

Number of authors to skip in listing

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Array of authors

```json
{  "authors": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "name": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/post/technology"    }  ]}
```

```json
{  "authors": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "name": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/post/technology"    }  ]}
```


================================================================================

# Relations
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/associations/relations`
---

Documentation for Associations API

## ðï¸Create Relation for you associated entities.

Create Relation.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

## ðï¸Get all relations By record Id

Get all relations by record Id

## ðï¸Delete Relation

Delete Relation


================================================================================

# Blogs
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/blogs`
---

Documentation for Blogs

## ðï¸Check url slug

The 'Check url slug' API allows check the blog slug validation which is needed before publishing any blog post. Please use blogs/check-slug.readonly. you can find the POST ID from the post edit url.

## ðï¸Update Blog Post

The 'Update Blog Post' API allows you update blog post for any given blog site. Please use blogs/post-update.write

## ðï¸Create Blog Post

The 'Create Blog Post' API allows you create blog post for any given blog site. Please use blogs/post.write

## ðï¸Get all authors

The 'Get all authors' Api return the blog authors for a given location ID. Please use 'blogs/author.readonly'

## ðï¸Get all categories

The 'Get all categories' Api return the blog categoies for a given location ID. Please use 'blogs/category.readonly'

## ðï¸Get Blog posts by Blog ID

The 'Get Blog posts by Blog ID' API allows you get blog posts for any given blog site using blog ID.Please use blogs/posts.readonly

## ðï¸Get Blogs by Location ID

The 'Get Blogs by Location ID' API allows you get blogs using Location ID.Please use blogs/list.readonly


================================================================================

# Check url slug
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/check-url-slug-exists`
---

# Check url slug

## /blogs/posts/url-slug-exists

The "Check url slug" API allows check the blog slug validation which is needed before publishing any blog post. Please use blogs/check-slug.readonly. you can find the POST ID from the post edit url.

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Indicates whether the url slug exists or not

```json
{  "exists": true}
```

```json
{  "exists": true}
```


================================================================================

# Get all categories
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/get-all-categories-by-location`
---

# Get all categories

## /blogs/categories

The "Get all categories" Api return the blog categoies for a given location ID. Please use "blogs/category.readonly"

## Requestâ

API VersionAvailable options2021-04-15

Number of categories to show in the listing

Number of categories to skip in listing

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Array of categories

```json
{  "categories": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "label": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/doc/category/agency-growth",      "urlSlug": "agency-growth"    }  ]}
```

```json
{  "categories": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "label": "HighLevel",      "locationId": "lMOzIQZne5m6zQ528sT6",      "updatedAt": "2025-01-03T11:06:35.822Z",      "canonicalLink": "https://tryghl.blog/doc/category/agency-growth",      "urlSlug": "agency-growth"    }  ]}
```


================================================================================

# Update Blog Post
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/update-blog-post`
---

# Update Blog Post

## /blogs/posts/:postId

The "Update Blog Post" API allows you update blog post for any given blog site. Please use blogs/post-update.write

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

You can find the blog id from blog site dashboard link

This needs to be array of category ids, which you can get from the category get api call.

This needs to be author id, which you can get from the author get api call.

Provide ISO timestamp

```json
{  "title": "Your blog title",  "locationId": "Location ID",  "blogId": "Blog ID",  "imageUrl": "Image URl",  "description": "A short description",  "rawHTML": "<h1>Your blog content</h1>",  "status": "PUBLISHED",  "imageAltText": "Alt text for your blog image",  "categories": [    "9c48df2694a849b6089f9d0d3513efe",    "6683abde331c041f32c07aee"  ],  "tags": [    "blog",    "seo"  ],  "author": "6683abde331c041f32c07aea",  "urlSlug": "any-blog-post-url",  "wordCount": 100,  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",  "publishedAt": "2025-02-05T18:30:47.000Z"}
```

```json
{  "title": "Your blog title",  "locationId": "Location ID",  "blogId": "Blog ID",  "imageUrl": "Image URl",  "description": "A short description",  "rawHTML": "<h1>Your blog content</h1>",  "status": "PUBLISHED",  "imageAltText": "Alt text for your blog image",  "categories": [    "9c48df2694a849b6089f9d0d3513efe",    "6683abde331c041f32c07aee"  ],  "tags": [    "blog",    "seo"  ],  "author": "6683abde331c041f32c07aea",  "urlSlug": "any-blog-post-url",  "wordCount": 100,  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",  "publishedAt": "2025-02-05T18:30:47.000Z"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Object containing response data of blog post update

```json
{  "updatedBlogPost": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

```json
{  "updatedBlogPost": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```


================================================================================

# Get Blog posts by Blog ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/get-blog-post`
---

# Get Blog posts by Blog ID

## /blogs/posts/all

The "Get Blog posts by Blog ID" API allows you get blog posts for any given blog site using blog ID.Please use blogs/posts.readonly

## Requestâ

API VersionAvailable options2021-04-15

search for any post by name

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Object containing response data of blog posts

```json
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

```json
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```


================================================================================

# Get Blogs by Location ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/blogs/get-blogs`
---

# Get Blogs by Location ID

## /blogs/site/all

The "Get Blogs by Location ID" API allows you get blogs using Location ID.Please use blogs/list.readonly

## Requestâ

API VersionAvailable options2021-04-15

search for any post by name

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Object containing response data of blog

```json
{  "data": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "name": "My blog"    }  ]}
```

```json
{  "data": [    {      "_id": "lMOzIQZne5m6zQ528sT6",      "name": "My blog"    }  ]}
```


================================================================================

# Brand Boards
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/brand-boards`
---

Documentation for Brand Boards API

## ðï¸Get Brand Boards

Retrieves all Brand Boards for a specific location

## ðï¸Get Brand Board

Retrieves a specific Brand Board by its ID

## ðï¸Update a Brand Board

Updates an existing Brand Board

## ðï¸Delete a Brand Board

Deletes a Brand Board

## ðï¸Create a new brand board

Creates a new brand board with logos, colors, and fonts


================================================================================

# Brand Voices
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/brand-voices`
---

Documentation for Brand Boards API

## ðï¸List Brand Voices

Get list of brand voices for a location

## ðï¸Create Brand Voice

Create a brand voice for a location

## ðï¸Get Brand Voice

Get a brand voice by ID

## ðï¸Update Brand Voice

Update a brand voice by ID

## ðï¸Delete Brand Voice

Delete a brand voice by ID

## ðï¸Set Default Brand Voice

Set a brand voice as the default for a location. The previous default will be unset.


================================================================================

# Create Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/create-brand-voice-v-1`
---

# Create Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Create a brand voice for a location

## Requestâ

API VersionAvailable options2021-04-15

Location ID

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Name

Creation type. "manual" creates with provided custom answers, "url" generates answers from a website, "description" generates answers from a text descriptionAvailable optionsmanualurldescription

Website URL to generate brand voice from. Required when type is "url"

Company description to generate brand voice from. Required when type is "description", optional when type is "url"

Brand voice answers. Required when type is "manual"

```json
{  "name": "My Brand Voice",  "type": "manual",  "url": "https://example.com",  "description": "We are a tech company focused on innovative solutions for small businesses",  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management"  }}
```

```json
{  "name": "My Brand Voice",  "type": "manual",  "url": "https://example.com",  "description": "We are a tech company focused on innovative solutions for small businesses",  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management"  }}
```

Created

* application/json

* SchemaExample (auto)
* Example (auto)

Brand voice ID

Brand voice name

Whether this is the default brand voice

Creation timestamp

Last update timestamp

Location ID

Whether the brand voice has been soft deleted

Brand voice answers

Trace ID of request

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```


================================================================================

# Delete Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/delete-brand-voice-v-1`
---

# Delete Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices/:brandVoiceId

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Delete a brand voice by ID

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Brand voice ID

Success

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the brand voice is deleted

Trace ID of request

```json
{  "deleted": true,  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "deleted": true,  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```


================================================================================

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


================================================================================

# Delete a Brand Board
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/delete-brand-board`
---

# Delete a Brand Board

## /brand-boards/:locationId/:id

Deletes a Brand Board

## Requestâ

API VersionAvailable options2021-04-15

Location ID where the brand board exists

Brand board ID to update, retrieve, or delete

Success

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


================================================================================

# Get Brand Board
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/get-brand-board-by-id`
---

# Get Brand Board

## /brand-boards/:locationId/:id

Retrieves a specific Brand Board by its ID

## Requestâ

API VersionAvailable options2021-04-15

Location ID where the brand board exists

Brand board ID to update, retrieve, or delete

Success

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


================================================================================

# Get Brand Boards
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/get-brand-boards-by-location`
---

# Get Brand Boards

## /brand-boards/:locationId

Retrieves all Brand Boards for a specific location

## Requestâ

API VersionAvailable options2021-04-15

Location ID where the brand boards exist

Maximum number of brand boards to returnDefault value:10

Number of brand boards to skip for paginationDefault value:0

Search term to filter brand boards by nameDefault value:

Include deleted brand boards in resultsDefault value:false

Success

* application/json

* SchemaExample (auto)
* Example (auto)

Array of brand boards for the location

Total number of brand boards matching the query

```json
{  "brandBoards": [    {      "_id": "507f1f77bcf86cd799439011",      "name": "My Brand Board",      "updatedAt": "2024-01-05T12:00:00.000Z",      "default": true,      "meta": {        "updatedBy": "user_abc123",        "lastAction": "UPDATE",        "sourceType": "blank"      }    }  ],  "totalCount": 42}
```

```json
{  "brandBoards": [    {      "_id": "507f1f77bcf86cd799439011",      "name": "My Brand Board",      "updatedAt": "2024-01-05T12:00:00.000Z",      "default": true,      "meta": {        "updatedBy": "user_abc123",        "lastAction": "UPDATE",        "sourceType": "blank"      }    }  ],  "totalCount": 42}
```


================================================================================

# Brand Boards API
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/brand-boards-api`
---

# Brand Boards API

Documentation for Brand Boards API

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# List Brand Voices
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/list-brand-voices-v-1`
---

# List Brand Voices

## /brand-boards/public/v1/locations/:locationId/voices

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Get list of brand voices for a location

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Number of brand voices to return. Defaults to 10, minimum is 1, maximum is 20Possible values: >= 1 and <= 20Default value:10

Possible values: >= 1 and <= 20Default value:10

Number of brand voices to skip for pagination. Defaults to 0, minimum is 0Possible values: >= 0Default value:0

Possible values: >= 0Default value:0

Search text for brand voice name

Whether to return deleted brand voices. Defaults to falseDefault value:false

Success

* application/json

* SchemaExample (auto)
* Example (auto)

List of brand voices

Total count of brand voices

Trace ID of request

```json
{  "items": [    {      "id": "507f1f77bcf86cd799439011",      "name": "My Brand Voice",      "isDefault": false,      "createdAt": "2024-01-05T12:00:00.000Z",      "updatedAt": "2024-01-05T12:00:00.000Z"    }  ],  "total": 25,  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "items": [    {      "id": "507f1f77bcf86cd799439011",      "name": "My Brand Voice",      "isDefault": false,      "createdAt": "2024-01-05T12:00:00.000Z",      "updatedAt": "2024-01-05T12:00:00.000Z"    }  ],  "total": 25,  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```


================================================================================

# Update Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/update-brand-voice-v-1`
---

# Update Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices/:brandVoiceId

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Update a brand voice by ID

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Brand voice ID

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Name

Updated answers

```json
{  "name": "My Brand Voice",  "answers": {    "brandName": "Brand Name",    "toneOfVoice": "Friendly"  }}
```

```json
{  "name": "My Brand Voice",  "answers": {    "brandName": "Brand Name",    "toneOfVoice": "Friendly"  }}
```

Success

* application/json

* SchemaExample (auto)
* Example (auto)

Brand voice ID

Brand voice name

Whether this is the default brand voice

Creation timestamp

Last update timestamp

Location ID

Whether the brand voice has been soft deleted

Brand voice answers

Trace ID of request

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```


================================================================================

# Set Default Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/set-default-brand-voice-v-1`
---

# Set Default Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices/:brandVoiceId/default

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Set a brand voice as the default for a location. The previous default will be unset.

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Brand voice ID

Success

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the operation was successful

Brand voice ID that was set as default

Trace ID of request

```json
{  "success": true,  "brandVoiceId": "507f1f77bcf86cd799439011",  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "success": true,  "brandVoiceId": "507f1f77bcf86cd799439011",  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```


================================================================================

# Businesses
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/businesses`
---

Documentation for business API

## ðï¸Update Business

Update Business

## ðï¸Delete Business

Delete Business

## ðï¸Get Business

Get Business

## ðï¸Get Businesses by Location

Get Businesses by Location

## ðï¸Create Business

Create Business


================================================================================

# Get Brand Voice
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/get-brand-voice-v-1`
---

# Get Brand Voice

## /brand-boards/public/v1/locations/:locationId/voices/:brandVoiceId

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Get a brand voice by ID

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Brand voice ID

Success

* application/json

* SchemaExample (auto)
* Example (auto)

Brand voice ID

Brand voice name

Whether this is the default brand voice

Creation timestamp

Last update timestamp

Location ID

Whether the brand voice has been soft deleted

Brand voice answers

Trace ID of request

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```

```json
{  "id": "507f1f77bcf86cd799439011",  "name": "My Brand Voice",  "isDefault": false,  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z",  "locationId": "oHJiAh0wDG3BzmzACVD6",  "deleted": false,  "answers": {    "brandName": "Acme Inc",    "toneOfVoice": "Professional and friendly",    "targetAudience": "Small business owners",    "customerPainPoints": "Difficulty with time management",    "businessType": "Software Development",    "companyWebsite": "https://example.com",    "companyEmail": "[email protected]",    "companyAddress": "123 Main St, Anytown, CA",    "phone": {      "phoneNumber": "5551234567",      "countryCode": "US"    },    "businessHours": "Mon-Fri 9am-5pm",    "brandPromise": "We deliver on time, every time",    "brandValues": "Integrity, Excellence, Innovation",    "brandPurpose": "To empower small businesses with technology",    "competitiveAdvantage": "Proprietary AI technology",    "risksOfInaction": "Falling behind competitors",    "uniqueSellingProposition": "The only solution that integrates with all major platforms",    "callToAction": "Schedule a demo today"  },  "traceId": "019e4ef5-a65e-4198-8cf9-8e93dca9bda4"}
```


================================================================================

# Create Business
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/create-business`
---

# Create Business

## /businesses/

Create Business

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

```json
{  "name": "Microsoft",  "locationId": "5DP4iH6HLkQsiKESj6rh",  "phone": "+18832327657",  "email": "[email protected]",  "website": "www.xyz.com",  "address": "street adress",  "city": "new york",  "postalCode": "12312312",  "state": "new york",  "country": "us",  "description": "business description"}
```

```json
{  "name": "Microsoft",  "locationId": "5DP4iH6HLkQsiKESj6rh",  "phone": "+18832327657",  "email": "[email protected]",  "website": "www.xyz.com",  "address": "street adress",  "city": "new york",  "postalCode": "12312312",  "state": "new york",  "country": "us",  "description": "business description"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Success Value

Business Response

```json
{  "success": true,  "buiseness": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```

```json
{  "success": true,  "buiseness": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```


================================================================================

# Business API
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/business-api`
---

# Business API

Documentation for business API

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# Delete Business
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/delete-business`
---

# Delete Business

## /businesses/:businessId

Delete Business

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Success value

```json
{  "success": true}
```

```json
{  "success": true}
```


================================================================================

# Update a Brand Board
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/brand-boards/update-brand-board`
---

# Update a Brand Board

## /brand-boards/:locationId/:id

Updates an existing Brand Board

## Requestâ

API VersionAvailable options2021-04-15

Location ID where the brand board exists

Brand board ID to update, retrieve, or delete

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Name of the brand board

Array of logos for the brand board

Array of colors for the brand board

Array of fonts for the brand board

Set as the default brand board for this location

Parent folder ID in media library (reserved for future use)

```json
{  "name": "My Brandboard 2",  "logos": [    {      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": true,  "parentId": "507f1f77bcf86cd799439011"}
```

```json
{  "name": "My Brandboard 2",  "logos": [    {      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": true,  "parentId": "507f1f77bcf86cd799439011"}
```

Success

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


================================================================================

# Get Business
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/get-business`
---

# Get Business

## /businesses/:businessId

Get Business

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Business Response

```json
{  "business": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```

```json
{  "business": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```


================================================================================

# Update Business
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/update-business`
---

# Update Business

## /businesses/:businessId

Update Business

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

```json
{  "name": "Microsoft",  "phone": "+18832327657",  "email": "[email protected]",  "postalCode": "12312312",  "website": "www.xyz.com",  "address": "street adress",  "state": "new york",  "city": "new york",  "country": "us",  "description": "business description"}
```

```json
{  "name": "Microsoft",  "phone": "+18832327657",  "email": "[email protected]",  "postalCode": "12312312",  "website": "www.xyz.com",  "address": "street adress",  "state": "new york",  "city": "new york",  "country": "us",  "description": "business description"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Success Value

Business Response

```json
{  "success": true,  "buiseness": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```

```json
{  "success": true,  "buiseness": {    "id": "63771dcac1116f0e21de8e12",    "name": "Microsoft",    "phone": "string",    "email": "[email protected]",    "website": "microsoft.com",    "address": "string",    "city": "string",    "description": "string",    "state": "string",    "postalCode": "string",    "country": "united states",    "updatedBy": {},    "locationId": "string",    "createdBy": {},    "createdAt": "2024-07-29T15:51:28.071Z",    "updatedAt": "2024-07-29T15:51:28.071Z"  }}
```


================================================================================

# Apply user availability schedule to a calendar
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/add-calendar-to-schedule`
---

# Apply user availability schedule to a calendar

## /calendars/schedules/:id/associations/:calendarId

Associates a calendar with the given schedule by adding the calendarId to a schedule

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the schedule

Unique identifier of the team calendar to add to the schedule

Calendar successfully added to schedule

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the operation was successful

```json
{  "success": true}
```

```json
{  "success": true}
```


================================================================================

# Get Businesses by Location
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/businesses/get-businesses-by-location`
---

# Get Businesses by Location

## /businesses/

Get Businesses by Location

## Requestâ

API VersionAvailable options2021-04-15

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Business Response

```json
{  "businesses": [    {      "id": "63771dcac1116f0e21de8e12",      "name": "Microsoft",      "phone": "string",      "email": "[email protected]",      "website": "microsoft.com",      "address": "string",      "city": "string",      "description": "string",      "state": "string",      "postalCode": "string",      "country": "united states",      "updatedBy": {},      "locationId": "string",      "createdBy": {},      "createdAt": "2024-07-29T15:51:28.071Z",      "updatedAt": "2024-07-29T15:51:28.071Z"    }  ]}
```

```json
{  "businesses": [    {      "id": "63771dcac1116f0e21de8e12",      "name": "Microsoft",      "phone": "string",      "email": "[email protected]",      "website": "microsoft.com",      "address": "string",      "city": "string",      "description": "string",      "state": "string",      "postalCode": "string",      "country": "united states",      "updatedBy": {},      "locationId": "string",      "createdBy": {},      "createdAt": "2024-07-29T15:51:28.071Z",      "updatedAt": "2024-07-29T15:51:28.071Z"    }  ]}
```


================================================================================

# Calendars
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/calendars`
---

Documentation for Calendars API

## ðï¸Get Free Slots

Get free slots for a calendar between a date range. Optionally a consumer can also request free slots in a particular timezone and also for a particular user.

## ðï¸Update Calendar

Update calendar by ID.

## ðï¸Get Calendar

Get calendar by ID

## ðï¸Delete Calendar

Delete calendar by ID

## ðï¸Get Calendars

Get all calendars in a location.

## ðï¸Create Calendar

Create calendar in a location.


================================================================================

# Appointment Notes
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/appointment-notes`
---

Documentation for Calendars API

## ðï¸Get Notes

Get Appointment Notes

## ðï¸Create Note

Create Note

## ðï¸Update Note

Update Note

## ðï¸Delete Note

Delete Note


================================================================================

# Calendar Events
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/calendar-events`
---

Documentation for Calendars API

## ðï¸Create appointment

Create appointment

## ðï¸Update Appointment

Update appointment

## ðï¸Get Appointment

Get appointment by ID

## ðï¸Get Calendar Events

Get Calendar Events

## ðï¸Get Blocked Slots

Get Blocked Slots

## ðï¸Create Block Slot

Create block slot

## ðï¸Update Block Slot

Update block slot by ID

## ðï¸Delete Event

Delete event by ID


================================================================================

# Availability
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/availability`
---

Documentation for Calendars API

## ðï¸List user availability schedule

Retrieve user availability schedules based on various filters including location, calendar, and user. Supports pagination.

## ðï¸Get user availability schedule

Retrieve a specific schedule by its unique identifier. Returns detailed information including rules, timezone, and associated calendars/users.

## ðï¸Update user availability schedule

Modify an existing schedule by updating its rules, timezone, and name All fields are optional - only provided fields will be updated.

## ðï¸Delete user availability schedule

Permanently remove a schedule and all its associated rules. This action cannot be undone.

## ðï¸Create user availability schedule

Create new schedule with specified rules, timezone, location, user and calendar associations.

## ðï¸Apply user availability schedule to a calendar

Associates a calendar with the given schedule by adding the calendarId to a schedule

## ðï¸Remove user availability schedule from a calendar

Removes the association between a team calendar and the given schedule by removing the calendarId from the schedule

## ðï¸Create event calendar availability schedule

Create a new availability schedule specifically for an event calendar. The calendar ID is provided in the path, and schedule rules and timezone are provided in the request body.

## ðï¸Get event calendar availability schedule

Retrieve the availability schedule for a specific event calendar. Returns the schedule associated with the calendar ID provided in the path.

## ðï¸Update event calendar availability schedule

Update the availability schedule for a specific event calendar. Only provided fields will be updated. The calendar ID is provided in the path.


================================================================================

# Calendar Groups
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/calendar-groups`
---

Documentation for Calendars API

## ðï¸Get Groups

Get all calendar groups in a location.

## ðï¸Create Calendar Group

Create Calendar Group

## ðï¸Validate group slug

Validate if group slug is available or not.

## ðï¸Delete Group

Delete Group

## ðï¸Update Group

Update Group by group ID

## ðï¸Disable Group

Disable Group


================================================================================

# Calendar Resources: Rooms & Equipments
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/calendar-resources-rooms-equipments`
---

Documentation for Calendars API

## ðï¸Get Calendar Resource

Get calendar resource by ID (Services V1)

## ðï¸Update Calendar Resource

Update calendar resource by ID (Services V1)

## ðï¸Delete Calendar Resource

Delete calendar resource by ID (Services V1)

## ðï¸List Calendar Resources

List calendar resources by resource type and location ID (Services V1)

## ðï¸Create Calendar Resource

Create calendar resource by resource type (Services V1)


================================================================================

# Calendars API
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/calendars-api`
---

# Calendars API

Documentation for Calendars API

## Authenticationâ

* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer AuthHTTP: Bearer Auth
* HTTP: Bearer Auth

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Sub-Account.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT

Use the Access Token generated with user type as Agency.Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

Security Scheme Type:httpHTTP Authorization Scheme:bearerBearer format:JWT

httpHTTP Authorization Scheme:bearerBearer format:JWT

HTTP Authorization Scheme:bearerBearer format:JWT

bearerBearer format:JWT

Bearer format:JWT

JWT


================================================================================

# Create appointment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-appointment`
---

# Create appointment

## /calendars/events/appointments

Create appointment

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

* If address is provided in the request body, the meetingLocationType defaults to custom.
* This value can be found in calendar.locationConfigurationsor calendar.teamMembers[].locationConfigurations
* false - If only meetingLocationId is provided
* true - If only meetingLocationType is provided

Title

Meeting location type.

* If address is provided in the request body, the meetingLocationType defaults to custom.

The unique identifier for the meeting location.

* This value can be found in calendar.locationConfigurationsor calendar.teamMembers[].locationConfigurations

Flag to override location config

* false - If only meetingLocationId is provided
* true - If only meetingLocationType is provided

Appointment statusAvailable optionsnewconfirmedcancelledshowednoshowinvalidcompletedactive

Assigned User Id

Appointment Description

Appointment Address

If set to true, the minimum scheduling notice and date range would be ignored

If set to false, the automations will not run. Defaults to trueDefault value: true

If true the time slot validation would be avoided for any appointment creation (even the ignoreDateRange)

RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. The rrule only be applied if ignoreFreeSlotValidation is true.

Calendar Id

Location Id

Contact Id

Start Time

End Time

```json
{  "title": "Test Event",  "meetingLocationType": "custom",  "meetingLocationId": "custom_0",  "overrideLocationConfig": true,  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "description": "Booking a call to discuss the project",  "address": "Zoom",  "ignoreDateRange": false,  "toNotify": false,  "ignoreFreeSlotValidation": true,  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

```json
{  "title": "Test Event",  "meetingLocationType": "custom",  "meetingLocationId": "custom_0",  "overrideLocationConfig": true,  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "description": "Booking a call to discuss the project",  "address": "Zoom",  "ignoreDateRange": false,  "toNotify": false,  "ignoreFreeSlotValidation": true,  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Calendar Id

Location Id

Contact Id

Start Time

End Time

Title

Meeting Location TypeDefault value: default

Appointment statusAvailable optionsnewconfirmedcancelledshowednoshowinvalidactivecompleted

Assigned User Id

Appointment Address

true if the event is recurring otherwise false

RRULE as per the iCalendar (RFC 5545) specification for recurring events

Date Added

Date Updated

Id

```json
{  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "title": "Test Event",  "meetingLocationType": "custom",  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "address": "Zoom",  "isRecurring": "true",  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "dateAdded": "2021-06-23T03:30:00+05:30",  "dateUpdated": "2021-06-23T04:30:00+05:30",  "id": "0TkCdp9PfvLeWKYRRvIz"}
```

```json
{  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "title": "Test Event",  "meetingLocationType": "custom",  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "address": "Zoom",  "isRecurring": "true",  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "dateAdded": "2021-06-23T03:30:00+05:30",  "dateUpdated": "2021-06-23T04:30:00+05:30",  "id": "0TkCdp9PfvLeWKYRRvIz"}
```


================================================================================

# Create Block Slot
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-block-slot`
---

# Create Block Slot

## /calendars/events/block-slots

Create block slot

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Title

Either calendarId or assignedUserId can be set, not both.

Either calendarId or assignedUserId can be set, not both.

Location Id

Start Time

End Time

```json
{  "title": "Test Event",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

```json
{  "title": "Test Event",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Id

Location Id

Title

Start Time

End Time

Calendar id

Assigned User Id

```json
{  "id": "0TkCdp9PfvLeWKYRRvIz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "title": "My event",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "0007BWpSzSwfiuSl0tR2"}
```

```json
{  "id": "0TkCdp9PfvLeWKYRRvIz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "title": "My event",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "0007BWpSzSwfiuSl0tR2"}
```


================================================================================

# Calendar Notifications
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/calendar-notifications`
---

Documentation for Calendars API

## ðï¸Get notifications

Get calendar notifications based on query

## ðï¸Create notification

Create Calendar notifications, either one or multiple. All notification settings must be for single calendar only

## ðï¸Get notification

Find Event notification by notificationId

## ðï¸Update notification

Update Event notification by id

## ðï¸Delete Notification

Delete notification


================================================================================

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


================================================================================

# Create event calendar availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-calendar-schedule`
---

# Create event calendar availability schedule

## /calendars/schedules/event-calendar/:calendarId

Create a new availability schedule specifically for an event calendar. The calendar ID is provided in the path, and schedule rules and timezone are provided in the request body.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the event calendar

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Schedule rules defining when the schedule is active

Timezone for the schedule (IANA timezone identifier)Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York"}
```

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York"}
```

Schedule created successfully for the event calendar

* application/json

* SchemaExample (auto)
* Example (auto)

The event calendar schedule

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```


================================================================================

# Create Calendar Resource
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-calendar-resource`
---

# Create Calendar Resource

## /calendars/resources/:resourceType

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Create calendar resource by resource type (Services V1)

## Requestâ

API VersionAvailable options2021-04-15

Calendar Resource TypeAvailable optionsequipmentsrooms

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Name of the calendar resource

Description of the calendar resource

Quantity of the equipment.

Quantity of the out of service equipment.

Capacity of the room.

Service calendar IDs to be mapped with the resource.

One room can be mapped with multiple service calendars.Possible values: <= 100

Possible values: <= 100

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "Projector",  "description": "Main conference room projector",  "quantity": 5,  "outOfService": 1,  "capacity": 20,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13"  ]}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "Projector",  "description": "Main conference room projector",  "quantity": 5,  "outOfService": 1,  "capacity": 20,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13"  ]}
```

Calendar resource created

* application/json

* SchemaExample (auto)
* Example (auto)

Location ID of the resource

Name of the resource

Type of the calendar resourceAvailable optionsequipmentsrooms

Whether the resource is active

Description of the resource

Quantity of the resource

Indicates if the resource is out of service

Capacity of the resource

Calendar IDs

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```


================================================================================

# Create Calendar Group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-calendar-group`
---

# Create Calendar Group

## /calendars/groups

Create Calendar Group

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Group name

Group description

Group slug

Whether the group is active

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "group a",  "description": "group description",  "slug": "15-mins",  "isActive": true}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "group a",  "description": "group description",  "slug": "15-mins",  "isActive": true}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

The created group object

```json
{  "group": {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "group a",    "slug": "15-mins"  }}
```

```json
{  "group": {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "group a",    "slug": "15-mins"  }}
```


================================================================================

# Create Calendar
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-calendar`
---

# Create Calendar

## /calendars/

Create calendar in a location.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Should the created calendar be active or draftDefault value: true

ð¨ Deprecated! Please use 'Calendar Notifications APIs' instead.

Location ID

Group Id

Team members are required for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member.

Event type for round robin distributionAvailable optionsRoundRobin_OptimizeForAvailabilityRoundRobin_OptimizeForEqualDistribution

Calendar name

Calendar description

Calendar slug for URL

Widget slug

Calendar typeAvailable optionsround_robineventclass_bookingcollectiveservice_bookingpersonal

Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout.Available optionsdefaultclassic

Title for calendar eventsDefault value: {{contact.name}}

```json
{{contact.name}}
```

Color for calendar events in hex formatDefault value: #039be5

Meeting location configuration for event calendar

This controls the duration of the meetingDefault value: 30

Unit for slot duration.Available optionsminshours

Slot interval reflects the amount of time the between booking slots that will be shown in the calendar.Default value: 30

Unit for slot interval.Available optionsminshours

Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up

Unit for slot buffer.Available optionsminshours

Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready

Unit for pre-buffer.Available optionsminshours

Maximum bookings per slot (per user). Maximum seats per slot in case of Class Booking Calendar.Default value: 1

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

Auto-confirm appointmentsDefault value: true

Send alert emails to assigned team member

Alert email address

Send Google invitation emailsDefault value: false

Allow rescheduling of appointmentsDefault value: true

Allow cancellation of appointmentsDefault value: true

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

Maximum bookings per slot (per user). Maximum seats per slot in case of Class Booking Calendar.Default value: 1

Number of appointments that can be booked for a given day

```json
{  "isActive": true,  "locationId": "ocQHyuzHvysMo5N5VsXc",  "groupId": "BqTwX8QFwXzpegMve9EQ",  "teamMembers": [    {      "userId": "ocQHyuzHvysMo5N5VsXc",      "priority": 0.5,      "isPrimary": true    }  ],  "eventType": "RoundRobin_OptimizeForAvailability",  "name": "test calendar",  "description": "this is used for testing",  "slug": "test1",  "widgetSlug": "test1",  "calendarType": "round_robin",  "widgetType": "classic",  "eventTitle": "{{contact.name}}",  "eventColor": "#039BE5",  "locationConfigurations": [    {      "kind": "custom",      "location": "https://meet.google.com/abc-def"    }  ],  "slotDuration": 30,  "slotDurationUnit": "mins",  "slotInterval": 30,  "slotIntervalUnit": "mins",  "slotBuffer": 15,  "slotBufferUnit": "mins",  "preBuffer": 10,  "preBufferUnit": "mins",  "appoinmentPerSlot": 1,  "appoinmentPerDay": 8,  "allowBookingAfter": 4,  "allowBookingAfterUnit": "days",  "allowBookingFor": 30,  "allowBookingForUnit": "days",  "enableRecurring": false,  "recurring": {    "freq": "WEEKLY",    "count": 4,    "bookingOption": "skip",    "bookingOverlapDefaultStatus": "confirmed"  },  "formId": "YlWd2wuCAZQzh2cH1fVZ",  "stickyContact": true,  "isLivePaymentMode": false,  "autoConfirm": true,  "shouldSendAlertEmailsToAssignedMember": false,  "alertEmail": "[email protected]",  "googleInvitationEmails": true,  "allowReschedule": true,  "allowCancellation": true,  "shouldAssignContactToTeamMember": true,  "shouldSkipAssigningContactForExisting": false,  "notes": "Please arrive 10 minutes early.",  "pixelId": "1234567890",  "formSubmitType": "ThankYouMessage",  "formSubmitRedirectURL": "https://example.com/thank-you",  "formSubmitThanksMessage": "Thank you for booking!",  "guestType": "count_only",  "consentLabel": "I confirm that I want to receive content from this company using any contact information I provide.",  "calendarCoverImage": "https://path-to-image.com",  "lookBusyConfig": {    "enabled": true,    "lookBusyPercentage": 50  },  "appointmentPerSlot": 1,  "appointmentPerDay": 8}
```

```json
{  "isActive": true,  "locationId": "ocQHyuzHvysMo5N5VsXc",  "groupId": "BqTwX8QFwXzpegMve9EQ",  "teamMembers": [    {      "userId": "ocQHyuzHvysMo5N5VsXc",      "priority": 0.5,      "isPrimary": true    }  ],  "eventType": "RoundRobin_OptimizeForAvailability",  "name": "test calendar",  "description": "this is used for testing",  "slug": "test1",  "widgetSlug": "test1",  "calendarType": "round_robin",  "widgetType": "classic",  "eventTitle": "{{contact.name}}",  "eventColor": "#039BE5",  "locationConfigurations": [    {      "kind": "custom",      "location": "https://meet.google.com/abc-def"    }  ],  "slotDuration": 30,  "slotDurationUnit": "mins",  "slotInterval": 30,  "slotIntervalUnit": "mins",  "slotBuffer": 15,  "slotBufferUnit": "mins",  "preBuffer": 10,  "preBufferUnit": "mins",  "appoinmentPerSlot": 1,  "appoinmentPerDay": 8,  "allowBookingAfter": 4,  "allowBookingAfterUnit": "days",  "allowBookingFor": 30,  "allowBookingForUnit": "days",  "enableRecurring": false,  "recurring": {    "freq": "WEEKLY",    "count": 4,    "bookingOption": "skip",    "bookingOverlapDefaultStatus": "confirmed"  },  "formId": "YlWd2wuCAZQzh2cH1fVZ",  "stickyContact": true,  "isLivePaymentMode": false,  "autoConfirm": true,  "shouldSendAlertEmailsToAssignedMember": false,  "alertEmail": "[email protected]",  "googleInvitationEmails": true,  "allowReschedule": true,  "allowCancellation": true,  "shouldAssignContactToTeamMember": true,  "shouldSkipAssigningContactForExisting": false,  "notes": "Please arrive 10 minutes early.",  "pixelId": "1234567890",  "formSubmitType": "ThankYouMessage",  "formSubmitRedirectURL": "https://example.com/thank-you",  "formSubmitThanksMessage": "Thank you for booking!",  "guestType": "count_only",  "consentLabel": "I confirm that I want to receive content from this company using any contact information I provide.",  "calendarCoverImage": "https://path-to-image.com",  "lookBusyConfig": {    "enabled": true,    "lookBusyPercentage": 50  },  "appointmentPerSlot": 1,  "appointmentPerDay": 8}
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


================================================================================

# Create Service Booking
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-service-booking`
---

# Create Service Booking

## /calendars/services/bookings

Create a new service booking

## Requestâ

API VersionAvailable options2021-04-15

If true the time slot validation would be avoided for any booking creation/update (even the skipSchedulingNotice)Default value:false

If set to true, the minimum scheduling notice and date range would be ignoredDefault value:false

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Contact ID

Start Time

End Time

Timezone

Services

Service Location ID (If not provided, then the default service location will be used)

Meeting Location (If service location is an ask the booker, then the meeting location is required)

Service Booking Title

Status. (If not provided, the status configured in Service Global Settings will be used.)Available optionsconfirmednew

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "timezone": "America/New_York",  "services": [    {      "id": "a3b4c5d6e7f8901234567890",      "staffId": "8MkU36Wps2w5bRbuGtw3"    }  ],  "serviceLocationId": "65e5f6dfacf123513228d384",  "meetingLocation": "123 Main St, Anytown, USA",  "title": "Service Appointment",  "status": "confirmed"}
```

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "timezone": "America/New_York",  "services": [    {      "id": "a3b4c5d6e7f8901234567890",      "staffId": "8MkU36Wps2w5bRbuGtw3"    }  ],  "serviceLocationId": "65e5f6dfacf123513228d384",  "meetingLocation": "123 Main St, Anytown, USA",  "title": "Service Appointment",  "status": "confirmed"}
```

Booking created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Booking ID

Location ID

Contact ID

Service Location ID

Service Booking Title

Start Time

End Time

Services

Timezone

Status

Tells if the booking is deleted

Date Added

Date Updated

Booking booked by metadata

Meeting Location (If service location is an ask the booker, then the meeting location is used for the booking)

Optional informative or warning messages (e.g. meeting location ignored for non-ask-booker locations)

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```


================================================================================

# Create Service
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-service-catalog`
---

# Create Service

## /calendars/services/catalog

Create new service in a location.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Service name

Unique URL-friendly identifier

Assigned staff members (at least one required)

Service description

Service event color (hex)

Service cover image URL

Service category ID (uses default category if not provided)

Payment details (default amount is 0, currency configured in Service Global Settings is used.)

This controls the duration of the appointment

Duration unitAvailable optionsminshours

Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready

Pre-buffer unitAvailable optionsminshours

Post-buffer: Additional time that can be added after an appointment, allowing for extra time to wrap up

Post-buffer unitAvailable optionsminshours

Whether service is private (not shown publicly)

Custom form ID (will be used to display the custom form on the booking page, if only one service is selected)

Service variations (pass empty array for no variations)

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Hair Styling",  "slug": "hair-styling",  "staff": [    {      "id": "65e5f6dfacf123513228d384"    }  ],  "description": "Full hair styling session",  "eventColor": "#66C61C",  "coverImage": "https://example.com/cover.jpg",  "serviceCategoryId": "65e5f6dfacf123513228d381",  "payment": {    "amount": 50,    "deposit": 20,    "depositType": "amount"  },  "serviceDuration": 30,  "serviceDurationUnit": "mins",  "preBuffer": 10,  "preBufferUnit": "mins",  "postBuffer": 15,  "postBufferUnit": "mins",  "isPrivate": false,  "formId": "65e5f6dfacf123513228d390",  "variations": [    {      "name": "Standard Haircut",      "serviceDuration": 30,      "payment": {        "amount": 50      }    }  ]}
```

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Hair Styling",  "slug": "hair-styling",  "staff": [    {      "id": "65e5f6dfacf123513228d384"    }  ],  "description": "Full hair styling session",  "eventColor": "#66C61C",  "coverImage": "https://example.com/cover.jpg",  "serviceCategoryId": "65e5f6dfacf123513228d381",  "payment": {    "amount": 50,    "deposit": 20,    "depositType": "amount"  },  "serviceDuration": 30,  "serviceDurationUnit": "mins",  "preBuffer": 10,  "preBufferUnit": "mins",  "postBuffer": 15,  "postBufferUnit": "mins",  "isPrivate": false,  "formId": "65e5f6dfacf123513228d390",  "variations": [    {      "name": "Standard Haircut",      "serviceDuration": 30,      "payment": {        "amount": 50      }    }  ]}
```

Service created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Service details

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling"  }}
```

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling"  }}
```


================================================================================

# Delete Calendar Resource
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-calendar-resource`
---

# Delete Calendar Resource

## /calendars/resources/:resourceType/:id

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Delete calendar resource by ID (Services V1)

## Requestâ

API VersionAvailable options2021-04-15

Calendar Resource TypeAvailable optionsequipmentsrooms

Calendar Resource ID

Calendar resource deleted

* application/json

* SchemaExample (auto)
* Example (auto)

Success

```json
{  "success": "true"}
```

```json
{  "success": "true"}
```


================================================================================

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


================================================================================

# Delete Calendar
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-calendar`
---

# Delete Calendar

## /calendars/:calendarId

Delete calendar by ID

## Requestâ

API VersionAvailable options2021-04-15

Calendar Id

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Success

```json
{  "success": "true"}
```

```json
{  "success": "true"}
```


================================================================================

# Create user availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-schedule`
---

# Create user availability schedule

## /calendars/schedules

Create new schedule with specified rules, timezone, location, user and calendar associations.

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Schedule rules defining when the schedule is active

Timezone for the schedule (IANA timezone identifier)Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Location ID where this schedule applies

Human-readable name for the schedule

User ID associated with the schedule

Calendar IDs associated with the schedule

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York",  "locationId": "IkqiJlXJ7o9h61tCHHod",  "name": "Business Hours Schedule",  "userId": "IkqiJlXJ7o9h61tCHHod",  "calendarIds": [    "WvVX9LpvlBO6K506xLbp",    "XyZ8MnQrStUvWxYzAbCdEf"  ]}
```

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "09:00",          "to": "17:00"        }      ]    }  ],  "timezone": "America/New_York",  "locationId": "IkqiJlXJ7o9h61tCHHod",  "name": "Business Hours Schedule",  "userId": "IkqiJlXJ7o9h61tCHHod",  "calendarIds": [    "WvVX9LpvlBO6K506xLbp",    "XyZ8MnQrStUvWxYzAbCdEf"  ]}
```

Schedule created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Schedule

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```


================================================================================

# Delete Note
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-appointment-note`
---

# Delete Note

## /calendars/appointments/:appointmentId/notes/:noteId

Delete Note

## Requestâ

API VersionAvailable options2021-04-15

Appointment ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the note was successfully deleted

```json
{  "success": true}
```

```json
{  "success": true}
```


================================================================================

# Create Service Location
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/create-service-location`
---

# Create Service Location

## /calendars/services/locations

Create a new service location

## Requestâ

API VersionAvailable options2021-04-15

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Location name

URL-friendly slug identifier

Phone number

Use a full street address when locationType is offline. Use a user-facing label when locationType is ask_booker.

URL of the cover image for this service location

Location typeAvailable optionsofflineask_booker

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Midtown Therapy Studio",  "slug": "midtown-therapy-studio",  "phone": "+1-212-555-0174",  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",  "locationType": "offline"}
```

```json
{  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Midtown Therapy Studio",  "slug": "midtown-therapy-studio",  "phone": "+1-212-555-0174",  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",  "locationType": "offline"}
```

Service location created successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Service Location ID

Location ID

Location name

Unique URL-friendly identifier for the service location

Whether location is activeDefault value: true

Whether location is private (not shown publicly)Default value: false

URL of the cover image displayed for this location

Location typeAvailable optionsofflineask_booker

Use a full street address when locationType is offline. Use a user-facing label when locationType is ask_booker.

Contact phone number for the service location

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```


================================================================================

# Delete Event
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-event`
---

# Delete Event

## /calendars/events/:eventId

Delete event by ID

## Requestâ

API VersionAvailable options2021-04-15

Event Id or Instance id. For recurring appointments send masterEventId to modify original series.

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

```json
{}
```

```json
{}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the event was successfully deleted

```json
{  "succeeded": true}
```

```json
{  "succeeded": true}
```


================================================================================

# Delete Notification
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-event-notification`
---

# Delete Notification

## /calendars/:calendarId/notifications/:notificationId

Delete notification

## Requestâ

API VersionAvailable options2021-04-15

Calendar ID

Notification ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Result of delete/update operation

```json
{  "message": "Notification deleted successfully"}
```

```json
{  "message": "Notification deleted successfully"}
```


================================================================================

# Delete Group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-group`
---

# Delete Group

## /calendars/groups/:groupId

Delete Group

## Requestâ

API VersionAvailable options2021-04-15

Group Id

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Success

```json
{  "success": "true"}
```

```json
{  "success": "true"}
```


================================================================================

# Delete Service
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-service-catalog`
---

# Delete Service

## /calendars/services/catalog/:serviceId

Delete service by ID.

## Requestâ

API VersionAvailable options2021-04-15

Service ID

Service deleted successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success

Success message

```json
{  "success": true,  "message": "Service deleted successfully"}
```

```json
{  "success": true,  "message": "Service deleted successfully"}
```


================================================================================

# Delete Service Booking
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-service-booking`
---

# Delete Service Booking

## /calendars/services/bookings/:bookingId

Delete a service booking by ID

## Requestâ

API VersionAvailable options2021-04-15

Unique Service Booking ID

Booking deleted successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Indicates if the deletion was successful

Response message

```json
{  "success": true,  "message": "Service booking deleted successfully"}
```

```json
{  "success": true,  "message": "Service booking deleted successfully"}
```


================================================================================

# Delete user availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-schedule`
---

# Delete user availability schedule

## /calendars/schedules/:id

Permanently remove a schedule and all its associated rules. This action cannot be undone.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the schedule to delete

Schedule deleted successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the deletion was successful

```json
{  "success": true}
```

```json
{  "success": true}
```


================================================================================

# Delete Service Location
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/delete-service-location`
---

# Delete Service Location

## /calendars/services/locations/:serviceLocationId

Delete a service location by ID

## Requestâ

API VersionAvailable options2021-04-15

Unique Service Location ID

Service location deleted successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Success

Success message

```json
{  "success": true,  "message": "Service deleted successfully"}
```

```json
{  "success": true,  "message": "Service deleted successfully"}
```


================================================================================

# List user availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-all-schedules`
---

# List user availability schedule

## /calendars/schedules/search

Retrieve user availability schedules based on various filters including location, calendar, and user. Supports pagination.

## Requestâ

API VersionAvailable options2021-04-15

Location ID to filter schedules by

User ID to filter schedules by specific user

Calendar ID for filtering schedules by specific calendar

Number of items to skip for paginationPossible values: >= 0Default value:0

Possible values: >= 0Default value:0

Maximum number of items to return (max 500)Possible values: >= 1 and <= 500Default value:50

Possible values: >= 1 and <= 500Default value:50

Schedules retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Array of schedules

```json
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "ocQHyuzHvysMo5N5VsXc"    }  ]}
```

```json
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "ocQHyuzHvysMo5N5VsXc"    }  ]}
```


================================================================================

# Update Group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/edit-group`
---

# Update Group

## /calendars/groups/:groupId

Update Group by group ID

## Requestâ

API VersionAvailable options2021-04-15

Group Id

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Group name

Group description

Group slug

```json
{  "name": "group a",  "description": "group description",  "slug": "15-mins"}
```

```json
{  "name": "group a",  "description": "group description",  "slug": "15-mins"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

The created group object

```json
{  "group": {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "group a",    "slug": "15-mins"  }}
```

```json
{  "group": {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "group a",    "slug": "15-mins"  }}
```


================================================================================

# Update Appointment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/edit-appointment`
---

# Update Appointment

## /calendars/events/appointments/:eventId

Update appointment

## Requestâ

API VersionAvailable options2021-04-15

Event Id or Instance id. For recurring appointments send masterEventId to modify original series.

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

* If address is provided in the request body, the meetingLocationType defaults to custom.
* This value can be found in calendar.locationConfigurationsor calendar.teamMembers[].locationConfigurations
* false - If only meetingLocationId is provided
* true - If only meetingLocationType is provided

Title

Meeting location type.

* If address is provided in the request body, the meetingLocationType defaults to custom.

The unique identifier for the meeting location.

* This value can be found in calendar.locationConfigurationsor calendar.teamMembers[].locationConfigurations

Flag to override location config

* false - If only meetingLocationId is provided
* true - If only meetingLocationType is provided

Appointment statusAvailable optionsnewconfirmedcancelledshowednoshowinvalidcompletedactive

Assigned User Id

Appointment Description

Appointment Address

If set to true, the minimum scheduling notice and date range would be ignored

If set to false, the automations will not run. Defaults to trueDefault value: true

If true the time slot validation would be avoided for any appointment creation (even the ignoreDateRange)

RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. The rrule only be applied if ignoreFreeSlotValidation is true.

Calendar Id

Start Time

End Time

```json
{  "title": "Test Event",  "meetingLocationType": "custom",  "meetingLocationId": "custom_0",  "overrideLocationConfig": true,  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "description": "Booking a call to discuss the project",  "address": "Zoom",  "ignoreDateRange": false,  "toNotify": false,  "ignoreFreeSlotValidation": true,  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

```json
{  "title": "Test Event",  "meetingLocationType": "custom",  "meetingLocationId": "custom_0",  "overrideLocationConfig": true,  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "description": "Booking a call to discuss the project",  "address": "Zoom",  "ignoreDateRange": false,  "toNotify": false,  "ignoreFreeSlotValidation": true,  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Calendar Id

Location Id

Contact Id

Start Time

End Time

Title

Meeting Location TypeDefault value: default

Appointment statusAvailable optionsnewconfirmedcancelledshowednoshowinvalidactivecompleted

Assigned User Id

Appointment Address

true if the event is recurring otherwise false

RRULE as per the iCalendar (RFC 5545) specification for recurring events

Date Added

Date Updated

Id

```json
{  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "title": "Test Event",  "meetingLocationType": "custom",  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "address": "Zoom",  "isRecurring": "true",  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "dateAdded": "2021-06-23T03:30:00+05:30",  "dateUpdated": "2021-06-23T04:30:00+05:30",  "id": "0TkCdp9PfvLeWKYRRvIz"}
```

```json
{  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "contactId": "0007BWpSzSwfiuSl0tR2",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "title": "Test Event",  "meetingLocationType": "custom",  "appointmentStatus": "confirmed",  "assignedUserId": "0007BWpSzSwfiuSl0tR2",  "address": "Zoom",  "isRecurring": "true",  "rrule": "RRULE:FREQ=DAILY;INTERVAL=1;COUNT=5",  "dateAdded": "2021-06-23T03:30:00+05:30",  "dateUpdated": "2021-06-23T04:30:00+05:30",  "id": "0TkCdp9PfvLeWKYRRvIz"}
```


================================================================================

# Update Block Slot
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/edit-block-slot`
---

# Update Block Slot

## /calendars/events/block-slots/:eventId

Update block slot by ID

## Requestâ

API VersionAvailable options2021-04-15

Event Id or Instance id. For recurring appointments send masterEventId to modify original series.

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Title

Either calendarId or assignedUserId can be set, not both.

Either calendarId or assignedUserId can be set, not both.

Location Id

Start Time

End Time

```json
{  "title": "Test Event",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

```json
{  "title": "Test Event",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "CVokAlI8fgw4WYWoCtQz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30"}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Id

Location Id

Title

Start Time

End Time

Calendar id

Assigned User Id

```json
{  "id": "0TkCdp9PfvLeWKYRRvIz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "title": "My event",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "0007BWpSzSwfiuSl0tR2"}
```

```json
{  "id": "0TkCdp9PfvLeWKYRRvIz",  "locationId": "C2QujeCh8ZnC7al2InWR",  "title": "My event",  "startTime": "2021-06-23T03:30:00+05:30",  "endTime": "2021-06-23T04:30:00+05:30",  "calendarId": "CVokAlI8fgw4WYWoCtQz",  "assignedUserId": "0007BWpSzSwfiuSl0tR2"}
```


================================================================================

# List Calendar Resources
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/fetch-calendar-resources`
---

# List Calendar Resources

## /calendars/resources/:resourceType

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

List calendar resources by resource type and location ID (Services V1)

## Requestâ

API VersionAvailable options2021-04-15

Calendar Resource TypeAvailable optionsequipmentsrooms

Location ID

Maximum number of results

Number of results to skip

Calendar resources listed

* application/json

* SchemaExample (auto)
* Example (auto)

* Array [
* ]

Location ID of the resource

Name of the resource

Type of the calendar resourceAvailable optionsequipmentsrooms

Whether the resource is active

Description of the resource

Quantity of the resource

Indicates if the resource is out of service

Capacity of the resource

Calendar IDs

```json
[  {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "yoga room",    "resourceType": "rooms",    "isActive": true,    "description": "Spacious yoga studio",    "quantity": 3,    "outOfService": 0,    "capacity": 85,    "calendarIds": [      "Jsj0xnlDDjw0SuvX1J13",      "oCM5feFC86FAAbcO7lJK"    ]  }]
```

```json
[  {    "locationId": "ocQHyuzHvysMo5N5VsXc",    "name": "yoga room",    "resourceType": "rooms",    "isActive": true,    "description": "Spacious yoga studio",    "quantity": 3,    "outOfService": 0,    "capacity": 85,    "calendarIds": [      "Jsj0xnlDDjw0SuvX1J13",      "oCM5feFC86FAAbcO7lJK"    ]  }]
```


================================================================================

# Disable Group
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/disable-group`
---

# Disable Group

## /calendars/groups/:groupId/status

Disable Group

## Requestâ

API VersionAvailable options2021-04-15

Group Id

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Is Active?

```json
{  "isActive": true}
```

```json
{  "isActive": true}
```

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Success

```json
{  "success": "true"}
```

```json
{  "success": "true"}
```


================================================================================

# Get Appointment
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-appointment`
---

# Get Appointment

## /calendars/events/appointments/:eventId

Get appointment by ID

## Requestâ

API VersionAvailable options2021-04-15

Event Id or Instance id. For recurring appointments send masterEventId to modify original series.

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Calendar event object

```json
{  "event": {    "id": "ocQHyuzHvysMo5N5VsXc",    "calendarId": "CVokAlI8fgw4WjWoC3IS",    "title": "Appointment with John"  }}
```

```json
{  "event": {    "id": "ocQHyuzHvysMo5N5VsXc",    "calendarId": "CVokAlI8fgw4WjWoC3IS",    "title": "Appointment with John"  }}
```


================================================================================

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


================================================================================

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


================================================================================

# Get Blocked Slots
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-blocked-slots`
---

# Get Blocked Slots

## /calendars/blocked-slots

Get Blocked Slots

## Requestâ

API VersionAvailable options2021-04-15

Location Id

User Id - Owner of an appointment. Either of userId, groupId or calendarId is required

Either of calendarId, userId or groupId is required

Either of groupId, calendarId or userId is required

Start Time (in millis)

End Time (in millis)

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of calendar events

```json
{  "events": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "calendarId": "CVokAlI8fgw4WjWoC3IS",      "title": "Appointment with John"    }  ]}
```

```json
{  "events": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "calendarId": "CVokAlI8fgw4WjWoC3IS",      "title": "Appointment with John"    }  ]}
```


================================================================================

# Get event calendar availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-calendar-schedule`
---

# Get event calendar availability schedule

## /calendars/schedules/event-calendar/:calendarId

Retrieve the availability schedule for a specific event calendar. Returns the schedule associated with the calendar ID provided in the path.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the event calendar

Schedule retrieved successfully for the event calendar

* application/json

* SchemaExample (auto)
* Example (auto)

The event calendar schedule

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```


================================================================================

# Get Calendar
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-calendar`
---

# Get Calendar

## /calendars/:calendarId

Get calendar by ID

## Requestâ

API VersionAvailable options2021-04-15

Calendar Id

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


================================================================================

# Get Calendar Events
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-calendar-events`
---

# Get Calendar Events

## /calendars/events

Get Calendar Events

## Requestâ

API VersionAvailable options2021-04-15

Location Id

User Id - Owner of an appointment. Either of userId, groupId or calendarId is required

Either of calendarId, userId or groupId is required

Either of groupId, calendarId or userId is required

Start Time (in millis)

End Time (in millis)

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of calendar events

```json
{  "events": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "calendarId": "CVokAlI8fgw4WjWoC3IS",      "title": "Appointment with John"    }  ]}
```

```json
{  "events": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "calendarId": "CVokAlI8fgw4WjWoC3IS",      "title": "Appointment with John"    }  ]}
```


================================================================================

# Get Calendar Resource
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-calendar-resource`
---

# Get Calendar Resource

## /calendars/resources/:resourceType/:id

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Get calendar resource by ID (Services V1)

## Requestâ

API VersionAvailable options2021-04-15

Calendar Resource TypeAvailable optionsequipmentsrooms

Calendar Resource ID

Calendar resource fetched

* application/json

* SchemaExample (auto)
* Example (auto)

Location ID of the resource

Name of the resource

Type of the calendar resourceAvailable optionsequipmentsrooms

Whether the resource is active

Description of the resource

Quantity of the resource

Indicates if the resource is out of service

Capacity of the resource

Calendar IDs

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```


================================================================================

# Get Calendars
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-calendars`
---

# Get Calendars

## /calendars/

Get all calendars in a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Group Id

Show draftedDefault value:true

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of calendars

```json
{  "calendars": [    {      "id": "0TkCdp9PfvLeWKYRRvIz",      "name": "test calendar",      "locationId": "ocQHyuzHvysMo5N5VsXc"    }  ]}
```

```json
{  "calendars": [    {      "id": "0TkCdp9PfvLeWKYRRvIz",      "name": "test calendar",      "locationId": "ocQHyuzHvysMo5N5VsXc"    }  ]}
```


================================================================================

# Get user availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-schedule-by-id`
---

# Get user availability schedule

## /calendars/schedules/:id

Retrieve a specific schedule by its unique identifier. Returns detailed information including rules, timezone, and associated calendars/users.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the schedule

Schedule found and retrieved successfully

* application/json

* SchemaExample (auto)
* Example (auto)

Schedule

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "ocQHyuzHvysMo5N5VsXc"  }}
```


================================================================================

# Get Groups
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-groups`
---

# Get Groups

## /calendars/groups

Get all calendar groups in a location.

## Requestâ

API VersionAvailable options2021-04-15

Location Id

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of calendar groups

```json
{  "groups": [    {      "locationId": "ocQHyuzHvysMo5N5VsXc",      "name": "group a",      "slug": "15-mins"    }  ]}
```

```json
{  "groups": [    {      "locationId": "ocQHyuzHvysMo5N5VsXc",      "name": "group a",      "slug": "15-mins"    }  ]}
```


================================================================================

# Get Service Location by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-location-by-id`
---

# Get Service Location by ID

## /calendars/services/locations/:serviceLocationId

Get service location by ID

## Requestâ

API VersionAvailable options2021-04-15

Unique Service Location ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Service Location ID

Location ID

Location name

Unique URL-friendly identifier for the service location

Whether location is activeDefault value: true

Whether location is private (not shown publicly)Default value: false

URL of the cover image displayed for this location

Location typeAvailable optionsofflineask_booker

Use a full street address when locationType is offline. Use a user-facing label when locationType is ask_booker.

Contact phone number for the service location

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```


================================================================================

# Get notifications
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-event-notification`
---

# Get notifications

## /calendars/:calendarId/notifications

Get calendar notifications based on query

## Requestâ

API VersionAvailable options2021-04-15

Calendar ID

Filter by active status

Include deleted notifications

Number of records to returnDefault value:100

Number of records to skipDefault value:0

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


================================================================================

# Get Service by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-catalog-by-id`
---

# Get Service by ID

## /calendars/services/catalog/:serviceId

Get service by ID.

## Requestâ

API VersionAvailable options2021-04-15

Service ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Service details

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling"  }}
```

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling"  }}
```


================================================================================

# Get Service Booking by ID
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-booking-by-id`
---

# Get Service Booking by ID

## /calendars/services/bookings/:bookingId

Get a specific service booking by ID

## Requestâ

API VersionAvailable options2021-04-15

Unique Service Booking ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Booking ID

Location ID

Contact ID

Service Location ID

Service Booking Title

Start Time

End Time

Services

Timezone

Status

Tells if the booking is deleted

Date Added

Date Updated

Booking booked by metadata

Meeting Location (If service location is an ask the booker, then the meeting location is used for the booking)

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA"}
```

```json
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "contactId": "9NkT25Vor1v4aQatFsv2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "title": "John Doe - Hair Styling",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30"    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "deleted": false,  "dateAdded": "2023-09-25T16:00:00+05:30",  "dateUpdated": "2023-09-25T16:00:00+05:30",  "createdBy": {    "userId": "7NkT25Vor1v4aQatFsv2",    "source": "public_api"  },  "meetingLocation": "123 Main St, Anytown, USA"}
```


================================================================================

# Get Service Bookings
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-bookings`
---

# Get Service Bookings

## /calendars/services/bookings

Retrieve service bookings for a location within a given date range, with an optional service location filter.

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Start Time (timestamp in milliseconds as string)

End Time (timestamp in milliseconds as string)

Timezone

Service Location ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

Service Bookings

```json
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "title": "John Doe - Hair Styling",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "timezone": "America/New_York",      "status": "confirmed",      "deleted": false    }  ]}
```

```json
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "title": "John Doe - Hair Styling",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "timezone": "America/New_York",      "status": "confirmed",      "deleted": false    }  ]}
```


================================================================================

# Get Service Locations
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-service-locations`
---

# Get Service Locations

## /calendars/services/locations

Get all service locations

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of service locations

```json
{  "serviceLocations": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Main Office"    }  ]}
```

```json
{  "serviceLocations": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Main Office"    }  ]}
```


================================================================================

# Get Services
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-services-catalog`
---

# Get Services

## /calendars/services/catalog

Get all services in a location.

## Requestâ

API VersionAvailable options2021-04-15

Location ID

Filter by service category ID

Filter services: true = private only, false = public only, unset = all services

Successful response

* application/json

* SchemaExample (auto)
* Example (auto)

List of services

```json
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling"    }  ]}
```

```json
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling"    }  ]}
```


================================================================================

# Service Bookings
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/service-bookings`
---

Documentation for Calendars API

## ðï¸Get Service Bookings

Retrieve service bookings for a location within a given date range, with an optional service location filter.

## ðï¸Create Service Booking

Create a new service booking

## ðï¸Get Service Booking by ID

Get a specific service booking by ID

## ðï¸Update Service Booking

Update an existing service booking

## ðï¸Delete Service Booking

Delete a service booking by ID


================================================================================

# Service Locations
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/service-locations`
---

Documentation for Calendars API

## ðï¸Get Service Locations

Get all service locations

## ðï¸Create Service Location

Create a new service location

## ðï¸Get Service Location by ID

Get service location by ID

## ðï¸Update Service Location

Update an existing service location

## ðï¸Delete Service Location

Delete a service location by ID


================================================================================

# Services
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/services`
---

Documentation for Calendars API

## ðï¸Get Services

Get all services in a location.

## ðï¸Create Service

Create new service in a location.

## ðï¸Get Service by ID

Get service by ID.

## ðï¸Update Service

Update service by ID.

## ðï¸Delete Service

Delete service by ID.


================================================================================

# Remove user availability schedule from a calendar
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/remove-calendar-from-schedule`
---

# Remove user availability schedule from a calendar

## /calendars/schedules/:id/associations/:calendarId

Removes the association between a team calendar and the given schedule by removing the calendarId from the schedule

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the schedule

Unique identifier of the calendar to remove from the schedule

Calendar successfully removed from schedule

* application/json

* SchemaExample (auto)
* Example (auto)

Whether the operation was successful

```json
{  "success": true}
```

```json
{  "success": true}
```


================================================================================

# Update Calendar Resource
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/update-calendar-resource`
---

# Update Calendar Resource

## /calendars/resources/:resourceType/:id

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

Update calendar resource by ID (Services V1)

## Requestâ

API VersionAvailable options2021-04-15

Calendar Resource TypeAvailable optionsequipmentsrooms

Calendar Resource ID

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Location ID

Name of the calendar resource

Description of the calendar resource

Quantity of the equipment.

Quantity of the out of service equipment.

Capacity of the room.

Service calendar IDs to be mapped with the resource.

One room can be mapped with multiple service calendars.Possible values: <= 100

Possible values: <= 100

Whether the resource is active

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "Projector",  "description": "Main conference room projector",  "quantity": 5,  "outOfService": 1,  "capacity": 20,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13"  ],  "isActive": true}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "Projector",  "description": "Main conference room projector",  "quantity": 5,  "outOfService": 1,  "capacity": 20,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13"  ],  "isActive": true}
```

Calendar resource updated

* application/json

* SchemaExample (auto)
* Example (auto)

Location ID of the resource

Name of the resource

Type of the calendar resourceAvailable optionsequipmentsrooms

Whether the resource is active

Description of the resource

Quantity of the resource

Indicates if the resource is out of service

Capacity of the resource

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85}
```

```json
{  "locationId": "ocQHyuzHvysMo5N5VsXc",  "name": "yoga room",  "resourceType": "rooms",  "isActive": true,  "description": "Spacious yoga studio",  "quantity": 3,  "outOfService": 0,  "capacity": 85}
```


================================================================================

# Get Free Slots
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/get-slots`
---

# Get Free Slots

## /calendars/:calendarId/free-slots

Get free slots for a calendar between a date range. Optionally a consumer can also request free slots in a particular timezone and also for a particular user.

## Requestâ

API VersionAvailable options2021-04-15

Calendar Id

Start Date (â ï¸ Important: Date range cannot be more than 31 days)

End Date (â ï¸ Important: Date range cannot be more than 31 days)

The timezone in which the free slots are returned

The user for whom the free slots are returned

The users for whom the free slots are returned

Availability map keyed by date (YYYY-MM-DD)

* application/json

* SchemaExample (auto)
* Example (auto)

```json
{  "2024-10-28": {    "slots": [      "2024-10-28T10:00:00-05:00",      "2024-10-28T11:00:00-05:00"    ]  },  "2024-10-29": {    "slots": [      "2024-10-29T10:00:00-05:00",      "2024-10-29T14:30:00-05:00"    ]  }}
```

```json
{  "2024-10-28": {    "slots": [      "2024-10-28T10:00:00-05:00",      "2024-10-28T11:00:00-05:00"    ]  },  "2024-10-29": {    "slots": [      "2024-10-29T10:00:00-05:00",      "2024-10-29T14:30:00-05:00"    ]  }}
```


================================================================================

# Update Note
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/update-appointment-note`
---

# Update Note

## /calendars/appointments/:appointmentId/notes/:noteId

Update Note

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


================================================================================

# Update event calendar availability schedule
**Source URL:** `https://marketplace.gohighlevel.com/docs/2021-04-15/ghl/calendars/update-calendar-schedule`
---

# Update event calendar availability schedule

## /calendars/schedules/event-calendar/:calendarId

Update the availability schedule for a specific event calendar. Only provided fields will be updated. The calendar ID is provided in the path.

## Requestâ

API VersionAvailable options2021-04-15

Unique identifier of the event calendar

* application/json

* BodyExample (auto)
* Example (auto)

### Bodyrequired

Updated schedule rules defining when the schedule is active

Updated timezone for the schedule (IANA timezone identifier)Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

Possible values: Value must match regular expression ^[A-Za-z_]+/[A-Za-z_]+$

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "08:00",          "to": "18:00"        }      ]    }  ],  "timezone": "America/Los_Angeles"}
```

```json
{  "rules": [    {      "type": "wday",      "day": "monday",      "intervals": [        {          "from": "08:00",          "to": "18:00"        }      ]    }  ],  "timezone": "America/Los_Angeles"}
```

Schedule updated successfully for the event calendar

* application/json

* SchemaExample (auto)
* Example (auto)

The event calendar schedule

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```

```json
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "weekday",        "day": "monday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ]      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp"  }}
```


================================================================================

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


================================================================================

