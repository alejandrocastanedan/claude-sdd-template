---
name: design-plan
description: "Úsala DESPUÉS de que el usuario apruebe el spec (`design-spec`), para convertirlo en un plan de tareas implementable. Corre la fase de planeación en el plan mode de Claude Code (investigación read-only + aprobación del plan) y, una vez aprobado, guarda el plan en `docs/plans/YYYY-MM-DD-title.md` con 4 secciones: Objetivo, Contexto del problema, Spec de referencia y Lista de tareas con detalles. Actívala cuando el usuario diga \"genera el plan\", \"design-plan\", \"/design-plan\", o cuando un spec ya esté aprobado y toque planear la implementación. NO empieces a implementar hasta que el plan esté guardado."
---

# design-plan — Convertir el spec aprobado en un plan de tareas

## Objetivo

Traducir un **spec aprobado** en un **plan de implementación** concreto y accionable, y dejarlo guardado como documento. Es el puente entre el *spec* (qué/para quién) y la implementación (cómo).

## Cuándo se ejecuta

- **Después** de que el usuario apruebe el spec en `design-spec`.
- Antes de escribir código.
- Si el spec aún no está aprobado, no planees: regresa a `design-spec` y completa el approval gate.

## Entradas

- El **spec aprobado** en `docs/specs/YYYY-MM-DD-title.md`.

## Procedimiento

1. **Localiza el spec aprobado** y léelo completo. Es la fuente de la verdad; el plan no lo contradice ni lo amplía por su cuenta.

2. **Define la ruta del plan.**
   - Reutiliza el mismo `YYYY-MM-DD-title` del spec aprobado para **emparejarlos**:
     `docs/specs/2026-01-31-foo.md` ↔ `docs/plans/2026-01-31-foo.md`.
   - Crea la carpeta `docs/plans/` si no existe.

3. **Planea en el plan mode de Claude Code.**
   - Entra al **plan mode** (el usuario puede activarlo con `Shift+Tab`; tú puedes usar la fase de planeación read-only).
   - Investiga en modo **solo lectura**: el spec, el código y el contexto existente; identifica qué reutilizar y qué construir.
   - Arma la lista de tareas ordenada, con dependencias y detalle suficiente para implementar sin re-decidir.

4. **Presenta el plan para aprobación** (la propia aprobación del plan mode / `ExitPlanMode`).
   - Si el usuario pide cambios, **itera** el plan y vuelve a presentarlo.
   - Repite hasta que lo apruebe.

5. **Guarda el plan.** Una vez aprobado (y ya fuera de plan mode, que es read-only), escribe el plan en `docs/plans/YYYY-MM-DD-title.md` con la estructura de abajo.

6. **Siguiente paso.** Con el plan guardado, el siguiente paso es **implementar**; al terminar, `verify-after-changes` comprueba el resultado contra este plan.

## Estructura del documento (4 secciones)

1. **Objetivo** — Qué se logra con este trabajo (derivado del Overview/objetivo del spec).
2. **Contexto del problema** — Resumen del problema y por qué importa (del spec).
3. **Spec de referencia** — Ruta/enlace al spec aprobado (`docs/specs/YYYY-MM-DD-title.md`). El spec manda sobre el plan.
4. **Lista de tareas a implementar (con detalles)** — Tareas ordenadas, cada una con:
   - **Qué hace** y por qué.
   - **Dónde** (archivos / áreas afectadas), qué reutilizar.
   - **Dependencias** con otras tareas.
   - **Criterio de "hecho"** para poder verificarla después.

## Principios

- **El spec manda:** el plan se deriva del spec aprobado, no lo reinterpreta.
- **Read-only al planear:** nada de editar archivos durante la planeación; el guardado va tras la aprobación.
- **Tareas verificables:** cada tarea debe poder comprobarse luego contra el plan (`verify-after-changes`).
- **No implementes** hasta que el plan esté aprobado y guardado.

## Salida

- Archivo `docs/plans/YYYY-MM-DD-title.md` (emparejado con su spec) con las 4 secciones.
- Plan **aprobado**, listo para implementar.
