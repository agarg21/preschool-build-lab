"""Original explanatory ribbon geometry; not a template or physical test."""

from math import cos, pi, sin
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "site/assets/paper-chain/linked-loops.png"


def main():
    image = Image.new("RGB", (900, 1100), "white")
    draw = ImageDraw.Draw(image)
    title = ImageFont.load_default(size=38)
    label = ImageFont.load_default(size=32)
    small = ImageFont.load_default(size=27)
    ink = "#202722"
    draw.text((35, 25), "Thread first. Then close.", font=title, fill=ink)

    def scene(stage, cy):
        faces = []
        offset = -0.5 if stage == 3 else 0

        def project(point):
            x, y, z = point
            return (230 + 88 * (0.85 * x + 0.55 * y), cy + 88 * (-z + 0.25 * x - 0.3 * y))

        def face(points, color):
            depth = sum(0.55 * x - 0.85 * y - 0.4 * z for x, y, z in points) / len(points)
            faces.append((depth, points, color))

        # Perpendicular ribbon loops are linked: the blue loop crosses the
        # green loop's plane once inside its hole and once outside the ring.
        for i in range(180):
            a, b = i * 2 * pi / 180, (i + 1) * 2 * pi / 180
            shade = int(18 * cos(a))
            color = (32 + shade, 120 + shade, 91 + shade)
            if 0.13 < a < 0.33:
                color = (184, 215, 201)
            face([(cos(a), -0.17, sin(a) + offset),
                  (cos(b), -0.17, sin(b) + offset),
                  (cos(b), 0.17, sin(b) + offset),
                  (cos(a), 0.17, sin(a) + offset)], color)
            if stage == 3:
                blue = (36 + shade, 102 + shade, 158 + shade)
                if pi - 0.1 < a < pi + 0.1:
                    blue = (183, 207, 228)
                face([(-0.17, sin(a), 1 - cos(a) + offset),
                      (-0.17, sin(b), 1 - cos(b) + offset),
                      (0.17, sin(b), 1 - cos(b) + offset),
                      (0.17, sin(a), 1 - cos(a) + offset)], blue)
        if stage == 2:
            for i in range(100):
                a, b = -2 + i * 0.04, -2 + (i + 1) * 0.04
                face([(-0.17, a, 0), (-0.17, b, 0), (0.17, b, 0), (0.17, a, 0)], (36, 102, 158))
        for _, points, color in sorted(faces, key=lambda item: item[0]):
            draw.polygon([project(point) for point in points], fill=color)

    rows = [
        (205, "1  Close the first loop", "Overlap this strip's\nown ends. Tape them."),
        (525, "2  Pass a new strip through", "Keep the new strip open.\nThread it through the hole."),
        (870, "3  Close the new loop", "Join the new strip's own ends.\nDo not tape one loop\nto the other."),
    ]
    for stage, (cy, heading, copy) in enumerate(rows, 1):
        scene(stage, cy)
        draw.text((35, cy - (175 if stage == 3 else 127)), heading, font=label, fill=ink)
        draw.multiline_text((440, cy - 25), copy, font=small, fill=ink, spacing=12)
        if stage < 3:
            draw.line((35, cy + 145, 865, cy + 145), fill="#cad3ce", width=2)
    draw.text((35, 1046), "Original KAL explanation. Not to scale or a cutting template.", font=ImageFont.load_default(size=25), fill=ink)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT, optimize=False)
    print(OUT)


if __name__ == "__main__":
    main()
