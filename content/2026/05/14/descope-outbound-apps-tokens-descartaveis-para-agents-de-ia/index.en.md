---
title: "Descope Outbound Apps: Disposable tokens for AI agents"
date: '2026-05-14T10:00:00-03:00'
slug: descope-outbound-apps-tokens-descartaveis-para-agents-de-ia
lang: en
translationKey: descope-outbound-apps-tokens-descartaveis-para-agents-de-ia-2026-05-14
tags:
  - descope
  - outbound-apps
  - oauth
  - security
  - ai-agents
draft: false
description: "Understanding the Outbound Apps architecture: disposable token vault pattern for OAuth credentials with AI agents and MCP servers."
---

# Understanding Outbound Apps: Token Vault Architecture for OAuth

## The Problem: Managing Third-Party Credentials

When your application needs to access user data from external services (Google Calendar, Salesforce, HubSpot), you face an architectural challenge: **how to store and manage access tokens securely?**

### The Alternatives and Their Problems

**Alternative 1: Own Database**
```
┌─────────┐      ┌──────────────┐      ┌──────────────┐
│  User   │──────│  Your App    │──────│  Your DB     │
└─────────┘      │              │      │ (tokens)     │
                 └──────────────┘      └──────────────┘
```
- You need to implement encryption, automatic refresh, audit
- In case of breach, all user tokens leak
- Complex compliance (SOC2, HIPAA, etc.)

**Alternative 2: Environment Variables**
- Doesn't work for multiple users (each user has their own token)
- Security anti-pattern

**Alternative 3: Specialized Vault (HashiCorp, AWS Secrets Manager)**
- Works, but adds operational complexity
- You still need to implement OAuth logic

## The Token Vault Pattern

A **Token Vault** is an architectural component that:
1. Stores access tokens (OAuth or API keys)
2. Automatically manages lifecycle (refresh, expiration)
3. Provides on-demand access via API
4. Audits all operations

**Outbound Apps** are an implementation of this pattern.

## What Are Outbound Apps

According to the documentation, Outbound Apps can:

1. **Connect to OAuth providers** (Google, Microsoft, LinkedIn, etc.) and manage the entire OAuth lifecycle
2. **Function as a vault** for OAuth tokens AND static API keys

### Main Use Cases

- **Incremental OAuth**: Start with minimal scopes at login, request additional permissions (calendar, contacts) only when needed
- **AI Agents and MCP**: Agents that need to securely access external services
- **Granular Access Control**: Define who can retrieve tokens using policies

## How It Works

### 3-Step Flow

```
1. CREATE APP
   Descope Console → Outbound Apps → + Outbound App
   ├─ Choose OAuth provider OR create "Custom API Key"
   └─ Configure client_id, client_secret, scopes

2. CONNECT USER
   User goes through OAuth flow → Descope stores:
   ├─ Access token
   ├─ Refresh token (if available)
   ├─ Consented scopes
   └─ Provider user ID (tokenSub)

3. USE TOKEN
   Your app calls Descope API → Receives valid access token
   → Uses it on provider API → Discards token
```

### 1. Creating an Outbound App

In the Descope console, you configure:

**For OAuth:**
```yaml
App ID: calendar-integration
Provider: Google Calendar
Client ID: abc123.apps.googleusercontent.com
Client Secret: GOCSPX-xyz789
Scopes:
  - https://www.googleapis.com/auth/calendar.readonly
Endpoints (pre-configured for known providers):
  Authorization: https://accounts.google.com/o/oauth2/v2/auth
  Token: https://oauth2.googleapis.com/token
Callback URL: https://api.descope.com/oauth/callback
```

**For API Key (Custom API Key App):**
```yaml
Type: Custom API Key
App ID: internal-api
Name: My Internal API
```

### 2. Connecting Users

There are 3 ways to connect users:

**A) Frontend SDKs** (React, Next.js, Web)

**B) Descope Flows** (no-code editor)

**C) REST API** directly

Example of starting a connection via API:

```bash
# Start OAuth flow
curl -X POST "https://api.descope.com/v1/oauth/authorize" \
  -H "Authorization: Bearer ${PROJECT_ID}" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "google",
    "redirectUrl": "https://myapp.com/callback"
  }'
```

The user is redirected to Google's consent screen, approves, and Descope stores the tokens.

### 3. Retrieving Tokens

After connecting, you can retrieve tokens in two ways:

#### A) Latest Valid Token (Recommended)

```bash
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/user/token/latest" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "appId": "calendar-integration",
    "userId": "user_123",
    "options": {
      "withRefreshToken": false,
      "forceRefresh": false
    }
  }'
```

**Important**: This API **always** returns a valid access token. If expired, Descope refreshes automatically before returning.

#### B) Token with Specific Scopes

```bash
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/user/token" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "appId": "calendar-integration",
    "userId": "user_123",
    "scopes": [
      "https://www.googleapis.com/auth/calendar.readonly"
    ],
    "options": {
      "withRefreshToken": false
    }
  }'
```

**Note**: Scopes must be **exactly** the same as used in the connection. If not, you get a 404 error.

### API Response

```json
{
  "token": {
    "id": "tok_abc123",
    "appId": "calendar-integration",
    "userId": "user_123",
    "tokenSub": "123456789",  // User ID at Google
    "accessToken": "ya29.a0AXooCgvMep7...",
    "accessTokenType": "Bearer",
    "accessTokenExpiry": "1741107113",  // Unix timestamp
    "hasRefreshToken": true,
    "scopes": [
      "https://www.googleapis.com/auth/calendar.readonly"
    ],
    "lastRefreshTime": "1741103514"
  }
}
```

**Notes:**
- `refreshToken` is only returned if `withRefreshToken: true`
- Expiration is set by OAuth provider (Google), not Descope
- Descope manages refresh, you always receive a valid token

## Tenant-Level Tokens

Besides per-user tokens, you can have per-tenant tokens:

```bash
# Latest tenant token
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/tenant/token/latest" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "appId": "salesforce",
    "tenantId": "tenant_456"
  }'
```

```bash
# Token with specific tenant scopes
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/tenant/token" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "appId": "salesforce",
    "tenantId": "tenant_456",
    "scopes": ["api", "refresh_token"]
  }'
```

## Using the Token on Provider API

After retrieving the token, use it immediately:

```bash
# Example: Google Calendar API
ACCESS_TOKEN="ya29.a0AXooCgvMep7..."

curl "https://www.googleapis.com/calendar/v3/calendars/primary/events" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Important principle**: The token should only exist in memory for the time needed to make the call. Don't store in persistent variables.

## Authentication for Token Retrieval

You can authenticate in two ways:

### 1. Management Key

Use in secure backends where you can store secrets:

```bash
Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}
```

### 2. Inbound App Token

Use in non-secure environments (MCP servers, agents):

```bash
Authorization: Bearer ${PROJECT_ID}:${ACCESS_TOKEN}
```

**Requirement**: The Inbound App Token must include the `outbound.token.fetch` scope. If not, the request is denied.

This allows applying policies: you can block an agent from accessing tokens in real-time, even if the user has already connected the app.

## Custom API Key Apps

For services that don't use OAuth, you can create API Key apps:

```bash
# Create API key app
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/create" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Internal API",
    "description": "API key for internal service"
  }'
```

Then, use flows or APIs to collect and store the user's/tenant's API key.

## Programmatic Management

### Create App

```bash
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/create" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Calendar App",
    "description": "Integration with Google Calendar",
    "logo": "https://example.com/logo.png"
  }'
```

### List Apps

```bash
curl "https://api.descope.com/v1/mgmt/outbound/apps" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}"
```

### Load Specific App

```bash
curl "https://api.descope.com/v1/mgmt/outbound/app/calendar-integration" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}"
```

### Update App

```bash
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/update" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "calendar-integration",
    "name": "Updated Name",
    "description": "Updated description"
  }'
```

### Delete App

```bash
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/delete" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "calendar-integration"
  }'
```

## Error Handling

### Common Status Codes

| Code | Meaning | Common Causes |
|--------|-------------|---------------|
| **401** | Unauthorized | Invalid management key or project ID |
| **403** | Forbidden | Insufficient permissions or tenant access denied |
| **404** | Token not found | User never connected the app, token was cleaned, or incorrect scopes |
| **500** | Server error | Invalid HTTP method (not POST) or malformed JSON payload |

### Example Error Handling

```javascript
async function fetchOutboundToken(appId, userId, scopes = null) {
  const headers = {
    "Authorization": `Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}`,
    "Content-Type": "application/json"
  };
  
  const endpoint = scopes 
    ? "/v1/mgmt/outbound/app/user/token"
    : "/v1/mgmt/outbound/app/user/token/latest";
  
  const body = { appId, userId };
  if (scopes) body.scopes = scopes;
  
  try {
    const response = await fetch(`https://api.descope.com${endpoint}`, {
      method: "POST",
      headers,
      body: JSON.stringify(body)
    });
    
    if (response.status === 404) {
      console.log("Token not found. User needs to connect the app first.");
      return null;
    }
    
    if (response.status === 401) {
      console.log("Invalid credentials. Check PROJECT_ID and MANAGEMENT_KEY.");
      return null;
    }
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error("Error fetching token:", error);
    return null;
  }
}
```

## Security Best Practices

### 1. Minimum Scope

Always request the minimum necessary permissions:

```javascript
// ❌ Bad - Full access
calendar.events  // See, edit, share, delete

// ✅ Good - Read only
calendar.events.readonly
```

### 2. Never Store Access Tokens

```javascript
// ❌ Bad
const token = await fetchToken();  // Store in variable
await callApi1(token);             // Use
await callApi2(token);             // Reuse after 10 minutes

// ✅ Good
async function executeWithFreshToken(operation) {
  const { token } = await fetchToken();  // Always get valid token
  try {
    return await operation(token.accessToken);
  } finally {
    // Token is automatically discarded when scope exits
  }
}
```

### 3. Always Use HTTPS

All calls must use TLS 1.2 or higher.

### 4. Don't Log Tokens

```javascript
// ❌ Bad
console.log("Token:", accessToken);  // Never do this

// ✅ Good
console.log("Token obtained for user:", userId);
console.log("Scopes:", scopes);
console.log("Expires at:", new Date(expiry * 1000));
```

### 5. Key Management

- Rotate Management Keys periodically
- Use Inbound App Tokens for agents/MCP (more granularity)
- Never expose Management Keys in frontend code

### 6. Access Policies

For agents/MCP, configure policies:

```yaml
# Conceptual policy example
- effect: allow
  action: outbound.token.fetch
  resource: app:calendar-integration
  condition:
    - user.role: admin
    
- effect: deny
  action: outbound.token.fetch
  resource: app:calendar-integration
  condition:
    - request.ip not in: ["10.0.0.0/8"]
```

## Implementation Checklist

- [ ] Configure app at OAuth provider with correct redirect URI
- [ ] Create Outbound App in Descope with minimum scopes
- [ ] Implement connection flow (SDK, Flow, or API)
- [ ] Implement token retrieval using Management Key or Inbound App
- [ ] Handle 404 error (user not connected)
- [ ] Use token immediately and discard
- [ ] Implement audit logs (who accessed which token when)
- [ ] Configure access policies if using Inbound Apps
- [ ] Periodic rotation of Management Keys
- [ ] Never log complete access tokens

## Reference Architecture: AI Agent

```
User: "Schedule meeting with client"
    ↓
┌─────────────────────────────────────┐
│  Agent Interface (LLM)              │
│  - Interprets intent                │
│  - Identifies tools: CRM + Calendar │
└─────────────────┬───────────────────┘
                  ↓
┌─────────────────────────────────────┐
│  MCP Server / Backend               │
│                                     │
│  1. Check user permissions          │
│                                     │
│  2. POST /outbound/app/user/token   │
│     → App: salesforce               │
│     → User: user_123                │
│     ← Receive access_token (valid)  │
│                                     │
│  3. Call Salesforce API             │
│     → Fetch contact                 │
│     ← Contact data                  │
│     → Discard token                 │
│                                     │
│  4. POST /outbound/app/user/token   │
│     → App: google-calendar          │
│     → User: user_123                │
│     ← Receive access_token (valid)  │
│                                     │
│  5. Call Google Calendar API        │
│     → Create event                  │
│     ← Confirmation                  │
│     → Discard token                 │
│                                     │
│  6. Audit log                       │
└─────────────────┬───────────────────┘
                  ↓
User: "Meeting scheduled successfully"
```

## Comparison: With vs Without Outbound Apps

### Without Outbound Apps (Traditional)

```
┌─────────┐     ┌──────────┐     ┌────────────┐     ┌──────────┐
│  User   │────▶│ Your App │────▶│ Your DB    │────▶│  Google  │
└─────────┘     └──────────┘     │ (tokens)   │     └──────────┘
                                 └────────────┘
                                 
You need to implement:
✗ Token encryption
✗ Automatic refresh
✗ Access audit
✗ Secret rotation
✗ Compliance (SOC2, etc.)
```

### With Outbound Apps

```
┌─────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  User   │────▶│ Your App │────▶│ Descope  │────▶│  Google  │
└─────────┘     └──────────┘     │ (vault)  │     └──────────┘
                                 └──────────┘
                                 
Descope manages:
✓ Encryption
✓ Automatic refresh
✓ Audit
✓ Lifecycle

Your app only:
✓ Requests token when needed
✓ Uses immediately
✓ Discards
```

## Trade-offs

### Advantages

1. **Security**: Tokens don't transit through your database
2. **Compliance**: Automatic audit integration
3. **Simplicity**: No need to implement refresh logic
4. **Granularity**: Real-time access policies (with Inbound Apps)
5. **Multiple formats**: Supports OAuth and static API keys

### Disadvantages

1. **Latency**: Extra call to Descope API for each operation
2. **Vendor Lock-in**: Dependency on the service
3. **Cost**: Additional service
4. **Complexity**: Another component in the architecture

### When to Use

✅ **Ideal for**:
- Multi-tenant SaaS applications
- AI Agents (MCP servers)
- Strict compliance requirements
- Teams that want to avoid OAuth complexity

❌ **Not ideal for**:
- Simple applications with few integrations
- Cases where latency is critical (< 50ms)
- Projects that cannot depend on external services

## Conclusion

Outbound Apps implement the Token Vault pattern, externalizing the complexity of OAuth credential management. Instead of storing tokens in your database, you retrieve them on-demand via API, use immediately, and discard.

The flow is simple: **connect the user once, retrieve tokens when needed, use and discard**.

This reduces your application's attack surface, simplifies compliance, and lets you focus on business logic instead of token security.

Remember: **the token should only exist in memory for the time strictly necessary to complete the operation**.

## Resources

- [Descope Outbound Apps Docs](https://docs.descope.com/identity-federation/outbound-apps)
- [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
