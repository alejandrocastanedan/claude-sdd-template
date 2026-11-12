# scripts/

Automatización **determinista** del proyecto. Aquí viven los scripts (por defecto **Python**) que reemplazan pasos que antes hacía el modelo "a mano".

## La idea
Cuando un paso se **repite** y ya sabes hacerlo bien, **promuévelo a código determinista** en vez de re-decidirlo cada sesión. Es el paralelo de la Bitácora: el conocimiento estable sube a su sección; los **procedimientos estables suben a un script**.

## Cuándo promover (deben cumplirse las tres)
- Se **repite** (lo hiciste igual ≥2–3 veces).
- La **consistencia importa** (la variación del modelo causa bugs o retrabajo).
- Es **especificable exacto** (entradas/salidas claras, sin juicio ambiguo).

## Cuándo NO
- Pasos de una sola vez.
- Los que requieren criterio/contexto que cambia cada vez.
- Donde la flexibilidad del modelo es justo lo que aporta valor.

## Convención
- Un script = una tarea. Nombre claro (`verbo-sustantivo.py`).
- Arriba, docstring con qué hace, entradas y salidas.
- Idempotente cuando se pueda; que **falle ruidoso**, no silencioso.
- Al crear uno, apúntalo en la **Bitácora** (qué automatizaste y por qué).

> No aplica a todos los proyectos. Si el tuyo no lo amerita, deja esta carpeta como está.
