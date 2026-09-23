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
