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
        "parent": "Stay beside the child. Choose intact lightweight cups for everyone who can reach them. Stop after mouthing, throwing, damage, climbing or unwanted collapse. Research-backed, not family-tested; open the guide for fit, rescue and cleanup.",
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
            "Set two books low.",
            "Lay one paper sheet across.",
            "Place one large object gently.",
            "Fold the paper and compare.",
        ],
        "parent": (
            "Stay close. Stop if books slide, paper tears, the object is thrown, "
            "or the setup becomes climbing play."
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


def related_routes_html(slug):
    links = []
    guide = GUIDE_ROUTES.get(slug)
    if guide:
        links.append(
            f'<a href="../{esc(guide["path"])}">{esc(guide["label"])}</a>'
        )
    links.extend(
        f'<a href="../{esc(route["path"])}">{esc(route.get("route_label", route["h1"]).rstrip("."))}</a>'
        for route in related_routes(slug)
    )
    links = links[:MAX_RELATED_ROUTES]
    if not links:
        return ""
    return f'''

        <section class="parent-strip" aria-label="Related activity pages">
          <strong>More ways to use this idea:</strong> {" · ".join(links)}
        </section>'''


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
    routes = related_routes_html(slug)
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
        </section>{routes}
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Back to activity cards</a></p>
    </footer>
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
        <p><strong>Keep it on the table:</strong> no wearing chains or hanging them across walkways. Stop if paper or tape goes in a mouth, the chain is pulled around a body, or play becomes unwanted or hard to control.</p>
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
        <p><strong>Joining feels too fiddly?</strong> Let the adult hold and join while the child chooses, counts or watches. Skip tape handling if the feel bothers them. Offer the same roles to siblings; stop if everyone needs more help than you can give.</p>
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
        <p><a href="https://www.wttw.com/kids/learn-and-play/activities/social-emotional-development/paper-chain">WTTW's Paper Chain</a> supports the thread-then-close sequence and an untimed assisted option. <a href="https://littlebinsforlittlehands.com/paper-chain-stem-challenge/">Little Bins' paper-chain challenge</a> supplies the one-sheet comparison idea. <a href="https://teachersareterrific.com/2015/08/the-paper-chain-an-easy-prep-stem-challenge.html">Teachers are Terrific's challenge</a> illustrates why the meaning of "chain" needs explicit rules. Sources checked September 23, 2026.</p>
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


def quick_page(slug):
    if slug == "foil-boat-test":
        return foil_boat_page()
    if slug == "paper-chain-test":
        return paper_chain_page()
    activity = {**ACTIVITIES[slug], **QUICK_CARD_OVERRIDES.get(slug, {})}
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
    description = activity.get("description", description)
    kicker = activity.get("kicker", f"{activity['time']} · age {activity['ages']}")
    routes = related_routes_html(slug)
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
        <p class="kicker">{esc(kicker)}</p>
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
        </section>{routes}
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
        cards.append(
            f'        <a class="mini-card" href="cards/{esc(slug)}.html"><strong>{esc(activity["title"])}</strong><span>{esc(activity["time"])} · {esc(activity["materials"])}</span></a>'
        )
    cards = "\n".join(cards)
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Activity Cards | Kid Activity Lab</title>
    <meta name="description" content="One-screen activity cards preschoolers can follow with parent help. Low-prep play using household materials.">
    <link rel="canonical" href="https://kidactivitylab.com/cards.html">
    <link rel="stylesheet" href="styles.css?v=card-games-1">
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
        <p class="dek">Each card is meant to fit on one screen: materials, steps, parent check, and source video when one is available.</p>
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
        (OUT / f"{slug}.html").write_text(quick_page(slug) if slug == "cup-tower" else page(row, slug))
    for slug in QUICK_CARD_SLUGS:
        (OUT / f"{slug}.html").write_text(quick_page(slug))
    (ROOT / "site" / "cards.html").write_text(cards_index())
    print(f"generated {len(CARD_ROWS) + len(QUICK_CARD_SLUGS)} card pages and cards index")


if __name__ == "__main__":
    main()
