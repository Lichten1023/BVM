"""Stub transpiler from a tiny language to 8001 assembly."""

from __future__ import annotations

import sys
from typing import Iterable


def transpile(source: str) -> str:
    """Convert the mini-language *source* into 8001 assembly.

    The supported subset is deliberately tiny and meant only for
    demonstration.  Currently recognised instructions are::

        SET <register>, <value>
        ADD <register>, <value>

    Unrecognised lines are emitted as comments so that future versions of
    the transpiler can handle them without failing.
    """
    output: list[str] = []
    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            # Skip blank lines and comments.
            continue
        tokens = line.split()
        cmd = tokens[0].upper()
        if cmd == "SET" and len(tokens) == 3:
            reg = tokens[1].rstrip(',')
            value = tokens[2]
            output.append(f"MVI {reg.upper()}, {value}")
        elif cmd == "ADD" and len(tokens) == 3:
            reg = tokens[1].rstrip(',')
            value = tokens[2]
            output.append(f"ADD {reg.upper()}, {value}")
        else:
            output.append(f"; TODO: {raw_line}")
    return "\n".join(output)


def transpile_file(path: str) -> str:
    """Read *path* and transpile its contents."""
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()
    return transpile(source)


def main(argv: Iterable[str] | None = None) -> int:
    argv = list(argv or sys.argv[1:])
    if len(argv) != 1:
        print("Usage: transpiler.py <source-file>")
        return 1
    asm = transpile_file(argv[0])
    print(asm)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
