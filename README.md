# Plantilla base SDD (Spec-Driven Development)

Plantilla de repositorio **agnóstica al lenguaje** que, al clonarla, te guía para llevar cualquier feature de una idea a algo **construido y verificado**, con el **spec como fuente de la verdad**. La guía vive en *skills*, sub-agentes y hooks de Claude Code dentro del propio repo.

## Requisitos

- [Claude Code](https://claude.com/claude-code), que es quien ejecuta las skills, sub-agentes y hooks.
- Python 3 en el PATH, para el hook `guard-secrets`. Si no lo tienes, quita el bloque `hooks` de `.claude/settings.json`.
- Opcional: cuentas de Vercel, GitHub y Supabase si vas a usar esas integraciones MCP. Se autentican por OAuth la primera vez que las conectas.

## Cómo usarla

1. **"Use this template"** en GitHub (o clona el repo) para crear tu proyecto nuevo.
2. Ejecuta la skill **`init-memory`** — crea el `CLAUDE.md` de tu proyecto y reemplaza el *starter*.
3. Por cada feature, sigue el flujo SDD:

   `brainstorming` → `design-spec` → `design-plan` → *implementar* → `verify-after-changes`

## Skills (`.claude/skills/`)

| Skill | Qué hace | Salida |
|---|---|---|
| `init-memory` | Crea la memoria del proyecto (paso 0) | `CLAUDE.md` |
| `brainstorming` | Aclara el feature + propone 2–3 approaches | approach elegido |
| `design-spec` | Spec desde la óptica del usuario (approval gate) | `docs/specs/YYYY-MM-DD-title.md` |
| `design-plan` | Plan de tareas vía plan mode | `docs/plans/YYYY-MM-DD-title.md` |
| `verify-after-changes` | Prueba 5 casos en el navegador vs plan/spec | luz verde / fixes |

Además: **`apply-design-system`** y **`apply-writing-style`** (estilo del proyecto), y sub-agentes en `.claude/agents/` (**`code-review`**, **`security-review`**).

## Estructura

```
.claude/skills/       skills: flujo SDD + estilo (apply-design-system, apply-writing-style)
.claude/agents/       sub-agentes (code-review, security-review)
.claude/hooks/        guardas del harness (guard-secrets: bloquea tocar .env/secretos)
.claude/settings.json config del harness + hooks
.claude/launch.json   dev server para verify-after-changes (edítalo para tu stack)
.mcp.json             integraciones MCP (Vercel, GitHub, Supabase)
.env.example          plantilla de secretos de runtime (copia a .env, gitignored)
style-guide/          sistema de diseño + reglas de escritura (llénalo por proyecto)
scripts/              automatización determinista (Python) — opcional, cuando aplique
docs/specs/           specs (fuente de la verdad)
docs/plans/           planes (emparejados con su spec)
CLAUDE.md             memoria/guía del proyecto + Bitácora (starter → lo genera init-memory)
```

## Integraciones esperadas

**Vercel** (MCP), **GitHub** (`gh` CLI o MCP) y **Supabase** (MCP). Se configuran en `.mcp.json`.

---

> Este README describe la **plantilla**. Al arrancar tu proyecto, reemplázalo por el tuyo y ejecuta `init-memory` para generar tu `CLAUDE.md`.

## Licencia

[MIT](LICENSE). Úsala, modifícala y compártela libremente; solo conserva el aviso de licencia.
