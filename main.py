"""Robot vacuum excuse writer.

Writes the vacuum's single-line excuse for missing a spot to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Deterministic,
stdlib only, no network.
"""

import os

LINE = "I circled that spot nine times, then it filed for harassment, so I settled out of court."


def main() -> None:
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
