"""Render an explanatory cutaway, not a template or physically tested model."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site/assets/paper-straw-rocket/fit-air-path.png"
INK, PAPER, STRAW, AIR = "#202722", "#8b6700", "#176b62", "#246b8f"


def main():
    image = Image.new("RGB", (900, 1000), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=34)
    small = ImageFont.load_default(size=29)
    title = ImageFont.load_default(size=42)

    def text(x, y, words, face=font, color=INK):
        draw.multiline_text((x, y), words, font=face, fill=color, spacing=8)

    def line(points, color=INK, width=4):
        draw.line(points, fill=color, width=width)

    text(40, 30, "Check the fit before launch", title)
    text(40, 92, "Side cutaway: fins omitted here", small)
    # The left edge is open around the straw. The closed nose stays beyond it.
    draw.polygon([(270, 245), (690, 245), (800, 295), (690, 345), (270, 345)],
                 fill="#fff6d6")
    line([(270, 245), (690, 245), (800, 295), (690, 345), (270, 345)], PAPER, 12)
    draw.rectangle((90, 274, 620, 316), fill="#d9efe3")
    line([(90, 274), (620, 274)], STRAW, 6)
    line([(90, 316), (620, 316)], STRAW, 6)
    line([(130, 295), (676, 295)], AIR, 7)
    draw.polygon([(676, 295), (653, 281), (653, 309)], fill=AIR)
    # Tape spans the twisted nose, not the open straw end.
    line([(747, 260), (732, 330)], "#ad2635", 12)
    text(280, 160, "Paper sleeve", color=INK)
    line([(428, 202), (428, 233)])
    text(590, 365, "Taped nose:\nclosed", small)
    line([(729, 360), (748, 322)])
    text(48, 368, "Straw stays\nwith the adult", small)
    line([(130, 351), (130, 324)])
    text(270, 452, "Open end: sleeve slides\nover the straw", small)
    line([(275, 441), (270, 350)])
    text(300, 540, "Air goes into the sleeve.", small, AIR)
    line([(40, 609), (860, 609)], "#d9ded8", 2)

    text(40, 644, "Rear view: four fins", title)
    # Orthogonal fins surround a central sleeve opening; none blocks the bore.
    draw.rectangle((162, 736, 178, 778), fill=PAPER)
    draw.rectangle((162, 822, 178, 864), fill=PAPER)
    draw.rectangle((106, 792, 148, 808), fill=PAPER)
    draw.rectangle((192, 792, 234, 808), fill=PAPER)
    draw.ellipse((148, 778, 192, 822), outline=INK, width=4)
    text(305, 738, "Spread the fins into a cross.\nKeep the center opening clear.\nPencil removed before launch.", small)
    text(40, 922, "Original KAL explanation. Not to scale or a cutting template.", ImageFont.load_default(size=25))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT, optimize=False)
    print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
