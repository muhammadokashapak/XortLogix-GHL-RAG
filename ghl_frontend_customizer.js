/**
 * GoHighLevel (GHL) Production Frontend Customization Engine
 * ============================================================================
 * Target Environment: GoHighLevel (HighLevel) Agency Custom JS / Sub-Account Custom Code
 * Capabilities:
 *  1. Dynamic DOM Monitoring (MutationObserver on <body> with debouncing)
 *  2. SPA Route Change Handling ('routeChangeEvent' & history pushState listener)
 *  3. External Script & Web Worker Dynamic Injection (Formula404 wrapper)
 *  4. Internal / Authenticated GHL REST API Invocations (rest_api_call)
 *  5. Custom Dashboard Themes & Role-Based UI Element Customization (rolesPermission)
 * ============================================================================
 */

(function () {
  'use strict';

  console.log("⚡ [GHL Customizer] Initializing Frontend Customization Engine...");

  // ==========================================================================
  // 1. External Script / Web Worker Loader (Formula404 Injection)
  // ==========================================================================
  async function checkforformula404(callback = function () { }) {
    var formula404 = document.createElement('script');
    formula404.id = 'formulaloadedf404';
    formula404.src = "https://scripts.jdfunnel.com/script.php?id=webworker_init404formula";
    formula404.onload = async function () {
      console.log("✅ [GHL Customizer] Formula404 helper loaded successfully.");
      callback();
    };

    if (typeof init_formula_404 === 'undefined' && !document.getElementById('formulaloadedf404')) {
      document.head.append(formula404);
    } else {
      callback();
    }
  }

  // ==========================================================================
  // 2. Safe REST API Invocation Helper
  // ==========================================================================
  async function executeGhlApi(endpoint, method = "GET", payload = null) {
    try {
      if (typeof rest_api_call === "function") {
        return await rest_api_call(endpoint, method, payload);
      } else {
        const baseUrl = "https://services.leadconnectorhq.com";
        const options = {
          method: method,
          headers: {
            "Authorization": `Bearer ${window.GHL_ACCESS_TOKEN || ''}`,
            "Version": "2021-07-28",
            "Content-Type": "application/json"
          }
        };
        if (payload && (method === "POST" || method === "PUT" || method === "PATCH")) {
          options.body = JSON.stringify(payload);
        }
        const res = await fetch(`${baseUrl}/${endpoint.replace(/^\/+/, '')}`, options);
        return await res.json();
      }
    } catch (err) {
      console.error(`❌ [GHL API Error] ${method} ${endpoint}:`, err);
      return null;
    }
  }

  // ==========================================================================
  // 3. Dynamic UI Customization & Role Permissions Handler
  // ==========================================================================
  async function rolesPermission() {
    const currentUrl = window.location.href;
    const isContactDetails = currentUrl.includes("contactsdetails") || currentUrl.includes("/contacts/detail");
    const isDashboard = currentUrl.includes("/dashboard");

    // A. Contact Details Page Customization
    if (isContactDetails) {
      const headerArea = document.querySelector(".contact-details-header, .action-bar, .hl-card-header");
      if (headerArea && !document.querySelector("#ghl-custom-contact-widget-btn")) {
        const btn = document.createElement("button");
        btn.id = "ghl-custom-contact-widget-btn";
        btn.className = "btn btn-primary custom-theme-btn";
        btn.style.margin = "0 8px";
        btn.innerText = "⚡ Fetch Live Contact Details";

        btn.onclick = async () => {
          // Extract contactId from URL (e.g. /contacts/detail/0YMWokxfopxwxDT8KD9A)
          const urlParts = window.location.href.split("/");
          let contactId = urlParts[urlParts.length - 1].split("?")[0];
          if (!contactId || contactId === "contactsdetails") {
            contactId = "0YMWokxfopxwxDT8KD9A"; // fallback reference ID
          }

          console.log(`🔍 [GHL Customizer] Requesting contact record for ID: ${contactId}`);
          const contactData = await executeGhlApi(`contacts/${contactId}`, "GET");
          console.log("📄 [GHL Customizer] Received Contact Data:", contactData);

          if (contactData && contactData.contact) {
            alert(`Contact: ${contactData.contact.name || contactData.contact.email}\nPhone: ${contactData.contact.phone || 'N/A'}`);
          }
        };

        headerArea.appendChild(btn);
      }
    }

    // B. Dashboard Theme & Widget Injector
    if (isDashboard) {
      const dashboardContainer = document.querySelector(".dashboard-container, .hl-dashboard");
      if (dashboardContainer && !document.querySelector("#ghl-custom-kpi-banner")) {
        const banner = document.createElement("div");
        banner.id = "ghl-custom-kpi-banner";
        banner.style.cssText = "background: linear-gradient(135deg, #1e293b, #0f172a); border: 1px solid #334155; border-radius: 12px; padding: 16px; margin: 15px 0; color: #f8fafc; display: flex; justify-content: space-between; align-items: center;";
        banner.innerHTML = `
          <div>
            <h4 style="margin: 0; font-weight: 700; color: #6366f1;">⚡ XortLogix Custom Intelligence Hub</h4>
            <p style="margin: 4px 0 0 0; font-size: 13px; color: #94a3b8;">Real-time Pipeline & CRM Health Monitor</p>
          </div>
          <span style="background: rgba(99, 102, 241, 0.2); color: #818cf8; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600;">Active</span>
        `;
        dashboardContainer.prepend(banner);
      }
    }
  }

  // ==========================================================================
  // 4. Dynamic DOM Monitoring (MutationObserver with Debounce)
  // ==========================================================================
  let mutationDebounceTimer = null;
  const target = document.querySelector("body");
  const config = { childList: true, subtree: true };

  const observer = new MutationObserver(() => {
    if (mutationDebounceTimer) clearTimeout(mutationDebounceTimer);
    mutationDebounceTimer = setTimeout(() => {
      rolesPermission();
    }, 120);
  });

  if (target) {
    observer.observe(target, config);
  }

  // ==========================================================================
  // 5. SPA Route Change Listener ('routeChangeEvent' & History Interceptor)
  // ==========================================================================
  window.addEventListener('routeChangeEvent', () => {
    console.log("📍 [GHL Customizer] Route change event detected:", window.location.href);
    rolesPermission();
  });

  // History state listener fallback for SPA navigation
  (function (history) {
    const pushState = history.pushState;
    history.pushState = function (state) {
      const result = pushState.apply(history, arguments);
      window.dispatchEvent(new Event('routeChangeEvent'));
      return result;
    };
  })(window.history);

  // ==========================================================================
  // 6. Bootstrap Initializer
  // ==========================================================================
  checkforformula404(async () => {
    rolesPermission();
  });

})();
