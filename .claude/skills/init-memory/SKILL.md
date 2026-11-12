---
name: init-memory
description: "Paso de arranque tras clonar la plantilla base SDD. Úsala como PRIMERA acción en un repositorio recién clonado para crear el archivo CLAUDE.md (la memoria del proyecto), haciéndole preguntas al usuario sobre qué se va a construir, y reemplazar el CLAUDE.md starter de la plantilla por uno específico del nuevo proyecto. Actívala cuando el usuario diga \"configura la memoria\", \"crea/inicializa el CLAUDE.md\", \"inicializa el proyecto\", \"arranquemos este repo\", \"el proyecto se trata de ___\", o cuando detectes un repo recién clonado de esta plantilla que aún tiene el CLAUDE.md starter."
---

# init-memory — Inicializar la memoria del proyecto

## Objetivo

Crear el `CLAUDE.md` del **nuevo proyecto** (su memoria base) a partir de una conversación breve con el usuario. Es el **paso 0** del flujo Spec-Driven Development (SDD) de esta plantilla, antes de `brainstorming`.

## Cuándo se ejecuta

- Justo después de clonar la plantilla, como **primera acción**.
- **Una sola vez** por proyecto. Después, el `CLAUDE.md` se mantiene actualizado a mano y al cerrar cada ciclo de trabajo.

## Procedimiento

1. **Reconoce el estado inicial.**
   - Si existe un `CLAUDE.md` *starter* de la plantilla, entiende que lo vas a **reemplazar** por uno específico del proyecto. No mezcles las instrucciones del template con la memoria del nuevo proyecto.

2. **Averigua de qué trata el proyecto.**
   - Parte de lo que el usuario ya dijo (p. ej. *"El proyecto se trata de ___"*).
   - Si no lo dijo, pregúntalo antes que nada.

3. **Haz preguntas de aclaración** (usa la herramienta de preguntas si está disponible; **3–5 como máximo**, de alto valor). Cubre lo necesario para una buena memoria:
   - **Qué se va a construir** — resumen en una frase.
   - **Problema / objetivo** que resuelve y para quién.
   - **Stack / tecnología** — o si es agnóstico al lenguaje.
   - **Alcance** de la primera versión — qué **sí** y qué **no**.
   - **Integraciones** relevantes (Vercel, GitHub, Supabase u otras).
   - **Restricciones o preferencias** de trabajo (idioma, convenciones).
   - No preguntes lo que puedas inferir con seguridad: recomienda un *default* y sigue.

4. **Genera el `CLAUDE.md`** del proyecto con esta estructura mínima:
   1. **Qué es este proyecto** — resumen, objetivo, stack.
   2. **Flujo de trabajo (SDD)** — referencia a las skills: `brainstorming` → `design-spec` → `design-plan` → build → `verify-after-changes`.
   3. **Estructura del Spec** — recordatorio de las 6 secciones: Overview, Usuario objetivo, Contexto del problema, Alcance de la v1, Comportamiento esperado, Posibles errores y mitigaciones.
   4. **Integraciones** — MCP/CLI que el proyecto usará.
   5. **Bitácora (memoria propia)** — incluye las reglas del starter (cuándo escribir, formato, consolidación); **las entradas arrancan vacías** en un repo nuevo.
   6. **Estado actual y pendientes** — checklist inicial.
   7. **Cómo trabajar en este repo** — idioma y convenciones.

5. **Escribe el archivo** en la raíz del repo, **reemplazando el starter**. Luego dale al usuario un resumen de lo que quedó y marca explícitamente lo que dejaste como *"pendiente de definir"*.

6. **Indica el siguiente paso.** Lo natural es continuar con la skill `brainstorming`.

## Principios

- **Preguntar antes de asumir**, pero sin abrumar: prioriza las preguntas que cambian el contenido del archivo.
- El `CLAUDE.md` es la **memoria viva** del proyecto: se actualiza al cerrar cada ciclo de trabajo.
- Mantén el **idioma del usuario**.
- No arranques `brainstorming`, `design-spec` ni ningún build hasta que la memoria esté creada.
