---
title: "Descope Outbound Apps: Tokens descartáveis para agents de IA"
date: '2026-05-14T10:00:00-03:00'
slug: descope-outbound-apps-tokens-descartaveis-para-agents-de-ia
translationKey: descope-outbound-apps-tokens-descartaveis-para-agents-de-ia-2026-05-14
tags:
  - descope
  - outbound-apps
  - oauth
  - security
  - ai-agents
draft: false
description: "Entendendo a arquitetura de Outbound Apps: padrão de Token Vault para credenciais OAuth com agents de IA e MCP servers."
---

# Entendendo Outbound Apps: Arquitetura de Token Vault para OAuth

## O Problema: Gestão de Credenciais de Terceiros

Quando sua aplicação precisa acessar dados de usuários em serviços externos (Google Calendar, Salesforce, HubSpot), você enfrenta um desafio arquitetural: **como armazenar e gerenciar tokens de acesso de forma segura?**

### As Alternativas e Seus Problemas

**Alternativa 1: Banco de Dados Próprio**
```
┌─────────┐      ┌──────────────┐      ┌──────────────┐
│ Usuário │──────│  Seu App     │──────│  Seu Banco   │
└─────────┘      │              │      │ (tokens)     │
                 └──────────────┘      └──────────────┘
```
- Você precisa implementar criptografia, refresh automático, auditoria
- Em caso de breach, todos os tokens dos usuários vazam
- Compliance complexo (SOC2, HIPAA, etc.)

**Alternativa 2: Variáveis de Ambiente**
- Não funciona para múltiplos usuários (cada usuário tem seu próprio token)
- Anti-padrão de segurança

**Alternativa 3: Vault Especializado (HashiCorp, AWS Secrets Manager)**
- Funciona, mas adiciona complexidade operacional
- Você ainda precisa implementar a lógica de OAuth

## O Padrão Token Vault

Um **Token Vault** é um componente arquitetural que:
1. Armazena tokens de acesso (OAuth ou API keys)
2. Gerencia automaticamente o ciclo de vida (refresh, expiração)
3. Fornece acesso sob demanda via API
4. Audita todas as operações

**Outbound Apps** são uma implementação desse padrão.

## O Que São Outbound Apps

Segundo a documentação, Outbound Apps podem:

1. **Conectar a provedores OAuth** (Google, Microsoft, LinkedIn, etc.) e gerenciar todo o ciclo de vida OAuth
2. **Funcionar como cofre (vault)** para tokens OAuth E chaves de API estáticas

### Casos de Uso Principais

- **OAuth Incremental**: Começar com escopos mínimos no login, solicitar permissões adicionais (calendário, contatos) apenas quando necessário
- **Agents de IA e MCP**: Agents que precisam acessar serviços externos de forma segura
- **Controle de Acesso Granular**: Definir quem pode recuperar tokens usando políticas

## Como Funciona

### Fluxo de 3 Etapas

```
1. CRIAR APP
   Console Descope → Outbound Apps → + Outbound App
   ├─ Escolher provedor OAuth OU criar "Custom API Key"
   └─ Configurar client_id, client_secret, scopes

2. CONECTAR USUÁRIO
   Usuário faz OAuth flow → Descope armazena:
   ├─ Access token
   ├─ Refresh token (se disponível)
   ├─ Escopos consentidos
   └─ ID do usuário no provedor (tokenSub)

3. USAR TOKEN
   Sua aplicação chama API Descope → Recebe access token válido
   → Usa na API do provedor → Descarta token
```

### 1. Criando um Outbound App

No console Descope, você configura:

**Para OAuth:**
```yaml
App ID: calendar-integration
Provedor: Google Calendar
Client ID: abc123.apps.googleusercontent.com
Client Secret: GOCSPX-xyz789
Scopes:
  - https://www.googleapis.com/auth/calendar.readonly
Endpoints (pré-configurados para provedores conhecidos):
  Authorization: https://accounts.google.com/o/oauth2/v2/auth
  Token: https://oauth2.googleapis.com/token
Callback URL: https://api.descope.com/oauth/callback
```

**Para API Key (Custom API Key App):**
```yaml
Tipo: Custom API Key
App ID: internal-api
Nome: Minha API Interna
```

### 2. Conectando Usuários

Existem 3 formas de conectar usuários:

**A) Frontend SDKs** (React, Next.js, Web)

**B) Descope Flows** (editor no-code)

**C) API REST** diretamente

Exemplo de início de conexão via API:

```bash
# Iniciar fluxo OAuth
curl -X POST "https://api.descope.com/v1/oauth/authorize" \
  -H "Authorization: Bearer ${PROJECT_ID}" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "google",
    "redirectUrl": "https://meuapp.com/callback"
  }'
```

O usuário é redirecionado para a tela de consentimento do Google, aprova, e o Descope armazena os tokens.

### 3. Recuperando Tokens

Depois de conectado, você pode recuperar tokens de duas formas:

#### A) Último Token Válido (Recomendado)

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

**Importante**: Esta API **sempre** retorna um access token válido. Se estiver expirado, o Descope faz refresh automaticamente antes de retornar.

#### B) Token com Scopes Específicos

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

**Nota**: Os scopes devem ser **exatamente** os mesmos usados na conexão. Se não forem, recebe erro 404.

### Resposta da API

```json
{
  "token": {
    "id": "tok_abc123",
    "appId": "calendar-integration",
    "userId": "user_123",
    "tokenSub": "123456789",  // ID do usuário no Google
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

**Observações:**
- `refreshToken` só é retornado se `withRefreshToken: true`
- A expiração é definida pelo provedor OAuth (Google), não pelo Descope
- O Descope gerencia o refresh, você sempre recebe um token válido

## Tokens em Nível de Tenant

Além de tokens por usuário, você pode ter tokens por tenant:

```bash
# Último token do tenant
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/tenant/token/latest" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "appId": "salesforce",
    "tenantId": "tenant_456"
  }'
```

```bash
# Token com scopes específicos do tenant
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/tenant/token" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "appId": "salesforce",
    "tenantId": "tenant_456",
    "scopes": ["api", "refresh_token"]
  }'
```

## Usando o Token na API do Provedor

Após recuperar o token, use-o imediatamente:

```bash
# Exemplo: Google Calendar API
ACCESS_TOKEN="ya29.a0AXooCgvMep7..."

curl "https://www.googleapis.com/calendar/v3/calendars/primary/events" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Princípio importante**: O token só deve existir na memória pelo tempo necessário para a chamada. Não armazene em variáveis persistentes.

## Autenticação para Recuperar Tokens

Você pode autenticar de duas formas:

### 1. Management Key

Use em backends seguros onde você pode armazenar secrets:

```bash
Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}
```

### 2. Inbound App Token

Use em ambientes não-seguros (MCP servers, agents):

```bash
Authorization: Bearer ${PROJECT_ID}:${ACCESS_TOKEN}
```

**Requisito**: O Inbound App Token deve incluir o scope `outbound.token.fetch`. Se não tiver, a requisição é negada.

Isso permite aplicar políticas: você pode bloquear um agente de acessar tokens em tempo real, mesmo que o usuário já tenha conectado o app.

## Custom API Key Apps

Para serviços que não usam OAuth, você pode criar apps de API Key:

```bash
# Criar app de API key
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/create" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Internal API",
    "description": "API key para serviço interno"
  }'
```

Depois, use flows ou APIs para coletar e armazenar a API key do usuário/tenant.

## Gerenciamento Programático

### Criar App

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

### Listar Apps

```bash
curl "https://api.descope.com/v1/mgmt/outbound/apps" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}"
```

### Carregar App Específico

```bash
curl "https://api.descope.com/v1/mgmt/outbound/app/calendar-integration" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}"
```

### Atualizar App

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

### Deletar App

```bash
curl -X POST "https://api.descope.com/v1/mgmt/outbound/app/delete" \
  -H "Authorization: Bearer ${PROJECT_ID}:${MANAGEMENT_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "calendar-integration"
  }'
```

## Tratamento de Erros

### Códigos de Status Comuns

| Código | Significado | Causas Comuns |
|--------|-------------|---------------|
| **401** | Unauthorized | Management key ou project ID inválido |
| **403** | Forbidden | Permissões insuficientes ou acesso ao tenant negado |
| **404** | Token not found | Usuário nunca conectou o app, token foi limpo, ou scopes incorretos |
| **500** | Server error | Método HTTP inválido (não POST) ou payload JSON malformado |

### Exemplo de Tratamento

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
      console.log("Token não encontrado. Usuário precisa conectar o app primeiro.");
      return null;
    }
    
    if (response.status === 401) {
      console.log("Credenciais inválidas. Verifique PROJECT_ID e MANAGEMENT_KEY.");
      return null;
    }
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error("Erro ao buscar token:", error);
    return null;
  }
}
```

## Boas Práticas de Segurança

### 1. Escopo Mínimo

Sempre solicite o mínimo de permissões necessário:

```javascript
// ❌ Ruim - Acesso total
calendar.events  // See, edit, share, delete

// ✅ Bom - Apenas leitura
calendar.events.readonly
```

### 2. Nunca Armazene Access Tokens

```javascript
// ❌ Ruim
const token = await fetchToken();  // Guarda na variável
await callApi1(token);             // Usa
await callApi2(token);             // Reusa depois de 10 minutos

// ✅ Bom
async function executeWithFreshToken(operation) {
  const { token } = await fetchToken();  // Sempre pega token válido
  try {
    return await operation(token.accessToken);
  } finally {
    // Token é descartado automaticamente ao sair do escopo
  }
}
```

### 3. Use HTTPS Sempre

Todas as chamadas devem usar TLS 1.2 ou superior.

### 4. Não Logue Tokens

```javascript
// ❌ Ruim
console.log("Token:", accessToken);  // Nunca faça isso

// ✅ Bom
console.log("Token obtido para usuário:", userId);
console.log("Scopes:", scopes);
console.log("Expira em:", new Date(expiry * 1000));
```

### 5. Gerenciamento de Chaves

- Roteie Management Keys periodicamente
- Use Inbound App Tokens para agents/MCP (mais granularidade)
- Nunca exponha Management Keys em código frontend

### 6. Políticas de Acesso

Para agents/MCP, configure políticas:

```yaml
# Exemplo conceitual de política
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

## Checklist de Implementação

- [ ] Configurar app no provedor OAuth com redirect URI correto
- [ ] Criar Outbound App no Descope com scopes mínimos
- [ ] Implementar fluxo de conexão (SDK, Flow ou API)
- [ ] Implementar recuperação de tokens usando Management Key ou Inbound App
- [ ] Tratar erro 404 (usuário não conectado)
- [ ] Usar token imediatamente e descartar
- [ ] Implementar logs de auditoria (quem acessou qual token quando)
- [ ] Configurar políticas de acesso se usando Inbound Apps
- [ ] Rotação periódica de Management Keys
- [ ] Nunca logar access tokens completos

## Arquitetura de Referência: Agent de IA

```
Usuário: "Agende reunião com cliente"
    ↓
┌─────────────────────────────────────┐
│  Interface do Agent (LLM)           │
│  - Interpreta intenção              │
│  - Identifica tools: CRM + Calendar │
└─────────────────┬───────────────────┘
                  ↓
┌─────────────────────────────────────┐
│  MCP Server / Backend               │
│                                     │
│  1. Verifica permissões do usuário  │
│                                     │
│  2. POST /outbound/app/user/token   │
│     → App: salesforce               │
│     → User: user_123                │
│     ← Recebe access_token (válido)  │
│                                     │
│  3. Call Salesforce API             │
│     → Busca contato                 │
│     ← Dados do contato              │
│     → Descarta token                │
│                                     │
│  4. POST /outbound/app/user/token   │
│     → App: google-calendar          │
│     → User: user_123                │
│     ← Recebe access_token (válido)  │
│                                     │
│  5. Call Google Calendar API        │
│     → Cria evento                   │
│     ← Confirmação                   │
│     → Descarta token                │
│                                     │
│  6. Log de auditoria                │
└─────────────────┬───────────────────┘
                  ↓
Usuário: "Reunião agendada com sucesso"
```

## Comparação: Com vs Sem Outbound Apps

### Sem Outbound Apps (Tradicional)

```
┌─────────┐     ┌──────────┐     ┌────────────┐     ┌──────────┐
│ Usuário │────▶│ Seu App  │────▶│ Seu Banco  │────▶│  Google  │
└─────────┘     └──────────┘     │ (tokens)   │     └──────────┘
                                 └────────────┘
                                 
Você precisa implementar:
✗ Criptografia de tokens
✗ Refresh automático
✗ Auditoria de acesso
✗ Rotação de secrets
✗ Compliance (SOC2, etc.)
```

### Com Outbound Apps

```
┌─────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ Usuário │────▶│ Seu App  │────▶│ Descope  │────▶│  Google  │
└─────────┘     └──────────┘     │ (vault)  │     └──────────┘
                                 └──────────┘
                                 
Descope gerencia:
✓ Criptografia
✓ Refresh automático
✓ Auditoria
✓ Ciclo de vida

Sua app só:
✓ Solicita token quando precisa
✓ Usa imediatamente
✓ Descarta
```

## Trade-offs

### Vantagens

1. **Segurança**: Tokens não transitam pelo seu banco
2. **Compliance**: Auditoria automática integrada
3. **Simplicidade**: Sem implementar refresh logic
4. **Granularidade**: Políticas de acesso em tempo real (com Inbound Apps)
5. **Múltiplos formatos**: Suporta OAuth e API keys estáticas

### Desvantagens

1. **Latência**: Chamada extra à API do Descope para cada operação
2. **Vendor Lock-in**: Dependência do serviço
3. **Custo**: Serviço adicional
4. **Complexidade**: Mais um componente na arquitetura

### Quando Usar

✅ **Ideal para**:
- Aplicações SaaS multi-tenant
- Agents de IA (MCP servers)
- Requisitos de compliance rigorosos
- Equipes que querem evitar complexidade OAuth

❌ **Não ideal para**:
- Aplicações simples com poucas integrações
- Casos onde latência é crítica (< 50ms)
- Projetos que não podem depender de serviços externos

## Conclusão

Outbound Apps implementam o padrão Token Vault, externalizando a complexidade de gestão de credenciais OAuth. Em vez de armazenar tokens no seu banco, você os recupera sob demanda via API, usa imediatamente e descarta.

O fluxo é simples: **conecte o usuário uma vez, recupere tokens quando necessário, use e descarte**.

Isso reduz a superfície de ataque da sua aplicação, simplifica compliance e permite que você se concentre na lógica de negócio em vez de segurança de tokens.

Lembre-se: **o token só deve existir na memória pelo tempo estritamente necessário para completar a operação**.

## Recursos

- [Descope Outbound Apps Docs](https://docs.descope.com/identity-federation/outbound-apps)
- [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
