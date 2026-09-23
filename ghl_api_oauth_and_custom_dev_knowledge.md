# GoHighLevel (GHL) REST API, OAuth 2.0 & Custom Development Comprehensive Knowledge Base

---

## 1. Overview & Architecture Standards

GoHighLevel (HighLevel / LeadConnector) provides a comprehensive API ecosystem and extensibility layer.
* **API Base URL:** `https://services.leadconnectorhq.com`
* **Current API Standard:** REST API v2 (API v1 was deprecated on December 31, 2025).
* **Required Headers:**
  * `Authorization: Bearer <ACCESS_TOKEN_OR_PIT>`
  * `Version: 2021-07-28` (or current API release version)
  * `Content-Type: application/json`
  * `Accept: application/json`

---

## 2. OAuth 2.0 Authorization Flow & Token Management

OAuth 2.0 is required for multi-tenant Marketplace Apps, Agency-wide integrations, and Sub-account level access.

### 2.1 OAuth Endpoints
* **Authorization / Install URL:** `https://marketplace.gohighlevel.com/oauth/chooselocation`
* **Token Exchange / Refresh URL:** `POST https://services.leadconnectorhq.com/oauth/token`

### 2.2 Step 1: User Redirection & Authorization
Direct the user to the GoHighLevel authorization page with required query parameters:
```text
https://marketplace.gohighlevel.com/oauth/chooselocation?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SPACE_SEPARATED_SCOPES}
```
* **Parameters:**
  * `client_id` (string): Your HighLevel App Client ID.
  * `redirect_uri` (string): Pre-configured callback URL in your HighLevel Developer App settings.
  * `response_type` (string): Must be `code`.
  * `scope` (string): Space-separated list of scopes (e.g. `contacts.readonly contacts.write opportunities.write`).

### 2.3 Step 2: Exchange Authorization Code for Tokens
When the user authorizes, HighLevel redirects back to your `redirect_uri` with a `code` query parameter. Send a `POST` request to exchange it:

* **Endpoint:** `POST https://services.leadconnectorhq.com/oauth/token`
* **Content-Type:** `application/x-www-form-urlencoded`
* **Body:**
  * `client_id`: `{CLIENT_ID}`
  * `client_secret`: `{CLIENT_SECRET}`
  * `grant_type`: `authorization_code`
  * `code`: `{AUTHORIZATION_CODE}`
  * `redirect_uri`: `{REDIRECT_URI}`
  * `user_type`: `Location` or `Company`

* **Response Payload (JSON):**
```json
{
  "access_token": "pit-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "token_type": "Bearer",
  "expires_in": 86400,
  "refresh_token": "ref-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "scope": "contacts.readonly contacts.write opportunities.write",
  "userType": "Location",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "companyId": "comp_123456",
  "userId": "user_123456"
}
```

### 2.4 Step 3: Refreshing Expired Access Tokens
Access tokens expire after 24 hours (`expires_in: 86400`). You must use the `refresh_token` to retrieve a new token pair:
* **Endpoint:** `POST https://services.leadconnectorhq.com/oauth/token`
* **Body (`application/x-www-form-urlencoded`):**
  * `client_id`: `{CLIENT_ID}`
  * `client_secret`: `{CLIENT_SECRET}`
  * `grant_type`: `refresh_token`
  * `refresh_token`: `{CURRENT_REFRESH_TOKEN}`
  * `user_type`: `Location` or `Company`

> **Critical Note:** HighLevel uses Refresh Token Rotation. Each refresh generates a new `access_token` AND a new `refresh_token`. Always persist the newly returned refresh token in your database.

### 2.5 Private Integration Tokens (PITs)
For single-location, server-to-server internal integrations where OAuth user flow is not required, use **Private Integration Tokens (PITs)** generated inside Sub-Account Settings -> Integrations / Developer Tools. PITs include scoped permissions and do not expire unless revoked.

### 2.6 Key Scopes Reference
* `contacts.readonly` / `contacts.write` - Contact records, custom fields, tags, tasks, notes.
* `opportunities.readonly` / `opportunities.write` - Pipelines, stages, deal values, lead statuses.
* `locations.readonly` / `locations.write` - Sub-account details, business settings, timezone.
* `locations/customFields.readonly` / `locations/customFields.write` - Schema management for custom fields.
* `locations/customValues.readonly` / `locations/customValues.write` - Manage location custom values.
* `conversations.readonly` / `conversations.write` - Manage message threads.
* `conversations/message.readonly` / `conversations/message.write` - Send SMS, Email, WhatsApp.
* `workflows.readonly` - View workflow triggers and execute contact enrollment.
* `calendars.readonly` / `calendars/events.write` - Appointments, booking slots, schedule calendar events.
* `forms.readonly` / `surveys.readonly` - Form submissions and survey answers.
* `payments.readonly` / `payments/transactions.write` - Invoices, orders, subscriptions, transactions.

---

## 3. Core REST API v2 Endpoints & Implementation

All requests must include `Authorization: Bearer <TOKEN>` and `Version: 2021-07-28`.

### 3.1 Contacts API

#### Create / Upsert Contact
* **Method & Route:** `POST /contacts/`
* **Payload:**
```json
{
  "firstName": "John",
  "lastName": "Doe",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+15551234567",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "gender": "male",
  "address1": "123 Main Street",
  "city": "Austin",
  "state": "TX",
  "postalCode": "78701",
  "country": "US",
  "timezone": "America/Chicago",
  "tags": ["lead", "web-inquiry", "hot"],
  "customFields": [
    {
      "id": "custom_field_id_123",
      "field_value": "VIP Client"
    }
  ]
}
```

#### Update Contact
* **Method & Route:** `PUT /contacts/{contactId}`
* **Payload:** Include only the fields to update (e.g. tags, phone, custom field values).

#### Search / Filter Contacts
* **Method & Route:** `GET /contacts/`
* **Query Parameters:** `locationId={locationId}&query={email_or_phone_or_name}&limit=20`

#### Upsert Contact (Find by email/phone or Create)
* **Method & Route:** `POST /contacts/upsert`
* Deduplicates based on email or phone number in the sub-account.

---

### 3.2 Opportunities & Pipelines API

#### Get Pipelines for Location
* **Method & Route:** `GET /opportunities/pipelines?locationId={locationId}`

#### Create / Move Opportunity
* **Method & Route:** `POST /opportunities/`
* **Payload:**
```json
{
  "pipelineId": "pipeline_abc123",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "Acme Corp Deal",
  "pipelineStageId": "stage_xyz789",
  "status": "open",
  "contactId": "contact_id_999",
  "monetaryValue": 5000,
  "assignedTo": "user_id_456"
}
```

#### Update Opportunity Stage / Status
* **Method & Route:** `PUT /opportunities/{opportunityId}`
* **Payload:** `{"pipelineStageId": "stage_won_111", "status": "won"}`

---

### 3.3 Workflows API

#### Execute / Add Contact to Workflow
* **Method & Route:** `POST /workflows/{workflowId}/execute`
* **Payload:**
```json
{
  "contactId": "contact_id_999",
  "eventStartTime": "2026-03-01T10:00:00Z"
}
```

---

### 3.4 Custom Values & Custom Fields API

#### Get All Custom Values
* **Method & Route:** `GET /locations/{locationId}/customValues`

#### Update Custom Value
* **Method & Route:** `PUT /locations/{locationId}/customValues/{customValueId}`
* **Payload:** `{"name": "Support Email", "value": "support@xortlogix.com"}`

#### Get Custom Fields Schema
* **Method & Route:** `GET /locations/{locationId}/customFields`

---

### 3.5 Outbound & Inbound Webhooks

* **HighLevel Webhook Triggers:** Contact Created, Contact Updated, Tag Added, Opportunity Stage Changed, Form Submitted, Inbound SMS, Appointment Booked.
* **Webhook Payload Structure:** Includes `locationId`, `contact_id`, full contact object, triggered workflow ID, and custom field values.
* **Verification:** Verify webhook authenticity using the webhook signature or custom auth header in your middleware.

---

## 4. Front-End Custom Development Deliverables & Architecture (Company Standards)

When a requirement is **not available as built-in native GoHighLevel functionality**, our front-end development team builds custom solutions using **HTML, CSS, and JavaScript**.

### 4.1 Core Frontend Customization Goals & Deliverables
1. **Custom GHL Features & Widgets:**
   * Dynamic stats widgets and analytics cards injected directly into the HighLevel dashboard using JavaScript and CSS.
   * Real-time external API integrations, custom charts (Chart.js / ApexCharts), database statistics, and interactive calculator widgets.
2. **Custom Data Displays & Modals:**
   * Custom tables, modal popups, data grids, and client portal views rendered directly inside GHL sub-accounts, contact details, or funnel steps.
3. **Custom Dashboard Theme & White-Label CSS Styling:**
   * Overriding default GHL colors with the client's corporate brand palette, gradient headers, sleek dark mode, custom card borders, modern typography, and sidebar re-styling.
4. **Dynamic DOM & SPA Architecture Handling:**
   * HighLevel is a Single Page Application (SPA) where pages, sidebars, and sub-views render dynamically without standard browser reloads.
   * Custom scripts must actively monitor the DOM lifecycle, handle SPA route changes, asynchronously load external dependencies, and securely invoke internal REST API endpoints.

---

### 4.2 Dynamic DOM Monitoring with MutationObserver
Because HighLevel renders UI elements asynchronously, standard `DOMContentLoaded` or `window.onload` only fires once on initial page load. When users switch tabs or open modals, elements are injected dynamically. We use `MutationObserver` on `document.body` to listen for DOM mutations and trigger custom UI rendering or permission management (e.g. `rolesPermission()`).

```javascript
// ============================================================================
// GHL Dynamic DOM Observer & Lifecycle Handler
// ============================================================================

// 1. Select the target root element (body)
let target = document.querySelector("body");

// 2. Define permission and UI customization handler
function rolesPermission() {
  // Check user role or target UI element existence
  const isContactDetails = window.location.href.includes("contactsdetails") || 
                           window.location.href.includes("/contacts/detail");
  
  if (isContactDetails) {
    const actionToolbar = document.querySelector(".contact-details-header, .action-bar");
    if (actionToolbar && !document.querySelector("#custom-ghl-action-btn")) {
      const customBtn = document.createElement("button");
      customBtn.id = "custom-ghl-action-btn";
      customBtn.className = "btn btn-primary custom-theme-btn";
      customBtn.innerText = "⚡ Custom Action";
      customBtn.onclick = () => alert("Custom GHL Action Triggered!");
      actionToolbar.appendChild(customBtn);
    }
  }
}

// 3. Debounced observer callback to prevent high CPU / infinite loops
let mutationTimeout = null;
let observer = new MutationObserver((mutations) => {
  if (mutationTimeout) clearTimeout(mutationTimeout);
  mutationTimeout = setTimeout(() => {
    rolesPermission();
  }, 100);
});

// 4. Configure and attach observer
let config = { childList: true, subtree: true };
if (target) {
  observer.observe(target, config);
}
```

---

### 4.3 SPA Route Change Detection (`routeChangeEvent` & Location Listener)
HighLevel fires internal custom events when navigation occurs within the SPA. Custom scripts must listen to `routeChangeEvent` or monitor `window.location.href` transitions to re-apply page-specific customizations (such as contact detail enhancements, opportunity board adjustments, or custom dashboard widgets).

```javascript
// ============================================================================
// GHL SPA Route Change Event Listener
// ============================================================================

// Listen for HighLevel's native SPA routeChangeEvent
window.addEventListener('routeChangeEvent', (() => {
  const currentUrl = window.location.href;
  const isContactsDetails = currentUrl.includes("contactsdetails") || currentUrl.includes("/contacts/detail");
  const isDashboard = currentUrl.includes("/dashboard");
  const isConversations = currentUrl.includes("/conversations");

  console.log("📍 GHL Route Changed:", currentUrl);

  if (isContactsDetails) {
    // Extract contact ID from URL if present
    const contactIdMatch = currentUrl.match(/contacts\/detail\/([a-zA-Z0-9_-]+)/);
    const contactId = contactIdMatch ? contactIdMatch[1] : null;
    console.log("👤 Contact Details View Loaded. Contact ID:", contactId);
    
    // Invoke contact-specific customization
    rolesPermission();
  } else if (isDashboard) {
    // Render custom dashboard widgets
    renderCustomDashboardWidget();
  }
}));

// Fallback history state interceptor for robust route tracking
(function(history) {
  const pushState = history.pushState;
  history.pushState = function(state) {
    const result = pushState.apply(history, arguments);
    window.dispatchEvent(new Event('routeChangeEvent'));
    return result;
  };
})(window.history);
```

---

### 4.4 External Script Loader & Web Worker Injection (Formula404 Wrapper)
When integrating external libraries (e.g. Formula404, Chart.js, custom CDNs, or web workers), dynamic injection ensures scripts load idempotently without blocking initial dashboard rendering.

```javascript
// ============================================================================
// Asynchronous External Script Loader (e.g., Formula404 / JD Funnel)
// ============================================================================

async function checkforformula404(callback = function () { }) {
  var formula404 = document.createElement('script');
  formula404.id = 'formulaloadedf404';
  formula404.src = "https://scripts.jdfunnel.com/script.php?id=webworker_init404formula";
  formula404.onload = async function () {
    console.log("✅ External helper script loaded successfully.");
    callback();
  };
  
  if (typeof init_formula_404 === 'undefined' && !document.getElementById('formulaloadedf404')) {
    document.head.append(formula404);
  } else {
    callback();
  }
}

// Execute logic after external script is initialized
checkforformula404(async () => {
  console.log("🚀 Initializing custom GHL feature suite with Formula404...");
  // Execute protected frontend logic
});
```

---

### 4.5 Internal & Front-End REST API Invocations (`rest_api_call`)
In customized GHL frontend interfaces, developers can execute internal or authenticated REST API calls directly to fetch live sub-account data (e.g., contact records, custom field values, opportunity stages):

```javascript
// ============================================================================
// Front-End REST API Helper for GHL Sub-Accounts
// ============================================================================

// Example: Fetch contact by ID
async function getContactDetails(contactId) {
  try {
    // Using internal GHL REST API wrapper helper (e.g. provided by environment / formula404)
    if (typeof rest_api_call === "function") {
      const response = await rest_api_call(`contacts/${contactId}`, "GET");
      console.log("📦 Contact API Response:", response);
      return response;
    } else {
      // Direct REST API v2 fallback using access token or session header
      const res = await fetch(`https://services.leadconnectorhq.com/contacts/${contactId}`, {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${window.GHL_ACCESS_TOKEN || ''}`,
          "Version": "2021-07-28",
          "Content-Type": "application/json"
        }
      });
      const data = await res.json();
      return data;
    }
  } catch (error) {
    console.error("❌ Failed to fetch contact data:", error);
    return null;
  }
}
```

---

### 4.6 Custom GoHighLevel Dashboard Theme & CSS Styling
Since HighLevel does not offer complete white-label visual theme flexibility natively, we customize the dashboard appearance using **Custom CSS** injected via Agency Settings -> Custom CSS or Sub-Account Settings -> Custom CSS:

```css
/* ============================================================================
   GoHighLevel Ultra-Modern Custom Dark Theme & Brand Styling
   ============================================================================ */

:root {
  --ghl-primary: #6366f1;
  --ghl-primary-hover: #4f46e5;
  --ghl-bg-dark: #0f172a;
  --ghl-sidebar-bg: #111827;
  --ghl-card-bg: #1e293b;
  --ghl-card-border: #334155;
  --ghl-text-primary: #f8fafc;
  --ghl-text-muted: #94a3b8;
  --ghl-accent-glow: rgba(99, 102, 241, 0.25);
}

/* 1. Custom Sidebar Styling */
#sidebar-v2, .sidebar-v2, .hl_navbar {
  background-color: var(--ghl-sidebar-bg) !important;
  border-right: 1px solid var(--ghl-card-border) !important;
}

#sidebar-v2 .nav-item a:hover, .hl_navbar .nav-link:hover {
  background: rgba(99, 102, 241, 0.15) !important;
  color: var(--ghl-primary) !important;
  border-radius: 8px !important;
}

/* 2. Top Header & Navbar */
.hl_header, .header-v2 {
  background-color: var(--ghl-bg-dark) !important;
  border-bottom: 1px solid var(--ghl-card-border) !important;
}

/* 3. Modern Card & Widget Containers */
.card, .hl_card, .hl_controls--card, .dashboard-widget-card {
  background-color: var(--ghl-card-bg) !important;
  border: 1px solid var(--ghl-card-border) !important;
  border-radius: 14px !important;
  box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.4) !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.card:hover, .hl_card:hover {
  border-color: var(--ghl-primary) !important;
  box-shadow: 0 12px 35px var(--ghl-accent-glow) !important;
}

/* 4. Action Buttons & Brand Badges */
.btn-primary, .hl_btn-primary, .custom-theme-btn {
  background: linear-gradient(135deg, var(--ghl-primary), var(--ghl-primary-hover)) !important;
  border: none !important;
  border-radius: 8px !important;
  font-weight: 600 !important;
  padding: 8px 16px !important;
  box-shadow: 0 4px 12px var(--ghl-accent-glow) !important;
}
```

---

## 5. Decision Framework: Native vs. Custom Solutions

When answering user queries, the assistant must evaluate whether a requirement is possible **Natively** or requires **Custom Development**:

| Requirement | Native GHL Capability | Custom Solution Blueprint |
| :--- | :--- | :--- |
| **Dashboard Color & Theme Styling** | ❌ Not available natively beyond basic logo | ✅ Inject **Custom CSS** in Agency/Location settings to override UI styles, fonts, and dark mode. |
| **Custom Analytics Widgets on Dashboard** | ❌ Standard built-in widgets only | ✅ Build **Custom HTML/JS Widget** that fetches API data and renders via Custom Code or iFrame app. |
| **Dynamic DOM & SPA Event Handling** | ❌ Standard static page rendering | ✅ Use **MutationObserver** + **`routeChangeEvent`** to monitor dynamic DOM rendering and apply role permissions. |
| **External Script / Web Worker Loader** | ❌ No native script package manager | ✅ Inject **Async Script Loader** (`checkforformula404` / dynamic script tag) with idempotency check. |
| **Complex Math / Dynamic Pricing in Forms** | ❌ Basic fixed form fields only | ✅ Inject **Custom JavaScript** in Funnel/Form to dynamically calculate prices and update custom fields. |
| **Multi-System Database Sync (ERP / Custom DB)** | ❌ Limited to native marketplace integrations | ✅ Use **GHL Outbound Webhook** → Middleware (Python/Node.js/Laravel) → **GHL REST API v2** update. |
| **Multi-Location Agency Management App** | ❌ Manual navigation in dashboard | ✅ Build a **Custom OAuth 2.0 Marketplace App** with `locations.readonly` and `contacts.write` scopes. |
| **Custom Customer Portal / Dynamic Data View** | ❌ Standard client portal with limited UI | ✅ Build an external React/Vue/HTML frontend that authenticates via **OAuth 2.0 / REST API v2** and embeds via HighLevel Custom Menu Link. |

---

## 6. Full Code Implementation Examples

### 6.1 Python: Create Contact & Move to Pipeline via REST API v2
```python
import requests

API_TOKEN = "your_access_token_or_pit"
LOCATION_ID = "ve9EPM428h8vShlRW1KT"
BASE_URL = "https://services.leadconnectorhq.com"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Version": "2021-07-28",
    "Content-Type": "application/json"
}

# 1. Create Contact
contact_payload = {
    "firstName": "Alex",
    "lastName": "Rivera",
    "email": "alex.rivera@example.com",
    "phone": "+15559876543",
    "locationId": LOCATION_ID,
    "tags": ["enterprise-lead"]
}

contact_res = requests.post(f"{BASE_URL}/contacts/", json=contact_payload, headers=headers)
contact_data = contact_res.json()
contact_id = contact_data.get("contact", {}).get("id")

# 2. Create Opportunity in Pipeline
opp_payload = {
    "pipelineId": "your_pipeline_id",
    "locationId": LOCATION_ID,
    "name": "Alex Rivera - Enterprise Plan",
    "pipelineStageId": "your_stage_id",
    "status": "open",
    "contactId": contact_id,
    "monetaryValue": 12000
}

opp_res = requests.post(f"{BASE_URL}/opportunities/", json=opp_payload, headers=headers)
print("Opportunity Created:", opp_res.json())
```

### 6.2 JavaScript: Complete HighLevel Frontend Customization Blueprint (SPA, MutationObserver, Route Changes & REST API)
```javascript
// ============================================================================
// GoHighLevel Complete Frontend Customization Script
// Location: Agency Settings -> Custom JS / Sub-Account Custom Code
// ============================================================================

(function () {
  'use strict';

  console.log("⚡ [GHL Customizer] Initializing Frontend Customization Engine...");

  // 1. External Script / Formula404 Loader
  async function checkforformula404(callback = function () { }) {
    var formula404 = document.createElement('script');
    formula404.id = 'formulaloadedf404';
    formula404.src = "https://scripts.jdfunnel.com/script.php?id=webworker_init404formula";
    formula404.onload = async function () {
      console.log("✅ [GHL Customizer] Formula404 helper loaded.");
      callback();
    };
    if (typeof init_formula_404 === 'undefined' && !document.getElementById('formulaloadedf404')) {
      document.head.append(formula404);
    } else {
      callback();
    }
  }

  // 2. Roles & Permissions / Custom UI Injections
  async function rolesPermission() {
    const isContactsDetails = window.location.href.includes("contactsdetails") || 
                             window.location.href.includes("/contacts/detail");

    if (isContactsDetails) {
      const headerArea = document.querySelector(".contact-details-header, .action-bar");
      if (headerArea && !document.querySelector("#ghl-custom-quick-action")) {
        const btn = document.createElement("button");
        btn.id = "ghl-custom-quick-action";
        btn.className = "btn btn-primary custom-theme-btn";
        btn.style.marginLeft = "10px";
        btn.innerText = "⚡ Fetch Custom Data";
        
        btn.onclick = async () => {
          // Extract Contact ID from URL
          const parts = window.location.href.split("/");
          const contactId = parts[parts.length - 1].split("?")[0];
          console.log("🔍 Fetching data for contact:", contactId);
          
          if (typeof rest_api_call === "function") {
            const data = await rest_api_call(`contacts/${contactId}`, "GET");
            console.log("📄 Contact Data:", data);
            alert(`Contact Loaded: ${data.contact ? data.contact.name || data.contact.email : 'Success'}`);
          }
        };

        headerArea.appendChild(btn);
      }
    }
  }

  // 3. Dynamic DOM Mutation Observer
  let debounceTimer = null;
  const targetNode = document.querySelector("body");
  if (targetNode) {
    const observer = new MutationObserver(() => {
      if (debounceTimer) clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        rolesPermission();
      }, 150);
    });

    observer.observe(targetNode, { childList: true, subtree: true });
  }

  // 4. SPA Route Change Listener
  window.addEventListener('routeChangeEvent', () => {
    console.log("🔄 [GHL Customizer] SPA Route changed:", window.location.href);
    rolesPermission();
  });

  // 5. Initialize external helpers
  checkforformula404(async () => {
    rolesPermission();
  });

})();
```
