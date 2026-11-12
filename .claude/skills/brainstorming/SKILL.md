---
name: brainstorming
description: "Úsala al INICIAR un feature nuevo, antes de planear o escribir código. Hace preguntas para eliminar la ambigüedad del objetivo del usuario (qué, para quién, alcance, restricciones, criterio de éxito) y termina proponiendo 2–3 approaches distintos para que el usuario decida cómo abordar el plan. Actívala cuando el usuario diga \"quiero un nuevo feature\", \"vamos a construir X\", \"tengo una idea para\", \"ayúdame a pensar cómo hacer\", \"brainstorming\", o cuando arranque cualquier feature cuyo objetivo o alcance no esté claro. Es el paso 1 (\"entender\") del flujo por feature; su salida alimenta a `design-plan`."
---

# brainstorming — Aclarar el feature y proponer approaches

## Objetivo

Convertir una idea difusa de feature en un objetivo **claro y sin ambigüedad**, y ofrecer **2–3 approaches** distintos para que el usuario elija con qué enfoque se hará el plan. Es el arranque del flujo por feature (entender → explorar → generar plan → implementar → verificar).

## Cuándo se ejecuta

- Al **iniciar un feature nuevo**, antes de `design-plan` / `design-spec` y antes de escribir código.
- Especialmente cuando el objetivo, el alcance o el "para qué" no están claros.

## Procedimiento

1. **Parte de lo que el usuario ya dijo.** Resume en una frase tu entendimiento del feature y señala qué falta por aclarar. No repreguntes lo que ya está claro.

2. **Haz preguntas para eliminar la ambigüedad** (usa la herramienta de preguntas si está disponible; **3–5 de alto valor**, no abrumes). Cubre lo que haga falta:
   - **Objetivo / problema** — ¿qué problema resuelve y por qué ahora?
   - **Usuario / contexto** — ¿para quién es y cómo lo usará?
   - **Alcance** — ¿qué **sí** entra en esta primera versión y qué **no**?
   - **Criterio de éxito** — ¿cómo sabremos que quedó bien / "hecho"?
   - **Restricciones** — técnicas, de tiempo, dependencias, datos o integraciones.
   - Si puedes inferir algo con seguridad, propón un *default* en vez de preguntar.

3. **Explora lo necesario** (opcional pero recomendado). Revisa el código y el contexto existente para que los approaches sean realistas y aprovechen lo que ya hay.

4. **Propón 2–3 approaches distintos** (no variaciones del mismo). Para cada uno:
   - **Nombre** corto y memorable.
   - **En qué consiste** — la idea central en 1–2 frases.
   - **Ventajas**.
   - **Desventajas / riesgos**.
   - **Esfuerzo** relativo (bajo / medio / alto).
   - **Cuándo conviene** elegirlo.

   Busca que cubran trade-offs reales (p. ej. *rápido y simple* vs. *robusto y escalable* vs. *mínimo riesgo*). Si tienes una recomendación, dila y explica por qué.

5. **Que el usuario decida.** Presenta los approaches y pídele que elija uno (usa la herramienta de preguntas con los approaches como opciones si está disponible).

6. **Cierra apuntando al siguiente paso.** Con el approach elegido y el objetivo ya claro, el siguiente paso es `design-plan` (o `design-spec` si el feature amerita un spec formal).

## Principios

- **Aclarar antes de proponer:** no presentes approaches sobre un objetivo ambiguo.
- **Preguntar sin abrumar:** prioriza las preguntas que más reducen la incertidumbre.
- **Approaches genuinamente distintos**, con trade-offs explícitos; nunca uno solo disfrazado de tres.
- **El usuario decide, tú recomiendas.**
- No pases a planear ni a implementar hasta que el usuario elija un approach.

## Salida

- Un objetivo del feature claro y sin ambigüedad.
- 2–3 approaches evaluados.
- Un approach **elegido por el usuario**, listo para `design-plan`.
