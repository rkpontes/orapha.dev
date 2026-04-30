---
title: "Desmistificando o processo de Propose no OpenSpec: O que acontece nos bastidores?"
date: '2026-04-29T23:22:42-03:00'
slug: desmistificando-o-processo-de-propose-no-openspec
tags:
  - openspec
  - engenharia-de-software
  - spec-driven-development
  - arquitetura
draft: false
description: "Uma explicação detalhada sobre os artefatos gerados pelo comando propose do OpenSpec e como eles organizam o desenvolvimento."
---

Quando executamos o comando de criação de uma nova proposta (propose) no OpenSpec — como por exemplo, ao iniciar a funcionalidade `add-course-enrollment-module` —, o sistema trabalha nos bastidores para gerar uma série de arquivos fundamentais para o sucesso do desenvolvimento. 

Se você já se perguntou para que serve cada um desses artefatos, este artigo é para você. Vamos explorar a anatomia de cada documento gerado e como eles garantem o alinhamento da equipe: desde a visão de negócios até a codificação.

---

## 1. O Proposal (`proposal.md`): O "Por Quê" e o "O Quê"

O documento de proposal é o ponto de partida da sua jornada. Ele serve como a ponte entre o negócio e a engenharia. 

* **O que contém:** Motivação da funcionalidade, o escopo exato do que será construído e quais "capabilities" (capacidades) novas estão sendo introduzidas no sistema. No nosso exemplo, ele mapeia o impacto no projeto e introduz o `enrollment-management`, `payment-gateway-adapter`, e o `enrollment-command-dispatch`.
* **Para que serve:** Garantir que todos os envolvidos (desenvolvedores, POs, stakeholders) tenham clareza sobre o valor que está sendo entregue e o tamanho da mudança, antes mesmo de escrevermos a primeira linha de código.

## 2. O Design Document (`design.md`): O "Como" em Alto Nível

Se o *Proposal* foca no negócio, o *Design Document* aprofunda no terreno técnico. Aqui moram as decisões de arquitetura e mitigação de riscos.

* **O que contém:** Documenta as decisões técnicas que guiarão o desenvolvimento. Por exemplo, a decisão de replicar o padrão já usado em "students" no frontend, a adoção de comandos determinísticos no BFF, o isolamento do adapter de pagamentos, e a garantia de idempotência via `request_id` com base em *polling*.
* **Para que serve:** Prevenir dores de cabeça futuras. Ao listar os riscos, suas mitigações e o plano de migração, a equipe técnica tem um mapa dos possíveis obstáculos e como contorná-los sem ferir a arquitetura da aplicação.

## 3. As Specs (`specs/*/spec.md`): As Regras do Jogo 

Uma das grandes sacadas do OpenSpec é dividir um problema complexo em "capabilities" (capacidades) menores, gerando especificações dedicadas para cada domínio do sistema:

### `specs/enrollment-management/spec.md` (Frontend)
Focado na experiência do usuário. Define os requisitos da interface: como a tabela de matrículas deve se comportar, regras para ocultar dados sensíveis, as ações permitidas (editar, remover, abrir URL, disparar modais de mensagem) e requisitos não funcionais como responsividade e sincronismo com o backend.

### `specs/payment-gateway-adapter/spec.md` (Integração)
Focado na comunicação com o parceiro. Define as regras do jogo com a API do Gateway de Pagamento: como criar, consultar, atualizar e cancelar os pagamentos. Além disso, garante o mapeamento correto dos status da API terceira para o domínio interno e formaliza a segurança na manipulação das credenciais.

### `specs/enrollment-command-dispatch/spec.md` (Backend/BFF)
Focado na robustez interna. Define as responsabilidades no BFF (Backend For Frontend), como a resolução determinística de configurações de provedores, a emissão de comandos de forma versionada, e a aplicação estrita de idempotência e rastreabilidade nos eventos.

## 4. O Plano de Ação (`tasks.md`): Colocando a Mão na Massa

A cereja do bolo de todo o processo de planejamento. Depois de entender o contexto, a arquitetura e os requisitos específicos, o OpenSpec compila tudo isso em um checklist acionável.

* **O que contém:** Um agrupamento lógico de tarefas. No caso da nossa funcionalidade de matrículas, foram gerados 12 grupos ordenados para a implementação: indo desde o *setup* inicial, passando pela modelagem do domínio, casos de uso, infraestrutura, desenvolvimento de tela/UI, construção de hooks, configuração de rotas e observabilidade, até fechar com testes e documentação final.
* **Para que serve:** É o guia de bolso do desenvolvedor. Ele permite que o time pegue tarefas independentes sabendo exatamente em qual ordem elas devem ser executadas, tornando o avanço previsível e fácil de acompanhar.

---

### Conclusão

Ter uma ideia brilhante é ótimo, mas transformá-la em software rodando em produção exige método. 

Com o processo de **Propose** do OpenSpec, toda a carga pesada de planejamento, organização arquitetural e divisão de tarefas é feita de forma fluida. O resultado são ciclos de desenvolvimento (sprints) extremamente previsíveis, documentação sempre viva e um *time-to-market* reduzido de forma inteligente e padronizada. 

Na próxima vez que o OpenSpec gerar esses artefatos, você saberá exatamente a importância de cada peça dessa engrenagem!
