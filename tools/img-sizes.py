#!/usr/bin/env python3
"""Make the smaller photo sizes the site serves to phones and small tiles.

    python3 tools/img-sizes.py             # from the repo root
    python3 tools/img-sizes.py --missing   # only sizes that don't exist (CI)

For every img/<name>.jpg it writes img/480/<name>.jpg and img/960/<name>.jpg
(480 and 960 px wide), unless they already exist and are newer
than the original. Needs Pillow (pip install pillow). The deploy workflow runs it
too, so a photo added without its sizes still gets them on lescopines.de.
"""
import sys
from pathlib import Path

from PIL import Image

WIDTHS = (480, 960)
QUALITY = 78
ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "img"


def main():
    missing_only = "--missing" in sys.argv
    made = 0
    for src in sorted(IMG.glob("*.jpg")):
        with Image.open(src) as im:
            im = im.convert("RGB")
            for w in WIDTHS:
                out = IMG / str(w) / src.name
                if out.exists() and (missing_only or out.stat().st_mtime >= src.stat().st_mtime):
                    continue
                out.parent.mkdir(exist_ok=True)
                h = round(im.height * w / im.width)
                small = im.resize((w, h), Image.LANCZOS) if im.width > w else im
                small.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
                made += 1
    # drop sizes whose original is gone
    for w in WIDTHS:
        for out in (IMG / str(w)).glob("*.jpg"):
            if not (IMG / out.name).exists():
                out.unlink()
                print("removed", out.relative_to(ROOT))
    print(f"{made} sizes written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
