# Descope Outbound Apps: Tokens Descartáveis para Agents de IA

## O Problema: Credenciais que Não Deveriam Existir

Você está construindo um agente de IA que precisa acessar o Google Calendar do usuário para marcar reuniões. A solução óbvia? Guardar o token OAuth no banco de dados e usar quando necessário.

**O problema:** Tokens persistentes são bombas-relógio. Se vazarem, alguém tem acesso indefinido aos dados do usuário. Se forem comprometidos, você descobre meses depois. E o pior: você dorme pensando "será que aquele token do usuário X está seguro?"

## A Solução: Tokens que Nascem para Morrer

O Descope Outbound Apps resolve isso com uma abordagem radical: **tokens de curta duração que o agente usa uma vez e descarta**.

Em vez de armazenar tokens longos no seu backend, você solicita um token **just-in-time** - válido apenas para aquela operação específica, com escopo mínimo necessário, e que expira em minutos.

### Por Que Isso Muda Tudo

| Abordagem Tradicional | Descope Outbound Apps |
|----------------------|----------------------|
| Tokens persistentes no DB | Tokens solicitados sob demanda |
| Refresh automático contínuo | Token de vida curta (5-15 min) |
| Se vazar = acesso indefinido | Se vazar = já expirou |
| Você gerencia OAuth | Descope gerencia OAuth |
| Escopo amplo "para garantir" | Escopo mínimo por operação |

## Como Funciona na Prática

### 1. Configuração do Outbound App

No console do Descope:

```
Outbound Apps → Add Outbound App → Google Calendar
├─ App ID: calendar-agent-prod
├─ Client ID: [seu client do Google]
├─ Client Secret: [seu secret do Google]
├─ Scopes Padrão: readonly (você pode sobrescrever via código)
└─ Token Lifetime: 300 segundos (5 minutos)
```

### 2. O Fluxo de Token Descartável

```
Agente precisa ler agenda
        ↓
Solicita token ao Descope (scope: calendar.readonly)
        ↓
Descope retorna token válido por 5 minutos
        ↓
Agente usa token imediatamente
        ↓
Token é descartado da memória
        ↓
Token expira (mesmo que alguém o intercepte)
```

## Implementação em Python

```python
import descope
from datetime import datetime, timedelta

class SecureAIAgent:
    def __init__(self):
        self.descope_client = descope.DescopeClient(
            project_id="seu-project-id",
            management_key="sua-management-key"
        )
    
    def get_temporary_token(self, user_id: str, scopes: list, ttl_seconds: int = 300):
        """
        Solicita um token de curta duração.
        TTL padrão: 5 minutos (você pode ajustar conforme a operação)
        """
        try:
            token_response = self.descope_client.management.outbound_app.generate_token(
                app_id="calendar-agent-prod",
                user_id=user_id,
                scopes=scopes,
                custom_claims={
                    "exp": datetime.utcnow() + timedelta(seconds=ttl_seconds),
                    "operation": "calendar_read",  # auditoria
                    "session_id": "unique-session-id"  # rastreabilidade
                }
            )
            
            return {
                "access_token": token_response["token"],
                "expires_in": ttl_seconds,
                "scope": " ".join(scopes)
            }
        except Exception as e:
            # Log seguro: não exponha o user_id em logs de erro
            print(f"[AUDIT] Falha na geração de token: {e}")
            raise
    
    def read_calendar(self, user_id: str, date: str):
        """
        Exemplo de operação: ler agenda do usuário.
        Token é gerado, usado e imediatamente descartado.
        """
        # 1. Solicitar token com escopo MÍNIMO necessário
        token_data = self.get_temporary_token(
            user_id=user_id,
            scopes=["calendar.events.readonly"],
            ttl_seconds=60  # 1 minuto é suficiente para uma leitura
        )
        
        access_token = token_data["access_token"]
        
        try:
            # 2. Usar o token imediatamente
            import requests
            
            response = requests.get(
                "https://www.googleapis.com/calendar/v3/calendars/primary/events",
                headers={"Authorization": f"Bearer {access_token}"},
                params={"timeMin": f"{date}T00:00:00Z"}
            )
            
            events = response.json()
            
            # 3. LOG DE AUDITORIA (quem fez o quê e quando)
            self._log_operation(
                user_id=user_id,
                operation="calendar_read",
                scopes_used=["calendar.events.readonly"],
                timestamp=datetime.utcnow()
            )
            
            return events
            
        finally:
            # 4. DESCARTAR O TOKEN DA MEMÓRIA
            # Em Python, podemos forçar a liberação
            access_token = None
            del access_token
    
    def schedule_meeting(self, user_id: str, meeting_data: dict):
        """
        Operação de escrita: requer escopo diferente e TTL maior.
        """
        token_data = self.get_temporary_token(
            user_id=user_id,
            scopes=["calendar.events"],  # escopo de escrita
            ttl_seconds=120  # 2 minutos para a operação completa
        )
        
        access_token = token_data["access_token"]
        
        try:
            response = requests.post(
                "https://www.googleapis.com/calendar/v3/calendars/primary/events",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json"
                },
                json=meeting_data
            )
            
            self._log_operation(
                user_id=user_id,
                operation="calendar_create",
                scopes_used=["calendar.events"],
                timestamp=datetime.utcnow()
            )
            
            return response.json()
            
        finally:
            access_token = None
            del access_token
    
    def _log_operation(self, user_id: str, operation: str, scopes_used: list, timestamp: datetime):
        """
        Auditoria: registre TODAS as operações para compliance.
        """
        audit_log = {
            "user_hash": self._hash_user_id(user_id),  # nunca logue IDs reais
            "operation": operation,
            "scopes": scopes_used,
            "timestamp": timestamp.isoformat(),
            "environment": "production"
        }
        
        # Envie para seu sistema de logs (Datadog, CloudWatch, etc)
        print(f"[AUDIT] {audit_log}")
    
    def _hash_user_id(self, user_id: str) -> str:
        """Hash do user_id para privacidade em logs."""
        import hashlib
        return hashlib.sha256(user_id.encode()).hexdigest()[:16]
```

## Padrão Avançado: Token por Operação

Para máxima segurança, você pode gerar tokens ainda mais granulares:

```python
class UltraSecureAgent:
    
    def execute_tool(self, user_id: str, tool_name: str, params: dict):
        """
        Cada ferramenta recebe seu próprio token com escopo exato.
        """
        
        tool_configs = {
            "calendar.read": {
                "scopes": ["calendar.events.readonly"],
                "ttl": 60,
                "endpoint": "calendar/v3/events"
            },
            "calendar.create": {
                "scopes": ["calendar.events"],
                "ttl": 120,
                "endpoint": "calendar/v3/events"
            },
            "contacts.lookup": {
                "scopes": ["contacts.readonly"],
                "ttl": 30,  # só precisa de 30 segundos!
                "endpoint": "people/v1/people"
            }
        }
        
        config = tool_configs.get(tool_name)
        if not config:
            raise ValueError(f"Ferramenta desconhecida: {tool_name}")
        
        # Token com tempo de vida MÍNIMO necessário
        token = self.get_temporary_token(
            user_id=user_id,
            scopes=config["scopes"],
            ttl_seconds=config["ttl"]
        )
        
        # Execute a operação e descarte
        try:
            result = self._call_provider_api(config["endpoint"], token, params)
            return result
        finally:
            # Garanta que o token seja removido
            del token
```

## Checklist de Segurança

### ✅ O Que Fazer

- **TTL mínimo possível**: Se a operação demora 5 segundos, defina TTL de 30 segundos
- **Escopo mínimo**: Nunca peça `calendar` completo se só precisa ler eventos
- **Auditoria completa**: Logue toda operação com hash do usuário
- **TLS everywhere**: Todas as chamadas devem ser HTTPS
- **Rotação de management keys**: Mude as chaves do Descope regularmente

### ❌ O Que Evitar

- ❌ Nunca armazene tokens em variáveis de ambiente
- ❌ Nunca logue tokens (mesmo que parcialmente)
- ❌ Nunca reutilize tokens entre operações
- ❌ Nunca use TTL maior que o necessário "para garantir"
- ❌ Nunca exponha management keys no código frontend

## Arquitetura de Produção

```
┌─────────────────────────────────────────────────────────────┐
│                      Usuário                                │
└─────────────────────────┬───────────────────────────────────┘
                          │ "Agende uma reunião"
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   Seu Backend/API                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Validar requisição                              │   │
│  │  2. Verificar permissões do usuário                 │   │
│  │  3. Determinar ferramentas necessárias              │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────┬───────────────────────────────────┘
                          │ Solicita token (scope: calendar.write, TTL: 2min)
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   Descope                                   │
│  ├─ Valida consentimento do usuário                         │
│  ├─ Gera token de curta duração                             │
│  └─ Retorna token + metadados                               │
└─────────────────────────┬───────────────────────────────────┘
                          │ Token válido por 2 minutos
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   Seu Backend/API                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  4. Usa token imediatamente                         │   │
│  │  5. Chama Google Calendar API                       │   │
│  │  6. Descarta token                                  │   │
│  │  7. Loga auditoria                                  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────┬───────────────────────────────────┘
                          │ Resposta para o usuário
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                      Usuário                                │
│              "Reunião agendada com sucesso!"               │
└─────────────────────────────────────────────────────────────┘
```

## Conclusão

Com Descope Outbound Apps e tokens de curta duração, você transforma a segurança do seu agente de IA de um problema contínuo em uma solução elegante. O agente recebe exatamente o que precisa, pelo tempo que precisa, e depois **nada**.

**O resultado?** Você pode dormir tranquilo sabendo que:
- Não há tokens vazando em logs
- Não há credenciais persistentes para serem roubadas
- Cada operação é rastreável e auditável
- Mesmo em caso de comprometimento, o dano é limitado a minutos

Tokens que nascem, vivem brevemente, e morrem - deixando apenas o registro de que fizeram seu trabalho.

---

**Próximos passos:**
1. Crie uma conta no [Descope](https://descope.com)
2. Configure seu primeiro Outbound App com Google Calendar
3. Implemente o padrão de token descartável em seu agente
4. Configure alertas de auditoria para operações suspeitas

**Lembre-se:** Segurança não é um estado, é um processo. Revise seus TTLs, escopos e logs regularmente.
