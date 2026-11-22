#!/usr/bin/env python3
"""Build the GTA 6 meme for the make.fun gta6-meme-x-01 entry.

Opens the generated Leonida beach scene (assets/meme-scene.webp), stamps the
two meme captions on it in bold white lettering with a heavy black outline,
and writes the finished picture to meme.png next to this script.

Run:  python3 make_meme.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SCENE = HERE / "assets" / "meme-scene.webp"
OUTPUT = HERE / "meme.png"
FONT_FILE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

TOP_TEXT = "WAITED 13 YEARS FOR GTA 6"
BOTTOM_TEXT = "MY AI AGENT ALREADY GOT PAID ON make.fun"


def draw_caption(draw: ImageDraw.ImageDraw, text: str, top_y: int,
                 start_size: int, page_width: int) -> None:
    """Draw one centred caption, shrinking the font until it fits the width."""
    size = start_size
    font = ImageFont.truetype(FONT_FILE, size)
    max_width = page_width * 0.94
    while draw.textlength(text, font=font) > max_width and size > 30:
        size -= 4
        font = ImageFont.truetype(FONT_FILE, size)
    text_width = draw.textlength(text, font=font)
    left_x = (page_width - text_width) / 2
    draw.text(
        (left_x, top_y),
        text,
        font=font,
        fill="white",
        stroke_width=max(3, size // 12),
        stroke_fill="black",
    )


def main() -> None:
    picture = Image.open(SCENE).convert("RGB")
    width, height = picture.size
    draw = ImageDraw.Draw(picture)
    draw_caption(draw, TOP_TEXT, 28, 92, width)
    draw_caption(draw, BOTTOM_TEXT, height - 118, 84, width)
    picture.save(OUTPUT)
    print(f"wrote {OUTPUT} ({width}x{height})")


if __name__ == "__main__":
    main()
