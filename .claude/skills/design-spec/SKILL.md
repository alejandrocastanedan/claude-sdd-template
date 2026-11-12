---
name: design-spec
description: "Úsala DESPUÉS de tener claridad del problema y del enfoque elegido (normalmente tras `brainstorming`), para diseñar el documento de especificación desde el punto de vista del usuario. Produce el archivo `docs/specs/YYYY-MM-DD-title.md` con 6 secciones fijas e incluye un approval gate: el usuario itera el spec o lo aprueba antes de continuar con `design-plan`. Actívala cuando el usuario diga \"hagamos el spec\", \"diseña la especificación\", \"design-spec\", o cuando ya haya claridad del feature y toque escribir el spec formal. NO pases a `design-plan` sin aprobación explícita del spec."
---

# design-spec — Diseñar el spec desde el punto de vista del usuario

## Objetivo

Redactar el documento de **especificación** de un feature, **desde la perspectiva del usuario** (qué necesita, qué verá y cómo se comportará; no cómo se implementa). El spec es la **fuente de la verdad** de la que luego se deriva el plan.

## Cuándo se ejecuta

- **Después** de tener claridad del problema y del enfoque elegido (típicamente tras `brainstorming`).
- Antes de `design-plan` y antes de escribir código.
- Si aún hay ambigüedad en el objetivo o el approach, primero usa `brainstorming`.

## Entradas

- El objetivo del feature ya claro y el **approach elegido** por el usuario en `brainstorming`.

## Procedimiento

1. **Confirma que hay claridad.** Si el objetivo o el approach siguen difusos, no escribas el spec: regresa a `brainstorming`.

2. **Define la ruta del archivo.**
   - Obtén la **fecha de hoy** del sistema (p. ej. `date +%F`) → `YYYY-MM-DD`.
   - Genera un **slug** corto del título: minúsculas, sin acentos, palabras separadas por guiones.
   - Ruta final: **`docs/specs/YYYY-MM-DD-title.md`** (crea la carpeta `docs/specs/` si no existe).

3. **Redacta el spec** con estas **6 secciones** (en este orden), siempre desde el punto de vista del usuario:
   1. **Overview** — ¿Qué se va a construir? Resumen breve.
   2. **Usuario objetivo** — ¿Para quién es? Perfil, contexto y necesidad.
   3. **Contexto del problema** — ¿Qué problema o situación lo motiva y por qué importa?
   4. **Alcance de la v1** — ¿Qué **sí** incluye y qué **NO** incluye la primera versión? Lista explícita de lo que queda fuera.
   5. **Comportamiento esperado** — Flujo normal y casos de uso: qué ve y qué hace el usuario (no la implementación).
   6. **Posibles errores y mitigaciones** — ¿Qué puede fallar o qué excepciones hay, y cómo se maneja/mitiga cada una?

4. **Guarda el archivo** en la ruta definida.

5. **Approval gate (obligatorio).** Presenta el spec al usuario y pregúntale explícitamente qué quiere hacer (usa la herramienta de preguntas si está disponible):
   - **Iterar** → pide el feedback puntual, actualiza el archivo y **vuelve a presentar**. Repite hasta que apruebe.
   - **Aprobar** → el spec queda congelado como fuente de la verdad.

6. **Continuar.** Solo tras la aprobación explícita, indica que el siguiente paso es `design-plan` (invocable como `/design-plan`).

## Principios

- **Punto de vista del usuario:** describe necesidades y comportamiento, no soluciones técnicas.
- **Alcance honesto:** lo que queda **fuera** de la v1 es tan importante como lo que entra.
- **Una sola fuente de la verdad:** el plan y el código se derivan del spec, no al revés.
- **No avances sin aprobación:** el approval gate es obligatorio; nada de `design-plan` ni código hasta el "aprobado".

## Salida

- Archivo `docs/specs/YYYY-MM-DD-title.md` con las 6 secciones.
- Spec **aprobado por el usuario**, listo para `design-plan`.
