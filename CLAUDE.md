# CLAUDE.md

> **Memoria del proyecto.** Léela al iniciar cualquier sesión de trabajo en este repo.
> Es la fuente de contexto para Claude/agentes. Mantenla actualizada al cerrar cada ciclo de trabajo.

> ⚠️ **Este es el `CLAUDE.md` _starter_ de la plantilla SDD.**
> **Primer paso en un repo recién clonado:** ejecuta la skill **`init-memory`** para reemplazar este starter por la memoria real de tu proyecto (rellena §1 con qué construyes, para quién y con qué stack).

---

## 1. Qué es este proyecto

> _`init-memory` rellenará esta sección._

Proyecto creado desde la **plantilla base SDD** (Spec-Driven Development): un flujo guiado por *skills* para ir de una idea a un feature construido y verificado, con el **spec como fuente de la verdad**.

- **Qué se construye:** _(por definir con `init-memory`)_
- **Para quién / problema:** _(por definir)_
- **Stack:** _(por definir)_

---

## 2. Flujo SDD (skills)

El trabajo sigue este flujo, guiado por las skills del repo (`.claude/skills/`):

0. **`init-memory`** — Una sola vez al clonar: crea el `CLAUDE.md` de tu proyecto haciéndote preguntas y **reemplaza** este starter.
1. **`brainstorming`** — Aclara el objetivo del feature con preguntas y propone 2–3 *approaches* para que elijas.
2. **`design-spec`** — Escribe el *spec* desde el punto de vista del usuario en `docs/specs/YYYY-MM-DD-title.md` (6 secciones, §3), con **approval gate**.
3. **`design-plan`** — Convierte el *spec* aprobado en un plan en `docs/plans/YYYY-MM-DD-title.md` (4 secciones, §4), vía **plan mode**.
4. **`verify-after-changes`** — Prueba los cambios en el navegador (5 casos) contra el plan y el spec; arregla o da **luz verde**.

---

## 3. Estructura del Spec (fuente de la verdad)

`design-spec` → `docs/specs/YYYY-MM-DD-title.md`. **6 secciones**:

1. **Overview** — ¿Qué se va a construir?
2. **Usuario objetivo** — ¿Para quién es?
3. **Contexto del problema** — ¿Qué lo motiva y por qué importa?
4. **Alcance de la v1** — ¿Qué incluye y qué **NO**?
5. **Comportamiento esperado** — Flujo normal y casos de uso.
6. **Posibles errores y mitigaciones** — ¿Qué puede fallar y cómo se mitiga?

Pasa por un **approval gate**: se itera hasta que lo apruebes; solo entonces se genera el plan. El spec es la **fuente de la verdad**.

---

## 4. Estructura del Plan

`design-plan` → `docs/plans/YYYY-MM-DD-title.md` (mismo `YYYY-MM-DD-title` que su spec). **4 secciones**:

1. **Objetivo** — Qué se logra.
2. **Contexto del problema** — Resumen del problema.
3. **Spec de referencia** — Ruta al spec aprobado.
4. **Lista de tareas (con detalles)** — Qué / dónde / dependencias / criterio de "hecho".

---

## 5. Integraciones (MCP / CLI)

Declaradas en `.mcp.json` como *remote MCP* hospedados con **OAuth** (sin secretos en el repo; cada clon autentica al conectarse la primera vez):

- **Vercel** — `https://mcp.vercel.com`
- **GitHub** — `https://api.githubcopilot.com/mcp/` (o vía `gh` CLI)
- **Supabase** — `https://mcp.supabase.com/mcp`

> Agregadores personales (p. ej. **Composio**) van a tu nivel **global**, no al template: llevan tu auth/cuenta y romperían la portabilidad de la plantilla.

---

## 6. Flujo de trabajo por feature nuevo

1. **Entender** — Aclarar qué y por qué; preguntar lo que no esté claro; no asumir.
2. **Explorar** — Revisar el código y el contexto existente; qué reutilizar.
3. **Generar plan** — Pasos concretos antes de implementar (`design-plan` / plan mode).
4. **Implementar** — Ejecutar el plan.
5. **Verificar contra el plan** — Probar y comprobar que quedó **"OK"** (`verify-after-changes`).

> **Regla:** no saltarse pasos. Entender/explorar → planear → implementar → verificar.

---

## 7. Cómo trabajar en este repo

- **Idioma:** español.
- **SDD primero:** ningún build empieza sin *spec*. El spec manda sobre el plan; el plan sobre el código.
- **Estilo del proyecto:** al construir UI/artefactos aplica `style-guide/design-system.md` (+ `style-guide/assets/`); al redactar entregables audítalos contra `style-guide/writing-style.md`. Skills: `apply-design-system` / `apply-writing-style`. Si el `style-guide/` está vacío, pídelo antes de asumir marca/tono.
- **Revisión:** antes de merge/deploy, corre los sub-agentes `code-review` (correctness/calidad) y `security-review` (OWASP) sobre los cambios.
- **Determinismo cuando aplique:** si un paso se repite y ya sabes hacerlo bien, promuévelo a un script determinista (p. ej. Python) en `scripts/` en vez de re-decidirlo cada vez. Solo donde repetición + consistencia lo ameriten (no a todo). Señal típica: una entrada de Bitácora que describe un procedimiento estable. Ver `scripts/README.md`.
- **Guardas (hooks):** el harness corre `guard-secrets` (`PreToolUse`) que bloquea leer/editar `.env` y archivos de secretos. Config en `.claude/settings.json` + `.claude/hooks/` (requiere Python 3). Es una guarda, no cubre `Bash`.
- **Cierre de ciclo:** al terminar un bloque de trabajo, actualizar esta memoria y registrar en la **Bitácora (§8)** lo aprendido.

---

## 8. Bitácora (memoria propia)

Registro de lo aprendido trabajando en este repo. **Aquí escribe Claude**; es su memoria entre sesiones. Vive en el `CLAUDE.md` (no en `docs/`) para que se cargue como contexto y de verdad se lea al arrancar.

**Cuándo escribir:** al **cerrar cualquier ciclo de trabajo** (terminas una tarea, resuelves un error, ajustas un flujo), pregúntate: *¿mi yo de la próxima sesión necesita saber esto?* Si sí, lo anotas. Si no, sigues.

**Qué anotar:** límites reales de APIs/MCP, patrones que funcionan, errores que se repiten, decisiones que acordamos, supuestos que resultaron falsos, gotchas del entorno.

**Qué NO anotar:** lo efímero, lo que ya está en otra sección de este `CLAUDE.md`, y lo que se deduce leyendo el código.

**Formato de cada entrada** (más recientes arriba):
> **AAAA-MM-DD — Tema corto.** Qué aprendiste (1–3 líneas). **Por qué importa:** consecuencia práctica.

**Mantenimiento:** lo obsoleto o contradicho se **corrige o se borra**, no se acumula. Al llegar a **~25 entradas**, consolida: lo que ya es un hecho estable del proyecto se **promueve a su sección** correspondiente y sale de la bitácora.

> En un repo **recién clonado** la bitácora arranca **vacía** (`init-memory` la resetea); se llena a medida que trabajas.

---

_(Sin entradas todavía.)_
