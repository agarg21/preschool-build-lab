from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE_URL = "https://kidactivitylab.com"


def url_for(path):
    if path.name == "index.html":
        rel = path.relative_to(SITE).parent.as_posix()
        return f"{BASE_URL}/" if rel == "." else f"{BASE_URL}/{rel}/"
    return f"{BASE_URL}/{path.relative_to(SITE).as_posix()}"


def main():
    today = date.today().isoformat()
    urls = sorted(SITE.rglob("*.html"), key=lambda p: p.relative_to(SITE).as_posix())
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in urls:
        html = path.read_text()
        if 'name="robots" content="noindex' in html:
            continue
        lines.extend(
            [
                "  <url>",
                f"    <loc>{url_for(path)}</loc>",
                f"    <lastmod>{today}</lastmod>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(lines) + "\n")
    print(f"wrote {SITE / 'sitemap.xml'}")


if __name__ == "__main__":
    main()
