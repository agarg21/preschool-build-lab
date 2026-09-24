"""Original folded-foil explanation, not a template or physical experiment."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "site/assets/foil-boat/empty-hull.png"


def main():
    image = Image.new("RGB", (900, 1000), "white")
    draw = ImageDraw.Draw(image)
    ink = "#202722"
    title = ImageFont.load_default(size=36)
    label = ImageFont.load_default(size=30)
    small = ImageFont.load_default(size=26)
    draw.text((35, 22), "One open boat. No cargo.", font=title, fill=ink)

    draw.text((35, 92), "1  Raise all four edges", font=label, fill=ink)
    draw.rectangle((90, 140, 320, 370), fill="#e6edef", outline=ink, width=3)
    for y in (170, 340):
        for x in range(90, 320, 16):
            draw.line((x, y, min(x + 8, 320), y), fill="#176b62", width=3)
    for x in (120, 290):
        for y in range(140, 370, 16):
            draw.line((x, y, x, min(y + 8, 370)), fill="#176b62", width=3)
    draw.multiline_text((400, 190), "Start with a foil square.\nFold near each edge.\nLeave the middle flat.\nDo not cut along the lines.", font=small, fill=ink, spacing=12)
    draw.line((35, 390, 865, 390), fill="#cad3ce", width=2)

    # The square's corner material remains present as an outside pleat;
    # it is not a cut tab. A top-oblique view keeps the cavity visible.
    def hull(y):
        back_left, back_right = (150, y), (355, y + 25)
        front_left, front_right = (70, y + 125), (275, y + 155)
        floor = [(155, y + 48), (318, y + 65), (266, y + 118), (118, y + 98)]
        draw.polygon([back_left, back_right, floor[1], floor[0]], fill="#c2d6df", outline=ink, width=3)
        draw.polygon([back_left, floor[0], floor[3], front_left], fill="#d4e3e9", outline=ink, width=3)
        draw.polygon(floor, fill="#eef3f5", outline=ink, width=3)
        draw.polygon([back_right, front_right, floor[2], floor[1]], fill="#aac5d2", outline=ink, width=3)
        draw.polygon([front_left, floor[3], floor[2], front_right], fill="#8fadb9", outline=ink, width=3)
        for x, cy in [back_left, back_right, front_left, front_right]:
            dx = -13 if x < 200 else 13
            draw.polygon([(x, cy), (x + dx, cy + 20), (x, cy + 30)], fill="#d6aa45", outline=ink, width=2)

    draw.text((35, 420), "2  Pinch the extra foil at each corner", font=label, fill=ink)
    hull(490)
    draw.multiline_text((420, 505), "Bring neighboring edges\ntogether. Pinch the corner\nflap against the outside.\nKeep every corner uncut.", font=small, fill=ink, spacing=12)
    draw.line((35, 700, 865, 700), fill="#cad3ce", width=2)
    draw.text((35, 725), "3  Leave the top open", font=label, fill=ink)
    hull(780)
    draw.multiline_text((420, 805), "Broad, flat bottom.\nRim roughly even.\nTry it empty with an adult.", font=small, fill=ink, spacing=12)
    draw.text((35, 960), "Original KAL explanation. Not to scale or a cutting template.", font=ImageFont.load_default(size=24), fill=ink)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT, optimize=False)
    print(OUT)


if __name__ == "__main__":
    main()
