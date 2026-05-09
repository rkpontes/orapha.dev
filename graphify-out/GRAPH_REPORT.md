# Graph Report - .  (2026-05-09)

## Corpus Check
- Large corpus: 276 files · ~427,426 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 436 nodes · 573 edges · 52 communities (38 shown, 14 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 37 edges (avg confidence: 0.83)
- Token cost: 15 input · 200 output

## Community Hubs (Navigation)
- [[_COMMUNITY_FlexSearch Library (Variant A)|FlexSearch Library (Variant A)]]
- [[_COMMUNITY_FlexSearch Library (Variant B)|FlexSearch Library (Variant B)]]
- [[_COMMUNITY_Hextra Main UI Components|Hextra Main UI Components]]
- [[_COMMUNITY_Homepage Metadata|Homepage Metadata]]
- [[_COMMUNITY_FlexSearch Integration|FlexSearch Integration]]
- [[_COMMUNITY_Portuguese Search|Portuguese Search]]
- [[_COMMUNITY_Blog Topics & Technologies|Blog Topics & Technologies]]
- [[_COMMUNITY_PT-BR Search (Minified)|PT-BR Search (Minified)]]
- [[_COMMUNITY_Spec-Driven Development Posts|Spec-Driven Development Posts]]
- [[_COMMUNITY_Main UI (Minified)|Main UI (Minified)]]
- [[_COMMUNITY_Medium Import Scripts|Medium Import Scripts]]
- [[_COMMUNITY_FlexSearch Core (A)|FlexSearch Core (A)]]
- [[_COMMUNITY_FlexSearch Core (B)|FlexSearch Core (B)]]
- [[_COMMUNITY_FlexSearch Core (C)|FlexSearch Core (C)]]
- [[_COMMUNITY_FlexSearch Core (D)|FlexSearch Core (D)]]
- [[_COMMUNITY_Index Generation Scripts|Index Generation Scripts]]
- [[_COMMUNITY_SOLID Principles Posts|SOLID Principles Posts]]
- [[_COMMUNITY_UI Components Hub|UI Components Hub]]
- [[_COMMUNITY_TOC Scroll System|TOC Scroll System]]
- [[_COMMUNITY_AI & Agent Engineering Posts|AI & Agent Engineering Posts]]
- [[_COMMUNITY_Tabs Component|Tabs Component]]
- [[_COMMUNITY_Theme System|Theme System]]
- [[_COMMUNITY_FlexSearch Utils (A)|FlexSearch Utils (A)]]
- [[_COMMUNITY_FlexSearch Utils (B)|FlexSearch Utils (B)]]
- [[_COMMUNITY_Mobile Menu|Mobile Menu]]
- [[_COMMUNITY_Favicon System|Favicon System]]
- [[_COMMUNITY_Switcher Menu Utilities|Switcher Menu Utilities]]
- [[_COMMUNITY_Code Copy System|Code Copy System]]
- [[_COMMUNITY_FlexSearch Main|FlexSearch Main]]
- [[_COMMUNITY_Flutter Entity Pattern|Flutter Entity Pattern]]
- [[_COMMUNITY_Security Posts|Security Posts]]
- [[_COMMUNITY_Back to Top|Back to Top]]
- [[_COMMUNITY_Banner Component|Banner Component]]
- [[_COMMUNITY_FlexSearch Extras (A)|FlexSearch Extras (A)]]
- [[_COMMUNITY_FlexSearch Extras (B)|FlexSearch Extras (B)]]
- [[_COMMUNITY_Flutter Modular|Flutter Modular]]
- [[_COMMUNITY_Code Generators Post|Code Generators Post]]
- [[_COMMUNITY_Nav Menu|Nav Menu]]
- [[_COMMUNITY_Language Switcher|Language Switcher]]
- [[_COMMUNITY_File Tree|File Tree]]
- [[_COMMUNITY_FlexSearch Internals (A)|FlexSearch Internals (A)]]
- [[_COMMUNITY_FlexSearch Internals (B)|FlexSearch Internals (B)]]
- [[_COMMUNITY_Blog Index|Blog Index]]
- [[_COMMUNITY_Copilot Instructions Post|Copilot Instructions Post]]
- [[_COMMUNITY_Moral Concerns Post|Moral Concerns Post]]
- [[_COMMUNITY_Archives Page|Archives Page]]
- [[_COMMUNITY_About Page|About Page]]

## God Nodes (most connected - your core abstractions)
1. `orapha.dev` - 21 edges
2. `B()` - 11 edges
3. `B()` - 11 edges
4. `orapha.dev` - 10 edges
5. `getActiveSearchElement()` - 9 edges
6. `e` - 9 edges
7. `getActiveSearchElement()` - 9 edges
8. `handleKeyDown()` - 7 edges
9. `n()` - 7 edges
10. `handleKeyDown()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Software Engineering Principles` --related_to--> `SOLID Principles`  [INFERRED]
  /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/03/19/voce-ainda-lembra-dos-principios-da-engenharia-de-software/index.md → /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2024/06/15/unlocking-the-secrets-of-solid-a-beginners-guide/index.md
- `OpenSpec` --implements--> `Spec-Driven Development`  [INFERRED]
  /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/04/29/desmistificando-o-processo-de-propose-no-openspec/index.md → /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/04/03/como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos/index.md
- `Spec Kit` --related_to--> `OpenSpec`  [INFERRED]
  /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/04/03/como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos/index.md → /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/04/29/desmistificando-o-processo-de-propose-no-openspec/index.md
- `Você está se sentindo um bosta com o surgimento da IA` --related_to--> `Vibe Coding está morto`  [INFERRED]
  /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/03/22/voce-esta-se-sentindo-um-bosta-com-o-surgimento-da-ia/index.md → /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/03/20/vibe-coding-esta-morto-por-que-a-ia-autonoma-exige-cercas-deterministicas-rigidas-para-realmente-funcionar/index.md
- `Agent Engineering + Agentic Flow Engineering` --related_to--> `Vibe Coding está morto`  [INFERRED]
  /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/03/19/agent-engineering-e-agentic-flow-engineering/index.md → /Users/raphaelpontes/Documents/Projetos/orapha_dev/content/2026/03/20/vibe-coding-esta-morto-por-que-a-ia-autonoma-exige-cercas-deterministicas-rigidas-para-realmente-funcionar/index.md

## Hyperedges (group relationships)
- **Hextra UI Subsystems** — theme_system, menu_system, code_copy_system, tab_system, toc_scroll_system, hamburger_menu, language_switcher [INFERRED 0.85]
- **FlexSearch Index Pair** — page_index, section_index [INFERRED 0.95]
- **LocalStorage Persistence Pattern** — theme_system, tab_system [INFERRED 0.85]

## Communities (52 total, 14 thin omitted)

### Community 0 - "FlexSearch Library (Variant A)"
Cohesion: 0.05
Nodes (14): ab, bb, c, d, db, f, h, l (+6 more)

### Community 1 - "FlexSearch Library (Variant B)"
Cohesion: 0.05
Nodes (15): ab, bb, c, d, db, f, h, k (+7 more)

### Community 2 - "Hextra Main UI Components"
Cohesion: 0.06
Nodes (27): applyTheme(), backToTop, codeElements, computeMenuTranslation(), darkModeQuery, dropdownToggles, faviconEl, folders (+19 more)

### Community 3 - "Homepage Metadata"
Cohesion: 0.11
Nodes (24): AI Agents, Artificial Intelligence, Code Generators, GitHub Copilot, Software Engineering Principles, FlexSearch, Flutter, GitHub (+16 more)

### Community 4 - "FlexSearch Integration"
Cohesion: 0.2
Nodes (19): displayResults(), finishSearch(), getActiveResult(), getActiveSearchElement(), getResultsLength(), handleInputChange(), handleKeyDown(), hideSearchResults() (+11 more)

### Community 5 - "Portuguese Search"
Cohesion: 0.2
Nodes (19): displayResults(), finishSearch(), getActiveResult(), getActiveSearchElement(), getResultsLength(), handleInputChange(), handleKeyDown(), hideSearchResults() (+11 more)

### Community 6 - "Blog Topics & Technologies"
Cohesion: 0.11
Nodes (20): Agent Engineering, Artificial Intelligence, Code Generation, GitHub Copilot, Entity Structure Pattern, Flutter, GitHub, Hextra Theme (+12 more)

### Community 7 - "PT-BR Search (Minified)"
Cohesion: 0.23
Nodes (18): a(), c(), d, e, f(), g(), i(), {inputElement:n} (+10 more)

### Community 8 - "Spec-Driven Development Posts"
Cohesion: 0.29
Nodes (16): No Spec-Driven Development, tudo começa pelos princípios, Constitution Phase, No Spec-Driven Development, specify é onde a ambiguidade começa a morrer, Specify Phase, No Spec-Driven Development, plan é onde a especificação vira estratégia, Plan Phase, No Spec-Driven Development, tasks é onde o plano vira unidades concretas, Tasks Phase (+8 more)

### Community 9 - "Main UI (Minified)"
Cohesion: 0.16
Nodes (10): a, computeMenuTranslation(), e, i(), o, r, resizeMenu(), s (+2 more)

### Community 10 - "Medium Import Scripts"
Cohesion: 0.31
Nodes (6): block_markdown(), clean_text(), description_from_markdown(), html_to_markdown(), inline_markdown(), markdown_escape()

### Community 11 - "FlexSearch Core (A)"
Cohesion: 0.22
Nodes (9): B(), Ea(), fb(), Ha(), Na(), P(), ra(), S() (+1 more)

### Community 12 - "FlexSearch Core (B)"
Cohesion: 0.25
Nodes (9): ba(), E(), I(), n, sa(), ta(), U(), ua() (+1 more)

### Community 13 - "FlexSearch Core (C)"
Cohesion: 0.25
Nodes (9): ba(), E(), I(), n, sa(), ta(), U(), ua() (+1 more)

### Community 14 - "FlexSearch Core (D)"
Cohesion: 0.22
Nodes (9): B(), Ea(), fb(), Ha(), Na(), P(), ra(), S() (+1 more)

### Community 15 - "Index Generation Scripts"
Cohesion: 0.36
Nodes (7): collect_posts(), escape_markdown(), extract_frontmatter(), generate_archives(), generate_index(), parse_post(), render_months()

### Community 16 - "SOLID Principles Posts"
Cohesion: 0.36
Nodes (9): Unlocking the Secrets of SOLID, Dependency Inversion Principle (DIP), Interface Segregation Principle (ISP), Liskov Substitution Principle (LSP), Open-Closed Principle (OCP), SOLID Principles, Single Responsibility Principle (SRP), Você ainda lembra dos princípios da engenharia de software (+1 more)

### Community 17 - "UI Components Hub"
Cohesion: 0.29
Nodes (8): Code Copy System, Mobile Hamburger Menu, Language Switcher, Main UI Module, Menu Management System, Tab Management System, Theme Switching System, TOC Scroll System

### Community 18 - "TOC Scroll System"
Cohesion: 0.29
Nodes (5): headingIds, headings, observer, toc, tocLinks

### Community 19 - "AI & Agent Engineering Posts"
Cohesion: 0.38
Nodes (7): Agent Engineering + Agentic Flow Engineering, Agents.md, Skills.md, Vibe Coding está morto, AI Harness Engineering, Model Context Protocol (MCP), Você está se sentindo um bosta com o surgimento da IA

### Community 20 - "Tabs Component"
Cohesion: 0.33
Nodes (4): index, key, saved, syncGroups

### Community 21 - "Theme System"
Cohesion: 0.4
Nodes (5): applyTheme(), switchTheme(), themes, themeToggleButtons, themeToggleOptions

### Community 22 - "FlexSearch Utils (A)"
Cohesion: 0.33
Nodes (6): ca(), Fa(), Ga(), ka(), kb(), la()

### Community 23 - "FlexSearch Utils (B)"
Cohesion: 0.33
Nodes (6): ca(), Fa(), Ga(), ka(), kb(), la()

### Community 24 - "Mobile Menu"
Cohesion: 0.4
Nodes (3): menu, sidebarContainer, sidebarLinks

### Community 26 - "Switcher Menu Utilities"
Cohesion: 0.83
Nodes (3): computeMenuTranslation(), resizeMenu(), toggleMenu()

### Community 29 - "FlexSearch Main"
Cohesion: 0.83
Nodes (4): FlexSearch Library, Page Search Index, PT-BR Search Module, Section Search Index

### Community 30 - "Flutter Entity Pattern"
Cohesion: 0.83
Nodes (4): Como estruturo minhas Entities no Flutter, Adapter, DTO, Entity

### Community 31 - "Security Posts"
Cohesion: 0.67
Nodes (4): Ensuring the Security of Your Flutter Application, EHT (Ethical Hacking Test), Gray Box Mode, Increase security in your Flutter applications

### Community 35 - "FlexSearch Extras (A)"
Cohesion: 0.67
Nodes (3): a, ya(), z()

### Community 36 - "FlexSearch Extras (B)"
Cohesion: 0.67
Nodes (3): a, ya(), z()

### Community 37 - "Flutter Modular"
Cohesion: 1.0
Nodes (3): Cubit, How to Integrate Flutter Modular with Flutter Bloc, Flutter Modular

### Community 38 - "Code Generators Post"
Cohesion: 1.0
Nodes (3): Code Generators in Flutter, build_runner, Macros

## Knowledge Gaps
- **138 isolated node(s):** `toc`, `tocLinks`, `headingIds`, `headings`, `observer` (+133 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Are the 5 inferred relationships involving `orapha.dev` (e.g. with `Hextra Theme` and `Spec-Driven Development`) actually correct?**
  _`orapha.dev` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `toc`, `tocLinks`, `headingIds` to the rest of the system?**
  _138 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `FlexSearch Library (Variant A)` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
- **Should `FlexSearch Library (Variant B)` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
- **Should `Hextra Main UI Components` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Homepage Metadata` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._
- **Should `Blog Topics & Technologies` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._