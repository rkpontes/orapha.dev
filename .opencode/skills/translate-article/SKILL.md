---
name: translate-article
description: "Translate blog articles from Portuguese to English. Creates index.en.md files following Hugo i18n best practices. Use when user asks to translate an article or create English version."
trigger: /translate
---

# /translate

Translate blog articles from Portuguese to English, creating properly formatted `index.en.md` files that integrate with Hugo's multilingual system.

## Usage

```
/translate                          # Translate current article (if in a post directory)
/translate <slug>                   # Translate specific article by slug
/translate content/2026/05/09/my-post/index.md  # Translate by full path
```

## What This Skill Does

1. Reads the Portuguese article (`index.md`)
2. Translates content to English (you, the AI, do the translation)
3. Creates `index.en.md` with proper frontmatter
4. Adds `translationKey` to both PT and EN versions for Hugo to link them
5. Preserves all metadata (date, tags, description, etc.)

## Translation Rules

When translating, follow these guidelines:

1. **Keep frontmatter structure intact**: Maintain YAML format exactly
2. **Translate the title naturally**: Don't literal translate - adapt for English readers
3. **Preserve markdown formatting**: Headers, lists, code blocks, links, images
4. **Don't translate:**
   - Code snippets and terminal commands
   - Proper names (people, companies, products)
   - Technical terms widely used in English (API, JSON, HTTP, etc.)
   - URLs and file paths
5. **Adapt expressions**: Portuguese idioms should become natural English expressions
6. **Maintain tone**: Keep the author's voice and style

## Process

### Step 1: Locate the article

If user provided a slug, find it:
```bash
find content -name "index.md" -path "*<slug>*" | head -1
```

If no slug provided, check if current directory is a post:
```bash
pwd | grep -q "content/" && ls index.md 2>/dev/null
```

### Step 2: Read the Portuguese article

Read `content/<path>/index.md` to get:
- Frontmatter (title, date, tags, description, etc.)
- Body content

### Step 3: Create translation

Create `content/<path>/index.en.md` with:

```yaml
---
title: "English Title Here"
date: '2026-05-09T10:00:00-03:00'  # Same date as PT version
slug: same-slug-as-pt
lang: en
translationKey: <unique-key>
tags:
  - same
  - tags
  - as-pt
draft: false
description: "English description here"
---

# English Title Here

Translated content here...
```

**Important:**
- Copy the `translationKey` from PT version if it exists
- If PT doesn't have `translationKey`, generate one: `slug-date` (e.g., `awesome-design-md-2026-05-09`)
- Add `lang: en` to mark this as English
- Keep `slug` identical to PT version
- Keep `date` identical to PT version

### Step 4: Update Portuguese version

If the PT version doesn't have `translationKey`, add it:

```yaml
---
title: "Título em Português"
translationKey: <same-key-as-en>  # Add this
# ... rest of frontmatter
---
```

## Examples

**Example 1: Translate current article**
```
User: /translate
System: Translating current article...
→ Creates index.en.md in current directory
→ Updates index.md with translationKey if needed
```

**Example 2: Translate by slug**
```
User: /translate awesome-design-md-o-catalogo-de-design-systems-para-agentes-de-ia
System: Found article at content/2026/05/09/awesome-design-md-o-catalogo-de-design-systems-para-agentes-de-ia/index.md
→ Translates and creates index.en.md
```

## Output

After translation, report:
- Source file (PT)
- Created file (EN)
- TranslationKey used
- Word count (approximate)

## Notes

- The EN article will automatically appear in the language switcher on the site
- Hugo links PT and EN via `translationKey`
- URLs will be: `/2026/05/09/slug/` (PT) and `/en/2026/05/09/slug/` (EN)
