#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageFilter

ASSETS = Path("assets")
SOURCE = ASSETS / "jackal_01.png"


def main() -> int:
    ASSETS.mkdir(parents=True, exist_ok=True)
    if not SOURCE.exists():
        raise SystemExit(f"Missing source asset: {SOURCE}")

    with Image.open(SOURCE) as source:
        base = source.convert("RGBA")

    try:
        width, height = base.size

        # Keep level 1 untouched. Generate progressively more pixelated
        # versions for levels 2-10.
        for level in range(2, 11):
            factor = level
            small = base.resize(
                (max(8, width // factor), max(12, height // factor)),
                Image.Resampling.BILINEAR,
            )
            image = small.resize((width, height), Image.Resampling.NEAREST)
            small.close()
            if level >= 5:
                blurred = image.filter(ImageFilter.GaussianBlur(radius=(level - 4) * 0.35))
                image.close()
                image = blurred
            image.save(ASSETS / f"jackal_{level:02d}.png")
            image.close()

        # Generate the application icon source used by build_mac.py.
        canvas = Image.new("RGBA", (1024, 1024), (255, 255, 255, 0))
        icon_subject = base.copy()
        icon_subject.thumbnail((880, 880), Image.Resampling.LANCZOS)
        x = (1024 - icon_subject.width) // 2
        y = (1024 - icon_subject.height) // 2
        canvas.paste(icon_subject, (x, y), icon_subject)
        canvas.save(ASSETS / "converter.png")
        icon_subject.close()
        canvas.close()
    finally:
        base.close()

    print("Generated jackal_02.png ... jackal_10.png and converter.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
