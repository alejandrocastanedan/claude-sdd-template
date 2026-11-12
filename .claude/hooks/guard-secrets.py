#!/usr/bin/env python3
"""PreToolUse guard: bloquea que Read/Edit/Write toquen archivos de secretos.

Recibe el JSON del hook por stdin (tool_name, tool_input, ...).
- exit 0  -> permitir
- exit 2  -> bloquear (stderr se muestra a Claude como razón)

Fail-open: ante un JSON malformado no bloquea (una guarda rota no debe frenar
todo el trabajo). Es una guarda, no una garantía; no cubre comandos de Bash.
"""
import sys
import os
import json
import fnmatch

# Nombres permitidos explícitamente (no son secretos reales).
ALLOW = {".env.example", ".env.sample", ".env.template"}

# Patrones (sobre el nombre de archivo, en minúsculas) que se consideran secretos.
SECRET_PATTERNS = [
    ".env", ".env.*",
    "*.pem", "*.key", "*.p12", "*.pfx",
    "id_rsa*",
    "*credentials*.json", ".credentials.json",
    "*.secret", "secrets.*",
]


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # fail-open

    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("path") or ""
    if not path:
        sys.exit(0)

    name = os.path.basename(path).lower()
    if name in ALLOW:
        sys.exit(0)

    if any(fnmatch.fnmatch(name, pat) for pat in SECRET_PATTERNS):
        sys.stderr.write(
            f"Bloqueado por guard-secrets: '{path}' parece un archivo de secretos. "
            "No leas ni edites secretos con las herramientas de archivo; usa variables "
            "de entorno o '.env.example'. (Ver .claude/hooks/guard-secrets.py)\n"
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
