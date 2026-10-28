from datetime import date
from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE_URL = "https://kidactivitylab.com"
NON_CONTENT_HTML = {"googled495b3fc6f0765f8.html"}
LEGACY_REDIRECT_HTML = {"collections/rainy-day-activities-for-preschoolers.html"}
CONTENT_LASTMODS = {
    "cards/lego-color-tower.html": "2026-10-28",
    "cards/tube-sculpture.html": "2026-10-28",
    "cards/spoon-transfer.html": "2026-10-27",
    "cards/balance-scale-baskets.html": "2026-10-27",
    "cards/measuring-tape-jumps.html": "2026-10-27",
    "cards/pattern-path.html": "2026-10-27",
    "collections/math-activities-for-4-year-olds-at-home.html": "2026-10-28",
    "cards/wind-tower-test.html": "2026-10-27",
    "cards/ramp-texture-test.html": "2026-10-27",
    "cards/water-drop-race.html": "2026-10-27",
    "cards/color-mixing-cups.html": "2026-10-27",
    "cards/ice-melt-rescue.html": "2026-10-27",
    "cards/shadow-shape-match.html": "2026-10-27",
    "cards/box-garage.html": "2026-10-27",
    "ages/activities-for-4-year-olds-at-home.html": "2026-10-28",
    "ages/activities-for-6-year-olds-at-home.html": "2026-10-28",
    "cards/blanket-river.html": "2026-10-27",
    "ages/activities-for-5-year-olds-at-home.html": "2026-10-28",
    "collections/building-activities-for-4-year-olds.html": "2026-10-28",
    "cards/paper-roll-play.html": "2026-10-27",
    "collections/no-cut-preschool-activities.html": "2026-10-27",
    "cards/duplo-games.html": "2026-10-27",
    "collections/fine-motor-activities-for-preschoolers.html": "2026-10-28",
    "articles/paper-straw-rocket.html": "2026-09-22",
    "articles/paper-helicopter-kids.html": "2026-09-19",
    "articles/paper-cup-tower-kids.html": "2026-10-27",
    "cards/cup-tower.html": "2026-10-27",
    "collections/independent-activities-for-preschoolers.html": "2026-10-27",
    "cards.html": "2026-10-28",
    "cards/cardboard-car-ramp.html": "2026-10-13",
    "articles/cardboard-box-car-ramp-preschoolers.html": "2026-10-13",
    "cards/ball-maze-box.html": "2026-10-02",
    "cards/paper-bridge.html": "2026-10-10",
    "cards/tape-road.html": "2026-10-05",
    "cards/foil-boat-test.html": "2026-09-24",
    "ages/stem-activities-for-4-year-olds.html": "2026-10-27",
    "collections/original-stem-activities-for-4-year-olds.html": "2026-10-27",
    "articles/paper-bridge-challenge-kids.html": "2026-09-26",
    "cards/paper-chain-test.html": "2026-10-15",
    "cards/sound-shaker-match.html": "2026-10-17",
    "cards/sink-or-float-tray.html": "2026-10-24",
    "cards/sock-ball-roll.html": "2026-10-27",
    "ages/activities-for-3-year-olds-at-home.html": "2026-10-27",
    "collections/no-prep-activities-for-preschoolers.html": "2026-10-27",
    "collections/science-experiments-for-4-year-olds.html": "2026-10-27",
    "collections/no-prep-stem-activities-for-4-year-olds.html": "2026-10-27",
    "collections/stem-activities-for-preschoolers.html": "2026-10-27",
    "articles/cardboard-ball-maze-kids.html": "2026-10-01",
    "articles/painter-tape-road-kids.html": "2026-09-15",
    "collections/engineering-activities-for-4-year-olds.html": "2026-10-27",
    "collections/indoor-activities-for-preschoolers.html": "2026-10-27",
}


def url_for(path):
    if path.name == "index.html":
        rel = path.relative_to(SITE).parent.as_posix()
        return f"{BASE_URL}/" if rel == "." else f"{BASE_URL}/{rel}/"
    return f"{BASE_URL}/{path.relative_to(SITE).as_posix()}"


def existing_lastmods():
    sitemap = SITE / "sitemap.xml"
    if not sitemap.exists():
        return {}
    root = ET.parse(sitemap).getroot()
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return {
        node.findtext("s:loc", namespaces=namespace): node.findtext("s:lastmod", namespaces=namespace)
        for node in root.findall("s:url", namespace)
    }


def main():
    today = date.today().isoformat()
    prior_lastmods = existing_lastmods()
    urls = sorted(SITE.rglob("*.html"), key=lambda p: p.relative_to(SITE).as_posix())
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in urls:
        rel = path.relative_to(SITE).as_posix()
        if rel in NON_CONTENT_HTML or rel in LEGACY_REDIRECT_HTML:
            continue
        html = path.read_text()
        if 'name="robots" content="noindex' in html:
            continue
        url = url_for(path)
        lastmod = CONTENT_LASTMODS.get(rel, prior_lastmods.get(url, today))
        lines.extend(
            [
                "  <url>",
                f"    <loc>{url}</loc>",
                f"    <lastmod>{lastmod}</lastmod>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(lines) + "\n")
    print(f"wrote {SITE / 'sitemap.xml'}")


if __name__ == "__main__":
    main()
