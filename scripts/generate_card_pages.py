import csv
import html
import re
from pathlib import Path

from generate_seo_pages import ACTIVITIES


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "video_activity_sources.csv"
OUT = ROOT / "site" / "cards"

CARD_ROWS = [
    "yt-cardboard-ramp-quick",
    "yt-painter-tape-road",
    "yt-cup-building-shorts",
    "yt-masking-tape-city",
    "yt-paper-plate-ramp",
    "yt-ramp-measure",
    "yt-train-tape",
    "yt-paper-towel-rolls-shorts",
    "yt-pom-pom-drop",
    "yt-paper-roll-drop",
    "yt-cardboard-tube-sculptures",
    "yt-magna-tiles-preschool",
    "yt-magna-tiles-three-builds",
    "yt-lego-learning-preschool",
    "yt-duplo-games",
    "yt-block-play-benefits",
]

SLUGS = {
    "yt-cardboard-ramp-quick": "cardboard-car-ramp",
    "yt-painter-tape-road": "tape-road",
    "yt-cup-building-shorts": "cup-tower",
    "yt-masking-tape-city": "tape-city",
    "yt-paper-plate-ramp": "paper-plate-ramp",
    "yt-ramp-measure": "car-ramp-distance-test",
    "yt-train-tape": "tape-train-tracks",
    "yt-paper-towel-rolls-shorts": "paper-roll-play",
    "yt-pom-pom-drop": "pom-pom-drop",
    "yt-paper-roll-drop": "paper-roll-drop",
    "yt-cardboard-tube-sculptures": "tube-sculpture",
    "yt-magna-tiles-preschool": "magnetic-tile-ideas",
    "yt-magna-tiles-three-builds": "magnetic-tile-house",
    "yt-lego-learning-preschool": "lego-color-tower",
    "yt-duplo-games": "duplo-games",
    "yt-block-play-benefits": "block-tower",
}

QUICK_CARD_SLUGS = [slug for slug in ACTIVITIES if slug not in set(SLUGS.values())]


def esc(value):
    return html.escape(value or "", quote=True)


def material_tiles(materials):
    parts = [p.strip() for p in materials.split(";") if p.strip()]
    parts = parts[:3] + ["Time"]
    return parts


def title_to_summary(row):
    return (
        f"{row['time']} · {row['mess']} mess · "
        f"{row['materials'].replace(';', ' +')}"
    )


def clean_step(step):
    return re.sub(r"[.。]+$", "", step.strip())


def quick_material_tiles(materials, time):
    parts = [p.strip() for p in materials.split(",") if p.strip()]
    return [("Need", part) for part in parts[:3]] + [("Time", time)]


def page(row, slug):
    steps = [row[f"kid_step_{i}"] for i in range(1, 5) if row.get(f"kid_step_{i}")]
    step_html = "\n".join(
        f'''          <div class="step-tile">
            <span class="step-number">{i}</span>
            <p>{esc(step)}</p>
          </div>'''
        for i, step in enumerate(steps, 1)
    )
    tiles = material_tiles(row["materials"])
    meta_values = []
    for label in tiles:
        if label == "Time":
            meta_values.append(("Time", row["time"]))
        else:
            meta_values.append(("Need", label))
    meta_values.append(("Mess", f"{row['mess']}"))
    meta_values = meta_values[:4]
    meta_html = "\n".join(
        f'          <div class="meta-tile"><strong>{esc(label)}</strong>{esc(value)}</div>'
        for label, value in meta_values
    )
    description_steps = ", ".join(clean_step(step).lower() for step in steps[:3])
    description = (
        f"{row['activity_title']} activity card for preschoolers: "
        f"{description_steps}."
    )
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(row['activity_title'])} Activity Card | Kid Activity Lab</title>
    <meta name="description" content="{esc(description)}">
    <link rel="canonical" href="https://kidactivitylab.com/cards/{esc(slug)}.html">
    <link rel="stylesheet" href="../styles.css?v=nav-stable-2">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="../index.html">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="../index.html">Home</a>
          <a href="../original/">Original</a>
          <a href="../cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main class="card-shell">
      <article class="kid-card">
        <p class="kicker">{esc(row['time'])} · age {esc(row['age'])}</p>
        <h1>{esc(row['activity_title'])}</h1>

        <iframe class="video-frame" src="{esc(row['embed_url'])}" title="{esc(row['title'])}" loading="lazy" allowfullscreen></iframe>

        <div class="card-meta" aria-label="Activity details">
{meta_html}
        </div>

        <section class="steps-grid" aria-label="Steps">
{step_html}
        </section>

        <section class="parent-strip" aria-label="Parent check">
          <strong>Parent check:</strong> {esc(row['safety_note'])}
        </section>

        <section class="parent-strip" aria-label="Source">
          <strong>Source idea:</strong> adapted from a creator video and simplified into a kid card. <a href="{esc(row['source_url'])}">Watch the source video</a>.
        </section>
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Back to activity cards</a></p>
    </footer>
  </body>
</html>
'''


def quick_page(slug):
    activity = ACTIVITIES[slug]
    steps = activity["steps"]
    step_html = "\n".join(
        f'''          <div class="step-tile">
            <span class="step-number">{i}</span>
            <p>{esc(step)}</p>
          </div>'''
        for i, step in enumerate(steps, 1)
    )
    meta_values = quick_material_tiles(activity["materials"], activity["time"])
    meta_values.append(("Mess", activity["mess"]))
    meta_values = meta_values[:4]
    meta_html = "\n".join(
        f'          <div class="meta-tile"><strong>{esc(label)}</strong>{esc(value)}</div>'
        for label, value in meta_values
    )
    description_steps = ", ".join(clean_step(step).lower() for step in steps[:3])
    description = (
        f"{activity['title']} activity card for kids age {activity['ages']}: "
        f"{description_steps}."
    )
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(activity['title'])} Activity Card | Kid Activity Lab</title>
    <meta name="description" content="{esc(description)}">
    <link rel="canonical" href="https://kidactivitylab.com/cards/{esc(slug)}.html">
    <link rel="stylesheet" href="../styles.css?v=nav-stable-2">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="../index.html">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="../index.html">Home</a>
          <a href="../original/">Original</a>
          <a href="../cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main class="card-shell">
      <article class="kid-card">
        <p class="kicker">{esc(activity['time'])} · age {esc(activity['ages'])}</p>
        <h1>{esc(activity['title'])}</h1>

        <div class="card-meta" aria-label="Activity details">
{meta_html}
        </div>

        <section class="steps-grid" aria-label="Steps">
{step_html}
        </section>

        <section class="parent-strip" aria-label="Parent check">
          <strong>Parent check:</strong> {esc(activity['parent'])}
        </section>

        <section class="parent-strip" aria-label="Best for">
          <strong>Best for:</strong> {esc(activity['best_for'])}.
        </section>
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Back to activity cards</a></p>
    </footer>
  </body>
</html>
'''


def cards_index():
    cards = "\n".join(
        f'        <a class="mini-card" href="cards/{esc(slug)}.html"><strong>{esc(activity["title"])}</strong><span>{esc(activity["time"])} · {esc(activity["materials"])}</span></a>'
        for slug, activity in ACTIVITIES.items()
    )
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Activity Cards | Kid Activity Lab</title>
    <meta name="description" content="One-screen activity cards preschoolers can follow with parent help. Low-prep play using household materials.">
    <link rel="stylesheet" href="styles.css?v=nav-stable-2">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="index.html">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="index.html">Home</a>
          <a href="original/">Original</a>
          <a href="cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero">
        <p class="kicker">Activity cards</p>
        <h1>Pick one small thing.</h1>
        <p class="dek">Each card is meant to fit on one screen: materials, steps, parent check, and source video when one is available.</p>
      </section>

      <section class="library-grid" aria-label="Activity cards">
{cards}
      </section>
    </main>

    <footer class="site-footer">
      <p>One-screen activity cards with parent safety checks.</p>
    </footer>
  </body>
</html>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with DATA.open() as f:
        rows = {row["source_id"]: row for row in csv.DictReader(f)}
    for source_id in CARD_ROWS:
        row = rows[source_id]
        slug = SLUGS[source_id]
        (OUT / f"{slug}.html").write_text(page(row, slug))
    for slug in QUICK_CARD_SLUGS:
        (OUT / f"{slug}.html").write_text(quick_page(slug))
    (ROOT / "site" / "cards.html").write_text(cards_index())
    print(f"generated {len(CARD_ROWS) + len(QUICK_CARD_SLUGS)} card pages and cards index")


if __name__ == "__main__":
    main()
