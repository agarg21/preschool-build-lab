from datetime import date
from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE_URL = "https://kidactivitylab.com"
NON_CONTENT_HTML = {"googled495b3fc6f0765f8.html"}
LEGACY_REDIRECT_HTML = {"collections/rainy-day-activities-for-preschoolers.html"}
CONTENT_LASTMODS = {
    "collections/indoor-activities-for-preschoolers.html": "2026-08-05",
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
