---
name: verify-after-changes
description: "Úsala cuando consideres TERMINADA la implementación del plan, para probar los cambios antes de dar por cerrado el trabajo. Probar = levantar el servidor de desarrollo, elegir 5 casos de prueba importantes y ejecutarlos directamente en el navegador; luego recoger feedback y comparar el resultado contra el plan y el spec. Si algo falla o no alcanza el objetivo, arréglalo y vuelve a probar; si todo cumple, da luz verde y termina. Actívala cuando el usuario o Claude diga \"ya terminé la implementación\", \"verifica los cambios\", \"prueba lo que hiciste\", \"verify-after-changes\", o al cerrar la fase de implementación."
---

# verify-after-changes — Probar los cambios contra el plan y el spec

## Objetivo

Comprobar que la implementación **realmente funciona** y **cumple el objetivo** antes de cerrar el ciclo: probando en el navegador, comparando contra el plan y el spec, y arreglando lo que falle hasta dar luz verde.

## Cuándo se ejecuta

- Cuando se considera **terminada la implementación** del plan.
- Es el paso final del flujo por feature (entender → explorar → generar plan → implementar → **verificar**).

## Referencias (dónde encontrar el plan y el spec)

- **Plan:** `docs/plans/YYYY-MM-DD-title.md` — la lista de tareas y el criterio de "hecho" de cada una.
- **Spec:** `docs/specs/YYYY-MM-DD-title.md` — el mismo `YYYY-MM-DD-title` que el plan (están emparejados). Contiene el "Comportamiento esperado" y los "Posibles errores y mitigaciones".

Localiza ambos antes de empezar; son la vara contra la que se mide todo.

## Procedimiento

1. **Levanta el servidor de desarrollo.**
   - Usa el arranque del proyecto (p. ej. `preview_start` leyendo `.claude/launch.json`, o el comando documentado en el `CLAUDE.md` del proyecto).

2. **Elige 5 casos de prueba importantes.**
   - Derívalos del **Comportamiento esperado** y los casos de uso del spec, más las tareas clave del plan.
   - Incluye al menos **un caso de error/excepción** de la sección "Posibles errores y mitigaciones" del spec.
   - Prioriza lo que más impacta el objetivo; no cubras trivialidades.

3. **Pruébalos directamente en el navegador.**
   - Ejecuta cada caso en el navegador (browser MCP): realiza la acción y **observa el resultado real** (no lo asumas).
   - Para cada caso anota: **resultado esperado vs. obtenido** y si pasó o falló.

4. **Recoge feedback y compara contra plan y spec.**
   - ¿Se cumplió el **objetivo**?
   - ¿Están **todas las tareas del plan** con su criterio de "hecho"?
   - ¿El comportamiento coincide con el **spec**? ¿Los errores previstos se manejan/mitigan?

5. **Decide.**
   - **Si algo falla o no alcanza el objetivo** → arréglalo, y **vuelve al paso 1** (re-prueba). Repite hasta que quede.
   - **Si todo cumple** → **luz verde**: reporta el resultado y cierra.

6. **Cierre de ciclo.** Al dar luz verde, registra en la **bitácora** lo aprendido y actualiza la memoria del proyecto (ver `CLAUDE.md`).

## Criterio de "OK" (luz verde)

Se da luz verde **solo si se cumplen todos**:

- Los **5 casos** importantes pasan en el navegador.
- El comportamiento coincide con el **"Comportamiento esperado"** del spec.
- **Todas las tareas del plan** cumplen su criterio de "hecho".
- Los **errores previstos** del spec se manejan/mitigan.

Si algo de lo anterior no se cumple, **no** es "OK": arreglar y volver a probar.

## Principios

- **Probar de verdad, en el navegador:** nada de "debería funcionar"; se observa el resultado real.
- **La vara es el plan + el spec**, no la opinión del momento.
- **Arreglar y re-probar** en bucle hasta cumplir; la luz verde es explícita.
- **Cerrar bien:** dejar constancia en la bitácora al terminar.

## Salida

- 5 casos probados en el navegador con su resultado.
- Fallos corregidos y re-probados, o **luz verde** con el objetivo cumplido.
- Bitácora/memoria actualizada al cerrar el ciclo.
