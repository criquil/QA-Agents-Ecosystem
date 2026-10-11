"""Valida encoding UTF-8 y caracteres corruptos en los archivos de texto del proyecto.

Uso: python utils/validate_encoding.py [ruta]
Sin argumentos valida todo el proyecto (excluye .git y node_modules).
"""
from __future__ import annotations

import sys
from pathlib import Path

SUSPECT_RANGES = (
    (0xFFFD, 0xFFFD, "replacement char (U+FFFD)"),
    (0x4E00, 0x9FFF, "CJK ideograph"),
    (0x3040, 0x30FF, "kana"),
    (0xAC00, 0xD7AF, "hangul"),
)


def scan(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    problems: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for ch in line:
            code = ord(ch)
            for low, high, label in SUSPECT_RANGES:
                if low <= code <= high:
                    problems.append((lineno, f"{label} U+{code:04X}"))
                    break
    return problems


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    targets = [root] if root.is_file() else sorted(
        p for p in root.rglob("*")
        if p.is_file()
        and p.suffix in {".md", ".json", ".yaml", ".yml", ".js", ".ts", ".py", ".ps1"}
        and not {".git", "node_modules", ".venv"} & set(p.parts)
    )

    total = 0
    for path in targets:
        problems = scan(path)
        if not problems:
            continue
        total += len(problems)
        print(f"{path.relative_to(root) if path.is_relative_to(root) else path}:")
        for lineno, label in problems:
            print(f"  L{lineno}: {label}")

    print(f"\n{total} problema(s) en {len(targets)} archivo(s) revisado(s).")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))