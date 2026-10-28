import csv
import html
import re
from pathlib import Path

from generate_seo_pages import ACTIVITIES, PAGES


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

ROUTE_PRIORITY = [
    "ages/stem-activities-for-4-year-olds.html",
    "collections/engineering-activities-for-4-year-olds.html",
    "collections/math-activities-for-4-year-olds-at-home.html",
    "collections/stem-activities-for-preschoolers.html",
    "ages/activities-for-4-year-olds-at-home.html",
    "collections/science-experiments-for-4-year-olds.html",
    "collections/building-activities-for-4-year-olds.html",
    "collections/no-prep-stem-activities-for-4-year-olds.html",
    "collections/no-prep-activities-for-preschoolers.html",
    "collections/indoor-activities-for-preschoolers.html",
    "collections/independent-activities-for-preschoolers.html",
    "collections/fine-motor-activities-for-preschoolers.html",
    "ages/activities-for-3-year-olds-at-home.html",
    "ages/activities-for-5-year-olds-at-home.html",
    "ages/activities-for-6-year-olds-at-home.html",
]
ROUTE_RANK = {path: index for index, path in enumerate(ROUTE_PRIORITY)}
MAX_RELATED_ROUTES = 3
GUIDE_ROUTES = {
    "tape-train-tracks": {
        "path": "articles/painter-tape-road-kids.html",
        "label": "Tape Road surface and route help",
    },
    "cup-tower": {
        "path": "articles/paper-cup-tower-kids.html",
        "label": "Full Paper Cup Tower guide",
    },
    "ball-maze-box": {
        "path": "articles/cardboard-ball-maze-kids.html",
        "label": "Full Cardboard Ball Maze guide",
    },
    "paper-bridge": {
        "path": "articles/paper-bridge-challenge-kids.html",
        "label": "Full Paper Bridge guide",
    },
    "tape-road": {
        "path": "articles/painter-tape-road-kids.html",
        "label": "Full Painter's Tape Road guide",
    },
    "tape-city": {
        "path": "articles/painter-tape-road-kids.html",
        "label": "Start with the Painter's Tape Road guide",
    },
}
QUICK_CARD_OVERRIDES = {
    "block-tower": {
        "kicker": "Editorial ages 3-6 | Adult models and stays",
        "description": "Block Tower: three checked owned blocks, one low placement or flat row, adult trial and top-first collection. Research-backed, not family-tested.",
    },
    "tape-train-tracks": {
        "kicker": "Editorial ages 3-6 | Adult sets and stays",
        "description": "Tape Train Tracks: an adult-prepared cardboard station, one suitable owned hand-pushed train and a first push or point/watch/end. Research-backed, not family-tested.",
    },
    "lego-color-tower": {
        "title": "LEGO Color Tower",
        "kicker": "Sort first | Adult checks and stays",
        "description": "Color Tower: four owned large DUPLO bricks, two visible color seeds, flat matching and optional two-brick stacks. Research-backed, not family-tested.",
    },
    "tube-sculpture": {
        "kicker": "Editorial ages 4-6 | Adult tapes and stays",
        "description": "Tube Sculpture: adult-checked whole tubes and a cardboard base, a first tape trial, one low arrangement or untaped/end fallback. Research-backed, not family-tested.",
    },
    "spoon-transfer": {
        "kicker": "One pom | Adult checks, models and stays",
        "description": "Spoon Transfer: one owned play pom-pom, an adult spoon-fit trial, two bowls and a tray. Scoop and tip, point, watch or decline; research-backed, not family-tested.",
    },
    "balance-scale-baskets": {
        "kicker": "Adult holds and loads | Point or watch",
        "description": "Cup Balance Watch: adult-made matching cup handles, central support, an empty-level check and supported loading. Uncalibrated observation; research-backed, not family-tested.",
    },
    "measuring-tape-jumps": {
        "kicker": "Place by hand | Compare gaps",
        "description": "Toy Distance Marks: an adult-prepared board, hand-placed block and nearer, farther or unclear comparison from one starting edge. No jumps or numeric measurement; research-backed, not family-tested.",
    },
    "pattern-path": {
        "kicker": "One AB pair | Adult sets choices",
        "description": "Pattern Path activity card: an adult-laid A-B-A-B starter, two next-piece choices, pointing or matching fallback, and one extension. Research-backed, not family-tested.",
    },
    "wind-tower-test": {
        "kicker": "Build low | Adult fans",
        "description": "Wind Tower Test activity card: a checked low block build, adult-only paper fan and standing, moved, fell or unclear result. Research-backed, not family-tested.",
    },
    "ramp-texture-test": {
        "kicker": "Same car | Adult steadies",
        "description": "Ramp Texture Test activity card: adult-supported floor ramp, same-car releases and one optional secured cloth comparison, with an unclear-result end. Research-backed, not family-tested.",
    },
    "water-drop-race": {
        "kicker": "One drop | Supported tilt",
        "description": "Water Drop Tilt activity card: one plain-water drop on supported wax paper, adult-steady tray movement and a moved, stayed or unclear result. No mouth tools; research-backed, not family-tested.",
    },
    "color-mixing-cups": {
        "kicker": "Adult mixes | Child notices",
        "description": "Color Mixing Cups activity card: adult-prepared red and yellow water, an empty receiving cup, and a look for difference or uncertainty. Research-backed, not family-tested.",
    },
    "ice-melt-rescue": {
        "kicker": "Adult handles | Child watches",
        "description": "Melting Ice Watch activity card: one plain ice cube in an adult-controlled tray, a look for change or not yet clear, and immediate cleanup. No added heat; research-backed, not family-tested.",
    },
    "shadow-shape-match": {
        "kicker": "Adult-controlled light | One block",
        "description": "Shadow Builder activity card: adult-controlled wall light, one checked opaque block and a small shadow-size comparison, with stop and rescue. Research-backed, not family-tested.",
    },
    "box-garage": {
        "kicker": "One car | Adult-guided",
        "description": "Box Garage activity card: one already-open box and one owned toy car, adult fit checks and a no-cut park-and-drive-out start. Research-backed, not family-tested.",
    },
    "blanket-river": {
        "kicker": "Toy-only | Adult-guided",
        "description": "Blanket River activity card: a tiny three-block crossing near one blanket edge for a hand-carried toy, never feet. Early adult fit and stop checks; research-backed, not family-tested.",
    },
    "duplo-games": {
        "kicker": "Open-ended | Adult-guided",
        "description": "DUPLO Games activity card: use four owned bricks in two matching pairs to copy a visible two-brick model, compare and reset. Research-backed, not family-tested by Kid Activity Lab.",
    },
    "cardboard-car-ramp": {
        "time": "Open-ended",
        "materials": "flat stiff cardboard, two broad closed books, one toy car",
    },
    "paper-chain-test": {
        "time": "Open-ended",
        "materials": "paper, tape, adult-prepared strips",
    },
    "cup-tower": {
        "time": "Open-ended",
        "mess": "Not measured",
        "materials": "2 matching lightweight paper cups and 1 optional spare",
        "kicker": "Open-ended | Adult-guided",
        "description": "Cup Tower activity card: put one cup upside down, balance a second cup bottom-to-bottom, then reset. Research-backed, not family-tested by Kid Activity Lab.",
        "steps": [
            "Adult puts one cup upside down.",
            "Set another bottom-to-bottom on it.",
            "Take the top cup off gently.",
            "Rebuild or try one change.",
        ],
        "parent": "Stay beside the child on a firm low clear surface, away from edges and feet. Choose intact lightweight cups suitable for everyone who can reach them; keep spares out of younger children's reach. Skip if you cannot stay and attend to them. Stop after mouthing, throwing, damage, climbing or unwanted collapse. Research-backed, not family-tested by Kid Activity Lab.",
        "best_for": "trying a small build and noticing what changes",
    },
    "ball-maze-box": {
        "time": "Open-ended",
        "materials": "shallow box lid, chunky blocks, large lightweight ball",
        "best_for": "building a path, rolling, changing one wall",
        "steps": [
            "Put the lid flat.",
            "Set three blocks as wide walls.",
            "Adult adds one large ball.",
            "Tilt gently, then reset.",
        ],
        "parent": (
            "Adult controls the ball and stays close. Stop after throwing, "
            "mouthing, hard shaking, a spill, or damaged material."
        ),
    },
    "paper-bridge": {
        "time": "Open-ended",
        "materials": "paper, two low closed books, large lightweight object",
        "best_for": "building, comparing, changing one thing",
        "steps": [
            "Adult sets two books low.",
            "Lay one paper sheet across.",
            "Place one large object gently.",
            "Optional: fold the paper and compare.",
        ],
        "parent": (
            "Stay beside the setup. Stop if books slide, the object is thrown, "
            "paper goes in a mouth or tears, or the setup becomes climbing play. "
            "Remove loose paper pieces before continuing."
        ),
    },
    "tape-road": {
        "time": "Open-ended",
        "materials": "surface-appropriate painter's tape, 1-2 large intact toy vehicles",
    },
    "tape-city": {
        "time": "Open-ended",
        "materials": "surface-appropriate painter's tape, large toy vehicles, chunky blocks",
    },
}


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


def related_routes(slug):
    routes = [page for page in PAGES if slug in page["activities"]]
    routes.sort(key=lambda page: (ROUTE_RANK.get(page["path"], len(ROUTE_RANK)), page["path"]))
    return routes[:MAX_RELATED_ROUTES]


def related_routes_html(slug, include_guide=True, max_links=MAX_RELATED_ROUTES):
    links = []
    guide = GUIDE_ROUTES.get(slug) if include_guide else None
    if guide:
        links.append(
            f'<a href="../{esc(guide["path"])}">{esc(guide["label"])}</a>'
        )
    links.extend(
        f'<a href="../{esc(route["path"])}">{esc(route.get("route_label", route["h1"]).rstrip("."))}</a>'
        for route in related_routes(slug)
    )
    links = links[:max_links]
    if not links:
        return ""
    return f'''

        <section class="parent-strip" aria-label="Related activity pages">
          <strong>More ways to use this idea:</strong> {" · ".join(links)}
        </section>'''


def page(row, slug):
    if slug == "cardboard-car-ramp":
        return ramp_card_page(row)
    if slug == "paper-roll-play":
        return paper_roll_card_page(row)
    is_tape_road = slug == "tape-road"
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
    meta_values.append(("Mess", "Not measured" if is_tape_road else row["mess"]))
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
    routes = related_routes_html(
        slug, include_guide=not is_tape_road,
        max_links=2 if is_tape_road else MAX_RELATED_ROUTES,
    )
    safety_note = (
        "Adult stays close, keeps loose tape and the roll out of reach, and removes the tape at the end. "
        "Stop for peeling, chewing, wrapping, throwing, mouthing, leaving the activity area, or any surface change."
        if is_tape_road else row["safety_note"]
    )
    guide_decision = '''

        <section class="tape-road-decision" aria-label="Decide before starting">
          <p><a href="../articles/painter-tape-road-kids.html">Full Painter&#x27;s Tape Road guide</a> for fit, board fallback, rescue, and cleanup.</p>
          <p>Adult chooses tape for the surface: follow the tape maker's guidance, test one strip in an inconspicuous area, then remove it and check the surface. If the floor or finish is unknown or unsuitable, use a large cardboard sheet, table, or tray you are willing to tape. Research-backed, not family-tested by Kid Activity Lab.</p>
        </section>''' if is_tape_road else ""
    parent_check = f'''

        <section class="parent-strip" aria-label="Parent check">
          <strong>Parent check:</strong> {esc(safety_note)}
        </section>'''
    video = f'''

        <iframe class="video-frame" src="{esc(row['embed_url'])}" title="{esc(row['title'])}" loading="lazy" allowfullscreen></iframe>'''
    early_parent_check = parent_check if is_tape_road else ""
    late_parent_check = "" if is_tape_road else parent_check
    early_video = "" if is_tape_road else video
    late_video = video if is_tape_road else ""
    card_class = "kid-card tape-road-card" if is_tape_road else "kid-card"
    css_version = "tape-road-card-1" if is_tape_road else "nav-stable-2"
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(row['activity_title'])} Activity Card | Kid Activity Lab</title>
    <meta name="description" content="{esc(description)}">
    <link rel="canonical" href="https://kidactivitylab.com/cards/{esc(slug)}.html">
    <link rel="stylesheet" href="../styles.css?v={css_version}">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="../original/">Original</a>
          <a href="../cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main class="card-shell">
      <article class="{card_class}">
        <p class="kicker">{esc(row['time'])} · age {esc(row['age'])}</p>
        <h1>{esc(row['activity_title'])}</h1>{guide_decision}{early_video}

        <div class="card-meta" aria-label="Activity details">
{meta_html}
        </div>{early_parent_check}

        <section class="steps-grid" aria-label="Steps">
{step_html}
        </section>{late_parent_check}{late_video}

        <section class="parent-strip" aria-label="Source">
          <strong>Source idea:</strong> adapted from a creator video and simplified into a kid card. <a href="{esc(row['source_url'])}">Watch the source video</a>.
        </section>{routes}
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Back to activity cards</a></p>
    </footer>
  </body>
</html>
'''


def paper_roll_card_page(row):
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Paper Roll Play Activity Card | Kid Activity Lab</title>
    <meta name="description" content="One empty paper roll, an adult beside you and a gentle push: a preschool start with material checks, a reset and a stop. Research-backed, not family-tested.">
    <link rel="canonical" href="https://kidactivitylab.com/cards/paper-roll-play.html">
    <link rel="stylesheet" href="../styles.css?v=nav-stable-2">
    <style>
      .paper-roll-card {{ max-width: 720px; margin: 0 auto; overflow-wrap: anywhere; }}
      .paper-roll-card h1 {{ font-size: min(2rem, 48px); line-height: 1.15; letter-spacing: 0; }}
      .paper-roll-card h2 {{ font-size: 1.25rem; line-height: 1.3; }}
      .paper-roll-card p {{ line-height: 1.5; }}
      .paper-roll-card .card-meta {{ grid-template-columns: 1fr; }}
      .paper-roll-card .steps-grid {{ grid-template-columns: 1fr; }}
      .paper-roll-card .step-tile {{ min-height: 0; padding: 14px; }}
      .paper-roll-card .step-tile p {{ margin: 8px 0 0; font-size: 1.15rem; }}
      .paper-roll-card summary {{ cursor: pointer; }}
    </style>
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links"><a href="/">Home</a><a href="../original/">Original</a><a href="../cards.html">Cards</a></div>
      </nav>
    </header>
    <main class="card-shell">
      <article class="kid-card paper-roll-card">
        <p class="kicker">Adult-guided &middot; preschool play</p>
        <h1>Paper Roll Play</h1>
        <p>One empty roll, one gentle push. Explore how it moves, with an adult beside you.</p>
        <p>Research-backed, not family-tested by Kid Activity Lab. Duration and mess have not been measured.</p>
        <div class="card-meta" aria-label="Materials">
          <div class="meta-tile"><strong>Need</strong>1 empty lightweight paper-towel roll and clear, level floor space.</div>
        </div>
        <section class="parent-strip" aria-label="Before starting">
          <h2>Adult check first</h2>
          <p>Choose a clean, dry, intact roll without staples, sharp edges, loose covering or attached parts. No hard mailing tubes, blade packaging, small toys, fillers, cords or ramp. If you cannot find a suitable roll, skip.</p>
          <p>Clear space away from steps and traffic. Stay beside every reachable child; skip if you cannot watch them all. Try only if the child can leave the roll out of their mouth and respond to your stop cue, with help.</p>
          <p>Stop for mouthing, tearing, damage, throwing, unsafe reach, lost adult attention or when the child wants to stop. This is an adult judgment, not a safety assurance.</p>
        </section>
        <section class="steps-grid" aria-label="Steps">
          <div class="step-tile"><span class="step-number">1</span><p>Adult: lay the empty roll on its curved side, opening sideways. Model a gentle push along the floor.</p></div>
          <div class="step-tile"><span class="step-number">2</span><p>Kid mission: push the empty roll and watch it move. Watching an adult push is also an option.</p></div>
          <div class="step-tile"><span class="step-number">3</span><p>Wait until it stops. Retrieve it together and put it back on its side.</p></div>
          <div class="step-tile"><span class="step-number">4</span><p>Push again only if wanted, or finish. No distance, speed or target to reach.</p></div>
        </section>
        <section class="parent-strip" aria-label="Rescue and cleanup">
          <h2>If it does not roll</h2>
          <p>Adult checks it is on its side and the space is clear, then models a gentle push. The child can watch or point instead. If it is unsuitable or unwanted, stop; do not add toys, a slope or force.</p>
          <p><strong>Finish:</strong> adult collects the roll and spares, removes damaged material and stores everything away.</p>
        </section>
        <section class="parent-strip" aria-label="Sources and testing status">
          <h2>Sources and testing status</h2>
          <p><a href="https://ei.northwestern.edu/toy-recommendations-toilet-paper-tubes/">Northwestern EIRG</a> describes empty-tube rolling. The floor start, script and controls here are Kid Activity Lab's editorial adaptation, not clinical guidance. General material and supervision checks draw on <a href="https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx">AAP toy guidance</a> and the <a href="https://www.cpsc.gov/s3fs-public/blk_media_5015_0.pdf#page=5">CPSC art-material guide</a>; they do not certify a reused roll.</p>
          <p>Sources checked October 27, 2026. Physical suitability, family understanding, enjoyment, learning and safety outcomes are unknown.</p>
          <details><summary>Previous video reference (optional)</summary><p><a href="{esc(row['source_url'])}">Original creator reference</a> from the earlier mixed-toy card, not the source of the empty-roll rule above. We have not verified its current playback. It is not needed to start this version.</p></details>
        </section>
      </article>
    </main>
    <footer class="site-footer"><p><a href="../cards.html">Back to activity cards</a></p></footer>
  </body>
</html>
'''


def ramp_card_page(row):
    routes = related_routes_html("cardboard-car-ramp")
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Cardboard Car Ramp Activity Card | Kid Activity Lab</title>
    <meta name="description" content="A no-cut cardboard car ramp start: materials, adult setup, a first roll and one rescue. Open the full guide for more help. Research-backed, not family-tested.">
    <link rel="canonical" href="https://kidactivitylab.com/cards/cardboard-car-ramp.html">
    <link rel="stylesheet" href="../styles.css?v=nav-stable-2">
    <style>
      .ramp-card {{ max-width: 720px; margin: 0 auto; padding: 20px; overflow-wrap: anywhere; }}
      .ramp-card h1 {{ font-size: 2rem; line-height: 1.15; letter-spacing: 0; margin: 8px 0 16px; }}
      .ramp-card h2 {{ font-size: 1.2rem; margin: 20px 0 8px; }}
      .ramp-card p, .ramp-card li {{ line-height: 1.5; }}
      .ramp-card p {{ margin: 10px 0; }}
      .ramp-card ol {{ padding-left: 1.5rem; margin: 8px 0; }}
      .ramp-card li {{ margin: 8px 0; }}
      .ramp-card .evidence {{ font-size: 0.9rem; }}
      .ramp-card .parent-strip {{ margin-top: 18px; }}
      .ramp-card .depth-link {{ display: block; width: fit-content; max-width: 100%; }}
      .ramp-card a:focus-visible {{ outline: 3px solid #176b62; outline-offset: 3px; }}
    </style>
  </head>
  <body>
    <header class="site-header"><nav class="nav" aria-label="Main navigation">
      <a class="brand" href="/">Kid Activity Lab</a>
      <div class="nav-links"><a href="/">Home</a><a href="../original/">Original</a><a href="../cards.html">Cards</a></div>
    </nav></header>
    <main><article class="ramp-card">
      <p class="kicker">Adult-guided · Open-ended</p>
      <h1>Cardboard Car Ramp</h1>
      <p class="start-cue"><strong>Adult check:</strong> Floor only; supervise. Stop for climbing, throwing or mouthing.</p>
      <p><strong>Use:</strong> one flat, stiff piece of cardboard, two broad sturdy closed books, and one toy car with freely turning wheels. No cutting or glue.</p>
      <p><strong>Parent check:</strong> Supervise directly and use toys appropriate for every child who can reach them. Stop for climbing, throwing or mouthing. No stairs or furniture.</p>
      <h2>Adult setup</h2>
      <ol>
        <li>Stack the two books flat on the floor. Clear a landing area away from feet, breakable objects and stairs.</li>
        <li>Rest one end of the cardboard on the books and the other on the floor. Test one car yourself; hold the cardboard if it slips.</li>
      </ol>
      <p><strong>Kid mission:</strong> Choose a car. Let it roll from the top without pushing. Or point to a car for the adult to roll.</p>
      <p><strong>If the car stops:</strong> try a shorter piece of cardboard or move the support closer to the middle. Keep the support low.</p>
      <p><a class="depth-link" href="../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start">Full setup and troubleshooting</a></p>
      <p><strong>Cleanup:</strong> put the books and car away; store the flat cardboard or recycle it.</p>
      <p class="evidence">Research-backed, not family-tested by Kid Activity Lab. Setup time and play duration are not measured. This is a compact version of our full guide; its sources and optional comparisons are there.</p>
      <p class="evidence"><strong>Original inspiration:</strong> <a href="{esc(row['source_url'])}">source video</a> (optional).</p>{routes}
    </article></main>
    <footer class="site-footer"><p><a href="../cards.html">Back to activity cards</a></p></footer>
  </body>
</html>
'''


def paper_chain_page():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Paper Chain: Make Linked Loops | Kid Activity Lab</title>
    <meta name="description" content="Make a paper chain with a clear thread-then-close start, an original loop diagram, fixes for separate rings, and an optional one-sheet challenge. Adult preparation.">
    <link rel="canonical" href="https://kidactivitylab.com/cards/paper-chain-test.html">
    <link rel="stylesheet" href="../styles.css?v=nav-stable-2">
    <style>
      .chain-guide { max-width: 700px; margin: 0 auto; padding: 24px 20px 40px; }
      .chain-guide h1 { font-size: 2rem; letter-spacing: 0; margin: 8px 0; }
      .chain-guide h2 { font-size: 1.35rem; letter-spacing: 0; margin: 24px 0 8px; }
      .chain-guide p, .chain-guide li { line-height: 1.5; }
      .chain-guide p { margin: 10px 0; }
      .chain-guide ol { padding-left: 1.5rem; margin: 10px 0; }
      .chain-guide li { margin: 7px 0; }
      .chain-guide .boundary { font-size: 0.9rem; color: #47534e; }
      .chain-guide .start { border-top: 2px solid #176b62; margin-top: 18px; }
      .chain-guide figure { margin: 24px 0; max-width: 580px; }
      .chain-guide img { display: block; width: 100%; height: auto; aspect-ratio: 9 / 11; }
      .chain-guide figcaption { font-size: 0.9rem; }
      .chain-guide details { border-top: 1px solid #cad3ce; padding: 16px 0; }
      .chain-guide summary { cursor: pointer; font-weight: 700; padding: 8px 0; }
      .chain-guide section { scroll-margin-top: 7rem; }
      .chain-guide a, .chain-guide summary { overflow-wrap: anywhere; }
      .chain-guide a:focus-visible, .chain-guide summary:focus-visible { outline: 3px solid #246b8f; outline-offset: 3px; }
      .chain-guide .jump { display: flex; flex-wrap: wrap; gap: 8px 24px; }
      .chain-guide .jump a { padding: 8px 0; }
    </style>
  </head>
  <body>
    <header class="site-header"><nav class="nav" aria-label="Main navigation">
      <a class="brand" href="/">Kid Activity Lab</a>
      <div class="nav-links"><a href="/">Home</a><a href="../original/">Original</a><a href="../cards.html">Cards</a></div>
    </nav></header>
    <main><article class="chain-guide">
      <p class="kicker">Paper + tape | Adult-guided</p>
      <h1>Make a paper chain</h1>
      <p>Turn two strips into linked loops. Then decide: add another, compare, or stop.</p>
      <p class="boundary">Research-backed; not family-tested by Kid Activity Lab.</p>
      <p><strong>Before you start:</strong> Keep paper, tape and chain on the table, out of a younger child's reach. Stay beside your child; put the materials away if you cannot watch both children. No wearing chains or hanging them across a walkway. Stop if paper or tape goes in a mouth, the chain is pulled around a body, or play becomes unwanted or hard to control.</p>
      <p><strong>Gather:</strong> ordinary paper, tape and scissors for the adult. Use a clear tabletop, with room to lay the chain down.</p>
      <p><strong>Adult setup:</strong> cut strips roughly 15 cm long and 2 cm wide (about 6 by 3/4 inches). This is our starting suggestion, not a tested best size. Check that a strip curls and its ends overlap without forcing; adjust if needed. Prepare tape pieces and put scissors away.</p>
      <section class="start" id="start" aria-labelledby="start-title">
        <h2 id="start-title">First, link two loops</h2>
        <ol>
          <li>Curl one strip. Overlap <strong>its own ends</strong> and tape them together to close the first loop.</li>
          <li>Pass a new, <strong>open strip through the hole</strong> in that loop.</li>
          <li>Bring the new strip's own ends together and tape them. Now the two loops are linked, not taped to each other.</li>
          <li>Repeat through the newest loop, or finish with two.</li>
        </ol>
        <p><strong>Say:</strong> "Can you put this strip through that loop?" Stay beside your child; hold the loop or handle the tape as needed. Choosing a strip or watching also counts as taking part.</p>
        <nav class="jump" aria-label="Activity help"><a href="#rescue">Loops not joining?</a><a href="#challenge">Try one sheet</a></nav>
      </section>
      <figure>
        <img src="../assets/paper-chain/linked-loops.png" width="900" height="1100" alt="Three stages: close the first loop; pass an open strip through its hole; close that new strip around the first loop by joining its own ends. The two loops interlock but are not taped to each other.">
        <figcaption>Original KAL explanation, not to scale or a cutting template. <a href="../assets/paper-chain/linked-loops.png">Open the full-size loop diagram</a>.</figcaption>
      </figure>
      <section id="rescue" aria-labelledby="rescue-title">
        <h2 id="rescue-title">Loops not joining?</h2>
        <p><strong>Two separate circles?</strong> Use a fresh open strip, pass it through the last loop, then close it. Closing it first leaves nothing to thread.</p>
        <p><strong>Tape lifting or paper tearing?</strong> The adult can reattach the same joint. For a free build, replace torn paper or finish. In the one-sheet trial below, repair with the original pieces or end that attempt; no extra paper.</p>
        <p><strong>Joining feels too fiddly?</strong> Let the adult hold and join while the child chooses, counts or watches. Skip tape handling if the feel bothers them. For a sibling, offer choosing or watching only if loose pieces stay out of reach and you can attend to both children; otherwise put the materials away and try later.</p>
        <p><strong>Finish:</strong> lay the chain down gently and notice which loop connects to which. Gather all strips, tape and offcuts. No timer is needed; setup, play time and cleanup effort have not been measured.</p>
      </section>
      <section id="challenge" aria-label="Optional one-sheet challenge">
        <details><summary>Optional: how long can one sheet reach?</summary>
          <p>After a linked start, choose these rules together. This is our version of a one-sheet challenge, not a universal rule set.</p>
          <ul>
            <li>Use one sheet per attempt. For comparison, start each attempt with the same size and type of paper. The adult still cuts; choose strip sizes together.</li>
            <li>Make interlocking loops only. Tape closes each loop; it does not extend the paper or join flat strips end-to-end.</li>
            <li>Lay chains side by side from a common starting point, without stretching. Which reaches farther? More links need not mean more length if their sizes differ.</li>
            <li>Repair only with that attempt's paper, or stop. A fresh sheet starts a new attempt. Changing the rules makes a different challenge.</li>
          </ul>
          <p>No race, ruler or printer needed. Prefer a target instead? Try the <a href="../collections/engineering-activities-for-4-year-olds.html#paper-chain-test">book-reach mission</a>; it uses the same loops without the one-sheet rule.</p>
        </details>
      </section>
      <details><summary>Sources and what we haven't tested</summary>
        <p><a href="https://www.wttw.com/kids/learn-and-play/activities/social-emotional-development/paper-chain">WTTW's Paper Chain</a> supports the thread-then-close sequence and an untimed assisted option. <a href="https://littlebinsforlittlehands.com/paper-chain-stem-challenge/">Little Bins' paper-chain challenge</a> supplies the one-sheet comparison idea. <a href="https://teachersareterrific.com/2015/08/the-paper-chain-an-easy-prep-stem-challenge.html">Teachers are Terrific's challenge</a> illustrates why the meaning of "chain" needs explicit rules. <a href="https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx">AAP guidance</a> supports checking younger children's reach to small objects in general, not a safety outcome for this setup. WTTW and AAP checked October 15, 2026; challenge sources rechecked October 7, 2026.</p>
        <p>Strip dimensions, roles, rescue suggestions, limits and comparison rules here are KAL editorial choices. We have not physically or family-tested this version. Age alone does not establish fit; dexterity, time, enjoyment, learning, mess and safety outcomes remain unknown.</p>
      </details>
      <p><a href="../cards.html">Choose another activity</a></p>
    </article></main>
    <footer class="site-footer"><p>Kid Activity Lab</p></footer>
  </body>
</html>
'''


def foil_boat_page():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Make a Foil Boat: An Empty-Boat Start | Kid Activity Lab</title>
    <meta name="description" content="Shape an empty foil boat with an adult, check whether it floats freely, and try a small repair or stop. Clear folds, a diagram and cleanup steps. No cargo needed.">
    <link rel="canonical" href="https://kidactivitylab.com/cards/foil-boat-test.html">
    <link rel="stylesheet" href="../styles.css?v=nav-stable-2">
    <style>
      .boat-guide { max-width: 700px; margin: 0 auto; padding: 24px 20px 40px; }
      .boat-guide h1 { font-size: 2rem; letter-spacing: 0; margin: 8px 0; }
      .boat-guide h2 { font-size: 1.35rem; letter-spacing: 0; margin: 24px 0 8px; }
      .boat-guide p, .boat-guide li { line-height: 1.5; }
      .boat-guide p { margin: 10px 0; }
      .boat-guide ol { padding-left: 1.5rem; margin: 10px 0; }
      .boat-guide li { margin: 8px 0; }
      .boat-guide .boundary { font-size: 0.9rem; color: #47534e; }
      .boat-guide .start { border-top: 2px solid #176b62; margin-top: 18px; }
      .boat-guide figure { margin: 24px 0; max-width: 580px; }
      .boat-guide img { display: block; width: 100%; height: auto; aspect-ratio: 9 / 10; }
      .boat-guide figcaption { font-size: 0.9rem; }
      .boat-guide details { border-top: 1px solid #cad3ce; padding: 16px 0; }
      .boat-guide summary { cursor: pointer; font-weight: 700; padding: 8px 0; }
      .boat-guide section { scroll-margin-top: 7rem; }
      .boat-guide a, .boat-guide summary { overflow-wrap: anywhere; }
      .boat-guide a:focus-visible, .boat-guide summary:focus-visible { outline: 3px solid #246b8f; outline-offset: 3px; }
      .boat-guide .jump { display: flex; flex-wrap: wrap; gap: 8px 24px; }
      .boat-guide .jump a { padding: 8px 0; }
    </style>
  </head>
  <body>
    <header class="site-header"><nav class="nav" aria-label="Main navigation">
      <a class="brand" href="/">Kid Activity Lab</a>
      <div class="nav-links"><a href="/">Home</a><a href="../original/">Original</a><a href="../cards.html">Cards</a></div>
    </nav></header>
    <main><article class="boat-guide">
      <p class="kicker">Foil + water | Adult-guided</p>
      <h1>Make a foil boat</h1>
      <p>Turn a flat sheet into an open boat. Will it float without touching the tray?</p>
      <p class="boundary">Research-backed; not family-tested by Kid Activity Lab.</p>
      <p><strong>Gather:</strong> one square of foil, a shallow tray, water and a towel. No coins, blocks or other cargo: this is an empty-boat start, not a load-carrying challenge.</p>
      <p><strong>Adult setup:</strong> put the tray on a stable, wipeable surface with the towel underneath. You control the water and stay beside the setup throughout. Even shallow water needs continuous adult supervision.</p>
      <section class="start" id="start" aria-labelledby="start-title">
        <h2 id="start-title">Shape it, then try it empty</h2>
        <ol>
          <li><strong>Raise the edges.</strong> Start with foil roughly 20 cm (8 inches) square. Fold all four edges upward about 2 cm (3/4 inch), leaving a broad, flat middle. These sizes are our starting suggestion, not a tested best fit.</li>
          <li><strong>Pinch the corners.</strong> Bring neighboring raised edges together at each corner. Pinch the extra foil into a small flap against the outside. Do not cut the corners. Keep the top open and the rim roughly even.</li>
          <li><strong>Adult places the empty boat.</strong> Add a shallow layer of water to the tray and lower the boat gently. Check that it can float clear of the bottom and sides, not sit on them. If you cannot check this in the shallow tray, stop; do not switch to a deeper vessel.</li>
          <li><strong>Notice one thing.</strong> Say, "Does it stay upright, lean, or let water in?" Finish there, or ask the adult to lift it out before changing one side.</li>
        </ol>
        <p><strong>Stop and clear up</strong> if foil goes in a mouth, tears, water spills, the tray moves, attention lapses or the child wants to leave. The adult removes the boat, gathers the foil, empties and stores the tray, and wipes spills. Do this before leaving; an older child is not a substitute supervisor.</p>
        <nav class="jump" aria-label="Activity help"><a href="#rescue">Boat not floating?</a><a href="#take-part">Ways to take part</a></nav>
      </section>
      <figure>
        <img src="../assets/foil-boat/empty-hull.png" width="900" height="1000" alt="Three stages: a square of foil with four fold lines near its edges; raise the edges and pinch the extra corner foil outside without cutting; leave a broad flat bottom, open top and even rim. No cargo goes inside.">
        <figcaption>Original KAL fold explanation, not a cutting template or proof of flotation. <a href="../assets/foil-boat/empty-hull.png">Open the full-size fold diagram</a>.</figcaption>
      </figure>
      <section id="rescue" aria-labelledby="rescue-title">
        <h2 id="rescue-title">Boat not floating?</h2>
        <p><strong>Resting on the tray?</strong> That is not a floating result. Stop this attempt if the boat cannot float freely in the shallow setup; choose a dry activity instead of adding depth.</p>
        <p><strong>Leaning or taking in water?</strong> The adult lifts it out, drains it over the tray and sets it on the towel. Look for a low rim, uneven bottom or tear. Gently flatten the bottom or raise one low edge. Replace torn foil or stop; pinching is not a guarantee against leaks.</p>
        <p>Try the empty boat once more if you both want to, or finish. No cargo or sinking contest is needed.</p>
      </section>
      <section id="take-part" aria-labelledby="take-part-title">
        <h2 id="take-part-title">Ways to take part</h2>
        <p>The adult can do the folding and all wet handling while the child chooses a side to change or watches. Use those roles for siblings too; stop if you cannot attend to everyone. If foil or water feels unwelcome, watch without touching or choose a <a href="paper-chain-test.html">dry paper-chain activity</a>.</p>
        <p>Age alone does not decide fit. Setup, play time, cleanup effort and individual handling ability have not been measured.</p>
      </section>
      <details><summary>Sources and what we haven't tested</summary>
        <p><a href="https://www.sciencebuddies.org/stem-activities/aluminum-foil-boats-float">Science Buddies</a> supports an open hull with a flat bottom and even rim. <a href="https://www.discoveryworld.org/wp-content/uploads/2022/09/Aluminum-Foil-Boat-.pdf">Discovery World</a> distinguishes floating from resting on the container. <a href="https://discovere.org/engineering-activities/foil-boats/">DiscoverE</a> suggests noticing leaning and leaks. Their cargo experiments are not this simpler empty-boat version.</p>
        <p><a href="https://www.cpsc.gov/Newsroom/News-Releases/2010/CPSC-Warns-of-In-Home-Drowning-Dangers-with-Bathtubs-Bath-Seats-Buckets">CPSC water guidance</a> calls for continuous supervision near water. No water depth makes this activity universally safe. Sources checked September 24, 2026; source guidance is not an endorsement of this adaptation.</p>
        <p>Sizes, roles, diagram, rescue and limits here are KAL editorial choices. We have not physically or family-tested this version. Flotation, timing, enjoyment, learning, mess and safety outcomes remain unknown. Coins and assorted blocks are not established substitutes, so this version leaves cargo out.</p>
      </details>
      <section class="parent-strip" aria-label="Related activity pages">
        <p><a href="../collections/engineering-activities-for-4-year-olds.html#foil-boat-test">Back to the engineering chooser</a></p>
      </section>
      <p><a href="../cards.html">Choose another activity</a></p>
    </article></main>
    <footer class="site-footer"><p>Kid Activity Lab</p></footer>
  </body>
</html>
'''


def magnet_hunt_pause_page():
    activity = ACTIVITIES["magnet-hunt"]
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Magnet Hunt Paused | Kid Activity Lab</title>
    <meta name="description" content="Magnet Hunt is paused while the magnet type and power are unspecified. Choose a maintained non-magnet activity instead.">
    <meta name="robots" content="noindex,follow">
    <link rel="canonical" href="https://kidactivitylab.com/cards/magnet-hunt.html">
    <link rel="stylesheet" href="../styles.css?v=nav-stable-2">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="../original/">Original</a>
          <a href="../cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main class="card-shell">
      <article class="kid-card">
        <p class="kicker">Activity paused</p>
        <h1>Magnet Hunt</h1>
        <section class="parent-strip" aria-label="Decision before starting">
          <strong>Do not start this version.</strong>
          <p>{esc(activity["parent"])}</p>
        </section>
        <section aria-labelledby="instead-title">
          <h2 id="instead-title">Choose a different start</h2>
          <p><a href="../cards/paper-bridge.html">Open Paper Bridge</a> for a non-magnet activity with its own adult check before the steps. Check that card's materials and stop conditions for your household.</p>
          <p><a href="../cards.html">Browse the activity cards</a> if paper, two low books and a suitable large lightweight toy are not available.</p>
        </section>
        <details>
          <summary>Why this card is paused</summary>
          <p>Use the owned product's documentation to establish type and power; a large size, intact appearance or age label alone does not settle this. Also pause for small, loose, cracked or missing magnets, younger-child reach or divided adult attention. Even if you can identify the magnet, this card does not currently offer a runnable setup; we have not checked an owned magnet or household test surface.</p>
          <p><a href="https://www.healthychildren.org/English/safety-prevention/at-home/Pages/Dangers-of-Magnetic-Toys-and-Fake-Piercings.aspx">AAP magnetic-toy guidance</a> warns about high-powered and loose magnets. <a href="https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Magnets">CPSC magnet guidance</a> describes ingestion hazards. These sources do not establish that an unspecified magnet in a home is suitable for this activity. The pause and alternate route are Kid Activity Lab editorial decisions; this version has not been family- or physically tested.</p>
        </details>
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Back to activity cards</a></p>
    </footer>
  </body>
</html>
'''


def quick_page(slug):
    if slug == "foil-boat-test":
        return foil_boat_page()
    if slug == "paper-chain-test":
        return paper_chain_page()
    if slug == "magnet-hunt":
        return magnet_hunt_pause_page()
    activity = {**ACTIVITIES[slug], **QUICK_CARD_OVERRIDES.get(slug, {})}
    steps = activity["steps"]
    step_html = "\n".join(
        f'''          <div class="step-tile">
            <span class="step-number">{i}</span>
            <p>{esc(step)}</p>
          </div>'''
        for i, step in enumerate(steps, 1)
    )
    meta_values = (
        [("Need", activity["materials"]), ("Time", activity["time"])]
        if slug == "sink-or-float-tray" else quick_material_tiles(activity["materials"], activity["time"])
    )
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
    description = activity.get("description", description)
    kicker = activity.get("kicker", f"{activity['time']} · age {activity['ages']}")
    is_ball_maze = slug == "ball-maze-box"
    is_paper_bridge = slug == "paper-bridge"
    is_sink_float = slug == "sink-or-float-tray"
    is_sock_roll = slug == "sock-ball-roll"
    is_cup_tower = slug == "cup-tower"
    is_duplo_game = slug == "duplo-games"
    is_blanket_river = slug == "blanket-river"
    is_box_garage = slug == "box-garage"
    is_shadow = slug == "shadow-shape-match"
    is_ice_watch = slug == "ice-melt-rescue"
    is_color_mix = slug == "color-mixing-cups"
    is_drop_tilt = slug == "water-drop-race"
    is_ramp_texture = slug == "ramp-texture-test"
    is_wind_tower = slug == "wind-tower-test"
    is_pattern_path = slug == "pattern-path"
    is_toy_distance = slug == "measuring-tape-jumps"
    is_cup_balance = slug == "balance-scale-baskets"
    is_spoon_transfer = slug == "spoon-transfer"
    is_tube_sculpture = slug == "tube-sculpture"
    is_color_tower = slug == "lego-color-tower"
    is_train = slug == "tape-train-tracks"
    is_block_tower = slug == "block-tower"
    has_start_cue = bool(activity.get("start_cue"))
    early_handoff = is_ball_maze or is_paper_bridge or is_cup_tower
    routes = related_routes_html(
        slug, include_guide=not early_handoff,
        max_links=2 if is_paper_bridge or is_cup_tower else MAX_RELATED_ROUTES,
    )
    parent_label = activity.get("parent_label", "Parent check")
    parent_check = f'''

        <section class="parent-strip" aria-label="{esc(parent_label)}">
          <strong>{esc(parent_label)}:</strong> {esc(activity['parent'])}
        </section>'''
    pre_meta_parent_check = parent_check if is_paper_bridge or is_cup_tower else ""
    activity_start = f'''

        <section class="parent-strip" aria-label="Before starting">
          <strong>Before you start:</strong> {esc(activity['start_cue'])}
        </section>''' if has_start_cue else ""
    activity_details = f'''

        <div class="card-meta" aria-label="Activity details">
{meta_html}
        </div>'''
    if is_box_garage or is_shadow or is_ice_watch or is_color_mix or is_drop_tilt or is_ramp_texture or is_wind_tower or is_pattern_path or is_toy_distance or is_cup_balance or is_spoon_transfer or is_tube_sculpture or is_color_tower or is_train or is_block_tower:
        prefix = "box-garage" if is_box_garage else "shadow" if is_shadow else "ice-watch" if is_ice_watch else "color-mix" if is_color_mix else "drop-tilt" if is_drop_tilt else "ramp-texture" if is_ramp_texture else "wind-tower" if is_wind_tower else "pattern-path" if is_pattern_path else "toy-distance" if is_toy_distance else "cup-balance" if is_cup_balance else "tube-sculpture" if is_tube_sculpture else "spoon-transfer"
        readiness = "\n".join(
            f'          <p><strong>{esc(label)}:</strong> {esc(text)}</p>'
            for label, text in activity["readiness_groups"]
        )
        if is_color_tower:
            prefix = "color-tower"
        if is_train:
            prefix = "train-station"
        if is_block_tower:
            prefix = "block-tower"
        activity_start = f'''

        <p class="{prefix}-materials"><strong>Need:</strong> {esc(activity['materials'])}.<br>Open-ended; duration and mess not measured.</p>
        <section class="parent-strip {prefix}-readiness" aria-label="Before starting">
          <h2>Before you start</h2>
{readiness}
          <p><strong>Stop:</strong> {esc(activity['stop'])}</p>
        </section>'''
        activity_details = ""
    activity_setup = f'''

        <section class="parent-strip" aria-label="Adult setup">
          <strong>Adult setup:</strong> {esc(activity['adult_setup'])}
        </section>''' if has_start_cue else ""
    if activity.get("adult_setup_groups"):
        setup_paragraphs = "\n".join(
            f'          <p><strong>{esc(label)}:</strong> {esc(text)}</p>'
            for label, text in activity["adult_setup_groups"]
        )
        activity_setup = f'''

        <section class="parent-strip" aria-label="Adult setup">
          <strong>Adult setup:</strong>
{setup_paragraphs}
        </section>'''
    early_parent_check = parent_check if is_ball_maze else ""
    late_parent_check = "" if early_handoff else parent_check
    source_note = ""
    if activity.get("sources"):
        links = "; ".join(
            f'<a href="{esc(url)}">{esc(label)}</a>'
            for label, url in activity["sources"]
        )
        source_note = f'''

        <details><summary>Sources and testing status</summary>
          <p>{links}.</p>
          <p>{esc(activity['source_note'])}</p>
        </details>'''
    early_guide = '''

        <section class="maze-card-decision" aria-label="Decide before starting">
          <p><a href="../articles/cardboard-ball-maze-kids.html">Full Cardboard Ball Maze guide</a> for fit, rescue, and cleanup.</p>
          <p>Fit: can the child move chunky blocks and follow a stop cue? Not family-tested by Kid Activity Lab.</p>
        </section>''' if is_ball_maze else ""
    if is_paper_bridge:
        early_guide = '''

        <section class="bridge-card-decision" aria-label="Decide before starting">
          <p><a href="../articles/paper-bridge-challenge-kids.html#bridge-start-title">Full Paper Bridge guide</a> for the optional fold, rescue, and cleanup. Research-backed; not family-tested by Kid Activity Lab.</p>
          <p><strong>Fit:</strong> Choose one intact large lightweight block or soft toy suitable for every child who can reach it. Try when your child can place it gently and follow a stop cue. Adult sets the low books. If a younger child mouths materials and you cannot keep spare materials out of reach while attending to both, skip.</p>
        </section>'''
    if is_cup_tower:
        early_guide = '''

        <section class="cup-card-decision" aria-label="Decide before starting">
          <p><a href="../articles/paper-cup-tower-kids.html">Full Paper Cup Tower guide</a> for fit, rescue and cleanup.</p>
          <p><strong>Fit:</strong> Try when the child can place a cup gently and follow a stop cue. Adult first checks that the matching cups balance and demonstrates two closed bottoms touching, not nesting. If they will not balance, use a row rather than forcing a tower.</p>
        </section>'''
    if is_duplo_game:
        early_guide = '''

        <p><strong>Copy beside me:</strong> Can two little towers look the same? Keep the model in sight and take turns making a match. This is not a memory test or race.</p>'''
    if is_ramp_texture:
        early_guide = '''

        <p><a href="../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start">Basic ramp setup and troubleshooting</a>. The guide compares landing surfaces, not a cloth covering. <a href="../collections/original-stem-activities-for-4-year-olds.html#ramp-detective">Deeper surface-observation routine</a>.</p>'''
    if is_pattern_path:
        early_guide = '''

        <p><a href="../collections/stem-activities-for-preschoolers.html#continue-a-pattern">Preschool pattern start and diagram</a>.</p>'''
    card_class = (
        "kid-card maze-card" if is_ball_maze else
        "kid-card bridge-card" if is_paper_bridge else
        "kid-card sink-float-card" if is_sink_float else
        "kid-card sock-roll-card" if is_sock_roll else
        "kid-card cup-tower-card" if is_cup_tower else
        "kid-card duplo-game-card" if is_duplo_game else
        "kid-card blanket-river-card" if is_blanket_river else
        "kid-card box-garage-card" if is_box_garage else
        "kid-card shadow-card" if is_shadow else
        "kid-card ice-watch-card" if is_ice_watch else
        "kid-card color-mix-card" if is_color_mix else
        "kid-card drop-tilt-card" if is_drop_tilt else
        "kid-card ramp-texture-card" if is_ramp_texture else
        "kid-card wind-tower-card" if is_wind_tower else
        "kid-card pattern-path-card" if is_pattern_path else
        "kid-card toy-distance-card" if is_toy_distance else
        "kid-card cup-balance-card" if is_cup_balance else
        "kid-card spoon-transfer-card" if is_spoon_transfer else
        "kid-card tube-sculpture-card" if is_tube_sculpture else
        "kid-card color-tower-card" if is_color_tower else
        "kid-card train-station-card" if is_train else
        "kid-card block-tower-card" if is_block_tower else "kid-card"
    )
    css_version = (
        "ball-maze-card-1" if is_ball_maze else
        "bridge-card-1" if is_paper_bridge else
        "sink-float-card-1" if is_sink_float else
        "sock-roll-card-1" if is_sock_roll else
        "cup-tower-card-1" if is_cup_tower else
        "duplo-game-card-1" if is_duplo_game else
        "blanket-river-card-1" if is_blanket_river else
        "box-garage-card-2" if is_box_garage else
        "shadow-card-1" if is_shadow else
        "ice-watch-card-1" if is_ice_watch else
        "color-mix-card-1" if is_color_mix else
        "drop-tilt-card-1" if is_drop_tilt else
        "ramp-texture-card-1" if is_ramp_texture else
        "wind-tower-card-1" if is_wind_tower else
        "pattern-path-card-1" if is_pattern_path else
        "toy-distance-card-1" if is_toy_distance else
        "spoon-transfer-card-1" if is_spoon_transfer else
        "tube-sculpture-card-1" if is_tube_sculpture else
        "color-tower-card-1" if is_color_tower else
        "train-station-card-1" if is_train else
        "block-tower-card-1" if is_block_tower else "nav-stable-2"
    )
    best_for = "" if is_color_tower or is_train or is_block_tower else f'''

        <section class="parent-strip" aria-label="Best for">
          <strong>Best for:</strong> {esc(activity['best_for'])}.
        </section>'''
    previous_video = '''

        <details><summary>Previous video reference (optional)</summary>
          <p>This earlier creator reference is not the source of the visible-copy rule above. Kid Activity Lab has not verified its current playback or instructions.</p>
          <iframe class="video-frame" src="https://www.youtube-nocookie.com/embed/giI5GHTVl20" title="Previous 3 Easy LEGO DUPLO Games Ideas video reference" loading="lazy" allowfullscreen></iframe>
          <p><a href="https://www.youtube.com/watch?v=giI5GHTVl20">Open the previous creator reference</a></p>
        </details>''' if is_duplo_game else ""
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(activity['title'])} Activity Card | Kid Activity Lab</title>
    <meta name="description" content="{esc(description)}">
    <link rel="canonical" href="https://kidactivitylab.com/cards/{esc(slug)}.html">
    <link rel="stylesheet" href="../styles.css?v={css_version}">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="../original/">Original</a>
          <a href="../cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main class="card-shell">
      <article class="{card_class}">
        <p class="kicker">{esc(kicker)}</p>
        <h1>{esc(activity['title'])}</h1>{early_guide}{pre_meta_parent_check}{activity_start}{activity_details}{early_parent_check}{activity_setup}

        <section class="steps-grid" aria-label="Steps">
{step_html}
        </section>{late_parent_check}{best_for}{routes}{source_note}{previous_video}
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Back to activity cards</a></p>
    </footer>
  </body>
</html>
'''


def cards_index():
    cards = []
    for slug, source_activity in ACTIVITIES.items():
        activity = {**source_activity, **QUICK_CARD_OVERRIDES.get(slug, {})}
        search_text = f'{activity["title"]} {activity["materials"]}'
        if slug == "measuring-tape-jumps":
            search_text += " Measuring Tape Jumps"
        if slug == "balance-scale-baskets":
            search_text += " Balance Basket Scale"
        summary = (
            "Paused; choose a non-magnet activity"
            if slug == "magnet-hunt" else
            f'Toy-only, adult stays beside | {activity["time"]} · {activity["materials"]}'
            if slug == "blanket-river" else
            f'One-car no-cut start, adult stays beside | {activity["time"]} · {activity["materials"]}'
            if slug == "box-garage" else
            f'Adult-controlled wall light | {activity["time"]} · {activity["materials"]}'
            if slug == "shadow-shape-match" else
            f'Adult handles; child watches | {activity["time"]} · {activity["materials"]}'
            if slug == "ice-melt-rescue" else
            f'Adult mixes; child notices | {activity["time"]} · {activity["materials"]}'
            if slug == "color-mixing-cups" else
            f'Adult steadies; child tilts or watches | {activity["time"]} · {activity["materials"]}'
            if slug == "water-drop-race" else
            f'Adult steadies; child releases or watches | {activity["time"]} · {activity["materials"]}'
            if slug == "ramp-texture-test" else
            f'Adult controls paper fan; standing is a result | {activity["time"]} · {activity["materials"]}'
            if slug == "wind-tower-test" else
            f'Adult sets ABAB; choose or point once | {activity["time"]} · {activity["materials"]}'
            if slug == "pattern-path" else
            f'Place by hand; compare marked gaps | {activity["time"]} · {activity["materials"]}'
            if slug == "measuring-tape-jumps" else
            f'Adult holds and loads; child watches | {activity["time"]} · {activity["materials"]}'
            if slug == "balance-scale-baskets" else
            f'Adult checks, models and stays; scoop or point | {activity["time"]} · {activity["materials"]}'
            if slug == "spoon-transfer" else
            f'Adult checks, tapes and stays; choose a low arrangement or point | {activity["time"]} · {activity["materials"]}'
            if slug == "tube-sculpture" else
            f'Adult checks and stays; match flat pairs or point | {activity["time"]} · {activity["materials"]}'
            if slug == "lego-color-tower" else
            f'Adult prepares board and stays; one station stop or point | {activity["time"]} · {activity["materials"]}'
            if slug == "tape-train-tracks" else
            f'Adult checks, models and stays; one placement or flat row | {activity["time"]} · {activity["materials"]}'
            if slug == "block-tower" else f'{activity["time"]} · {activity["materials"]}'
        )
        cards.append(
            f'        <a class="mini-card" href="cards/{esc(slug)}.html"><strong>{esc(activity["title"])}</strong><span>{esc(summary)}</span><template data-search="{esc(search_text)}"></template></a>'
        )
    cards = "\n".join(cards)
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Activity Cards | Kid Activity Lab</title>
    <meta name="description" content="Activity cards with materials, short steps, and parent checks for preschool play.">
    <link rel="canonical" href="https://kidactivitylab.com/cards.html">
    <link rel="stylesheet" href="styles.css?v=cards-finder-1">
    <script src="assets/cards-finder.js?v=2" defer></script>
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="original/">Original</a>
          <a href="cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero">
        <p class="kicker">Activity cards</p>
        <h1>Pick one small thing.</h1>
        <p class="library-jump"><a href="#activity-card-finder">Browse activity cards</a></p>
        <p class="dek">Choose a card for its materials, short steps, and parent check. Some ideas link to a deeper guide or source video.</p>
      </section>

      <section class="game-promo" aria-labelledby="card-game-promo-title">
        <div>
          <p class="kicker">One standard deck</p>
          <h2 id="card-game-promo-title">Choose a card game by readiness, not guesswork.</h2>
          <p>Compare five familiar games by players, pace, rank and suit load, then open one frozen starting setup.</p>
        </div>
        <a class="game-promo-link" href="collections/card-games-for-kids.html">Open the five-game chooser</a>
      </section>

      <p class="content"><a href="articles/paper-helicopter-kids.html">Paper Helicopter: full cut, fold and drop guide</a></p>
      <p class="content"><a href="articles/paper-straw-rocket.html">Paper Straw Rocket: printable model with adult setup and launch</a></p>

      <section class="card-finder" id="activity-card-finder" aria-labelledby="activity-card-finder-title">
        <h2 id="activity-card-finder-title">Activity cards</h2>
        <div class="card-finder-controls" hidden>
          <label for="card-finder-query">Find by title or material</label>
          <div class="card-finder-row">
            <input id="card-finder-query" type="search" autocomplete="off">
            <button id="card-finder-clear" type="button" disabled>Clear</button>
          </div>
          <p id="card-finder-count" role="status" aria-live="polite"></p>
          <p id="card-finder-empty" hidden>No activity cards match. Try another title or material, or use Clear to see all cards. Looking for a card game instead? <a href="collections/card-games-for-kids.html">Open the standard-deck game chooser</a>.</p>
        </div>
      </section>

      <section class="library-grid" aria-label="Activity cards">
{cards}
      </section>
    </main>

    <footer class="site-footer">
      <p>Activity cards with parent checks.</p>
    </footer>
  </body>
</html>
'''


def main():
    from contributor_pages import sync_contributor_pages

    OUT.mkdir(parents=True, exist_ok=True)
    with DATA.open() as f:
        rows = {row["source_id"]: row for row in csv.DictReader(f)}
    for source_id in CARD_ROWS:
        row = rows[source_id]
        slug = SLUGS[source_id]
        (OUT / f"{slug}.html").write_text(quick_page(slug) if slug in {"cup-tower", "duplo-games", "tube-sculpture", "lego-color-tower", "tape-train-tracks", "block-tower"} else page(row, slug))
    for slug in QUICK_CARD_SLUGS:
        (OUT / f"{slug}.html").write_text(quick_page(slug))
    (ROOT / "site" / "cards.html").write_text(cards_index())
    sync_contributor_pages()
    print(f"generated {len(CARD_ROWS) + len(QUICK_CARD_SLUGS)} card pages and cards index")


if __name__ == "__main__":
    main()
