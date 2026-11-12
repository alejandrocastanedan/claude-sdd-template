# .claude/hooks/

Guardas que **el harness** ejecuta en eventos del ciclo (no las corre el modelo). Se configuran en `.claude/settings.json`.

- **`guard-secrets.py`** — `PreToolUse` sobre `Read` / `Edit` / `Write`: bloquea tocar `.env` y archivos de secretos (`*.pem`, `*.key`, `*credentials*.json`, `id_rsa*`, …). Permite `.env.example`. Requiere **Python 3** en el PATH (el comando es `python3`). En Windows, si solo tienes `python`, cámbialo en `.claude/settings.json`.

> Al clonar, Claude Code pedirá **aprobar los hooks del proyecto** — revísalos antes de aceptar.
>
> Límite honesto: no cubre `Bash` (p. ej. `cat .env`), porque inspeccionar comandos de shell es frágil. Es una **guarda**, no una garantía. Si no tienes Python, quita el bloque `hooks` de `.claude/settings.json`.
