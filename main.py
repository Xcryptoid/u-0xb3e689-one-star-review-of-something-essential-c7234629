"""Entrypoint: copy the pre-written entry.txt into MAKEFUN_OUTPUT_DIR.

Standard library only. No network, no fonts, no rendering, and nothing
is written back into this directory.
"""

import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
