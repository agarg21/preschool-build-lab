"""Render KAL's editorial cut/fold map; this is not a flight-tested template."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site/assets/paper-helicopter/cut-fold-map.png"
CUT, FOLD, INK = "#ad2635", "#176b62", "#202722"


def main():
    image = Image.new("RGB", (900, 1400), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=38)
    small = ImageFont.load_default(size=32)
    title = ImageFont.load_default(size=46)

    def text(x, y, words, fill=INK, face=font):
        draw.multiline_text((x, y), words, font=face, fill=fill, spacing=9)

    def line(points, color=FOLD, width=7):
        draw.line(points, fill=color, width=width)

    def cut(start, end):
        dx, dy = end[0] - start[0], end[1] - start[1]
        length = (dx * dx + dy * dy) ** 0.5
        for distance in range(0, int(length), 27):
            a, b = distance / length, min(distance + 17, length) / length
            line([(start[0] + a * dx, start[1] + a * dy),
                  (start[0] + b * dx, start[1] + b * dy)], CUT)
        x, y = end
        draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=CUT)

    # One 7 x 21 cm editorial blank, scaled at 40 px/cm; see the guide.
    left, right, top, bottom = 80, 360, 230, 1070
    center = 220
    junction, roots, sides, base = 550, 570, 650, 970
    body_left, body_right = left + 280 / 3, left + 560 / 3
    text(50, 35, "Adult cut-and-fold map", face=title)
    cut((50, 122), (120, 122))
    text(145, 97, "CUT to a dot", CUT)
    line([(50, 180), (120, 180)])
    text(145, 155, "FOLD on a solid green line", FOLD, small)
    draw.rectangle((left, top, right, bottom), fill="#f1f7f5", outline=INK, width=4)
    draw.rectangle((body_left + 4, sides + 4, body_right - 4, bottom - 4), fill="#d9eae4")
    line([(left, roots), (center, junction), (right, roots)])
    line([(body_left, sides), (body_left, bottom)])
    line([(body_right, sides), (body_right, bottom)])
    line([(left, base), (right, base)])
    cut((center, top), (center, junction))
    cut((left, sides), (body_left, sides))
    cut((right, sides), (body_right, sides))

    text(420, 245, "CUT down\nthe center.\nSTOP at the dot.", CUT)
    line([(390, 367), (380, 367), (center + 14, junction - 13)], INK, 2)
    text(420, 454, "FOLD blades:\none toward you,\none away.", FOLD)
    line([(408, 548), (right + 7, roots)], INK, 2)
    text(420, 655, "CUT inward\nfrom both sides.\nSTOP at each dot.", CUT)
    line([(400, 681), (right + 6, sides)], INK, 2)
    text(420, 849, "FOLD sides\nover the uncut\nmiddle strip.", FOLD)
    line([(410, 885), (body_right + 8, 885)], INK, 2)
    text(420, 1046, "FOLD the\nbottom up\nthrough all layers.", FOLD)
    line([(410, 1071), (right + 8, base)], INK, 2)
    text(78, 1130, "Keep the middle uncut.", face=small)
    text(50, 1230, "KAL proportions, not actual size.\nA planning diagram, not a tested flight result.", face=small)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT, optimize=False)
    print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
