import csv
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE_URL = "https://kidactivitylab.com"
CSS_VERSION = "nav-stable-2"


TUBE_DROP_DEFAULT = {
    "tube_drop": True,
    "ages": "3-5",
    "age_label": "Check abilities, not age alone",
    "time": "Time not measured",
    "mess": "Not measured",
    "mess_label": "Cleanup not measured",
    "help": "high",
    "help_label": "Adult holds throughout",
    "materials": "1 short open paper tube, 1 intact LARGE owned age-labelled play-pom, 1 shallow unbreakable receiver",
    "best_for": "Same held-tube default: release one checked play-pom and watch it land",
    "start_cue": "Adult stays. Skip: mouthing or uncertain fit.",
    "adult_setup_groups": [
        ("Fit or decline", "Follow the owned play set's age, warning and use labels for EVERY reachable child. Choose ONE intact LARGE play-pom, not loose craft poms, food, cotton, balls or marbles. Check the short lightweight open paper tube: clean, dry and intact, without staples, sharp edges, loose covering or residue. Large alone is not sufficient; supervision does not make unsuitable parts acceptable. Uncertain labels, condition or fit? Choose another activity, not a purchase or smaller filler."),
        ("Adult and space", "Place a stable shallow unbreakable receiver on a low clear surface away from edges, feet and walkways. Adult stays beside EVERY reachable child, holds the tube with its lower opening CLEAR ABOVE the receiver and its top within comfortable reach, and controls all unused material. No wall tape, cutting, tongs or child-catching job. Skip for mouthing, tearing, younger reach you cannot control or unavailable attention. Try when the child can release with help and pause on request; otherwise the adult drops while the child watches or points. Declining is valid; no forced touch, naming or counting."),
        ("Trial before child access", "Adult tries the ONE pom: it must fall FREELY through the tube and land in the receiver WITHOUT pushing or squeezing. No suitable combination? End; do not force it or switch to smaller filler. This checks immediate passage only, not material suitability or safety."),
    ],
    "stop": "Stop for mouthing, tearing or shedding, throwing, damage, unstable receiver, blocked passage, uncertain reach, discomfort, a request to stop or shifted adult attention. Adult takes and accounts for all materials; no forceful poking or shaking at people.",
    "adult_setup": "Adult holds the checked tube clear above the receiver and models one free drop. Say: Let go at the top; watch where it comes out. The adult may drop while the child watches or points.",
    "steps": ["Adult holds the tube above the receiver.", "Release the ONE checked pom at the top, or watch the adult do it.", "Watch it come out below and land; no catching required.", "Adult retrieves ONLY after landing. Offer the same pom again if wanted, or end."],
    "parent_label": "Rescue and collection",
    "parent": "Stuck or not seen? Stop child action. Adult takes the tube and pom out of child reach, locates and collects the ONE item without poking, squeezing or shaking at people. Recheck once only if the same free passage is plainly restored; otherwise end, not smaller filler. For texture refusal, watch or point without handling, or stop. Account for the ONE pom, tube and receiver, remove damaged pieces and store all materials out of reach.",
    "sources": [
        ("SDN: tube drop and no-mouthing supervision", "https://www.sdn.org.au/media/2726/healthy-bodies-pom-pom-drop.pdf"),
        ("Linds Makes: written held-tube variation", "https://www.lindsmakes.com/pom-pom-drop/"),
        ("Becker: one-at-a-time drop and receiver", "https://www.shopbecker.com/resource-cafe/activity-page/math/drop-and-plop-color-game/"),
        ("AAP: toy labels, condition and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
    ],
    "source_note": "Sources checked October28,2026. SDN describes tubes on a box and supervision against mouthing. Linds Makes describes and pictures a held tube; Becker describes and pictures receivers below attached tubes. Our ONE adult-held tube, checked owned play-pom, low receiver, free-passage trial, roles, rescue and stop are editorial synthesis, not either source's exact setup or inspected creator-video instructions. We exclude small craft fillers, cotton, balls, marbles, tongs, wall courses, child catching, paint, races and required color sorting. Source ages, photos, large size and supervision do not certify readiness or material fit. AAP supplies general toy-selection guidance, not certification of this set. Paper Roll Drop and Pom Pom Drop use this SAME default, not separately tested recipes. Research-backed, not family-tested by Kid Activity Lab. No product recommendation, developmental claim or safety assurance.",
}


ACTIVITIES = {
    "cardboard-car-ramp": {
        "title": "Cardboard Car Ramp",
        "url": "../cards/cardboard-car-ramp.html",
        "ages": "3-5",
        "time": "2 min",
        "mess": "low",
        "help": "low",
        "materials": "cardboard, books, toy cars",
        "best_for": "quick building, toy car play, cause and effect",
        "steps": ["Stack books.", "Lay cardboard on top.", "Pick a car.", "Roll and change the ramp."],
        "parent": "Keep the ramp low and away from stairs.",
    },
    "tape-road": {
        "title": "Tape Road",
        "url": "../cards/tape-road.html",
        "ages": "3-6",
        "time": "3 min",
        "mess": "low",
        "help": "low",
        "materials": "painter tape, toy cars",
        "best_for": "indoor movement, pretend play, rainy days",
        "steps": ["Make a road.", "Add parking spots.", "Drive cars.", "Peel tape up after play."],
        "parent": "Test tape on the floor first.",
    },
    "cup-tower": {
        "title": "Cup Tower",
        "url": "../cards/cup-tower.html",
        "ages": "3-6",
        "time": "1 min",
        "mess": "low",
        "help": "low",
        "materials": "paper cups",
        "best_for": "stacking, counting, reset-friendly play",
        "steps": ["Stack cups.", "Make it taller.", "Knock it down.", "Build again."],
        "parent": "Use lightweight cups only.",
    },
    "paper-roll-drop": {
        **TUBE_DROP_DEFAULT,
        "title": "Paper Roll Drop",
        "url": "../cards/paper-roll-drop.html",
    },
    "pom-pom-drop": {
        **TUBE_DROP_DEFAULT,
        "title": "Pom Pom Drop",
        "url": "../cards/pom-pom-drop.html",
    },
    "magnetic-tile-house": {
        "title": "Magnetic Tile House",
        "url": "../cards/magnetic-tile-house.html",
        "flat_house": True,
        "ages": "3-6",
        "age_label": "Check abilities, not age alone",
        "time": "Time not measured",
        "mess": "Not measured",
        "mess_label": "Cleanup not measured",
        "help": "high",
        "help_label": "Adult stays beside setup",
        "materials": "TWO intact LARGE tiles from ONE identifiable, age-labelled owned set: ONE square and ONE triangle; firm low dry level space",
        "start_cue": "Flat picture only. Adult stays. Skip mouthing or uncertain fit.",
        "best_for": "The standing-house version is withdrawn. This is an optional DIFFERENT task: a flat house PICTURE, not a room for a toy. Nothing goes inside; there is NO opening door",
        "adult_setup_groups": [
            ("Fit or decline", "Check the owned set's identity, age labels, warnings, use and recall notices for EVERY reachable child. Inspect faces, edges and joins for cracks, damage, loose or missing parts and exposed magnets. Use only the TWO intact LARGE shapes if appropriate for them all. Unknown identity, labels, condition or uncontrolled younger reach means decline. No tiny or mini pieces, loose magnets, balls, rods, cubes, mixed-set assumptions, dismantling or taped repairs. Inspection and supervision do not certify suitability."),
            ("Adult and space", "Clear a firm low dry level space away from edges and traffic. Stay beside EVERY reachable child and control both tiles and all spares throughout. Skip for mouthing, rough handling or unavailable attention. Try only if the child can lay a piece gently and pause on request; otherwise the adult places while the child watches or points, or decline."),
        ],
        "stop": "End for mouthing, throwing, discomfort, damage, missing parts, exposed magnets, uncontrolled movement, uncertain reach or shifted adult attention. If the pieces cannot remain flat under adult control, separate them or end. For damaged or uncertain material, follow the owned maker's guidance; do not repair and continue.",
        "adult_setup": "Lay the square FLAT. Lay the triangle FLAT outside ONE square edge, with its broad edge facing the square and opposite corner pointing away. A SMALL GAP is fine: no magnetic join, snap, force, upright wall or supported roof is needed. If pieces pull together or repel, separate them and leave a gap, or end.",
        "steps": [
            'Adult says: "This square is the house picture. Which way could the roof point?"',
            "Lay the triangle flat as modelled, point, watch or decline. No naming, counting or story is required.",
            "Notice the square body and triangle roof as a PICTURE. Keep both flat; nothing goes inside.",
            "If wanted, the adult moves one flat piece apart to reset. Otherwise end.",
        ],
        "parent": "Adult controls separation and accounts for BOTH tiles, checks for damage and stores them and all spares away. Leave a gap or end if movement is not controlled. This is not a standing-house or toy-enclosure recipe.",
        "sources": [
            ("MAGNA-TILES: beginner flat-house option", "https://magnatiles.com/"),
            ("MAGNA-TILES: supervision and condition", "https://magnatiles.com/pages/faq"),
            ("Manufacturer flat house pattern", "https://cdn.shopify.com/s/files/1/0734/5009/4831/files/HauntedHouse.pdf?v=1791815584"),
            ("CPSC: magnet context", "https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Magnets"),
            ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Sources checked October28,2026. Manufacturer text supports laying simple houses flat; its inspected flat pattern uses mini tiles and a printable, which we do NOT transfer. Our TWO LARGE owned shapes, gap, layout, roles, rescue and stop are editorial synthesis, not that exact pattern or an inspected creator-video procedure. Brand, source ages and supervision do not establish owned-set fit, compatibility, strength or safety. Research-backed, not family-tested by Kid Activity Lab. Time, mess, comprehension, enjoyment, engagement, learning, repeatability and safety outcomes are UNKNOWN. No product recommendation or purchase is needed.",
    },
    "magnetic-tile-ideas": {
        "title": "Magnetic Tile Builds (paused)",
        "url": "../cards/magnetic-tile-ideas.html",
        "tile_build_pause": True,
        "ages": "3-6",
        "time": "Not measured",
        "mess": "Not measured",
        "help": "Read the different activity's adult role",
        "materials": "This version is paused; choose a different checked activity or decline",
        "best_for": "A pause and choice notice, not a standing-build recipe",
        "steps": [],
        "pause_reason": "Our old wall, roof and knockdown instructions do not establish the pieces, first connection, support and controlled end well enough to run this version. A quick magnet or condition check does not fill those gaps. This is not a finding that all magnetic tiles are unsuitable.",
        "flat_url": "../cards/magnetic-tile-house.html",
        "flat_label": "Different flat house picture",
        "box_url": "../cards/box-garage.html",
        "box_label": "Different one-car Box Garage",
        "parent": "BEFORE handling, open the chosen activity and read its owned-material, adult-role, stop and collection checks for EVERY reachable child, or decline. Adult stays beside the setup. Skip for mouthing, uncertain materials or reach, or unavailable attention. Size, brand and a quick check do not establish fit. Do not substitute tiles or blocks into the box recipe.",
        "source_note": "Sources checked October28,2026. Manufacturer build inventories and product-specific finished examples do not establish our old generic sequence; an attributed two-room challenge is a prompt, not a procedure. The old linked creator video was not watched or transcribed. We do not claim it contradicts our page or that no suitable procedure exists. The two alternatives have their own maintained source and use checks; neither is an equivalent standing or two-room task. Research-backed editorial decision, not family-tested by Kid Activity Lab. Owned fit, time, mess, enjoyment, learning, repeatability and safety outcomes are UNKNOWN. No product recommendation or purchase.",
    },
    "block-tower": {
        "title": "Block Tower",
        "url": "../cards/block-tower.html",
        "ages": "3-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Editorial ages 3-6; check readiness",
        "mess_label": "Mess not measured",
        "help_label": "Adult checks, models and stays",
        "materials": "3 matching intact large lightweight non-interlocking blocks with flat faces; no small or detachable parts, magnets or batteries",
        "best_for": "choosing one on-top placement or a flat row, not a height or counting challenge",
        "readiness_groups": [
            ("Materials", "Follow owned toy age, warning and use labels for EVERY reachable child. Check condition and flat faces. No suitable owned blocks? Choose another activity, not a purchase or substitute small pieces."),
            ("Adult and space", "Clear a firm level floor patch away from feet, doors, walking paths, faces, pets and breakables. Adult stays beside every reachable child and keeps spares out of reach."),
            ("Fit or skip", "Try when the child can place gently with help and follow a stop cue. Pointing, watching or declining is valid. Skip for mouthing, younger reach you cannot control, distress or unavailable attention."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab."),
        ],
        "stop": "End for mouthing, throwing, climbing, damage, sliding or unstable pieces, unwanted collapse, discomfort or shifted attention. No pushing a tower over or building higher to get a result.",
        "adult_setup_groups": [
            ("Trial", "BEFORE child access, place TWO blocks flat side by side, touching. Center the THIRD flat on ONE lower block with its entire bottom supported by that block, NOT across the seam. Keep only TWO blocks high. If it rocks, slides, tips or needs force, remove the top and use a flat row or end."),
            ("Offer", "Adult takes the top block off FIRST and puts it beside the base. Say: Which lower block could this sit on? Offer one placement, pointing or watching. A wider footprint is not a stability guarantee."),
        ],
        "steps": [
            "Choose one lower block. With adult help, place the third flat on it, or point for the adult; keep its whole bottom supported and only two blocks high.",
            "If stacking does not fit or is unwanted, adult removes any top FIRST and leaves ALL THREE flat in a row. That is a finished build; watching or ending is valid.",
            "Adult takes the top off FIRST, if stacked, then collects the base. Repeat with the SAME pieces only if wanted, or finish; no required count, height or knockdown.",
        ],
        "parent_label": "Rescue and cleanup",
        "parent": "If checked blocks do not match or stack, choose a flat row or end; do not add height, force or heavy pieces. Adult keeps pieces low, removes any top before the base, collects ALL THREE blocks and any spares, checks the floor and stores everything out of reach. Duration and mess have not been measured.",
        "sources": [
            ("NAEYC: flat stacking and adult modelling", "https://www.naeyc.org/resources/pubs/yc/mar2020/rocking-and-rolling-building-new-skills-block-construction-toddler"),
            ("NZ Ministry of Education: space, own pace and tidying", "https://www.education.govt.nz/parents-and-caregivers/early-learning/early-learning-home/simple-toys-and-endless-play/blocks-stack-it-build-it-knock-it-down"),
            ("Mississippi State Extension: clear space and block arrangements", "https://accessibility.extension.msstate.edu/publications/block-play"),
            ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Sources checked October28,2026. Flat stacking, adult modelling, clear space, own pace and tidying are source-backed. The three-block, two-high floor start, widened base, trial, roles, stops and flat-row rescue are Kid Activity Lab editorial adaptations, not an inspected creator-video procedure or tested setup. Source photos do not establish this arrangement. Owned block fit, stability, family understanding, timing, mess, enjoyment, learning and safety outcomes are unknown. No product recommendation, developmental rule or safety assurance.",
    },
    "car-ramp-distance-test": {
        "title": "Car Ramp Distance Test",
        "url": "../cards/car-ramp-distance-test.html",
        "ages": "4-6",
        "time": "Open-ended",
        "time_label": "Time not measured",
        "mess": "Not measured",
        "mess_label": "Mess not measured",
        "help": "adult stays",
        "help_label": "Adult sets up and stays",
        "materials": "flat stiff cardboard, TWO broad sturdy closed books, 1 suitable intact owned freely rolling toy vehicle; no tape or loose marker required",
        "best_for": "noticing a stopping spot, not measuring speed or choosing a winner",
        "distance_start": True,
        "guide_url": "../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start",
        "guide_label": "Read the cardboard-ramp checks before handling",
        "start_cue": "Adult stays. Stop: mouthing, throwing, support slips.",
        "fit_cue": "Follow owned toy age, warning and use labels for EVERY reachable child. Use an intact freely rolling vehicle without small or detachable parts, magnets or batteries. Adult clears floor space with room for a natural stop, sets and stabilizes the low ramp, and stays beside all children. Skip for mouthing, younger reach you cannot control, unsuitable materials or unavailable attention. Point, watch or decline; no forced touching, counting or naming.",
        "adult_setup_groups": [
            ("Fit", "Follow owned toy age, warning and use labels for EVERY reachable child. Choose one intact freely rolling vehicle without small or detachable parts, magnets or batteries. No fit or uncertain labels? Choose another activity; do not buy a replacement for this start."),
            ("Space and adult", "Clear a floor lane away from stairs, walkways, faces, feet, pets and breakables, with room for a natural stop. Adult sets and stabilizes the cardboard on TWO broad sturdy closed books and stays beside every reachable child. Skip for mouthing, younger reach you cannot control, unsuitable materials or unavailable attention. Point, watch or decline; no forced touch, counting or naming."),
        ],
        "adult_setup": "BEFORE child handling, read the full ramp checks. Adult makes the low floor setup and trials ONE car. Point to a repeatable starting spot; use the same part of the car at that spot each time. Let go WITHOUT pushing and wait for a natural stop. Point to the stopped position from beside the lane, then collect the car before any reset. No tape, loose marker or second car is required.",
        "steps": [
            "Put the SAME car at the adult's starting spot, or point for the adult. Let go WITHOUT pushing.",
            "Wait for a natural stop, then point to the spot, watch or finish. Keep hands and feet out of the rolling lane.",
            "Only if wanted, repeat with the SAME car, ramp, floor and release spot. The stop may be near the first spot, farther, closer or unclear; one roll is enough.",
        ],
        "stop": "Stop for climbing, throwing, mouthing, sliding supports, damaged parts, the car leaving the clear lane, discomfort or attention shifting.",
        "parent_label": "Rescue and collection",
        "parent": "A pushed, veering, blocked or not-off-ramp run is unclear, not a failed child or a winner. Adult may reset the SAME low setup once or end; no stronger push, taller support or forced repeat. Collect the car, books, cardboard and any spares, check the floor and store all materials out of reach. Setup, duration and mess have not been measured.",
        "extension": "Later, an optional SECOND owned car needs its own label and condition checks. Keep the ramp, floor, release position and release method the same. Cars differ in several ways: do not claim that weight or size alone caused a result, that this is a calibrated fair test, or that a farther stop means higher speed. Pointing, free play or ending remains valid.",
        "sources": [
            ("PNC: wheeled trials and natural stopping marks", "https://www.pnc.com/en/about-pnc/corporate-responsibility/grow-up-great/lesson-center/transportation/rolling-with-ramps.html"),
            ("PEEP: matching conditions and natural stops", "https://peepandthebigwideworld.com/en/educators/curriculum/center-based-educators/ramps/activity/stand-alone/491/rolling-on-different-surfaces-indoors/"),
            ("PEEP: roll-out space and target context", "https://peepandthebigwideworld.com/en/educators/curriculum/center-based-educators/ramps/activity/stand-alone/489/steep-and-steeper/"),
            ("PBS: written comparison context, not a watched video", "https://www.pbs.org/video/cars-ramps-jlzsqr/"),
            ("AAP: owned toy labels, condition and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Written sources checked October28,2026. PNC supplies wheeled trials/stopping marks, PEEP matching-condition/natural-stop/target context, and PBS written comparison context. Their balls, marbles, simultaneous races, escalating heights, taps, timers and fastest-result claims are not transferred. Our one-car, point-only first observation, optional repeat, roles, controls and unclear/end branches are editorial adaptations using the maintained cardboard guide, not a source-tested exact procedure. The old creator video was not watched or used as this procedure's authority. Research-backed, not family-tested by Kid Activity Lab. Owned fit, physical performance, understanding, enjoyment, learning, repeatability, time, mess and safety outcomes remain unknown. No product recommendation or safety assurance.",
    },
    "paper-plate-ramp": {
        "title": "Paper Plate Ramp",
        "url": "../cards/paper-plate-ramp.html",
        "ages": "Paused",
        "time": "Paused",
        "mess": "Not measured",
        "help": "not runnable",
        "materials": "Not a runnable plate setup",
        "best_for": "Paused; choose a different-material ramp or end",
        "steps": [],
        "pause_reason": "The old plate, car and books instructions did not give a complete plate construction. The original museum project is a different cut-and-taped spiral around a cardboard tube. That project is not the procedure offered here.",
        "alternative_url": "../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start",
        "alternative_label": "Different materials: cardboard-ramp guide",
        "alternative_check": "The alternative needs flat stiff cardboard, TWO broad sturdy closed books and a suitable intact owned toy vehicle, not a plate substitute. Follow owned toy age, warning and use labels for EVERY reachable child; avoid small or detachable parts, magnets and batteries. Adult clears floor space, sets and stabilizes the low support and stays beside all children. Read the guide's checks BEFORE child handling.",
        "parent": "Only have a plate, unsuitable materials, mouthing, younger reach you cannot control or no adult attention? Do not switch; end or choose another activity. Do not bend, cut or tape a plate to improvise this old version. Pointing, watching or declining is valid. Adult puts the unused plate and spares out of reach. Stop for climbing, throwing, mouthing, sliding, damage, discomfort or lost attention; use the guide's rescue and collection before leaving.",
        "source_note": "Research-backed decision, not family-tested by Kid Activity Lab. Source linkage and current written instructions were checked October28,2026; the creator video was not watched. The museum project is not being declared unsafe, and no plate construction is certified here. Pausing the incomplete quick version and offering the existing cardboard guide are editorial decisions. Owned fit, physical performance, timing, mess, understanding, enjoyment, learning and safety outcomes remain unknown.",
    },
    "tape-train-tracks": {
        "title": "Tape Train Tracks",
        "url": "../cards/tape-train-tracks.html",
        "ages": "3-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Editorial ages 3-6; check readiness",
        "mess_label": "Mess not measured",
        "help_label": "Adult sets and stays",
        "materials": "1 suitable owned hand-pushed toy train, 1 sacrificial cardboard board, owned removable painter tape",
        "best_for": "one pretend station stop between visible tape lines, not mechanical tracks or a precision test",
        "readiness_groups": [
            ("Materials", "Choose ONE intact large owned hand-pushed toy train. Follow its age and warning labels for EVERY reachable child. No magnets, batteries, cords, detachable or loose small parts, damage, motor or launch mechanism, or linked train cars. No suitable owned train? Choose another activity, not a purchase. An owned large vehicle can use the separate Tape Road routine only if that activity's checks fit."),
            ("Adult and space", "Use ONE intact flat sacrificial cardboard board, fully supported on a low stable clear surface away from edges and walkways. Adult selects owned removable painter tape whose instructions fit this use, follows its labels and removal limits, and controls the roll, strips and spares. No household-floor or furniture default, electrical or duct tape, stronger adhesive, blades, tools, heat or chemicals. Stay beside every reachable child. Skip mouthing, younger reach you cannot control, unavailable attention or inability to pause. Point, watch or decline; no forced touch or train sounds."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. The one-train, three-strip start, fit trial, roles and stop rules are editorial choices, not a source-tested setup or safety guarantee. A brief tape test does not prove future clean removal. Owned fit, child response, time, mess, learning and safety outcomes are unknown."),
        ],
        "stop": "Stop for tape peeling, chewing or wrapping; toy mouthing, throwing, damage or loose parts; forced motion, board moving, materials leaving the setup, discomfort, surface change or attention shifting.",
        "adult_setup_groups": [
            ("Tape check", "BEFORE child access, adult makes short strips by hand away from children only if the owned tape permits; otherwise use an untaped board route or end. Press and gently remove ONE short tape test piece on that board per the tape's instructions; clear the piece and any bits. Cardboard may tear. Failed hold, shedding or uncertain fit or labels? Use an untaped board route or end, not stronger tape."),
            ("Layout", "If continuing, lay TWO short straight parallel strips wider apart than the actual train, plus ONE short cross-strip joining them at the far end: the station mark. All three strips lie flat with no loose edges, within the board and comfortable reach. No extra ties, loop, crossing or props."),
            ("Train trial", "Adult gently pushes the train along the clear gap to the station and stops. Wheels run on cardboard BETWEEN the lines, not on tape rails; the tape does not guide wheels mechanically. It must move freely without force, catching or board movement. Failed tape or route? Remove strips and use a bare-board trip ONLY if the train now moves freely and the board stays still. Otherwise end, never force motion. Return the train to the open end. Say: Take the train between these lines. Stop at this station mark."),
        ],
        "steps": [
            "Push the train once between the lines toward the station mark, or point for the adult to do it. Watch or decline if wanted; stopping elsewhere is a valid finish.",
            "If tape or the route does not fit, adult removes loose tape and points to a spot on the bare board as the pretend station. Only if the train moves freely on the still board, make one gentle untaped trip, watch or end.",
            "Adult may reset the SAME train only if wanted. No speed or precision target, required sounds, longer route, extra pieces or required repeat. This is a pretend station stop, not a railway-building challenge.",
        ],
        "parent_label": "Rescue and cleanup",
        "parent": "Adult collects the train, all used tape (ALL THREE route strips if laid, whether still attached or already removed), the tape roll and any bits; checks the surface and floor; follows the owned tape's removal guidance and stores all materials out of reach. Adult clears or discards a damaged board. Do not leave an accessible setup unattended. Setup, duration and mess have not been measured.",
        "sources": [
            ("Toy Association: Tape Track", "https://www.toyassociation.org/genius/play-ideas-tips/play-ideas/tape-track.aspx"),
            ("Princeton: Train Time (2014)", "https://popgoesthepage.princeton.edu/train-time/"),
            ("Preschool Toolkit: cardboard train tracks (2016)", "https://preschooltoolkit.com/blog/diy-train-tracks-for-pretend-play/"),
            ("3M UK: follow owned tape and removal instructions", "https://www.3m.co.uk/3M/en_GB/home-improvement-eu/correct-tape-removal/"),
            ("3M Canada: tape types and surface limits", "https://www.scotchblue.com/3M/en_CA/scotchblue-ca/your-questions/"),
            ("AAP: toy labels and parts guidance", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Sources checked October28,2026. Parallel tape routes, cardboard support and pretend station stops are source-backed mechanisms. Source photos show larger loops, ties and a crafted train, not this exact three-strip reduction or an approved owned toy/tape combination. Our quantity, straight geometry, board choice, trials, roles, alternatives, stops and collection are editorial, not an inspected creator-video procedure or tested setup. Source floor, electrical-tape, small-prop, tool, pull-cord, water and developmental claims are not transferred. No universal clean-removal, physical safety, clinical, learning or family outcome is established.",
    },
    "lego-color-tower": {
        "title": "LEGO or DUPLO Color Tower",
        "url": "../cards/lego-color-tower.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Editorial ages 4-6; check readiness",
        "mess_label": "Mess not measured",
        "help_label": "Adult stays beside setup",
        "materials": "4 intact large owned DUPLO bricks: same shape, 2 matching-color pairs",
        "best_for": "matching two visible colors, then an optional two-brick stack; no color naming or counting required",
        "readiness_groups": [
            ("Materials", "Use four intact large basic DUPLO bricks of the same compatible shape and footprint: two matching-color pairs, with two colors the child can distinguish. Follow the owned set's age and warning labels for EVERY reachable child. No small standard LEGO, loose or detachable small parts, magnets, battery pieces, damage, tools or mixed-family substitutes. No suitable owned set? Choose another activity, not a purchase."),
            ("Adult and space", "Use a low stable clear surface away from edges and walkways. Adult stays beside every reachable child; keep spares and small LEGO out of reach. Skip for mouthing, younger reach you cannot control, unavailable attention or inability to pause. Point, watch or decline without forced touch, grip, color naming or counting. If the colors do not look distinct, watch an adult flat arrangement or end; do not quiz or correct the child."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. The exact four-brick reduction, fit trial, roles and stop rules are editorial choices, not a source-tested recipe or safety guarantee. Owned fit, child response, time, mess, learning and safety outcomes are unknown."),
        ],
        "stop": "Stop for mouthing, throwing, damage or loose parts, forceful pulling, collapse, discomfort, pieces leaving the surface or attention shifting.",
        "adult_setup": "BEFORE child access, gently check each matching pair joins, stays joined and separates without teeth, force or tools. Failed fit? Keep flat pairs or end, not smaller pieces or more pressure. Lay ALL FOUR loose again. Put ONE brick of each color side by side, separated and visible as seeds; keep the other two as choices. If modeling helps, place one choice beside its matching seed, then RETURN it to the choices; leave both seeds in place. Say: Which brick could go beside one that looks the same?",
        "steps": [
            "Choose one brick from the two choices. Put it BESIDE its matching-color seed, or point for the adult to place it. Offer the last brick or finish; no speed, score or spoken answer.",
            "Optional: make ONE two-brick stack from a matching pair. Adult steadies the lower brick, studs up; align the matching brick above and press gently. No force. Keep both stacks on the surface and at two bricks high; try the other pair only if wanted.",
            "If choosing or joining is difficult, leave flat pairs, watch or end. No taller tower or required repeat. Adult handles separation; do not pull hard or use teeth or tools.",
        ],
        "parent_label": "Rescue and cleanup",
        "parent": "Flat pairs are a complete finish, not a failed tower. Adult collects ALL FOUR bricks and any bits, checks surface and floor, separates gently without teeth or tools, stores everything out of reach and clears the area. Do not leave an accessible setup unattended. Duration and mess have not been measured.",
        "sources": [
            ("Play Included: Sorting Bricks (undated public PDF, inspected October28)", "https://assets.ctfassets.net/ly9gc1zip4av/1wGLm5J367UbqaIHSibQFa/1a00039d471f36dce697d21d2980b1ee/ACTIVITY_02_-_SORTING_BRICKS.pdf"),
            ("LEGO Foundation: Colour Sorting (2016 booklet, PDF page14 / printed26)", "https://education.theiet.org/media/5551/duplo-activity-booklet-pdf-1-140kb.pdf#page=14"),
            ("LEGO: check the specific set's age markings", "https://www.lego.com/en-us/themes/duplo/about"),
            ("AAP: toy labels and parts guidance", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Play Included supports fewer bricks, two groups, a visible seed and adult modeling; the Foundation booklet supports color sorting followed by optional same-color building. Their larger or varied sets and photos do not validate this exact four-large-DUPLO routine. The Foundation's adjacent hidden-model activity is not used here. Play Included's current resource portal requires an account; this public PDF was inspected without one. Our quantity, geometry, pair trial, roles, alternatives, stop and collection rules are editorial, not an inspected creator-video procedure or tested setup. No clinical, developmental, safety or family outcome is established.",
    },
    "duplo-games": {
        "title": "DUPLO Games",
        "url": "../cards/duplo-games.html",
        "ages": "3-5",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check readiness first",
        "mess_label": "Mess not measured",
        "help_label": "Adult stays beside setup",
        "materials": "4 large DUPLO bricks: 2 matching pairs that look different",
        "parent_label": "Rescue and cleanup",
        "best_for": "copying one visible two-brick model, not a memory test or race",
        "start_cue": "Adult checks four intact large owned DUPLO bricks: two matching shape-and-colour pairs that look different from each other. Follow the set's age/warning labels for every child who can reach it; keep spares and small LEGO out of younger reach. Use a firm low clear space and stay beside all reachable children. Try when the child can place bricks with help and follow a stop cue; skip if parts, pairs or attention do not fit. Stop for mouthing, throwing, damage, forceful pulling, discomfort or unwanted collapse. Research-backed, not family-tested by Kid Activity Lab.",
        "adult_setup": "Take one brick from each pair and join them into a two-brick tower. Leave it visible. Give the child the matching two bricks. Say: Can you make yours look like mine, beside it? No timer, winner or height target.",
        "steps": ["Look at the adult's two-brick tower.", "Copy it beside the model with the matching two bricks.", "Compare which brick is on the bottom and top.", "Gently separate; swap builder and copier if wanted."],
        "parent": "Keep the model visible. Point to the next match or let the adult place it; use a side-by-side row if joining is unwanted. Adult handles stuck bricks without teeth or pulling hard. Collect all four, remove damaged parts and store away. Duration and mess have not been measured.",
        "sources": [
            ("LEGO Foundation: Can You Copy? (PDF page15)", "https://info.firstinspires.org/hubfs/Education_Resources/LEGO_Foundation_Six_Bricks_Booklet.pdf#page=15"),
            ("Raising Children Network: stacking and building", "https://raisingchildren.net.au/preschoolers/play-learning/low-cost-play-ideas/stacking-and-building-games"),
            ("AAP: toy labels and material guidance", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Sources checked October27,2026. Visible model copying is source-backed; the four-brick reduction, scripts, help, stop and cleanup are Kid Activity Lab editorial adaptations. This is not the source's six-brick model, a memory test or an adaptation of the earlier creator video. Owned-part suitability and all family, physical, timing, mess, learning and safety outcomes are unknown. No product recommendation or safety assurance.",
    },
    "tube-sculpture": {
        "title": "Tube Sculpture",
        "url": "../cards/tube-sculpture.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Editorial ages 4-6; check fit",
        "mess_label": "Mess not measured",
        "help_label": "Adult checks, tapes and stays",
        "materials": "2 whole clean dry paper-towel-type cardboard tubes, 1 flat intact sacrificial cardboard base large enough for both, owned painter tape",
        "best_for": "choosing a low tube arrangement and noticing its shape, or pointing for the adult",
        "readiness_groups": [
            ("Materials", "Adult checks intact tubes and base: no staples, sharp or torn edges, dampness, loose fibers, unknown residue/coatings or packing plastic. No heavy industrial tubes, small decorations or fillers. Follow owned tape guidance for the planned use. Unsuitable or uncertain? Choose another activity. No cutting, glue, heat, solvents, slotting or tools."),
            ("Adult and space", "Use a stable low clear surface away from edges and walkways. Stay beside every reachable child, steady the base and control the tape roll and loose strips. Try when the child can place with help and pause on request, or point for you. Skip for mouthing, peeling/wrapping, younger reach you cannot control or unavailable attention."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. The two-tube layout, tape trial and controls are editorial adaptations, not tested protection or an adhesion promise. Pointing, watching or declining is enough; no forced touch, grip, counting or naming."),
        ],
        "stop": "End for mouthing, peeling/wrapping, throwing, damaged or loose material, rolling/sliding, discomfort or shifted adult attention. No launchers, steps, climbing, pulling attached tubes or lifting the assembly. Adult collects materials.",
        "adult_setup": "BEFORE child access, lay the FIRST tube on its long side, fully on the base, not upright. Hold it still. Lay one tape strip across its curved body near one end; press both free ends onto the base on opposite sides. Repeat near the other end. Both strips must reach the base on both sides with no loose ends; keep tube openings clear. Gently check for rolling, lifting or peeling, not strength. Failed hold? Remove loose tape; choose an untaped flat arrangement or end, not stronger glue or stacking. Keep this adult model on the base if continuing.",
        "steps": ["Place the SECOND tube on its long side beside the first, parallel or at an angle, fully inside the base edges. Do not stack tubes across or inside each other. Or point for the adult to place it.", "Adult holds and attaches the second tube with the same two-strip method. If it rolls or tape lifts, adult collects loose tape and chooses the untaped flat arrangement or ends.", "Look from above or beside. What shape do you see? Point, name it or just look. One arrangement is enough; no extra pieces, height goal or required repeat."],
        "parent_label": "Rescue and cleanup",
        "parent": "If tape will not hold, remove loose tape and look at the tubes lying untaped on the base, or end. Do not add weights or stronger glue. Adult slowly removes tape; if cardboard tears, stop peeling and collect the damaged piece. Collect all tape, fibers and tubes, check table and floor, clear the surface and store ALL materials out of reach. Do not leave the assembly accessible unattended. Duration, effort and mess are not measured.",
        "sources": [("Grinnell Arts: tape-joined tube sculpture", "https://www.grinnellarts.org/crafts-activities-blog/2017/6/23/recyclable-sculptures"), ("Core Knowledge: adult model and cardboard base (PDF pp92-94)", "https://www.coreknowledge.org/wp-content/uploads/2025/11/CKVA_GK_TG_W2.pdf"), ("Chicago Children's Museum: paper forms on a flat base", "https://www.chicagochildrensmuseum.org/parenting-playbook-posts/2020/7/13/at-home-activity-whoop-de-doo-roller-coaster-sculpture"), ("AAP: general parts and age guidance", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Grinnell, Chicago and AAP bodies rechecked October28,2026; Core Knowledge pp92-94 re-read from the October27 download. Sources support tube/tape assemblage, an adult model and a cardboard base, not this exact horizontal two-tube strap procedure. That layout, counts, roles, trial, untaped/end fallback and cleanup are Kid Activity Lab editorial adaptations, not an inspected source procedure or tested setup. We exclude source knives, slit joints, glue, paint, small decorations and height challenges. AAP gives general toy guidance, not certification of reused cardboard. Owned tape instructions govern its use; no source verifies this cardboard joint or damage-free removal. Actual fit, adhesion, hygiene, understanding, enjoyment, learning, repetition, duration, mess and safety outcomes are unknown. The old creator video was not watched or used as this procedure's source. No product recommendation or safety assurance.",
    },
    "tape-city": {
        "title": "Tape City",
        "url": "../cards/tape-city.html",
        "ages": "3-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Editorial ages 3-6; check readiness",
        "mess_label": "Mess not measured",
        "help_label": "Adult tapes and stays",
        "materials": "owned surface-appropriate painter's tape, compatible allowed surface or removable board, 1 intact large hand-pushed toy vehicle and OPTIONAL 1 intact large lightweight nonmagnetic block; BOTH toys without small or detachable parts, magnets or batteries",
        "best_for": "adding one pretend place beside an existing short road, or keeping a plain road",
        "readiness_groups": [
            ("Surface", "Use the full road guide first. Follow owned tape AND surface instructions, including a hidden-area test. A brief test does not guarantee later clean removal; a board can tear too. No allowed compatible surface or board? Decline."),
            ("Fit and adult", "Follow owned toy age, warning and use labels for EVERY reachable child. Adult applies and removes ALL tape, controls roll and spares, stays beside all children and clears a firm level area away from feet and walkways. Try when the child can push gently and pause. Skip for mouthing, younger reach you cannot control or unavailable attention."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. Pointing, watching or declining is valid."),
        ],
        "stop": "End for peeling tape, chewing, wrapping, mouthing, throwing, climbing, damage, unstable support, surface change, discomfort, unwanted action or lost attention. Do not force tape, wheels or a building to work.",
        "adult_setup_groups": [
            ("Road first", "BEFORE child access, use the guide's surface checks, short broad road and parking start. Adult tries one gentle vehicle push. If tape or the vehicle does not fit, use the guide's untaped/end rescue. Keep tape roll, loose bits and spares out of reach."),
            ("Optional place", "Place ONE checked block lying FLAT BESIDE the road, OUTSIDE the wheel and parking path, as a pretend building. No stacking, bridge, roof, ramp, extra figures or tools. No suitable block? Keep a plain road, not a substitute small toy or purchase."),
        ],
        "steps": [
            "Choose a plain road or one flat building beside it. Place the checked block with adult help, or point for the adult; no building is required.",
            "Say: Where could the vehicle park? Push gently to the guide's parking place, point or watch. Pause when asked; ending is valid.",
            "Finish, or repeat the SAME short route only if wanted. Adult handles all tape and collection; no bigger city or timed reset is required.",
        ],
        "parent_label": "Rescue and cleanup",
        "parent": "If the building distracts or does not fit, adult removes it; use the plain road or point/watch/end. For tape or vehicle trouble use the full guide's untaped/end rescue, not more force. Adult follows owned removal instructions, stops peeling if the surface changes, collects ALL used tape and bits, roll, vehicle, optional block and spares, checks the area and stores everything out of reach. Duration and mess have not been measured.",
        "sources": [
            ("Toy Association: short wide road and surface warning", "https://www.toyassociation.org/genius/play-ideas-tips/play-ideas/tape-track.aspx"),
            ("TALK: optional block buildings", "https://textandlearn.org/tools/hands-on/toddler-activities/masking-tape-roads/"),
            ("FrogTape: product-specific hidden-area test", "https://www.frogtape.com/how-to-use/painters-tape"),
            ("MSU Extension: clear space and block arrangements", "https://accessibility.extension.msstate.edu/publications/block-play"),
            ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Sources audited October28,2026; Toy Association, TALK and FrogTape rechecked for this repair, MSU and AAP retained from that day's reviewed audit. Short wide roads and optional block buildings are source-backed. One flat block, exact counts, roles, skips, stops and collection are Kid Activity Lab editorial adaptations, not an inspected creator-video procedure or tested setup. FrogTape describes painting, not a universal tape-play recipe; its wet-paint, blade and tool instructions are not adopted. Small cars, magnetic props, long routes, crawling and developmental promises are excluded. Complete road setup remains in the linked guide. Owned fit, adhesion, removal, family understanding, time, mess, enjoyment, learning and safety outcomes are unknown. No brand recommendation or damage-free promise.",
    },
    "sock-ball-roll": {
        "title": "Sock Ball Roll",
        "url": "../cards/sock-ball-roll.html",
        "ages": "3-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "mess_label": "Mess not measured",
        "help": "adult-guided",
        "help_label": "Adult stays beside lane",
        "materials": "two clean soft socks, one low empty basket",
        "best_for": "aiming one gentle floor roll toward a target",
        "description": "Sock Ball Roll: an adult-guided floor roll toward a low basket, with a closer-target rescue. Research-backed, not family-tested by Kid Activity Lab.",
        "start_cue": "Adult: clear a short floor lane away from stairs, doors, cords, breakables and walkways. Stay beside every child who can reach it; skip if you cannot watch them all. Try when the child can release along the floor and pause on request. Stop for throwing, running, mouthing, a loose sock, discomfort, or anyone entering the lane. Research-backed, not family-tested by Kid Activity Lab.",
        "adult_setup": "Use socks only, without ties or hard fillers. Push one sock into the other's toe and fold the cuff over it into a soft ball with no trailing fabric. Put the empty basket on the floor nearby. It is a target to roll toward, not a rim to roll over. If the ball comes apart, stop and remake it.",
        "steps": ["Put the sock ball on the floor.", "Roll gently toward the basket; touching it is optional.", "Pause, then walk to collect the ball and reset."],
        "parent": "If aiming stalls, bring the basket closer or gently roll to an adult partner instead. No basket? Use that partner-roll option in the same clear lane. Take turns one at a time; do not lengthen the lane beyond adult reach. End by putting away the socks and basket and clearing the floor.",
        "sources": [
            ("Raising Children Network sock-ball ideas", "https://raisingchildren.net.au/guides/activity-guides/movement/sock-balls-fun-movement-coordination-activity-for-kids"),
            ("AAP activity planning", "https://www.healthychildren.org/English/healthy-living/fitness/pages/Encouraging-Your-Child-to-be-Physically-Active.aspx"),
        ],
        "source_note": "Sources checked October 27, 2026. RCN describes sock balls, floor targets and pushing or rolling adaptations; AAP gives general ability, space and adult-participation guidance. This one-ball, roll-toward-basket setup and its stop/rescue rules are KAL editorial synthesis, not a tested safety method. Time, mess, comprehension, enjoyment, learning and physical outcomes are unknown.",
    },
    "spoon-transfer": {
        "title": "Spoon Transfer",
        "url": "../cards/spoon-transfer.html",
        "ages": "3-5",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Editorial ages 3-5; check fit",
        "mess_label": "Mess not measured",
        "help_label": "Adult checks, models and stays",
        "materials": "1 intact LARGE owned play pom-pom from an age-labelled play set, 1 smooth wide/deep spoon comfortable to hold, 2 stable unbreakable bowls and 1 rimmed tray",
        "best_for": "trying a scoop, carry and tip, or pointing for the adult",
        "readiness_groups": [
            ("Materials", "Adult checks labels, condition and suitability for every reachable child. No shedding, loose filling, damaged or detachable parts. No craft fluff, food, beans, rice, pasta, coins, beads, marbles, magnets, water or cork substitutes. No suitable owned play pom? Choose another activity."),
            ("Adult and fit", "Stay beside every reachable child and steady bowls as needed. Try when the child can hold the spoon comfortably and pause on request, or point for you. Skip for mouthing, uncertain parts, younger reach you cannot control or unavailable attention. Size and supervision are not a choking guarantee; do not test materials in a mouth."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. This one-pom fit trial and controls are editorial adaptations, not tested protection. Watching or declining is enough; no forced grip, counting or spoken answer."),
        ],
        "stop": "End for mouthing, shedding, throwing, force, spoon play toward bodies, lost control, discomfort, anything leaving the tray or shifted adult attention. Adult collects all materials.",
        "adult_setup": "Use a stable low clear table away from edges. Set bowls side by side on the tray, one pom in one bowl and the other empty. BEFORE child access, adult gently scoops that pom, carries it above the empty bowl and tips it in once. It must rest freely on the spoon: no squeezing, stabbing, flicking or launching. Failed fit? Skip, not smaller filler. Return the pom to the starting bowl if continuing.",
        "steps": ["Try one scoop from the starting bowl. Use a comfortable hand, or point for the adult to scoop while you watch.", "Carry the spoon above the empty bowl and tip the pom inside. One try is enough; you can stop without finishing.", "Dropped in the tray? Put the spoon down. Adult collects the pom and may replace it once if you want, or end. Do not chase pieces or race."],
        "parent_label": "Rescue and cleanup",
        "parent": "If scooping is difficult, watch one adult model or end; do not force a grip or use smaller filler. A pom leaving the tray ends the activity. Adult collects the pom and any loose bits, checks table and floor, clears the surface and stores ALL pom, spoon, bowls and tray out of reach. Duration, effort and mess are not measured.",
        "sources": [("Montessori Academy: two bowls, hand-fit spoon and adult model", "https://montessoriacademy.com.au/montessori-at-home/toddler-resources/scooping-spooning-and-pouring/"), ("SDN: pom-poms, bowls and adult stays", "https://www.sdn.org.au/village-of-learning/activities-scoop-sort-and-pour/"), ("The Toy Foundation: large-spoon context", "https://toyfoundation.org/genius/play-ideas-tips/play-ideas/pom-pom-fun-games.aspx"), ("AAP: owned toy labels, condition and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources checked October27,2026. Montessori Academy Home Lesson Four supplies the two-bowl, hand-fit spoon, tray and adult demonstration. SDN supplies pom-pom scooping with an adult staying; The Toy Foundation supplies large-spoon context. The single owned age-labelled play-pom, fit trial, roles, skip/stop and cleanup are Kid Activity Lab editorial adaptations, not an inspected source procedure or tested setup. We exclude source food/small fillers, jug pouring, tongs, timed races and forced non-dominant-hand use. AAP gives general toy guidance, not certification of this set. Source age labels and photos do not prove readiness or fit. Owned fit, understanding, enjoyment, learning, repetition, duration, mess and safety outcomes are unknown. No product recommendation, therapy or safety assurance.",
    },
    "paper-bridge": {
        "title": "Paper Bridge",
        "url": "../cards/paper-bridge.html",
        "ages": "4-6",
        "time": "3 min",
        "mess": "low",
        "help": "medium",
        "materials": "paper, two books, toy car",
        "best_for": "engineering, problem solving, testing",
        "steps": ["Put books apart.", "Lay paper across.", "Try a car.", "Fold paper stronger."],
        "parent": "Keep books low and stable.",
    },
    "box-garage": {
        "title": "Box Garage",
        "url": "../cards/box-garage.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check readiness first",
        "mess_label": "Mess not measured",
        "help_label": "Adult stays beside setup",
        "materials": "1 already-open small cardboard box, 1 large lightweight toy car",
        "best_for": "pretend parking with one car, not a child-sized box build",
        "readiness_groups": [
            ("Box and car", "Adult checks a clean, empty, dry, intact box without staples, sharp edges, plastic packing or loose pieces; choose another box or skip rather than repair it during play. Check the owned car's age/warning labels for every child who can reach it; use intact large pieces without loose small parts, magnets or battery parts."),
            ("Space", "Clear floor space away from walking routes. Toys only: no sitting, climbing, wearing or shutting anyone inside the box."),
            ("Adult and child", "Stay beside every reachable child and keep tools, packing and spare pieces away. Try when the child can roll with help and follow a stop cue; watching or pointing is an option. Skip if fit, space or attention do not match."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab."),
        ],
        "stop": "Stop for mouthing, throwing, loose pieces, torn or sharp cardboard, feet or climbing, body entry, blocked walking routes or lost adult attention.",
        "adult_setup": "Put the already-open box on its side on the clear floor, with the opening facing the player and unobstructed. Check the car can roll in and out without catching, force or lifting the box. No cutting or tape is needed for this one-car start.",
        "steps": ["Drive the car through the ready opening.", "Park the car. Say or point to where it is.", "Drive back out through the same opening. Repeat or finish."],
        "parent_label": "Rescue and cleanup",
        "parent": "If the car catches, park beside the box instead; do not force the car or cut a new entrance. Adult may model while the child watches or points. Adult puts away the box and car and clears the walking area. Duration and mess have not been measured.",
        "sources": [("Purdue ELM: pretend garages and car fit", "https://elmcurriculum.org/lesson/focusing-and-remembering-block-12-12-24-months/"), ("Raising Children Network: cardboard play and adult tools", "https://raisingchildren.net.au/guides/activity-guides/making-and-building/playing-with-cardboard-boxes"), ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources checked October27,2026. Pretend garages, car fit and general adult-tool/toy guidance are source-backed. The one-box/car start, no-cut reduction, floor/attention controls, script and rescue are Kid Activity Lab editorial adaptations. Purdue's younger-child memory lesson and photos do not validate this preschool setup, dimensions, age fit or learning. RCN text was accessible; browser article viewing was challenged. Physical fit, hygiene, family understanding, enjoyment, learning and safety outcomes are unknown. Not a tested setup, product recommendation or safety assurance; the old creator video was not watched.",
    },
    "blanket-river": {
        "title": "Blanket River",
        "url": "../cards/blanket-river.html",
        "ages": "3-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check readiness first",
        "mess_label": "Mess not measured",
        "help_label": "Adult stays beside setup",
        "materials": "1 flat blanket, 3 large lightweight blocks (2 low supports and 1 longer span), 1 large lightweight toy",
        "best_for": "making a tiny pretend crossing for a hand-carried toy, never for feet",
        "mission": "Help a hand-carried toy cross a tiny pretend river near one blanket edge, not the blanket's full width.",
        "fit_cue": "Check owned toy and block age/warning labels for every child who can reach them. Use intact large lightweight pieces without loose small parts, magnets or battery parts. Clear a low floor area away from doors and walking routes; the blanket must stay flat. State that the route is for the toy, not for feet. Stay beside every reachable child and keep spares away. Try when the child can place with help and follow a stop cue; watching or pointing is an option. Skip if parts, space or attention do not fit. Research-backed, not family-tested by Kid Activity Lab.",
        "stop": "Stop for mouthing, throwing, damaged pieces, blanket bunching or slipping, running, climbing, feet on the route, blocked paths, lost adult attention or unwanted collapse.",
        "adult_setup": "Choose a tiny crossing near one blanket edge, not across its full width. Check two low wide blocks can sit a short gap apart with the longer block resting on both. Do not force a span that does not fit; use a flat toy path instead.",
        "steps": ["With adult help, place the two low supports and rest the longer block across both.", "Carry the toy in your hand over the tiny bridge and back; keep its weight in your hand, not on the bridge.", "Put the toy back at the start. Repeat the pretend crossing or finish."],
        "parent_label": "Rescue and cleanup",
        "parent": "If the span does not fit, lay blocks flat as a path for the hand-carried toy; do not add height, widen the gap or use force. Adult may move the toy while the child watches or points. Adult puts away the blanket, blocks and toy, clearing the walking area. Duration and mess have not been measured.",
        "sources": [("Mississippi State Extension: Block Play", "https://extension.msstate.edu/publications/block-play"), ("SDSU Extension: block bridging", "https://extension.sdstate.edu/playing-blocks"), ("AAP: toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources checked October27,2026. Block bridging and pretend props are source-backed. This tiny near-edge blanket story, owned-piece selection, hand-carried toy, adult script, stop and cleanup are Kid Activity Lab editorial adaptations, not a tested setup or load test. Source photos do not show this exact blanket arrangement. Physical fit, stability, blanket slip, family understanding, enjoyment, learning and safety outcomes are unknown. No product recommendation or safety assurance.",
    },
    "sink-or-float-tray": {
        "title": "Sink or Float Tray",
        "url": "../cards/sink-or-float-tray.html",
        "ages": "4-6",
        "time": "Not measured",
        "time_label": "Time not measured",
        "mess": "Not measured",
        "mess_label": "Mess not measured",
        "help": "medium",
        "help_label": "Adult stays beside child",
        "materials": "shallow tray, a little water, one intact large bath toy",
        "best_for": "predicting and observing one object's movement in water",
        "start_cue": "Adult checks one intact large water-play toy's age label and condition, and keeps water and toy out of a younger child's reach. No suitable toy? Skip. Also skip if you cannot watch constantly or prevent access. Stop and empty the tray if attention shifts or anyone reaches for water. Not family-tested by Kid Activity Lab.",
        "adult_setup": "Put the shallow tray on a stable table with a little water. Adult places and retrieves the toy. If bottom contact is unclear, do not add water to force a result.",
        "steps": ["Guess: up or down?", "Adult puts toy in; watch.", "Off bottom? Floats. Drops through water to bottom? Sinks.", "Unsure? Say 'unclear'; adult empties tray."],
        "parent": "Adult empties the tray immediately and puts the toy away. Do not leave standing water behind.",
        "kicker": "Editorial ages 4-6 | Predict",
        "description": "Predict and observe what one adult-placed bath toy does in a shallow tray. Research-backed idea; this home version has not been family-tested by Kid Activity Lab.",
        "sources": [
            ("NAEYC sink-or-float example", "https://www.naeyc.org/our-work/families/support-science-learning"),
            ("AAP water supervision", "https://www.healthychildren.org/English/news/Pages/AAP-releases-updated-drowning-prevention-recommendations.aspx"),
            ("AAP empty-container guidance", "https://www.healthychildren.org/English/safety-prevention/at-play/Pages/Infant-Water-Safety.aspx"),
            ("CPSC toy age and small-part guidance", "https://www.cpsc.gov/id/Safety-Education/Toys"),
        ],
        "source_note": "NAEYC describes prediction and observation with objects in water. AAP gives general attentive water-supervision and empty-container guidance; CPSC gives toy age and small-part guidance. This one-toy tray, placement, result and stop sequence is KAL editorial synthesis, not a tested safety method. Time, mess, comprehension, enjoyment, learning and physical outcomes are unknown.",
    },
    "ice-melt-rescue": {
        "title": "Melting Ice Watch",
        "url": "../cards/ice-melt-rescue.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check readiness first",
        "mess_label": "Mess not measured",
        "help_label": "Adult handles; child watches",
        "materials": "1 plain water ice cube, 1 shallow nonbreakable tray, 1 adult spoon, 1 towel",
        "best_for": "noticing solid ice and liquid water while an adult handles the materials",
        "readiness_groups": [
            ("Materials", "Use plain ice with nothing frozen inside and an intact shallow nonbreakable tray. The spoon is for the adult. No added water, heat, salt, colour or embedded toys; this is not a snack or a toy-rescue activity."),
            ("Adult and space", "Adult handles the ice, spoon and meltwater throughout. Set the tray on a stable level surface away from edges and walking routes, beyond every child's reach but visible to them. Stay beside every reachable child; keep spares away."),
            ("Fit or skip", "Try only when every child can watch with hands away and respond to a stop cue. Pointing or saying what you notice are options. Skip if a child mouths or reaches for materials, or you cannot maintain reach control and attention."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab."),
        ],
        "stop": "End and collect if a child reaches for the ice, tray or spoon, mouths material, ice leaves the tray, water spills, anyone is uncomfortable or adult attention shifts.",
        "adult_setup": "Start with the empty dry tray and towel ready for cleanup. Adult uses the spoon to place one plain water ice cube in the tray, without adding water. Point out its starting shape and any liquid already there. Keep the tray beyond children's reach while they look; no cold touching is required.",
        "steps": ["Look at the ice without touching. Point to its shape.", "Look again: is the ice smaller, or is there more liquid around it?", "Say or point: changed or not yet clear. Finish whenever you want; no need to wait for all the ice to melt."],
        "parent_label": "Rescue and cleanup",
        "parent": "If a change is not clear, say 'not yet clear' and end, or look again only while the adult can stay. Do not add heat, water or tools for the child to force a result. Adult takes remaining ice and meltwater to a sink out of children's reach and empties the tray immediately, then dries the tray and work area and puts away the spoon, tray and towel. Do not leave ice or standing water accessible. Duration and mess have not been measured.",
        "sources": [("Sciencenter: plain-ice alternative and observation", "https://sciencenter.org/wp-content/uploads/using-tools-and-melting-ice-1.pdf"), ("AAP: water reach and immediate emptying", "https://www.healthychildren.org/English/safety-prevention/at-play/Pages/Infant-Water-Safety.aspx")],
        "source_note": "Sources checked October27,2026. Sciencenter includes plain ice as an alternative to frozen toys and prompts observation; its tool-rich photos do not show this exact setup. The one-cube look-only reduction, adult-only handling, beyond-reach placement, script, stop and cleanup are Kid Activity Lab editorial adaptations, not a tested safety method. AAP gives general water-supervision and empty-container guidance, not certification of a tray or a contact/temperature rule. Owned material suitability, hygiene, physical outcomes, family understanding, enjoyment, learning and safety are unknown. No measured melt rate or duration, medical guidance, product recommendation or safety assurance.",
    },
    "magnet-hunt": {
        "title": "Magnet Hunt",
        "url": "../cards/magnet-hunt.html",
        "ages": "4-6",
        "time": "Not measured",
        "mess": "Not measured",
        "help": "medium",
        "materials": "Magnet Hunt paused; choose another activity",
        "best_for": "a material decision before any magnet activity",
        "steps": [],
        "parent": "This card is paused. Do not use a known or suspected high-powered or rare-earth magnet, or one with unknown type and power.",
    },
    "shadow-shape-match": {
        "title": "Shadow Builder",
        "url": "../cards/shadow-shape-match.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "mess_label": "Mess not measured",
        "help_label": "Adult controls the light",
        "materials": "1 owned flashlight, 1 checked large opaque block, clear wall",
        "best_for": "noticing how moving one object changes its shadow, not a matching game or test",
        "readiness_groups": [
            ("Materials", "Adult checks the flashlight's instructions, intact casing and closed, secured battery compartment. Use it only as its instructions permit; no lasers, candles or exposed bulbs. Check the block's age/warning labels for every reachable child; use a large intact opaque (not see-through) block without loose small parts, magnets or battery parts."),
            ("Adult and space", "Keep light on wall, never faces. Stay beside every reachable child and keep the light and spare pieces under adult control. Keep a clear walking path visible; dim only enough to see the shadow."),
            ("Fit or skip", "Try when the child can move the block with help and follow a stop cue; watching or pointing is an option. Skip if materials, steady wall beam, space or adult attention do not fit, or dimness is unwanted."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab."),
        ],
        "stop": "Switch off if the beam leaves the wall, a child reaches for the light or battery parts, a piece is mouthed or thrown, attention shifts, or anyone is uncomfortable.",
        "adult_setup": "Set the flashlight on a stable low surface pointing at the clear wall, away from the walking path. Adult checks that it stays still and makes a visible shadow when the block is between light and wall. Keep the light fixed; start the block nearer the wall, leaving room to move it toward the light without touching the flashlight. If this cannot be arranged, skip.",
        "steps": ["Hold the checked block between the steady light and wall, nearer the wall.", "Move the block a little nearer the light, not the light itself. Look for a bigger shadow.", "Move the block back. Say or point: bigger, smaller or unclear? Repeat or finish."],
        "parent_label": "Rescue and cleanup",
        "parent": "If the shadow is unclear or the flashlight becomes the toy, switch it off and park it. Adult checks the opaque block is between light and wall. Resume only after an adult restores a steady wall-pointed beam and a visible shadow; the child moves the block or watches the adult move it. Otherwise end. Brighten the room if wanted. Adult switches off and puts away the light, block and spares, clearing the walking path. Duration and mess have not been measured.",
        "sources": [("PBS: wall light and shadow-size comparison", "https://www.pbs.org/parents/crafts-and-experiments/put-on-a-shadow-play"), ("Gryphon House: adult-controlled wall light", "https://www.gryphonhouse.com/early-childhood-activities/light-and-shadow"), ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources checked October27,2026. Blocking light, moving an object and adult wall-light control are source-backed. The one-owned-block reduction, readiness checks, visible walking path, no-face/switch-off rules, script and rescue are Kid Activity Lab editorial adaptations. PBS uses cutout figures and Gryphon describes a classroom; neither validates this exact home geometry or an owned device. Source photos are not proof of scale or physical performance. Flashlight/block suitability, family understanding, enjoyment, learning and safety outcomes are unknown. Not a tested setup, medical guidance, product recommendation or safety assurance.",
    },
    "foil-boat-test": {
        "title": "Empty Foil Boat",
        "url": "../cards/foil-boat-test.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "Adult stays throughout",
        "mess_label": "Mess: not measured",
        "help_label": "Adult stays throughout",
        "materials": "foil, shallow water tray, towel; no cargo",
        "best_for": "noticing whether an empty hull floats, leans or leaks",
        "steps": ["Raise the foil edges.", "Pinch corners without cutting.", "Adult checks empty flotation.", "Lift out, change one side or stop."],
        "parent": "Adult controls water and stays beside the tray. Stop for mouthing, torn foil, spills or lost attention; empty and store the tray before leaving. Not family-tested; open the guide for folds, clearance and rescue.",
    },
    "straw-bridge": {
        "title": "Straw Bridge",
        "url": "../cards/straw-bridge.html",
        "ages": "4-6",
        "time": "Time not measured",
        "mess": "Not measured",
        "help": "Adult joins and stays",
        "materials": "SIX whole straight paper straws of equal length, TWO strips of owned painter's tape, TWO broad low closed books of matching height; no load required",
        "best_for": "joining a flat row and noticing an empty span",
        "fit_cue": "Adult stays beside the setup and owns tape, books, trials and collection. Skip for mouthing, uncontrolled younger reach, damaged materials or uncertain adult attention. Child may choose, point, watch or end. Check owned material and tape directions; decline if they do not fit. No cutting straws or substituting bendy, silicone or plastic straws in this start.",
        "stop": "Stop for loose tape, bent, wet or damaged straws, sliding supports, mouthing, throwing, climbing, wanting to leave or lost adult attention. Remove any optional object before any change; do not reinforce under load.",
        "steps": [
            "Adult lays SIX whole paper straws side by side on a flat dry surface, ends even. Keep one FLAT row, not a round bundle.",
            "Adult lays a tape strip across the row near one end, folds it around BOTH outside edges and joins the tape to itself underneath. Repeat near the other end. Each band wraps the WHOLE flat row, not individual straws. Do not squeeze or twist; end if the tape will not hold or straws deform.",
            "Adult puts TWO broad low CLOSED books flat on clear floor, at matching height with a gap shorter than the straws. Lay the deck so BOTH ends of EVERY straw rest well on the covers. Do not tape it to the books. Adult checks the EMPTY span while staying beside it.",
            "Look or point: flat, bending or slipping? Do not push. No object is required. Adult can lift the empty deck off, move books closer for ONE empty retry, or end. Loose tape or damaged straws mean end, not another trial.",
        ],
        "rescue": "If it will not span, lift it off before moving books closer for one empty retry, or end. Keep the joined row flat on the floor for a DIFFERENT joining-only activity if its tape and straws remain intact; that is not a bridge. Do not add cups, stacks, clips, string or hanging loads.",
        "optional_load": "Only after an intact, stable empty trial: the adult may gently place and remove ONE owned intact LARGE lightweight flat-base block that fits wholly on the deck without balancing. Check its condition, label and suitability for EVERY reachable child. If base, size, fit or adult control is uncertain, stay empty or end. No cups, coins, marbles, washers, driving or load-to-failure. Remove the object before ANY change; stop if it bends or slips.",
        "cleanup": "Adult removes the optional object first, lifts the deck off the books, collects all tape, straws and loose fragments, then puts the books away. End with any damaged or loose material; do not leave pieces for younger children.",
        "parent": "Adult joins and stays; read fit, stop, joint and empty-trial checks before handling. Low closed books replace the old cup supports. Research-backed editorial start, not physically or family-tested by Kid Activity Lab.",
        "sources": [
            ("U-M activity: whole-row tape wrap only", "https://www.uofmhealth.org/camp-little-victors/straw-flute"),
            ("Science Buddies: flatness and over-tight tape", "https://www.sciencebuddies.org/science-fair-projects/project-ideas/CE_p011/civil-engineering/the-effect-of-bridge-design-on-weight-bearing-capacity"),
            ("TeachEngineering: joined-straw material comparison", "https://www.teachengineering.org/content/uot_/activities/uot-2982-fairy-tale-engineering/uot-2982-fairy-tale-research-activity-worksheet.pdf"),
            ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"),
        ],
        "source_note": "Sources checked October 28, 2026. U-M describes a paper-straw flute: we use its written whole-row wrapping principle only, not cutting, blowing, mouthing or medical guidance. Science Buddies describes flat straw assemblies and warns against tape that twists or deforms them. TeachEngineering compares joined straws in a different hanging-load activity, not this deck. The SIX straws, TWO bands, no-cut paper material, low-book layout, empty trial, optional block, diagram, roles and stops are KAL editorial adaptations, not a source-tested preschool setup. No truss, hanging-load or break-to-failure challenge is offered. Actual assembly, adhesion, fit, stability, understanding, timing, mess, enjoyment, repetition, learning and safety outcomes are unknown; no strength or universal safety promise.",
    },
    "paper-chain-test": {
        "title": "Paper Chain Test",
        "url": "../cards/paper-chain-test.html",
        "ages": "4-6",
        "time": "6 min",
        "mess": "low",
        "help": "medium",
        "materials": "paper strips, tape",
        "best_for": "loops, strength, comparing designs",
        "steps": ["Make one paper loop.", "Tape it closed.", "Add another.", "Compare long and short."],
        "parent": "Adult cuts strips before play.",
    },
    "ramp-texture-test": {
        "title": "Ramp Texture Test",
        "url": "../cards/ramp-texture-test.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check release and readiness",
        "mess_label": "Mess not measured",
        "help_label": "Adult steadies the ramp",
        "materials": "1 flat stiff cardboard piece, 2 broad sturdy closed books, 1 owned toy car, 1 optional thin flat dish towel, owned masking tape",
        "best_for": "noticing where the same car stops on a plain ramp and one optional covered ramp",
        "readiness_groups": [
            ("Materials", "Adult checks intact cardboard, books, towel and freely turning car wheels; follow the owned toy and tape labels. Use a car appropriate for every child who can reach it, without loose parts. Adult handles tape, spare materials and cover changes."),
            ("Adult and space", "Floor only, with a clear landing and walking path. Adult stays beside every reachable child and steadies the ramp throughout. Retrieve the car only after it stops; no climbing, standing on books or ramp, throwing or chasing."),
            ("Fit or skip", "Try when the child can let go without pushing and follow a stop cue, or watch the adult release. Pointing instead of touching the towel is optional. Skip if space, mouthing, material labels, stability or attention do not fit."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab."),
        ],
        "stop": "End if the ramp or books slip, cardboard bends, the towel bunches or comes loose, a part loosens, anyone mouths materials, climbs, throws, becomes uncomfortable or attention shifts. No forcing a launch or raising the ramp to get a result.",
        "adult_setup": "On the floor, stack the two books flat and lean one cardboard end on them, the other on the floor. Check support and hold it steady. Adult first releases the car without pushing from one chosen spot. If it will not freely roll or the setup will not stay stable, skip the comparison; do not keep adding height. Keep tape and spares out of reach. Choose one start spot to use for both rolls.",
        "steps": ["Adult steadies the plain ramp. Let go of the car at the chosen spot without pushing, or watch the adult. Wait until it stops before retrieving.", "Adult covers the wheel path with the thin towel and secures it flat with masking tape, following owned labels. Keep the same books and height. Adult checks for loose edges, folds or catches; if it will not stay flat, skip this roll and finish.", "With the ramp still steadied, release the same car from the same spot without pushing. Notice: nearer, farther, about the same, stuck or unclear. One comparison is enough; you can finish."],
        "parent_label": "Rescue and cleanup",
        "parent": "If stuck or unclear, finish rather than push harder or raise the ramp. Adult removes the cover; return to one plain roll only if stable and wanted, or end. Adult promptly puts away the car, tape, towel, books and cardboard and clears the floor. Duration and mess are not measured; a single result does not prove friction alone caused it.",
        "sources": [("PBS: supported ramp, secured covering and same-start releases", "https://www.pbs.org/parents/crafts-and-experiments/friction-racing"), ("PEEP: roll, slide or stay and assistance", "https://www.peepandthebigwideworld.com/en/educators/curriculum/family-child-care-educators/ramps/activity/guided-activity/244/roll-or-slide-indoors/"), ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources checked October27,2026. Supported ramps, secured coverings and same-start release comparisons are source-backed. The two-book floor setup, one-cloth reduction, adult roles, readiness, stop and rescue are Kid Activity Lab editorial adaptations, not a tested setup. PBS uses repeated measured trials; PEEP includes varied objects and assistance. Neither source age labels, photos nor educator observations validate this exact arrangement. Owned toy and tape suitability, adhesion, ramp stability, car motion, family understanding, timing, mess, enjoyment, learning and safety outcomes are unknown. No guaranteed nearer or farther result, clinical rule, product recommendation or safety assurance.",
    },
    "wind-tower-test": {
        "title": "Wind Tower Test",
        "url": "../cards/wind-tower-test.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check placement and readiness",
        "mess_label": "Mess not measured",
        "help_label": "Adult controls the paper fan",
        "materials": "6 matching intact lightweight nonmagnetic blocks with no small or detachable parts, 1 adult-prepared folded paper fan",
        "best_for": "noticing whether a low block build stands, moves or falls during adult fanning",
        "readiness_groups": [
            ("Materials", "Follow the owned toy labels and check blocks and paper for damage or loose pieces. Adult folds the paper fan and controls it and spares. No electric fan, hairdryer, heavy book or mouth blowing."),
            ("Adult and space", "Use a level floor away from walking paths. Adult stays beside every reachable child. Before fanning, move everyone's hands and bodies clear of possible falling pieces; leave room to wave without touching blocks or people. Retrieve only after the fan stops and pieces settle."),
            ("Fit or skip", "Try when the child can place blocks gently and follow a stop cue, or point and watch the adult. Skip if labels, mouthing, space, attention or keeping the fan clear do not fit. Stop if falling or noise is unwelcome."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. Counts, layout and waves are editorial choices, not calibrated wind or tested protection."),
        ],
        "stop": "End for loose parts, mouthing, throwing, climbing, fan contact risk, discomfort or shifted attention. Stop fanning sooner if pieces move or fall, or anyone wants to stop. Never fan harder, move closer or build taller to force collapse.",
        "adult_setup": "Adult checks a flat three-block base on the floor. Add up to three blocks on top only if steady and wanted; use no more than two layers and keep below the child's chest. If the blocks will not sit flat, use a single row or skip fanning. Choose one fan position with room for a small clear wave and keep it for any repeat. Keep spares out of reach.",
        "steps": ["Place three blocks side by side. With adult help, add up to three on top only if steady, or watch. Keep the build below the child's chest.", "Move hands and bodies clear. Adult alone makes up to three small slow paper-fan waves from the chosen spot, without touching blocks or people. Stop sooner if pieces move or fall, or anyone wants to stop.", "Notice or point: standing, moved, fell or unclear. Wait for the fan to stop and pieces to settle before retrieving. One fan test is enough; you can finish."],
        "parent_label": "Rescue and cleanup",
        "parent": "If nothing moves or the result is unclear, finish without stronger or closer fanning. If wanted, adult helps make a lower or wider build from the same blocks and repeats from the same spot with the same gentle waves; force is not calibrated. Otherwise keep a flat row or end. Adult promptly puts the fan and blocks away and clears the floor. Duration and mess are not measured.",
        "sources": [("Franklin Institute: block building and hand-held airflow", "https://fi.edu/en/science-and-education/science-recipes/building-tall"), ("Kansas Children's Discovery Center: standing and same-distance retesting", "https://kansasdiscovery.org/materials-testing-discovery-at-home/"), ("Boston Children's Museum: folded-paper fans and no-movement results", "https://resourcehub.bostonchildrensmuseum.org/resources/wind-races"), ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources reviewed October27,2026. Block building, hand-held airflow, descriptive observation and consistent-position retesting are source-backed. The six-block, at-most-two-layer floor default, adult-only paper fan, up-to-three gentle waves, readiness and stop rules are Kid Activity Lab editorial adaptations, not a tested setup. Source tall builds, electric fans, small loose objects, age labels, photos, timing and learning claims do not validate this arrangement. Owned material fit, fan force, stability, motion, family understanding, duration, mess, enjoyment, learning and safety outcomes are unknown. A standing or fallen build is not proof of wind resistance or safety; no clinical rule or product recommendation.",
    },
    "pattern-path": {
        "title": "Pattern Path",
        "url": "../cards/pattern-path.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check matching and placement",
        "mess_label": "Mess not measured",
        "help_label": "Adult sets the starter and choices",
        "materials": "6 intact lightweight nonmagnetic blocks: 3 of kind A and 3 of kind B, visibly different in shape, type or color; no small or detachable parts",
        "best_for": "noticing and continuing one repeating AB pair",
        "readiness_groups": [
            ("Materials", "Adult follows owned toy labels and checks condition and suitability for every reachable child. Size alone is not assurance. Use two kinds the child can distinguish without naming colors."),
            ("Adult and space", "Use a stable tabletop away from edges. This is a row of blocks, not a walking path. Adult stays beside every reachable child and controls spare pieces."),
            ("Fit or skip", "Try when the child can match two kinds and gently place a piece, or point for the adult. Otherwise match two alike, watch or end. Skip if labels, mouthing, visibility or attention do not fit."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. Counts, script, retry and controls are editorial choices."),
        ],
        "stop": "End for mouthing, throwing, damaged or loose parts, discomfort or shifted attention, or whenever the child wants to stop. Adult gathers all pieces and puts them away.",
        "adult_setup": "Call the two kinds A and B. Lay four blocks A-B-A-B, using two of each kind. Name or point to the AB pair once. Offer the remaining A and B together and ask what comes next; do not supply the answer immediately.",
        "steps": ["Look along A-B-A-B. Choose the next piece from the adult's A and B choices, or point for the adult to place it.", "If it continues the pattern, say or point to the AB part that repeats. No color names are needed.", "One extension is enough. You can watch, stop or help the adult collect the blocks; no need to keep repeating."],
        "parent_label": "Rescue and cleanup",
        "parent": "If B is chosen, point to the first AB pair and compare the second; offer one supported retry. Then end or match two alike with the adult. Matching is not a completed repeating pattern. No response is a reason to watch or end, not drill or assess. Adult collects and stores all blocks. Duration and mess are not measured.",
        "sources": [("DREME: repeating units and concrete objects", "https://preschoolmath.stanford.edu/toolkit/patterns-at-a-glance/"), ("DREME: next-piece choices and pointing", "https://prek-math-te.stanford.edu/patterns-algebra/pattern-and-algebra-assessment-protocols"), ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources checked October27,2026. Repeated units, concrete objects, next-piece choices and pointing are source-backed. The six-piece, two-unit starter, adult roles, one-extension limit, retry, matching alternative and stop rules are Kid Activity Lab editorial adaptations, not a tested setup. DREME's assessment context is not our child assessment; source age labels and examples do not establish individual readiness. Owned material fit, understanding, enjoyment, learning, duration, mess and safety outcomes are unknown. No clinical rule, product recommendation or safety assurance.",
    },
    "measuring-tape-jumps": {
        "title": "Toy Distance Marks",
        "url": "../cards/measuring-tape-jumps.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check gentle placement and pointing",
        "mess_label": "Mess not measured",
        "help_label": "Adult prepares and removes tape",
        "materials": "1 intact lightweight owned nonmagnetic block with no small or detachable parts, 1 large flat cardboard board, owned painter's tape handled by the adult",
        "best_for": "comparing two marked gaps from one common starting edge",
        "readiness_groups": [
            ("Materials", "Check block labels, condition and fit for every reachable child. Adult handles tape, follows its instructions and must test a hidden spot. Skip incompatible surfaces; cardboard is not guaranteed damage-free."),
            ("Adult and space", "Adult stays beside every reachable child. Board stays flat on a stable level table away from edges, with marks visible and room beside each."),
            ("Fit or skip", "Gently lift and place, point for the adult or watch. No counting or color naming needed. Skip for mouthing, poor visibility or unavailable attention."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. Layout and controls are editorial choices, not tested protection."),
        ],
        "stop": "Stop for loose, chewed or wrapped tape, mouthing or throwing the block, discomfort, surface change or shifted attention. No child jumping, toy jumping, rolling or launching.",
        "adult_setup": "Lay three short parallel strips along the board: start, nearer destination, farther destination. Leave room beside each for the block. Point to the start-strip edge facing the destinations and each destination edge facing start. These facing edges define the two gaps; the block is only a pretend toy marker.",
        "steps": ["Lift the block and gently place it beside the nearer destination mark, or point for the adult.", "Move it by hand beside the farther mark. Compare both gaps from the same named starting edge.", "Say or point: nearer, farther or unclear. One comparison is enough; you can watch or finish."],
        "parent_label": "Rescue and cleanup",
        "parent": "If judging is unclear, adult points along each gap once. Then watch or end; no repeats are needed. Do not add a launcher or force an answer. Adult removes and collects every tape strip, stores the block, tape and board, and clears the table. Duration and mess are not measured.",
        "sources": [("Learning Trajectories: visual distance comparison", "https://www.learningtrajectories.org/math-activities/frog-jump-measure"), ("DREME: comparison versus consistent-unit measurement", "https://preschoolmath.stanford.edu/toolkit/measurement-at-a-glance/"), ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx"), ("FrogTape: surface guidance and hidden-area checks", "https://www.frogtape.com/how-to-use/painters-tape")],
        "source_note": "Sources checked October27,2026. Common-reference visual comparison and toy-label and tape-surface checks are source-backed. The hand-placed block, cardboard board, three-strip layout, facing-edge instructions, roles and stop rules are Kid Activity Lab editorial adaptations, not an inspected source procedure or a tested setup. Learning Trajectories uses specific frog hoppers and later equal units; neither is used here. This is qualitative gap comparison, not a measured jump or numerical measurement. Source age labels, examples and assessment context do not validate individual readiness or our arrangement. Owned material fit, adhesion, understanding, enjoyment, learning, duration, mess and safety outcomes are unknown. No product recommendation, clinical rule or safety assurance.",
    },
    "balance-scale-baskets": {
        "title": "Cup Balance Watch",
        "url": "../cards/balance-scale-baskets.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Watch or point without touching",
        "mess_label": "Mess not measured",
        "help_label": "Adult assembles, holds and loads",
        "materials": "1 intact owned plastic hanger with symmetric notches, 2 matching paper cups, yarn, adult scissors and hole punch, 2 intact lightweight owned nonmagnetic objects that fit inside the cups",
        "best_for": "noticing cup positions in an adult-held balance, not measuring weight",
        "readiness_groups": [
            ("Materials", "Adult checks hanger, cup rims, yarn and attachments. Check object labels, condition and fit for every reachable child; no small detachable parts, coins, beans, marbles or loose fillers. If materials or retention are uncertain, skip; do not improvise a mount."),
            ("Adult and space", "Adult handles all tools, yarn, hanger and loads over a clear level floor. Child watches or points from beyond reach of yarn, hanger and moving cups. Skip if you cannot maintain this separation and attend to every reachable child. No child handling, body wrapping, pulling or climbing."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab. Adult roles and controls are editorial choices, not tested protection. Watching or declining is enough; no counting or spoken answer needed."),
        ],
        "stop": "End for reaching, pulling, mouthing, throwing, loose knots, torn rims, bending, swinging, contact, discomfort or shifted attention. Lower cups onto the floor before handling; never leave the assembly hanging unattended.",
        "adult_setup": "Away from children, adult makes two opposite holes about 1 inch below each cup rim and cuts two equal yarn pieces about 1 foot (30 cm) long. Tie each end through an opposite hole to make a handle. Put one handle on each notch, equally far from center and with equal hanging lengths. Inspect knots and rims; skip damage or insecure attachment. Adult alone holds the central hook without pinning the bar level, low over the floor with cups hanging free, not touching each other or the floor. Start EMPTY and let motion settle. If cups are uneven, touching, binding or unclear, lower them to rest on the floor and end. No door, cabinet, pencil or book supports.",
        "steps": ["Adult rests both cups on the floor before adding at most one checked object to each. Child watches from beyond reach.", "Adult lifts by the central hook and lets motion settle. Point or say: left lower, right lower, roughly level or unclear. Do not force a balance or an answer.", "One observation is enough. Adult lowers both cups onto the floor before removing anything. Roughly level is not proof of equal weight; this homemade balance is uncalibrated."],
        "parent_label": "Rescue and cleanup",
        "parent": "Unclear or uneven? End rather than add counterweights or repeat. Adult removes objects with cups resting on the floor, disassembles the yarn handles, stores ALL yarn, hanger, tools, cups and objects out of reach, and clears the floor. Duration, effort and mess are not measured.",
        "sources": [("PBS SoCal: matching cups and yarn handles", "https://www.pbssocal.org/education/family-math-activity-make-a-balance-scale"), ("PBS/MPT: symmetric cups and central support (page 5)", "https://d43fweuh3sg51.cloudfront.net/media/media_files/c6b12008-91f2-412d-9284-086b727071af/a1235226-67e6-45a0-8cb8-e8fe2aeee299.pdf#page=5"), ("PBS: empty cups level before comparison", "https://www.pbs.org/parents/crafts-and-experiments/balancing-nature"), ("AAP: owned toy labels and parts", "https://www.healthychildren.org/English/safety-prevention/at-home/Pages/how-to-buy-safe-toys.aspx")],
        "source_note": "Sources checked October27,2026. Matching cup handles, symmetric hanging lengths and central support, and an empty-level check are source-backed. We use the PBS SoCal handle construction, not PBS's different threaded loop. Adult-only roles, low floor setup, supported loading, one object per cup and stop rules are Kid Activity Lab editorial adaptations, not a tested setup. Construction lengths are nominal, not safety thresholds or load ratings. We exclude source door/book mounts, child handling, small loads and measurement games. This is an uncalibrated observation, not numeric weighing or proof of equal mass. Source age labels do not establish readiness. Owned strength, attachment, grip behavior, fit, understanding, enjoyment, learning, duration, mess and safety outcomes are unknown. No product recommendation, clinical rule or safety assurance.",
    },
    "color-mixing-cups": {
        "title": "Color Mixing Cups",
        "url": "../cards/color-mixing-cups.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check readiness first",
        "mess_label": "Mess not measured",
        "help_label": "Adult mixes; child notices",
        "materials": "3 clear nonbreakable cups, water, owned red and yellow food coloring, 1 adult spoon, 1 rimmed tray, 1 towel",
        "best_for": "noticing whether two prepared colors look different after an adult mixes them",
        "readiness_groups": [
            ("Materials", "Use intact clear nonbreakable cups and owned food coloring only as its labels permit. No paint, cleaning dye or other chemicals. Adult handles coloring, caps, spoon and liquids; keep supplies away. No tasting or contact with mouths or eyes."),
            ("Adult and space", "Use a stable level surface away from edges and walking routes. Keep the tray beyond every child's reach but visible. Stay beside every reachable child and control all materials throughout; this is not independent play."),
            ("Fit or skip", "Try only when every child can watch with hands away and respond to a stop cue. Pointing or describing is optional. Skip for mouthing, reaching, unwanted color play, unsuitable labels or personal constraints, unclear source colors or unavailable adult attention."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab."),
        ],
        "stop": "End and collect if a child reaches for materials, mouths them, liquid spills, anyone is uncomfortable or adult attention shifts.",
        "adult_setup": "Away from children, prepare a little red-tinted water in one cup and yellow-tinted water in another, following the coloring labels. Do not fill cups to the top. Store coloring and caps away. Put both cups and a third empty receiving cup on the rimmed tray, with the towel ready. Check the source colors look distinct and the receiver has room for two small spoonfuls; otherwise skip.",
        "steps": ["Look at the two source cups. Point to red or yellow if you want.", "Watch the adult put one small spoonful of yellow water, then one of red, into the empty receiving cup and gently mix once.", "Look at the mixture beside the source cups. Say or point: different, the same or unclear. Naming a color is optional; finish whenever you want."],
        "parent_label": "Rescue and cleanup",
        "parent": "If the change is unclear or watching is unwanted, end. Do not keep adding dye or pour full cups together to force a result. Adult immediately empties and rinses all three cups and the tray at a sink out of children's reach, dries the work area, and stores the cups, spoon and supplies. Leave no accessible standing water. Duration, mess and staining have not been measured.",
        "sources": [("PEEP: separate red-yellow sources and observation", "https://www.peepandthebigwideworld.com/en/educators/curriculum/family-child-care-educators/color/activity/guided-activity/101/mixing-food-coloring-red-and-yellow/"), ("PBS: receiving containers and uncertain predictions", "https://www.pbs.org/parents/crafts-and-experiments/testing-hypotheses-while-color-mixing"), ("AAP: water reach and immediate emptying", "https://www.healthychildren.org/English/safety-prevention/at-play/Pages/Infant-Water-Safety.aspx")],
        "source_note": "Sources checked October27,2026. PEEP uses classroom tray compartments and child-handled tools; PBS uses more containers and a recording chart. Separate sources and a mixing destination are source-backed. The three-cup adult-only spoon reduction, labels, placement, script, skip/stop and cleanup are Kid Activity Lab editorial adaptations, not a tested setup. AAP gives general water guidance, not dye or cup certification. No source image proves this arrangement or capacity. Owned material suitability, hygiene, actual shade, visibility, staining, family understanding, enjoyment, learning and safety are unknown. No measured timing, medical advice, product recommendation or safety assurance.",
    },
    "sound-shaker-match": {
        "title": "Sound Shaker Match",
        "url": "../cards/sound-shaker-match.html",
        "ages": "4-6",
        "time": "Not measured",
        "time_label": "Time not measured",
        "mess": "Not measured",
        "mess_label": "Mess not measured",
        "help": "medium",
        "help_label": "Adult stays beside child",
        "materials": "4 opaque lidded containers, rice, dry pasta (adult fills)",
        "best_for": "listening for matching sounds",
        "start_cue": "Keep filler and shakers out of younger children's reach; stay beside the player. Skip if lids or reach are uncertain, or the player opens lids or cannot follow a stop cue. Stop and collect pieces if a lid opens, a container cracks or filler spills. Not family-tested by Kid Activity Lab.",
        "adult_setup": "Away from children, put the same small amount of rice in two opaque lidded containers and the same amount of dry pasta in two more; close and check every lid.",
        "steps": ["Shake one closed container.", "Shake another and listen.", "Set two that sound alike together.", "Unsure? Compare just two again with your adult."],
        "parent": "The adult puts all containers and remaining filler away after play.",
        "kicker": "Sound matching | Editorial ages 4-6",
        "description": "Compare matching sounds in four adult-prepared closed containers. Research-backed idea; this home version has not been family-tested by Kid Activity Lab.",
        "sources": [
            ("NAEYC sound-pair example", "https://www.naeyc.org/resources/pubs/tyc/oct2015/10-unique-dollar-store-finds"),
            ("AAP small-object guidance", "https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"),
        ],
        "source_note": "NAEYC describes a preschool sound-matching game; AAP gives general small-object and younger-child reach guidance. The four-container home setup, closure check and stop sequence are KAL editorial choices, not a tested safety method. Time, mess, enjoyment, learning and physical outcomes are unknown.",
    },
    "ball-maze-box": {
        "title": "Ball Maze Box",
        "url": "../cards/ball-maze-box.html",
        "ages": "4-6",
        "time": "8 min",
        "mess": "low",
        "help": "medium",
        "materials": "box lid, blocks, ping-pong ball",
        "best_for": "planning, slopes, hand control",
        "steps": ["Put blocks in a lid.", "Add a ball.", "Tilt the maze.", "Move one wall."],
        "parent": "Use a large ball and avoid marbles.",
    },
    "water-drop-race": {
        "title": "Water Drop Tilt",
        "url": "../cards/water-drop-race.html",
        "ages": "4-6",
        "time": "Open-ended",
        "mess": "Not measured",
        "help": "adult-guided",
        "age_label": "Check grip and readiness",
        "mess_label": "Mess not measured",
        "help_label": "Adult steadies the tray",
        "materials": "1 shallow nonbreakable rimmed tray, 1 wax-paper piece, owned tape, 1 adult dropper, 1 small water cup, plain unheated water, 1 towel",
        "best_for": "noticing whether one water drop moves when a supported tray tilts",
        "readiness_groups": [
            ("Materials", "Adult checks intact tray and dropper and the owned tape's labels. Adult handles tape, dropper, cup and spares; keep them out of children's reach. No straw, blowing, dye, toothpick or tasting."),
            ("Adult and space", "Use a stable level table away from edges, electronics and walking routes. Adult stays beside every reachable child and steadies the far rim throughout. Child holds the near rim with both hands; the far edge stays on the table."),
            ("Fit or skip", "Try when the child can make a small supported move with help and follow a stop cue. Watching or pointing while the adult tilts is optional; adult holds both rims for this route. Skip if mouthing, grip, paper attachment, drop visibility or attention does not fit."),
            ("Evidence", "Research-backed, not family-tested by Kid Activity Lab."),
        ],
        "stop": "Lower the tray flat and end if paper loosens, the whole tray lifts off the table, grip slips, water escapes, a child reaches for tools or mouths materials, anyone is uncomfortable or attention shifts.",
        "adult_setup": "Fit a wax-paper piece flat inside the dry tray's rim. Adult tapes its dry edges down and checks it stays attached. Use the dropper to place one plain water drop near the middle. Skip if it soaks in or no bead is visible. Put the cup, dropper and spare materials out of reach, with the towel ready. Check adult and child can hold the named rims while one edge stays supported; otherwise watch only or skip.",
        "steps": ["Find the drop. Adult steadies the far rim; hold the near rim with both hands, or watch.", "With adult help, lift the near edge a little while the far edge stays on the table. Then lower it flat.", "Say or point: moved, stayed or unclear. If it moved, try one more small tilt or finish. Otherwise end; this is not a timed race."],
        "parent_label": "Rescue and cleanup",
        "parent": "If the drop stays put or movement is unclear, flatten the tray and end. Do not add more water or bring back mouth tools to force a result. Adult immediately empties the tray and water cup at a sink out of children's reach, collects the paper and tape, dries the tray and work area, and stores the tray, dropper and supplies. Leave no accessible standing water. Duration and mess have not been measured.",
        "sources": [("Science World: water drops and tilt alternative", "https://www.scienceworld.ca/resource/water-drop-races/"), ("PBS: wax paper on a tray and tilting", "https://www.pbs.org/parents/crafts-and-experiments/experiment-with-water-drops"), ("Boston Children's Museum: paper support, dropper and cleanup", "https://resourcehub.bostonchildrensmuseum.org/resources/squeeze-it")],
        "source_note": "Sources checked October27,2026. Science World and PBS explicitly offer tilting; Boston describes taped wax paper, dropper use, supervision and emptying water. The one-drop secured shallow-tray reduction, plain water, adult-only tools, hand placement, supported edge, fit/stop and rescue are Kid Activity Lab editorial adaptations, not a tested setup. Source educator-testing, age labels, photos and timing do not validate this arrangement or child fit. Owned material suitability, adhesion, grip, visibility, drop motion, hygiene, family understanding, enjoyment, learning and safety are unknown. No measured timing, breath training, clinical rule, product recommendation or safety assurance.",
    },
}


ACTIVITIES["blanket-river"]["start_cue"] = (
    ACTIVITIES["blanket-river"]["fit_cue"] + " Stop: " + ACTIVITIES["blanket-river"]["stop"]
)
ACTIVITIES["box-garage"]["fit_cue"] = " ".join(
    text for _, text in ACTIVITIES["box-garage"]["readiness_groups"]
)
ACTIVITIES["box-garage"]["start_cue"] = (
    ACTIVITIES["box-garage"]["fit_cue"] + " Stop: " + ACTIVITIES["box-garage"]["stop"]
)
ACTIVITIES["shadow-shape-match"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["shadow-shape-match"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["shadow-shape-match"]["stop"]
ACTIVITIES["ice-melt-rescue"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["ice-melt-rescue"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["ice-melt-rescue"]["stop"]
ACTIVITIES["color-mixing-cups"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["color-mixing-cups"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["color-mixing-cups"]["stop"]
ACTIVITIES["water-drop-race"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["water-drop-race"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["water-drop-race"]["stop"]
ACTIVITIES["ramp-texture-test"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["ramp-texture-test"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["ramp-texture-test"]["stop"]
ACTIVITIES["wind-tower-test"]["fit_cue"] = " ".join(
    text for _, text in ACTIVITIES["wind-tower-test"]["readiness_groups"]
)
ACTIVITIES["wind-tower-test"]["start_cue"] = (
    ACTIVITIES["wind-tower-test"]["fit_cue"] + " Stop: " + ACTIVITIES["wind-tower-test"]["stop"]
)
ACTIVITIES["pattern-path"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["pattern-path"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["pattern-path"]["stop"]
ACTIVITIES["measuring-tape-jumps"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["measuring-tape-jumps"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["measuring-tape-jumps"]["stop"]
ACTIVITIES["balance-scale-baskets"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["balance-scale-baskets"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["balance-scale-baskets"]["stop"]
ACTIVITIES["spoon-transfer"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["spoon-transfer"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["spoon-transfer"]["stop"]
ACTIVITIES["tube-sculpture"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["tube-sculpture"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["tube-sculpture"]["stop"]


ACTIVITIES["lego-color-tower"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["lego-color-tower"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["lego-color-tower"]["stop"]


ACTIVITIES["tape-train-tracks"]["adult_setup"] = " ".join(
    text for _, text in ACTIVITIES["tape-train-tracks"]["adult_setup_groups"]
)
ACTIVITIES["tape-train-tracks"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["tape-train-tracks"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["tape-train-tracks"]["stop"]


ACTIVITIES["block-tower"]["fit_cue"] = " ".join(
    text for _, text in ACTIVITIES["block-tower"]["readiness_groups"]
)
ACTIVITIES["block-tower"]["start_cue"] = (
    ACTIVITIES["block-tower"]["fit_cue"] + " Stop: " + ACTIVITIES["block-tower"]["stop"]
)
ACTIVITIES["block-tower"]["adult_setup"] = " ".join(
    text for _, text in ACTIVITIES["block-tower"]["adult_setup_groups"]
)


ACTIVITIES["tape-city"]["start_cue"] = " ".join(
    text for _, text in ACTIVITIES["tape-city"]["readiness_groups"]
) + " Stop: " + ACTIVITIES["tape-city"]["stop"]
ACTIVITIES["tape-city"]["adult_setup"] = " ".join(
    text for _, text in ACTIVITIES["tape-city"]["adult_setup_groups"]
)


PAGES = [
    {
        "path": "ages/activities-for-3-year-olds-at-home.html",
        "page_type": "age",
        "primary": "activities for 3 year olds at home",
        "title": "Activities for 3 Year Olds at Home | Kid Activity Lab",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 48px); } }",
        "h1": "Activities for 3 year olds at home.",
        "kicker": "Age 3",
        "description": "Low-prep activities for 3 year olds at home using blocks, tape, cups, paper rolls, toy cars, and household materials.",
        "intro": "Three year olds usually do best with short, visible steps and activities that can be reset quickly. These picks avoid long craft instructions and start with things you probably already have out.",
        "tip": "Use each activity's checks before starting. Block Tower is adult-guided: the adult checks, models and stays beside every reachable child.",
        "activities": ["cup-tower", "cardboard-car-ramp", "tape-road", "paper-roll-drop", "duplo-games", "block-tower", "magnetic-tile-house", "sock-ball-roll"],
        "related": ["games for 3 year olds at home", "fun activities for 3 year olds at home", "indoor activities for 3 year olds at home"],
    },
    {
        "path": "ages/activities-for-4-year-olds-at-home.html",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 48px); } }",
        "page_type": "age",
        "primary": "activities for 4 year olds at home",
        "title": "Activities for 4 Year Olds at Home | Kid Activity Lab",
        "h1": "Activities for 4 year olds at home.",
        "kicker": "Age 4",
        "description": "Easy activities for 4 year olds at home: building, pretend play, ramps, tape roads, blocks, magnetic tiles, and low-mess STEM prompts.",
        "intro": "Four year olds can handle a little more planning: make a road, test a ramp, build a bridge, or set up a tiny city. Keep the activity small enough that the child still owns the work.",
        "tip": "If you need one activity now, choose the cardboard ramp. If your child wants a challenge, open the original age-4 STEM test pack. Tape City first needs the road guide's surface checks and adult tape handling; quietness, mess and setup time are not measured. Magnetic Tile Builds is paused; read its different checked choices or decline, not a wall or roof start.",
        "chooser_title": "Start here by parent situation",
        "chooser_label": "Age 4 at-home chooser",
        "chooser": [
            ("A checked car-ramp start fits", ("Cardboard ramp parent guide", "../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start"), "Read owned-material and adult checks first; setup, play and cleanup time are not measured."),
            ("I want a 5-10 minute STEM challenge", ("Original age-4 STEM test pack", "../collections/original-stem-activities-for-4-year-olds.html"), "Five activities with parent jobs, kid steps, safety notes, and stop rules."),
            ("I want more STEM choices", ("STEM activities for 4 year olds", "../ages/stem-activities-for-4-year-olds.html"), "A broader chooser for ramps, bridges, shadows, towers, and water tests."),
            ("I want a pretend place", "Tape City; Magnetic Tile Builds is paused", "Tape City starts with checked tape/surface and one optional flat block; adult stays. Quietness, mess and setup time are not measured. Magnetic Tile Builds offers DIFFERENT checked choices, not this standing or two-room job."),
        ],
        "activity_overrides": {
            "car-ramp-distance-test": {
                "title": "Cardboard ramp for toy cars",
                "url": "../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start",
                "link_text": "Open ramp parent guide at the checked start",
                "suppress_late_link": True,
            },
            "paper-bridge": {
                "title": "Bridge Rescue paper bridge",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#bridge-rescue",
                "link_text": "Open in original STEM test pack",
            },
        },
        "after_activity_sections": [
            {
                "title": "When to choose the original STEM pack",
                "body": "Use the original age-4 STEM pack when you want the activity to have a clear test: roll farther, build stronger, make a bigger shadow, survive wind, or carry more cargo. Use the quick cards when you just need one screen and a fast start.",
            }
        ],
        "activities": ["tape-city", "car-ramp-distance-test", "paper-bridge", "magnetic-tile-ideas", "tape-train-tracks", "lego-color-tower", "spoon-transfer", "box-garage"],
        "related": ["games for 4 year olds at home", "educational activities for 4 year olds at home", "indoor activities for 4 year olds at home"],
    },
    {
        "path": "ages/activities-for-5-year-olds-at-home.html",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 48px); } }",
        "page_type": "age",
        "primary": "activities for 5 year olds at home",
        "title": "Activities for 5 Year Olds at Home | Kid Activity Lab",
        "h1": "Activities for 5 year olds at home.",
        "kicker": "Age 5",
        "description": "Screen-free activities for 5 year olds at home with quick building challenges, measuring games, fine motor practice, and pretend play.",
        "intro": "Five year olds are ready for simple challenges: test, compare, rebuild, and explain what changed. These activities stay low-prep but add just enough problem solving to feel bigger.",
        "tip": "Ask one question: What changed when you moved it, folded it, stacked it, or tried again?",
        "activities": ["car-ramp-distance-test", "paper-plate-ramp", "paper-bridge", "tube-sculpture", "lego-color-tower", "tape-city", "magnetic-tile-ideas", "blanket-river"],
        "related": ["games for 5 year olds at home", "educational activities for 5 year olds at home", "fun activities for 5 year olds at home"],
    },
    {
        "path": "ages/activities-for-6-year-olds-at-home.html",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 48px); } }",
        "page_type": "age",
        "primary": "activities for 6 year olds at home",
        "title": "Activities for 6 Year Olds at Home | Kid Activity Lab",
        "h1": "Activities for 6 year olds at home.",
        "kicker": "Age 6",
        "description": "At-home activities for 6 year olds: quick STEM builds, toy car tests, paper bridges, LEGO/DUPLO challenges, and indoor rainy-day play.",
        "intro": "Six year olds often want a real challenge, not a baby activity. These picks keep setup simple while adding measuring, comparing, planning, and redesigning.",
        "tip": "For this age, turn each activity into a challenge: make it taller, farther, stronger, slower, or quieter.",
        "activities": ["car-ramp-distance-test", "paper-bridge", "tube-sculpture", "tape-city", "lego-color-tower", "paper-plate-ramp", "magnetic-tile-ideas", "box-garage"],
        "related": ["games for 6 year olds at home", "educational activities for 6 year olds at home", "homeschool activities for 6 year olds"],
    },
    {
        "path": "collections/no-prep-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "no prep activities for preschoolers",
        "title": "No Prep Activities for Preschoolers | Kid Activity Lab",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 43px); } }",
        "h1": "No-prep activities for preschoolers.",
        "kicker": "No prep",
        "description": "No-prep preschool activities parents can start quickly with household items: cups, blocks, toy cars, tape, socks, books, and cardboard.",
        "intro": "This page is for the moment when you need something now. The activities use visible materials, short steps, and quick cleanup. No printable, no long supply list, no complicated craft setup.",
        "tip": "Choose what is already out, then read its adult-role checks. Block Tower is an adult-guided small start; its duration and mess are not measured.",
        "activities": ["cup-tower", "block-tower", "cardboard-car-ramp", "sock-ball-roll", "tape-road", "paper-roll-drop", "duplo-games", "magnetic-tile-house", "spoon-transfer"],
        "related": ["easy no prep activities for kids", "no prep activities for toddlers", "no prep activities for kids"],
    },
    {
        "path": "collections/indoor-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "indoor activities for preschoolers",
        "title": "Indoor Activities for Preschoolers: Choose by Moment | Kid Activity Lab",
        "h1": "Indoor activities for preschoolers.",
        "kicker": "Choose for this moment",
        "description": "Choose an indoor activity for a preschooler by space, materials, energy, and adult role, with clear setup, rescue, stop, and parent checks.",
        "intro": "The useful question is not how many ideas you can collect. It is what fits this child, this room, and this moment. Start with one bounded choice, then use the rescue or stop instead of forcing it.",
        "indoor_layout": True,
        "tip": "Adult clears and watches one short floor lane. Skip if you cannot attend to every child who can reach it. Roll one soft sock ball toward a nearby low basket, not over its rim; walk to reset. Stop for throwing, running or anyone entering the lane. Check the local fit and stop note before starting.",
        "evidence_note": "This chooser reconciles current extension, education, and publisher sources with Kid Activity Lab editorial guidance. Kid Activity Lab has not family-tested these setups. Fit, timing, mess, engagement, enjoyment, learning, repeatability, and safety outcomes are unknown.",
        "readiness_note": "Check every child who can reach the setup, not only the intended preschooler. Clear one defined area away from stairs, doors, pets, breakable objects, and active walkways. Remove damaged materials. If any child may mouth a piece, use larger solid materials, stay within reach, and watch continuously. Choose the direct supervision and stopping point the actual room and child require.",
        "image": {
            "src": "../assets/preschool-indoor/indoor-moment-chooser.webp",
            "alt": "Illustrated indoor activity zones with rolled socks and a basket, a short paper path, a low toy-car ramp, a block home, and playing cards",
            "width": "1672",
            "height": "941",
            "caption": "Kid Activity Lab illustration of five indoor activity routes. It is not a family-test photo and does not show measured use.",
        },
        "chooser_title": "Choose by the moment you are in",
        "chooser_label": "Indoor preschool activity chooser by moment, space, and adult role",
        "chooser": [
            ("I need one thing now", ("Soft-Sock Target Roll", "#sock-target-roll"), "One short, clear floor lane; one sock ball and a low basket target", "Check fit, place the target, and stay beside the lane"),
            ("Movement needs a boundary", ("Paper Puddle Path", "#paper-puddle-path"), "A short clear strip of floor; large paper shapes and painter tape", "Test and secure the materials, then call one slow movement"),
            ("Pretend play sounds right", ("Tape Road Delivery", "#tape-road-delivery"), "A table or small floor square; painter tape and large toy vehicles", "Make one short route and name a delivery job"),
            ("A cause-and-effect project fits", ("Low Car Ramp", "#low-car-ramp"), "A clear floor patch; flat cardboard, thick books, and one toy car", "Check the cardboard and keep the ramp low and floor-level"),
            ("The child wants to build", ("Make a Toy Place", "#make-a-toy-place"), "A table or clear floor square; large blocks or small boxes and one large toy", "Offer a small material set and let the child decide the structure"),
            ("Big-floor pretend play fits", ("Blanket Toy Crossing", "#blanket-toy-crossing"), "A clear floor area; one flat blanket, large supports, and one toy", "Keep the route for the toy, not for feet or climbing"),
            ("We want a rule-based game", ("Standard-Deck Card Game Chooser", "../collections/card-games-for-kids.html"), "A table or clear floor area; standard cards and the players named by the game", "Choose a game by player count and manage the rules and ending"),
        ],
        "support_steps": [
            ("Define the footprint", "Name the one table, floor square, or short lane the activity may use. Keep doors and walkways open."),
            ("Give one child-facing job", "Say the next visible action: roll to the basket, cross the puddles, deliver the toy, or make a place."),
            ("Rescue by shrinking", "Move the target closer, use fewer pieces, shorten the path, or finish one wall. Do not add a bigger explanation."),
            ("Stop and clear", "Use the named stop, remove loose materials, and return the room to an ordinary walking space."),
        ],
        "rainy_rotation": [
            ("Move", "Choose the sock roll or the short paper path; keep the route bounded and walk to reset.", "#sock-target-roll"),
            ("Make or build", "Choose the low ramp or a toy place; offer one material set rather than a room-wide project.", "#low-car-ramp"),
            ("Quieter route", "Choose the tape-road delivery or a standard-deck game that fits the available players.", "#tape-road-delivery"),
        ],
        "indoor_starts": [
            {
                "slug": "sock-target-roll",
                "title": "Soft-Sock Target Roll",
                "job": "Move in one lane",
                "stop_before_action": True,
                "mission": "Roll one soft sock ball toward a nearby low basket. Touching the target is optional; do not try to roll over the rim.",
                "materials": ACTIVITIES["sock-ball-roll"]["materials"],
                "adult_role": ACTIVITIES["sock-ball-roll"]["adult_setup"],
                "steps": ACTIVITIES["sock-ball-roll"]["steps"],
                "rescue": ACTIVITIES["sock-ball-roll"]["parent"],
                "stop": "Stop for throwing, running, mouthing, a loose sock, discomfort, or anyone entering the lane.",
                "parent": "Clear a short floor lane away from stairs, doors, cords, breakables and walkways. Stay beside every child who can reach it; skip if you cannot watch them all. Try when the child can release along the floor and pause on request. Research-backed, not family-tested by Kid Activity Lab.",
                "url": "../cards/sock-ball-roll.html",
                "link_text": "Open the matching sock-roll card",
            },
            {
                "slug": "paper-puddle-path",
                "title": "Paper Puddle Path",
                "job": "Move inside a short footprint",
                "mission": "Travel across three or four large paper shapes using one movement the adult names.",
                "materials": "three or four large paper shapes, painter tape suitable for the local floor",
                "adult_role": "Test the tape, secure every shape flat, and keep the path short enough to supervise from one position.",
                "steps": ["Stand beside the first shape.", "Step onto each shape using the named movement.", "Walk around the path to reset."],
                "rescue": "Use two shapes within one easy step and ask for one crossing.",
                "stop": "Stop and clear the path if paper or tape lifts, the path slides, running starts, or the route reaches a doorway or walkway.",
                "parent": "Before making the path, check the floor and spacing yourself. If you cannot watch every child who can reach it and stay close enough to stop the route, skip this start.",
                "stop_before_action": True,
                "url": "https://extension.psu.edu/programs/betterkidcare/content-areas/environment-curriculum/activities/all-activities/active-play-for-rainy-days",
                "link_text": "See the source activity shape",
            },
            {
                "slug": "tape-road-delivery",
                "title": "Tape Road Delivery",
                "job": "Pretend in a small area",
                "mission": "Deliver one large toy vehicle from a start line to a home, shop, or garage.",
                "materials": "painter tape suitable for the local surface, one to three large toy vehicles",
                "adult_role": "Test the tape and make one short route inside a defined play area rather than across a walkway.",
                "steps": ["Choose where the delivery starts.", "Drive one vehicle to the named place.", "Return it to the start or choose one new delivery."],
                "rescue": "Use one straight tape strip and one vehicle.",
                "stop": "Stop if tape is peeled or mouthed, vehicles are thrown, or the road expands into an active walking route.",
                "parent": "Check the surface before and after taping, use large intact toys, and remove the route when play ends.",
                "url": "../cards/tape-road.html",
                "link_text": "Open the base tape-road card",
            },
            {
                "slug": "low-car-ramp",
                "title": "Low Car Ramp",
                "job": "Make and notice",
                "mission": "Roll one toy car down a low cardboard ramp, then change one support and roll again.",
                "materials": "flat cardboard, one or two thick books, one intact toy car",
                "adult_role": "Remove staples and rough cardboard, build on the floor, and keep the top support low.",
                "steps": ["Place the car at the top.", "Let it roll without pushing it toward a person.", "Change one book or the cardboard angle and roll again."],
                "rescue": "Use one book and one roll, then stop.",
                "stop": "Stop if the car is thrown, the books are pulled apart, the ramp becomes a step, or the setup moves toward stairs or furniture.",
                "parent": "Keep the route floor-level, away from faces and feet, and remove damaged cardboard or vehicles.",
                "url": "../articles/cardboard-box-car-ramp-preschoolers.html",
                "link_text": "Open the fuller car-ramp guide",
            },
            {
                "slug": "make-a-toy-place",
                "title": "Make a Toy Place",
                "job": "Build a quieter route",
                "mission": "Make a floor, wall, doorway, or roof that gives one large toy a place to be.",
                "materials": "six to ten large lightweight blocks or small empty boxes, one large toy",
                "adult_role": "Check the material condition, choose a table or floor square, and offer only the small set.",
                "steps": ["Put the toy where its place will be.", "Add one wall or boundary.", "Choose a doorway, roof, or second wall."],
                "rescue": "Place two blocks as a doorway and let the toy move through once.",
                "stop": "Stop if pieces are thrown, stacked overhead, climbed on, or moved into a walkway.",
                "parent": "Use intact pieces suitable for every child who can reach them; clear the structure from ordinary walking space after play.",
                "url": "../collections/building-activities-for-4-year-olds.html",
                "link_text": "Open nine preschool building choices",
            },
            {
                **ACTIVITIES["blanket-river"],
                "slug": "blanket-toy-crossing",
                "title": "Blanket Toy Crossing",
                "job": "Pretend with a floor boundary",
                "adult_role": ACTIVITIES["blanket-river"]["adult_setup"],
                "rescue": ACTIVITIES["blanket-river"]["parent"],
                "parent": ACTIVITIES["blanket-river"]["fit_cue"],
                "stop_before_action": True,
                "url": "../cards/blanket-river.html",
                "link_text": "Open the base blanket-river card",
            },
        ],
        "activities": ["tape-road", "sock-ball-roll", "blanket-river", "cardboard-car-ramp", "cup-tower"],
        "related": ["rainy day activities for preschoolers", "active indoor games for preschoolers", "indoor gross motor activities for preschoolers", "screen free activities for kids indoors"],
        "related_routes": [
            ("Preschool building chooser", "Choose a material and structure job when the child wants a deeper build.", "../collections/building-activities-for-4-year-olds.html"),
            ("Standard-deck card games", "Choose by player count, pace, matching, and adult rules support.", "../collections/card-games-for-kids.html"),
            ("No-prep preschool activities", "Choose from a broader set when visible household materials are the main constraint.", "../collections/no-prep-activities-for-preschoolers.html"),
        ],
        "sources": [
            ("ParentMap: Indoor Play Activities From a Preschool Teacher", "https://www.parentmap.com/things-to-do/indoor-play-activities-preschool-teacher/", "Publisher roundup used for low-stress parent-job and result-shape context; its teacher framing and family use do not become Kid Activity Lab evidence."),
            ("Brightwheel: Indoor Recess Games and Activities", "https://mybrightwheel.com/blog/indoor-recess", "Commercial education article used for active, quiet, and short-break category shape; classroom and product claims are not adopted."),
            ("Pre-K Pages: Indoor Recess Games and Activities", "https://www.pre-kpages.com/indoor-recess-games-and-activities-for-preschoolers/", "Teacher-oriented source used to identify group, music, and rule requirements that a home-facing chooser must surface."),
            ("Penn State Better Kid Care: Active Play for Rainy Days", "https://extension.psu.edu/programs/betterkidcare/content-areas/environment-curriculum/activities/all-activities/active-play-for-rainy-days", "University extension source for paper-puddle and bounded movement shapes; local space, readiness, and safety outcomes remain unmeasured."),
            ("Reach All Readers: Indoor Gross Motor Activities", "https://reachallreaders.com/indoor-gross-motor-activities/", "Used only for movement-subjob and candidate-shape context; old, affiliate, developmental, and safe-in-practice claims are not adopted."),
            ("PBS Kids for Parents: Rainy Day Activities", "https://www.pbs.org/parents/rainy-day-activities", "Broad publisher hub used to confirm that rainy day is a context spanning movement, making, games, and media rather than a second copy of indoor ownership."),
        ],
        "evidence": "KAL-RES-008 refreshed 36 Semrush US queries on 2026-08-04, preserved six explicitly incomplete cached Google samples with 82 accessible links, inspected nine ranking/source pages, and selected one existing indoor owner. Complete GSC queries and both candidate page rows remain unavailable.",
        "first_2_month_impression_expectation": "UNKNOWN; the existing URL has no public-safe GSC page baseline.",
    },
    {
        "path": "collections/independent-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "independent activities for preschoolers",
        "title": "Independent Activities for Preschoolers | Kid Activity Lab",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 43px); } }",
        "h1": "Independent activities for preschoolers.",
        "kicker": "Independent play",
        "description": "Independent preschool activity choices with parent setup and activity-specific adult involvement. Cup Tower and Box Garage are adult-guided, not hands-off activities.",
        "intro": "Independent does not mean unsupervised. Let the child choose and try actions while keeping the adult involvement the activity needs. Cup Tower below requires an adult beside the setup throughout, not just a quick demonstration. Box Garage also requires an adult to stay beside every reachable child.",
        "tip": "Start together and check the activity's adult role before choosing. For Cup Tower, stay beside every child who can reach the cups; skip it if you cannot attend to them. For Box Garage, choose the adult-guided one-car start or skip if you cannot stay beside it. Paper Roll Drop is adult-held throughout, not hands-off play; skip if attention or materials do not fit.",
        "activities": ["magnetic-tile-house", "magnetic-tile-ideas", "block-tower", "cup-tower", "duplo-games", "paper-roll-drop", "tape-road", "box-garage"],
        "activity_overrides": {
            "cup-tower": {
                "time": "Open-ended",
                "mess": "Not measured",
                "mess_label": "Mess not measured",
                "help_label": "Adult stays beside setup",
                "materials": "2 matching lightweight paper cups and 1 optional spare",
                "best_for": "an adult-guided small balance, not a hands-off choice",
                "start_cue": "Try when the child can place a cup gently and follow a stop cue. Adult checks intact cups and a firm low clear surface, away from edges and feet, and stays beside every child who can reach them. Keep spares out of younger children's reach; skip if you cannot attend. Stop after mouthing, throwing, damage, climbing or unwanted collapse. Research-backed, not family-tested by Kid Activity Lab.",
                "adult_setup": "Check that the matching cups can balance. Put one cup opening-down and demonstrate the other opening-up, with the two closed bottoms touching. Do not push one cup inside the other.",
                "steps": ["Adult puts one cup upside down.", "Set another bottom-to-bottom on it.", "Take the top cup off gently.", "Rebuild or try one change."],
                "parent": "If the cups will not balance, try a different matching pair or arrange a row instead. Lift cups off rather than forcing a collapse. Collect the set when done; adult removes damaged cups and loose pieces and stores the cups out of younger reach. Timing and mess have not been measured.",
                "url": "../articles/paper-cup-tower-kids.html",
                "link_text": "Full Paper Cup Tower guide",
                "link_before_steps": True,
            },
        },
        "related": ["independent work for preschoolers", "independent art activities for preschoolers", "independent learning activities for preschoolers"],
    },
    {
        "path": "collections/fine-motor-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "fine motor activities for preschoolers",
        "title": "Fine Motor Activities for Preschoolers | Kid Activity Lab",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 43px); } }",
        "h1": "Fine motor activities for preschoolers.",
        "kicker": "Fine motor",
        "description": "Fine motor activities for preschoolers using pom poms, paper rolls, blocks, tape, spoons, cups, and household objects.",
        "intro": "Fine motor practice does not have to look like worksheets. Preschoolers build hand strength and control while dropping, stacking, peeling, scooping, connecting, and balancing.",
        "tip": "Adult checks labels, condition and abilities for every child who can reach the materials. Unsuitable parts, mouthing, uncertain younger-child reach or unavailable attention mean choose another activity. Size or direct supervision is not permission to use unsuitable items.",
        "activities": ["paper-roll-drop", "pom-pom-drop", "spoon-transfer", "lego-color-tower", "duplo-games", "magnetic-tile-ideas", "cup-tower", "tape-road"],
        "related": ["fine motor activities for preschoolers at home", "fine motor activities for preschoolers pdf", "fine motor activities for preschoolers printables"],
    },
    {
        "path": "collections/stem-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "stem activities for preschoolers",
        "title": "STEM Activities for Preschoolers | Kid Activity Lab",
        "h1": "STEM activities for preschoolers.",
        "kicker": "Three ways into STEM",
        "description": "Compare three preschool STEM activities using common materials: change a shadow, test a paper bridge, or continue a repeating pattern.",
        "intro": "Choose the kind of question that fits what you have now: change a shadow, test a bridge, or continue a pattern. Each bounded start is complete on this page; the deeper routes carry the longer science, engineering, and math jobs.",
        "preschool_stem_layout": True,
        "head_style": "@media (max-width: 480px) { .preschool-stem-hero h1 { font-size: min(2.5rem, 43px); } }",
        "evidence_note": "This chooser combines current Head Start, TERC, Smithsonian Science in Pre-K, and NAEYC sources with Kid Activity Lab editorial guidance. Kid Activity Lab has not family-tested these setups. The activity selection, readiness cues, materials, scripts, substitutions, and stop points are editorial choices. Timing, mess, comprehension, engagement, enjoyment, learning, repeatability, frustration, and safety outcomes are unknown.",
        "image": {
            "src": "../assets/preschool-stem/preschool-stem-three-ways.webp",
            "alt": "Three illustrated preschool STEM material sets: a flashlight and large block facing a blank wall; a paper bridge across two closed books with a large plastic lid; and four alternating blue-and-yellow pieces with one loose blue piece ready to continue the pattern.",
            "width": "1672",
            "height": "941",
            "caption": "From left: science shadow materials, engineering paper-bridge materials, and math pattern materials. Kid Activity Lab AI-generated illustration; not a family-test photo or evidence of measured use or outcomes.",
        },
        "chooser_title": "Choose one way to investigate",
        "chooser": [
            {
                "lane": "Science",
                "action": "Change a shadow",
                "href": "#shadow-change",
                "summary": "Use a stable flashlight, one large object, and a blank wall.",
            },
            {
                "lane": "Engineering",
                "action": "Test a paper bridge",
                "href": "#paper-bridge-test",
                "summary": "Span two low closed books, test once, then fold once.",
            },
            {
                "lane": "Math",
                "action": "Continue a pattern",
                "href": "#continue-a-pattern",
                "summary": "Start A-B-A-B with two kinds of large pieces.",
            },
        ],
        "leads": [
            {
                "slug": "shadow-change",
                "lane": "Science | Observe a change",
                "title": "Shadow Builder",
                "mission": "Move one large object closer to and farther from the light to make one larger shadow and one smaller shadow.",
                "materials": "a flashlight, one large opaque block or household object, and a blank wall",
                "substitution": "No block is needed; use one large opaque household object that is easy to hold and does not break.",
                "readiness": "Use this start when the child can follow a one-step stop cue and move one large object while the light stays still. The adult operates the flashlight if the child points it toward people or cannot leave it stable.",
                "adult_role": "Put the flashlight on a stable surface pointing at the wall, dim only enough to see the shadow, and keep the walking path clear. Do not aim the light at a face.",
                "steps": [
                    "Put the object between the light and the wall.",
                    "Move the object closer to the light and notice the shadow.",
                    "Move it farther from the light and compare the two shadow sizes.",
                ],
                "stop": "Stop after the two contrasting shadows or sooner if the light will not stay pointed at the wall. Switch off the light and restore the walking path.",
            },
            {
                "slug": "paper-bridge-test",
                "lane": "Engineering | Build and test",
                "title": "Bridge Rescue",
                "mission": "Span the gap, test the flat paper, then fold the paper once and compare one stronger version if the first bends.",
                "materials": "one sheet of paper, two broad closed books, and one large lightweight object such as a block, plastic lid, or toy",
                "substitution": "Use a large lightweight plastic lid or block if no suitable toy is available. Keep the two closed books as the low supports.",
                "readiness": "Use this start when the child can place one sheet across a gap and release one light object without lifting, climbing on, or striking the books. The adult owns the supports and ends the setup if that boundary does not hold.",
                "adult_role": "Put one book flat on each side of a short floor-level gap and keep both supports low and stable. The child places the paper and tests one object.",
                "steps": [
                    "Lay the paper across the short gap.",
                    "Set the large light object on the middle, then lift it off.",
                    "If the paper bends, fold it once, span the gap again, and compare one more test.",
                ],
                "stop": "Stop after one flat and one folded test. End sooner if the books become climbing, throwing, or finger-trapping objects; return the books and paper when done.",
            },
            {
                "slug": "continue-a-pattern",
                "lane": "Math | Compare and continue",
                "title": "Pattern Path",
                "mission": "Add the next piece, say or point to the repeating part, and extend the path once.",
                "materials": "two colors or types of large blocks, tiles, household objects, or adult-prepared paper squares",
                "substitution": "Use any two visibly different kinds of large pieces that are appropriate for the youngest child who can reach them.",
                "readiness": "Use this start when the child can match two visibly different pieces and place one next item. If repeating is not yet manageable, switch to matching two alike pieces and do not call that result a completed pattern.",
                "adult_role": "Start an A-B-A-B sequence with four pieces, name the two parts once, and ask what comes next without supplying the answer immediately.",
                "steps": [
                    "Look across the four-piece A-B-A-B start.",
                    "Choose the piece that comes next and place it.",
                    "Say or point to the repeating part after placing the one next piece.",
                ],
                "stop": "Stop after one correct extension or one supported retry. Collect every loose piece at cleanup.",
            },
        ],
        "related_routes": [
            ("Science investigations", "Choose from light, water, motion, and other observable questions.", "../collections/science-experiments-for-4-year-olds.html"),
            ("Engineering challenges", "Choose a mission, run a visible test, and make one redesign.", "../collections/engineering-activities-for-4-year-olds.html"),
            ("Hands-on math", "Choose counting, pattern, measuring, sorting, or comparing activities.", "../collections/math-activities-for-4-year-olds-at-home.html"),
            ("Age-four STEM", "Choose a fuller activity route organized for the current age-four cluster.", "../ages/stem-activities-for-4-year-olds.html"),
        ],
        "legacy_routes": [
            ("Open the original age-four STEM pack", "../collections/original-stem-activities-for-4-year-olds.html"),
            ("Scan the activity-card library", "../cards.html"),
        ],
        "sources": [
            ("HeadStart.gov: Science Preschool", "https://headstart.gov/school-readiness/article/science-preschool"),
            ("TERC Head Start on Engineering: Everyday Engineering", "https://www.terc.edu/hse/everyday-engineering/"),
            ("Smithsonian Science in Pre-K: Light and Shadows", "https://scienceinprek.si.edu/open-exploration-light-and-shadows"),
            ("NAEYC: Two Mathematical Heads Are Better than One", "https://www.naeyc.org/resources/pubs/yc/fall2022/peer-based-math-learning"),
            ("NAEYC: The Intentional Teacher excerpt", "https://www.naeyc.org/sites/default/files/globally-shared/downloads/PDFs/resources/pubs/intentional-teacher-third-edition-chap-1-excerpt.pdf"),
        ],
        "activities": ["paper-bridge", "cardboard-car-ramp", "cup-tower"],
        "related": ["engineering activities for preschoolers", "science activities for preschoolers", "stem projects for preschoolers"],
    },
    {
        "path": "ages/stem-activities-for-4-year-olds.html",
        "head_style": "@media (max-width: 390px) { .hero h1 { font-size: min(2.6rem, 66px); } }",
        "page_type": "age",
        "primary": "stem activities for 4 year olds",
        "title": "STEM Activities for 4 Year Olds at Home | Kid Activity Lab",
        "h1": "STEM activities for 4 year olds.",
        "kicker": "Age 4 STEM",
        "description": "Choose simple STEM activities for 4 year olds at home, including low-mess ramps, bridges, shadows, towers, water tests, and the original age-4 STEM test pack.",
        "intro": "Four year olds learn STEM best when the question is visible: Will it roll farther? Will it float? Will the bridge hold? These activities keep the setup small and give the child something real to test.",
        "tip": "Use one question per activity: What do you think will happen, and what changed when we tried again?",
        "start_block": {
            "title": "Start with the original age-4 STEM test pack",
            "body": "The original test pack has parent jobs, read-aloud steps and stop rules. It is not family-tested by Kid Activity Lab; setup, play and cleanup times have not been measured. Age labels here are editorial, not permission to lower a toy's age requirement. Check materials and younger-sibling access before choosing; skip a setup you cannot supervise.",
            "link_text": "Open the original age-4 STEM test pack",
            "url": "../collections/original-stem-activities-for-4-year-olds.html",
        },
        "chooser": [
            ("I prefer a dry setup", "Ramp Detective or Shadow Builder", "Choose floor space for a car, or a clear wall with an adult-controlled light."),
            ("My child likes stories", "Bridge Rescue", "A checked block or soft toy crossing a pretend river gives the test a story; an adult can place it gently."),
            ("We have light blocks", "Windproof Tower", "Check labels and condition; an adult fans a low tower."),
            ("We can handle water", "Empty Foil Boat", "No cargo; an adult controls water and stays throughout."),
            ("My child wants to watch", "Shadow Builder", "The adult can move the object while the child points or watches."),
        ],
        "activity_overrides": {
            "car-ramp-distance-test": {
                "title": "Ramp Detective car test",
                "time": "Time not measured",
                "mess": "Not measured",
                "mess_label": "Dry setup; cleanup varies",
                "help_label": "Adult stays involved",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#ramp-detective",
                "link_text": "Open in original test pack",
                "guide_url": "../collections/original-stem-activities-for-4-year-olds.html#before-start",
                "guide_label": "Read original-pack material and stop checks before handling",
                "best_for": "one plain roll first; optional surface observation in Ramp Detective",
                "steps": ACTIVITIES["car-ramp-distance-test"]["steps"][:2] + ["For an OPTIONAL surface-change routine, use Ramp Detective in the original pack after its before-start checks. Adult selects and handles the towel or placemat, keeps car, ramp and release spot the same, and checks for slipping. A stuck, veering or unclear roll is a result; point, watch or end."],
            },
            "paper-bridge": {
                "title": "Bridge Rescue paper bridge",
                "time": "Time not measured",
                "mess": "Not measured",
                "mess_label": "Dry setup; cleanup varies",
                "help_label": "Adult stays involved",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#bridge-rescue",
                "link_text": "Open in original test pack",
                "materials": "paper, two low books, one large lightweight block or soft toy; check it for each child who can reach it",
                "best_for": "engineering, story play, watching paper bend",
                "steps": ["Set two low books flat, with a gap shorter than the paper.", "Lay paper across both book covers.", "Gently place one checked object and watch.", "Remove it; try one fold or stop."],
                "parent": "Stay close, with fingers clear underneath; an adult can place the object while a child watches. Stop for sliding books, torn or mouthed paper, thrown objects or climbing. If paper slips, remove the object, move books closer and check the empty bridge, or end. Collect materials when done.",
            },
            "shadow-shape-match": {
                "title": "Shadow Builder",
                # Keep this independently reviewed owner free of new compact-card fields.
                "adult_setup": "",
                "sources": [],
                "parent_label": "Parent check",
                "time": "Time not measured",
                "mess": "Not measured",
                "mess_label": "Dry setup; cleanup varies",
                "help_label": "Adult stays involved",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#shadow-builder",
                "link_text": "Open in original test pack",
                "best_for": "light, shapes, changing shadows",
                "start_cue": "Keep light on wall, not faces. Switch off if beam leaves wall.",
                "materials": "flashlight, one checked large opaque block, clear wall",
                "steps": ["Adult lights the wall.", "Child picks the checked block.", "Move it near the wall; look.", "Move it nearer the light; compare."],
                "parent": "Keep the light still and supervise. If it becomes the toy, switch it off and park it. Resume only if an adult can relight it and keep it steady on the wall; the child moves the block or watches the adult move it. Otherwise end and collect the materials.",
            },
            "wind-tower-test": {
                "title": "Windproof Tower",
                "time": "Time not measured",
                "mess": "Not measured",
                "mess_label": "Dry setup; cleanup varies",
                "help_label": "Adult stays involved",
                "materials": ACTIVITIES["wind-tower-test"]["materials"],
                "parent": ACTIVITIES["wind-tower-test"]["parent"],
                "url": "../collections/original-stem-activities-for-4-year-olds.html#windproof-tower",
                "link_text": "Open in original test pack",
                "best_for": ACTIVITIES["wind-tower-test"]["best_for"],
            },
            "foil-boat-test": {
                "title": "Empty Foil Boat",
                "url": "../cards/foil-boat-test.html",
                "link_text": "Open the empty-boat steps and diagram",
            },
        },
        "activities": ["car-ramp-distance-test", "paper-bridge", "foil-boat-test", "shadow-shape-match", "pattern-path", "wind-tower-test", "color-mixing-cups", "ramp-texture-test"],
        "related": ["easy stem activities for 4 year olds", "stem activities for 4 year olds at home", "science activities for 4 year olds"],
    },
    {
        "path": "collections/engineering-activities-for-4-year-olds.html",
        "page_type": "collection",
        "primary": "engineering activities for preschoolers",
        "title": "Engineering Activities for Preschoolers | Kid Activity Lab",
        "h1": "Engineering activities for preschoolers ages 4-6.",
        "route_label": "Engineering activities for 4 year olds",
        "kicker": "Preschool engineering | Ages 4-6",
        "description": "Choose preschool engineering activities and checked-card choices with paper, foil, blocks, cups, straws, and toy cars. Read each route's checks first.",
        "intro": "Pick a small problem, give the child a clear mission, test the build, and change one thing. These research-backed challenges use household materials and show the adult job without taking over the design.",
        "tip": "For Paper Bridge, choose a DIFFERENT stationary-object test, not a moving-car road. Read its adult, material and stop checks BEFORE handling, or decline.",
        "tip_link": ("Check the different paper-bridge choice", "#paper-bridge"),
        "image_warning": "The pictured car on folded paper is not the stationary-object start offered below. Do not copy that structure as instructions; check the different choice before handling.",
        "engineering_layout": True,
        "evidence_note": "Kid Activity Lab created this chooser from current source and search research. We have not family-tested these setups. The age range, adult roles, rescue steps, and first changes are editorial guidance; timing, mess, engagement, learning, repeatability, and safety outcomes are unknown.",
        "image": {
            "src": "../assets/preschool-engineering/engineering-challenge-materials.webp",
            "alt": "Paper bridge, foil boat, cup tower, box-lid maze, straws, and painter tape arranged as engineering challenge materials.",
            "width": "1672",
            "height": "941",
            "caption": "Illustration of possible materials, not a Kid Activity Lab family-test photo. The car on folded paper is not the different stationary-object test offered below; do not copy it as that setup.",
        },
        "chooser_title": "Choose by what is already out",
        "chooser_label": "Preschool engineering activity chooser",
        "chooser": [
            ("Paper, two low closed books and one suitable large block or soft toy", ("Different stationary Paper Bridge test", "#paper-bridge"), "Read this choice's checks before handling; adult stays. Not a moving-car road."),
            ("A tray can get wet", ("Empty Foil Boat", "#foil-boat-test"), "An adult stays beside the tray; try an empty hull, no cargo."),
            ("Blocks or cups are ready", [("Wind Tower", "#wind-tower-test"), ("Cup Doorway (paused)", "#cup-tower")], "Wind Tower: Keep the build low and run one gentle test. Cup Doorway is paused; read a different choice's checks before handling or decline."),
            ("Toy cars are the hook", [("Target Ramp", "#car-ramp-distance-test"), ("Box Garage", "#box-garage")], "Set the boundary or target; let the child decide the change."),
            ("Six whole paper straws, owned tape and two low closed books", ("Straw Bridge: empty first", "#straw-bridge"), "Adult joins and stays; read the card's checks before handling. No cup supports or required toy load."),
            ("A box lid, chunky blocks and suitable large ball", ("Ball Maze", "#ball-maze-box"), "Use Ball Maze's own checks; adult controls the ball while the child chooses the layout or points."),
        ],
        "process_steps": [
            ("Ask", "What must the build do?"),
            ("Imagine", "Name or draw more than one possible idea."),
            ("Plan", "Choose materials and one idea to try first."),
            ("Create and test", "Build it, then run the visible test."),
            ("Improve", "Change one part using what the test showed."),
        ],
        "activity_overrides": {
            "paper-bridge": {
                "slug": "paper-bridge",
                "title": "Paper Bridge",
                "paper_bridge_handoff": True,
                "steps": [],
            },
            "straw-bridge": {
                "slug": "straw-bridge",
                "title": "Straw Bridge",
                "straw_bridge_handoff": True,
                "steps": [],
            },
            "foil-boat-test": {
                "slug": "foil-boat-test",
                "title": "Empty Foil Boat",
                "materials": "foil, shallow tray, water, towel; no cargo",
                "mission": "Watch an empty foil boat: does it stay upright, lean or let water in?",
                "adult_role": "Set the tray on a stable wipeable surface with a towel beneath; control the water and stay beside it throughout. Open the linked folds and diagram before starting.",
                "steps": ["Raise all four foil edges; pinch corners without cutting.", "Adult lowers the empty boat and checks it floats clear of the tray bottom and sides.", "Watch, then ask the adult to lift it out before a change."],
                "link_text": "Open the empty-boat steps and diagram",
                "test": "Is it floating freely, rather than resting on the tray? No cargo-capacity test here.",
                "redesign": "Adult lifts and drains onto the towel; try raising one low edge or flattening an uneven bottom.",
                "rescue": "Replace torn foil or stop. If it cannot float freely in the shallow setup, choose a dry activity, not a deeper vessel.",
                "stop": "Stop for mouthing, torn foil, spills, a moving tray, lost attention or wanting to leave.",
                "parent": "Adult gathers foil, empties and stores the tray, and wipes spills before leaving. Shallow water still requires continuous adult supervision. Watching is an option; no family testing or safety outcome is claimed.",
            },
            "paper-chain-test": {
                "slug": "paper-chain-test",
                "title": "Paper Chain Reach Test",
                "materials": "pre-cut paper strips, painter tape, one book",
                "mission": "Build a paper chain long enough to wrap around the book and meet at the top.",
                "adult_role": "Pre-cut wide strips and hold the book still while the child joins loops.",
                "steps": ["Make and tape one paper loop.", "Thread each open strip through the last loop, then overlap and tape that strip's own ends.", "Wrap the chain around the book."],
                "link_text": "Open the linked-loop steps and diagram",
                "test": "Do the two ends meet without pulling a loop apart?",
                "redesign": "Add one loop or replace the narrowest loop with a wider strip.",
                "rescue": "Use a smaller book or start with three large loops already joined.",
                "stop": "Stop if tape or strips go in a mouth, the book tips, or joining loops has become an adult-only job.",
                "parent": "Keep scissors out of the play area and use a light book with rounded corners.",
            },
            "wind-tower-test": {
                "slug": "wind-tower-test",
                "title": "Wind Tower",
                "materials": ACTIVITIES["wind-tower-test"]["materials"],
                "mission": "Build low, then watch one adult fan test. The build may stay standing.",
                "adult_role": ACTIVITIES["wind-tower-test"]["adult_setup"],
                "steps": ACTIVITIES["wind-tower-test"]["steps"],
                "test": "Standing, moved, fell or unclear are all results; no collapse is required.",
                "redesign": "Only if wanted, make a lower or wider build using the same blocks and repeat from the same fan position with the same gentle waves. This is not calibrated force.",
                "rescue": ACTIVITIES["wind-tower-test"]["parent"],
                "stop": ACTIVITIES["wind-tower-test"]["stop"],
                "parent": ACTIVITIES["wind-tower-test"]["fit_cue"],
                "stop_before_action": True,
            },
            "car-ramp-distance-test": {
                "slug": "car-ramp-distance-test",
                "title": "Target Ramp",
                "materials": ACTIVITIES["car-ramp-distance-test"]["materials"],
                "mission": "Notice whether a car stops near a spot the adult points to; no target hit is required.",
                "adult_role": ACTIVITIES["car-ramp-distance-test"]["adult_setup"],
                "steps": ["Make one plain roll from the adult's starting spot WITHOUT pushing, or point for the adult.", "After the car stops, adult points to a nearby target spot from beside the lane, then moves the hand out before another roll. No tape or loose target object is needed.", "If wanted, release the SAME car again from the SAME spot on the SAME low setup. Watch where it stops or end."],
                "test": "Nearer, farther, beside the target, not off the ramp or unclear are observations, not speed measurements or a guaranteed hit.",
                "redesign": "Only after the car is collected, an adult may LOWER the support within the full guide's low, stable setup checks, then recheck before release. Do not add height, push harder or ask the child to move supports. If it will not stay stable, end.",
                "rescue": ACTIVITIES["car-ramp-distance-test"]["parent"],
                "stop": ACTIVITIES["car-ramp-distance-test"]["stop"],
                "parent": ACTIVITIES["car-ramp-distance-test"]["fit_cue"],
                "stop_before_action": True,
            },
            "ball-maze-box": {
                "slug": "ball-maze-box",
                "title": "Box-Lid Ball Maze",
                "materials": "shallow intact box lid, three chunky blocks, one large lightweight foam ball",
                "mission": "Make a path that lets the ball travel from one corner to the opposite corner.",
                "adult_role": "Choose pieces for every child who can reach the setup, keep the lid below face level, and stay beside it. The adult controls when the ball enters and leaves the lid.",
                "steps": ["Build a wide path with three chunky block walls.", "Ask the adult to place the ball in one corner.", "Tilt gently, then put the lid flat for the adult to remove the ball."],
                "test": "Can the ball reach the opposite corner without getting trapped?",
                "redesign": "Move one wall to open the place where the ball stopped.",
                "rescue": "Use only three walls and make a wide path first.",
                "stop": "Stop if the ball or a block goes in a mouth, is thrown, or leaves the clear area; if the lid is shaken or lifted near a face; or if any material is damaged.",
                "parent": "The adult keeps the ball and spare blocks out of reach between runs and removes the ball first at cleanup. This editorial setup is not a safety assurance.",
            },
            "box-garage": {
                "slug": "box-garage",
                "title": "Two-Car Box Garage",
                "materials": "already-open small box, 2 appropriate large lightweight toy cars, short painter-tape bay marks prepared by the adult",
                "mission": "Use two parking bays so one car can leave without moving the other. This is an optional extension to the one-car start.",
                "adult_role": "Set the open box on its side on clear floor with the opening unobstructed. Check both cars already fit side by side and one can leave without force. Adult tests and places the short bay tape, handles any adjustment and keeps spare tape away. If this does not fit, choose the one-car start; do not cut or widen the box during play.",
                "steps": ["Park both cars in the ready box.", "Point to the two adult-prepared bays and choose one car to leave.", "Roll that car out through the ready opening without moving the other."],
                "test": "Do both cars fit, and can one leave without hitting the other?",
                "redesign": "Ask the adult to adjust one bay mark, choose a different already-open box or return to one car. Never force an exit or cut during play.",
                "rescue": "Use the one-car start without bay tape, or park beside the box if the car catches. Adult removes tape and puts away both cars and the box after play; timing and mess are unmeasured.",
                "stop": ACTIVITIES["box-garage"]["stop"] + " Stop if tape loosens, goes in a mouth or cutting would be needed.",
                "parent": ACTIVITIES["box-garage"]["fit_cue"],
                "stop_before_action": True,
                "link_text": "Open the base activity card: one-car no-cut start",
                "sources": ACTIVITIES["box-garage"]["sources"] + [("PBS: parking-line spacing principle", "https://www.pbs.org/parents/crafts-and-experiments/cardboard-parking-garage")],
                "source_note": ACTIVITIES["box-garage"]["source_note"] + " PBS describes car-based line spacing in a multilevel painted/glued build, not this box. This two-car clearance extension and adult-prepared tape marks are KAL editorial choices, not tested geometry or tape performance.",
            },
            "cup-tower": {
                "slug": "cup-tower",
                "title": "Cup Doorway",
                "cup_doorway_pause": True,
                "steps": [],
            },
        },
        "activities": ["paper-bridge", "straw-bridge", "foil-boat-test", "paper-chain-test", "wind-tower-test", "car-ramp-distance-test", "ball-maze-box", "box-garage", "cup-tower"],
        "related": ["preschool engineering activities", "engineering activities for 4 year olds", "stem engineering activities for preschoolers"],
        "related_routes": [
            ("Building activities for 4 year olds", "Blocks, structures, and open-ended building play.", "../collections/building-activities-for-4-year-olds.html"),
            ("STEM activities for preschoolers", "A broader mix of science, math, engineering, and discovery.", "../collections/stem-activities-for-preschoolers.html"),
            ("STEM activities for 4 year olds", "Age-four routes across ramps, light, water, patterns, and structures.", "../ages/stem-activities-for-4-year-olds.html"),
        ],
        "sources": [
            ("TERC Head Start on Engineering: Everyday Engineering", "https://www.terc.edu/hse/everyday-engineering/"),
            ("HeadStart.gov: Exploring Engineering with Preschoolers", "https://www.headstart.gov/school-readiness/teacher-time-series/exploring-engineering-preschoolers"),
        ],
    },
    {
        "path": "collections/science-experiments-for-4-year-olds.html",
        "page_type": "collection",
        "primary": "science experiments for 4 year olds",
        "title": "Science Experiments for 4 Year Olds | Kid Activity Lab",
        "h1": "Science experiments for 4 year olds.",
        "kicker": "Science",
        "description": "Simple science experiments for 4 year olds using water, ice, shadows, colors, sound, ramps, and household materials.",
        "intro": "The strongest science experiments for 4 year olds are short and observable. The child should be able to predict, test, notice, and try again without waiting for a long result.",
        "tip": "Pick experiments where the result is easy to see: sinking, floating, melting, mixing, rolling, or making a sound.",
        "head_style": "@media (max-width: 480px) { .hero h1 { overflow-wrap: anywhere; } }",
        "activities": ["sink-or-float-tray", "ice-melt-rescue", "shadow-shape-match", "color-mixing-cups", "sound-shaker-match", "water-drop-race", "ramp-texture-test"],
        "related": ["easy science experiments for 4 year olds", "science activities for 4 year olds at home", "preschool science experiments"],
    },
    {
        "path": "collections/math-activities-for-4-year-olds-at-home.html",
        "page_type": "collection",
        "primary": "math activities for 4 year olds at home",
        "title": "Math Activities for 4 Year Olds at Home | Kid Activity Lab",
        "h1": "Math activities for 4 year olds at home.",
        "head_style": ".hero h1 { overflow-wrap: anywhere; } @media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 43px); } }",
        "kicker": "Early math",
        "description": "Hands-on math activities for 4 year olds at home: patterns, counting, measuring, comparing weight, sorting colors, towers, and tape marks.",
        "intro": "At age 4, math works best when it is built into play. Counting cups, repeating patterns, comparing distance, and balancing objects all give a child math language without a worksheet.",
        "tip": "Use words like more, fewer, longer, shorter, heavier, lighter, same, different, next, and again.",
        "activities": ["pattern-path", "measuring-tape-jumps", "balance-scale-baskets", "lego-color-tower", "cup-tower", "block-tower", "magnetic-tile-ideas", "spoon-transfer"],
        "related": ["easy math activities for 4 year olds", "preschool math activities at home", "hands on math activities for preschoolers"],
    },
    {
        "path": "collections/no-prep-stem-activities-for-4-year-olds.html",
        "page_type": "collection",
        "primary": "no prep stem activities for 4 year olds",
        "title": "No-Prep STEM Activities for 4 Year Olds | Kid Activity Lab",
        "h1": "No-prep STEM activities for 4 year olds.",
        "kicker": "No prep STEM",
        "description": "No-prep STEM activities for 4 year olds using cups, blocks, socks, paper, toy cars, flashlights, ramps, and household objects.",
        "intro": "This page is for the moment when you want STEM play without gathering a supply list. Most of these start with one object, one question, and one quick test.",
        "tip": "Choose the activity that matches what is already out: blocks, cups, toy cars, paper, socks, or a flashlight.",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 48px); } }",
        "activities": ["cup-tower", "block-tower", "sock-ball-roll", "paper-bridge", "shadow-shape-match", "ramp-texture-test", "pattern-path", "tape-road"],
        "related": ["easy stem activities for kids", "no prep stem activities preschool", "quick stem activities for preschoolers"],
    },
    {
        "path": "collections/building-activities-for-4-year-olds.html",
        "head_style": "@media (max-width: 480px) { .hero h1 { font-size: min(2.5rem, 43px); } }",
        "page_type": "collection",
        "primary": "building activities for preschoolers",
        "title": "Building Activities for Preschoolers | Kid Activity Lab",
        "h1": "Building activities for preschoolers.",
        "route_label": "Building activities for 4 year olds",
        "kicker": "Preschool building | Age 4 route included",
        "description": "Choose preschool building activities with blocks, cups, magnetic tiles, paper, straws, tubes, and blankets. Start by material and the kind of structure a child wants to make.",
        "intro": "Choose what is already out, then give the child one structure job: make a place, build up, span a gap, shape a sculpture, or build big on the floor. These research-backed routes keep the design with the child and make the adult setup visible.",
        "tip": "The old block-or-tile Toy Home instructions are withdrawn. For a toy-entry job, Box Garage uses DIFFERENT materials: an already-open box and a suitable owned car, not tiles or a flat picture. Read its checks before handling materials or decline.",
        "tip_link": ("Check the different Box Garage start", "../cards/box-garage.html"),
        "building_layout": True,
        "evidence_note": "Kid Activity Lab created this chooser from current source and search research. We have not family-tested these setups. The age-four route, material choices, adult roles, rescue steps, and stop boundaries are editorial guidance; timing, mess, engagement, learning, repeatability, and safety outcomes are unknown.",
        "readiness_note": "Choose materials that are appropriate for the youngest child who can reach the build. Remove cracked or damaged materials and any piece with an exposed magnet. If any child may mouth materials, stay within reach and watch continuously; skip straws, loose tape, and other loose pieces and use larger solid blocks instead. The Wide-Base Tower below instead requires skipping for mouthing or younger reach you cannot control; larger blocks do not remove its checks. The different flat house picture and Box Garage also require skipping for mouthing or uncertain reach; the larger-block/watch suggestion does NOT override either activity's checks. The different stationary Paper Path test also requires skipping for mouthing, uncontrolled younger reach or uncertain adult attention; the larger-block/watch suggestion does NOT override these checks. Straw Span also requires skipping for mouthing, uncontrolled younger reach, damaged materials or uncertain adult attention; larger blocks or watching do NOT override these checks. Read its checked card before handling; low closed books replace its old cup supports.",
        "image_warning": "Cup Doorway is paused. Do not copy the cup-over-gap depiction in this illustration; it is not a qualified setup. Material checks do not supply its missing instructions. The paper on stacked books is also not the different stationary Paper Path start offered below; do not copy those stacks as instructions.",
        "image": {
            "src": "../assets/preschool-building/building-material-chooser.webp",
            "alt": "Illustration of large blocks, paper cups, a paper bridge, a cardboard-tube sculpture, and a blanket path as preschool building material choices.",
            "width": "1672",
            "height": "941",
            "caption": "Illustrated material routes, not a Kid Activity Lab family-test photo or a product recommendation. The cup-doorway depiction is withdrawn as instructions; do not copy it. The paper on stacked books is not the different stationary Paper Path test below, which uses two low closed books, not these stacks. The blanket path is a toy-only material prompt, not the three-block start below or a child-bearing route.",
        },
        "chooser_title": "Choose by what is ready and what to build",
        "chooser_label": "Preschool building activity chooser",
        "chooser": [
            ("Already-open box and suitable owned car (DIFFERENT materials)", ("Toy Home", "#magnetic-tile-house"), "Read the maintained Box Garage checks before handling; skip if fit, reach or adult attention is uncertain."),
            ("Large blocks", ("Wide-Base Tower", "#block-tower"), "Wide-Base Tower needs three checked matching blocks; adult models and stays."),
            ("Paper cups", ("Cup Doorway (paused)", "#cup-tower"), "Do not start this doorway. Read a different choice's checks before handling or decline."),
            ("Paper, two low closed books and one suitable large block or soft toy", ("Different stationary Paper Path test", "#paper-bridge"), "Read this choice's checks before handling; adult stays. Not a moving-toy path."),
            ("Six whole paper straws, owned tape and two low closed books", ("Straw Span: empty first", "#straw-bridge"), "Adult joins and stays; read the card's checks before handling. No cup supports or required toy load."),
            ("Two whole tubes, cardboard base and owned painter tape", ("Tube Sculpture", "#tube-sculpture"), "Adult checks and attaches; child chooses a low arrangement or points. Untaped or end if tape fails."),
            ("Blanket, three large blocks and one large toy", ("Blanket Crossing", "#blanket-river"), "Adult stays beside a tiny toy-only crossing; never for feet."),
        ],
        "support_steps": [
            ("Name the job", "Ask what the structure is for: a home, wall, tower, path, bridge, or sculpture."),
            ("Offer a small set", "Put out enough material to start without filling the whole play area."),
            ("Ask about space", "Try prompts such as: What could go inside, under, beside, or across?"),
            ("Protect the child's design", "Handle setup or material checks, then let the child place and change the pieces."),
        ],
        "activity_overrides": {
            "magnetic-tile-house": {
                "slug": "magnetic-tile-house",
                "title": "Toy Home",
                "job": "Make a place",
                "checked_handoff": True,
                "handoff_url": "../cards/box-garage.html",
                "handoff_label": "Check the different Box Garage start",
                "materials": "DIFFERENT materials: an already-open box and suitable owned car, not magnetic tiles or blocks",
                "mission": "After the linked checks, choose the maintained park-and-out task or decline. A flat tile picture is NOT a room for a toy.",
                "parent": "The previous tile-or-block house instructions are withdrawn. Read the Box Garage owned-material, fit, adult-role, stop and collection checks BEFORE handling. Adult stays beside every reachable child; skip mouthing, uncertain reach, unsuitable materials or unavailable attention. Do not substitute tiles into that recipe.",
            },
            "magnetic-tile-ideas": {
                "slug": "magnetic-tile-ideas",
                "title": "Connected Rooms",
                "job": "Two-room version paused",
                "pause_reason": "Our Connected Rooms instructions do not establish the pieces, first connection, openings and controlled end well enough to run this two-room version. The old flat-outline rescue was not a complete setup either. This is not a finding that all magnetic tiles are unsuitable.",
                "steps": [],
            },
            "block-tower": {
                "slug": "block-tower",
                "title": "Wide-Base Tower",
                "job": "Build up",
                "materials": ACTIVITIES["block-tower"]["materials"],
                "mission": "Choose one on-top placement above a two-block footprint, or leave all three flat.",
                "adult_role": ACTIVITIES["block-tower"]["adult_setup"],
                "rescue": ACTIVITIES["block-tower"]["parent"],
                "stop": ACTIVITIES["block-tower"]["stop"],
                "parent": ACTIVITIES["block-tower"]["fit_cue"],
                "stop_before_action": True,
            },
            "cup-tower": {
                "slug": "cup-tower",
                "title": "Cup Doorway",
                "job": "Make an opening",
                "cup_doorway_pause": True,
                "steps": [],
            },
            "paper-bridge": {
                "slug": "paper-bridge",
                "title": "Paper Path",
                "paper_bridge_handoff": True,
                "steps": [],
            },
            "straw-bridge": {
                "slug": "straw-bridge",
                "title": "Straw Span",
                "job": "Join materials",
                "straw_bridge_handoff": True,
                "steps": [],
            },
            "tube-sculpture": {
                "slug": "tube-sculpture",
                "title": "Tube Sculpture",
                "job": "Make a sculpture",
                "mission": "Choose a low arrangement of two whole tubes on a base, then look at its shape. Pointing, watching or declining is enough.",
                "adult_role": ACTIVITIES["tube-sculpture"]["adult_setup"],
                "rescue": ACTIVITIES["tube-sculpture"]["parent"],
                "parent": " ".join(text for _, text in ACTIVITIES["tube-sculpture"]["readiness_groups"]),
                "stop_before_action": True,
            },
            "wind-tower-test": {
                "slug": "wind-tower-test",
                "title": "Low Block Wall",
                "job": "Build a boundary",
                "materials": "six to ten lightweight blocks, one large toy",
                "mission": "Make a low wall that marks a space for the toy.",
                "adult_role": "Set a short floor boundary and keep the blocks away from walkways.",
                "steps": ["Place two blocks end to end.", "Continue the wall in a line or curve.", "Choose where to leave an opening."],
                "rescue": "Make a flat three-block line and stop there.",
                "stop": "Stop if blocks enter a walkway, are thrown, or become a climbing setup.",
                "parent": "Keep the wall low and clear it from paths as soon as the building session ends.",
                "link_text": "Open the test-and-redesign version",
            },
            "blanket-river": {
                "slug": "blanket-river",
                "title": "Blanket Crossing",
                "job": "Make a tiny toy crossing",
                "adult_role": ACTIVITIES["blanket-river"]["adult_setup"],
                "rescue": ACTIVITIES["blanket-river"]["parent"],
                "parent": ACTIVITIES["blanket-river"]["fit_cue"],
                "stop_before_action": True,
            },
        },
        "activities": ["magnetic-tile-house", "magnetic-tile-ideas", "block-tower", "cup-tower", "paper-bridge", "straw-bridge", "tube-sculpture", "wind-tower-test", "blanket-river"],
        "related": ["preschool building activities", "building activities for 4 year olds", "block activities for preschoolers"],
        "related_routes": [
            ("Engineering activities for preschoolers", "Choose this when the child wants a problem, a visible test, and one redesign.", "../collections/engineering-activities-for-4-year-olds.html"),
            ("STEM activities for preschoolers", "Browse a broader mix of science, math, engineering, and discovery.", "../collections/stem-activities-for-preschoolers.html"),
            ("Indoor activities for preschoolers", "Choose a different small-room activity job, including roads, ramps, and quieter play.", "../collections/indoor-activities-for-preschoolers.html"),
        ],
        "sources": [
            ("Mississippi State Extension: Block Play", "https://extension.msstate.edu/publications/block-play"),
            ("Smithsonian Science in Pre-K: Getting Ready, Building Structures", "https://scienceinprek.si.edu/getting-ready-building-structures"),
            ("Smithsonian Science in Pre-K: Focused Exploration, Building Structures", "https://scienceinprek.si.edu/focused-exploration-building-structures"),
            ("DREME/Stanford: Draw Your Building", "https://preschoolmath.stanford.edu/resource/draw-your-building/"),
            ("Penn State Better Kid Care: Blocks, Great Toys for All Ages", "https://extension.psu.edu/programs/betterkidcare/early-care/tip-pages/all/blocks-great-toys-for-all-ages"),
            ("South Dakota State Extension: Playing With Blocks", "https://extension.sdstate.edu/playing-blocks"),
        ],
        "evidence": "KAL-RES-007 refreshed 36 Semrush US queries on 2026-08-04, retained seven explicitly incomplete SERP samples, inspected 14 ranking/community pages and six education sources, and promoted one existing-page preschool-building owner.",
        "first_2_month_impression_expectation": "UNKNOWN; the existing URL has no public-safe GSC page baseline.",
    },
]


LEGACY_REDIRECTS = [
    {
        "path": "collections/rainy-day-activities-for-preschoolers.html",
        "destination": "indoor-activities-for-preschoolers.html",
        "canonical": f"{BASE_URL}/collections/indoor-activities-for-preschoolers.html",
        "title": "Rainy Day Activities for Preschoolers Moved | Kid Activity Lab",
        "description": "Rainy-day preschool ideas now live in the Kid Activity Lab indoor activity chooser.",
        "h1": "Rainy-day ideas now live in the indoor chooser.",
    }
]


MANUAL_SEO_TARGETS = [
    {
        "path": "articles/paper-straw-rocket.html",
        "page_type": "article",
        "primary": "straw rocket",
        "related": ["straw rocket for kids", "paper straw rocket"],
        "evidence": "KAL-RES-015 September21 source/visual qualification; retained September17 DataForSEO US straw rocket2900 TOOL_ESTIMATE, child variant UNKNOWN. KAL-IMP-014 parent-led template guide; not family-tested. Organic difficulty and attainable rank UNKNOWN.",
        "index_status": "index",
        "first_2_month_impression_expectation": "UNKNOWN; no straw-rocket GSC baseline or traffic forecast.",
    },
    {
        "path": "articles/paper-helicopter-kids.html",
        "page_type": "article",
        "primary": "paper helicopter experiment",
        "related": ["paper helicopter", "how to make a paper helicopter", "paper helicopter for kids"],
        "evidence": "KAL-RES-013 September17 DataForSEO US estimates and incomplete SERPs; KAL-RES-014 September18 source qualification; KAL-IMP-013 September19 original parent guide. Geometry is editorial and not family-tested. Organic difficulty and achievable rank are unknown.",
        "index_status": "index",
        "first_2_month_impression_expectation": "UNKNOWN; no helicopter GSC baseline or traffic forecast.",
    },
    {
        "path": "articles/paper-cup-tower-kids.html",
        "page_type": "article",
        "primary": "paper cup tower challenge",
        "related": ["paper cup tower for kids", "cup stacking activity"],
        "evidence": "KAL-IMP-012 uses the imported September13 Semrush US20 estimate, current September17 incomplete activity-led public results and source reconciliation, and a measured failed compact-card task. The reduced noncompetitive guide is editorial, not family-tested; complete query rows and search outcomes are unavailable.",
        "index_status": "index",
        "first_2_month_impression_expectation": "UNKNOWN; no guide GSC page baseline or traffic forecast.",
    },
    {
        "path": "articles/painter-tape-road-kids.html",
        "page_type": "article",
        "primary": "masking tape road",
        "related": [
            "masking tape road for kids",
            "painter's tape road for kids",
        ],
        "evidence": "KAL-RES-012 retained one small September 13 Semrush US estimate, inspected a current activity-led but incomplete result sample and public parent questions, reconciled current sources, and selected one singular guide owner. Child-specific variants returned explicit zero-volume variation rows; complete GSC query rows remain unavailable.",
        "index_status": "index",
        "first_2_month_impression_expectation": "UNKNOWN; new singular guide with no KAL GSC page baseline.",
    },
    {
        "path": "articles/cardboard-ball-maze-kids.html",
        "page_type": "article",
        "primary": "cardboard ball maze",
        "related": [
            "ball maze for kids",
        ],
        "evidence": "KAL-RES-011 collected current September 13 Semrush US estimates, inspected current DIY maze result types and maintained source pages, and selected one singular guide owner. The child-specific variant returned zero volume; complete GSC query rows remain unavailable.",
        "index_status": "index",
        "first_2_month_impression_expectation": "UNKNOWN; new singular guide with no KAL GSC page baseline.",
    },
    {
        "path": "articles/paper-bridge-challenge-kids.html",
        "page_type": "article",
        "primary": "paper bridge challenge",
        "related": [
            "paper bridge stem challenge",
            "paper bridge challenge for kids",
            "how to make a paper bridge",
        ],
        "evidence": "KAL-RES-010 refreshed 20 exact Semrush US candidate queries on 2026-09-06, inspected current paper-bridge result types and ranking pages, and selected one singular guide owner. Variants overlap; complete GSC query rows remain unavailable.",
        "index_status": "index",
        "first_2_month_impression_expectation": "UNKNOWN; new singular guide with no KAL GSC page baseline.",
    },
    {
        "path": "collections/card-games-for-kids.html",
        "page_type": "collection",
        "primary": "card games for kids",
        "related": [
            "family card games",
            "easy card games for kids",
            "card games for kids with a deck of cards",
            "2 player card games for kids",
        ],
        "evidence": "KAL-RES-004 refreshed 12 Semrush US queries on 2026-07-31, sampled 8 limited SERPs, and inspected 25 ranking/rules pages; one chooser owns the broad informational job.",
        "index_status": "index",
        "first_2_month_impression_expectation": "UNKNOWN; new cluster with no KAL GSC baseline.",
    }
]


def esc(value):
    return html.escape(value or "", quote=True)


def rel_root(path):
    depth = len(Path(path).parent.parts)
    return "../" * depth


def page_activity(page, key):
    activity = dict(ACTIVITIES[key])
    activity.update(page.get("activity_overrides", {}).get(key, {}))
    return activity


def chooser_pick_cell(pick):
    if isinstance(pick, list):
        return " or ".join(
            f'<a href="{esc(url)}">{esc(text)}</a>'
            for text, url in pick
        )
    if isinstance(pick, tuple):
        text, url = pick
        return f'<a href="{esc(url)}">{esc(text)}</a>'
    return esc(pick)


def tile_build_pause_choices(activity):
    return f'''          <p class="tile-build-pause-cue"><strong>Do not start this version.</strong></p>
          <p>{esc(activity["pause_reason"])}</p>
          <p><a href="{esc(activity["flat_url"])}">{esc(activity["flat_label"])}</a>: a flat PICTURE, not a standing structure or room for a toy.</p>
          <p><a href="{esc(activity["box_url"])}">{esc(activity["box_label"])}</a>: DIFFERENT materials, an already-open box and suitable owned car; ONE park-and-out job, NOT two rooms.</p>
          <p>{esc(activity["parent"])}</p>
          <p>Neither choice fulfills the paused standing or two-room task. Research-backed decision, not family-tested by Kid Activity Lab. Time, mess and physical outcomes are unknown.</p>'''


def activity_card(activity):
    if activity.get("tile_build_pause"):
        return f'''        <article class="seo-activity tile-build-pause">
          <h2>{esc(activity["title"])}</h2>
{tile_build_pause_choices(activity)}
          <p><a class="small-link" href="{esc(activity["url"])}">Why this build is paused</a></p>
        </article>'''
    if activity["url"] == "../cards/paper-plate-ramp.html":
        return f'''        <article class="seo-activity plate-pause">
          <h2>Paper Plate Ramp (paused)</h2>
          <p><strong>Do not start this version.</strong> {esc(activity['pause_reason'])}</p>
          <p><a href="{esc(activity['alternative_url'])}">{esc(activity['alternative_label'])}</a></p>
          <p>{esc(activity['alternative_check'])}</p>
          <p>{esc(activity['parent'])}</p>
          <p>Research-backed decision; not family-tested by Kid Activity Lab. Time, mess and physical outcomes are unknown.</p>
        </article>'''
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    link = ""
    if activity["url"]:
        link_text = activity.get("link_text", "Open card")
        link = f'<a class="small-link" href="{esc(activity["url"])}">{esc(link_text)}</a>'
    start_cue = (
        f'\n            <p class="activity-start-cue"><strong>Adult check:</strong> {esc(activity["start_cue"])}</p>'
        if activity.get("start_cue") else ""
    )
    early_link = f"\n            <p>{link}</p>" if activity.get("link_before_steps") else ""
    late_link = "" if early_link or activity.get("suppress_late_link") else "          " + link
    adult_setup = (
        f'\n          <p><strong>Adult setup:</strong> {esc(activity["adult_setup"])}</p>'
        if activity.get("adult_setup") else ""
    )
    if activity.get("adult_setup_groups"):
        setup_paragraphs = "".join(
            f'<p><strong>{esc(label)}:</strong> {esc(text)}</p>'
            for label, text in activity["adult_setup_groups"]
        )
        adult_setup = '\n          <div class="activity-setup"><strong>Adult setup:</strong>' + setup_paragraphs + '</div>'
    if activity.get("distance_start") or activity.get("tube_drop") or activity.get("flat_house"):
        adult_setup += f'\n          <p><strong>Stop:</strong> {esc(activity["stop"])}</p><p><strong>First model:</strong> {esc(activity["adult_setup"])}</p><p>Research-backed, not family-tested by Kid Activity Lab. Time, mess and physical outcomes are unknown.</p>'
    source_note = ""
    if activity.get("sources"):
        links = "; ".join(
            f'<a href="{esc(url)}">{esc(label)}</a>'
            for label, url in activity["sources"]
        )
        source_note = f'\n          <details><summary>Sources and testing status</summary><p>{links}.</p><p>{esc(activity["source_note"])}</p></details>'
    depth_links = (
        '\n          <p><a href="../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start">Basic ramp setup and troubleshooting</a> (the guide compares landing surfaces, not a cloth covering). <a href="../collections/original-stem-activities-for-4-year-olds.html#ramp-detective">Deeper surface-observation routine</a>.</p>'
        if activity["url"] == "../cards/ramp-texture-test.html" else
        '\n          <p><a href="../collections/stem-activities-for-preschoolers.html#continue-a-pattern">Preschool pattern start and diagram</a> with readiness alternatives.</p>'
        if activity["url"] == "../cards/pattern-path.html" else ""
    )
    guide_handoff = (
        f'\n            <p><a href="{esc(activity["guide_url"])}">{esc(activity["guide_label"])}</a></p>'
        if activity.get("distance_start") else
        '\n            <p><a href="../articles/painter-tape-road-kids.html">Full Painter\'s Tape Road guide</a> for surface, first road, rescue and removal checks before starting.</p>'
        if activity["url"] == "../cards/tape-city.html" else ""
    )
    heading_support = start_cue + guide_handoff if activity.get("distance_start") else guide_handoff + start_cue
    return f'''        <article class="seo-activity">
          <div>
            <h2>{esc(activity["title"])}</h2>{heading_support}{early_link}
            <p>{esc(activity["best_for"])}</p>
            <div class="source-tags">
              <span class="tag">{esc(activity.get("age_label", activity["ages"] + " years"))}</span>
              <span class="tag">{esc(activity.get("time_label", activity["time"]))}</span>
              <span class="tag">{esc(activity.get("mess_label", activity["mess"] + " mess"))}</span>
              <span class="tag">{esc(activity.get("help_label", activity["help"] + " help"))}</span>
            </div>
          </div>
          <div class="activity-materials"><strong>Need</strong>{esc(activity["materials"])}</div>{adult_setup}
          <ol class="card-steps">{steps}</ol>
          <p class="activity-parent"><strong>{esc(activity.get("parent_label", "Parent check"))}:</strong> {esc(activity["parent"])}</p>
{late_link}{depth_links}{source_note}
        </article>'''


def straw_bridge_handoff_card(activity, layout):
    return f'''        <article class="seo-activity {layout}" id="{esc(activity["slug"])}">
          <p class="challenge-label">Adult joins; empty span first</p>
          <h2>{esc(activity["title"])}</h2>
          <p class="straw-start-cue"><strong>Join a flat row; try it EMPTY first.</strong></p>
          <p><strong>Need:</strong> {esc(ACTIVITIES["straw-bridge"]["materials"])}. These low closed books replace the old cup supports.</p>
          <p><strong>BEFORE handling:</strong> {esc(activity["fit_cue"])}</p>
          <p><strong>Stop:</strong> {esc(activity["stop"])}</p>
          <p><a href="../cards/straw-bridge.html">Open the checked joint, diagram and empty-trial steps</a>. No toy is required. Read the card's separate fit checks before any optional one-block observation.</p>
          <p>Research-backed editorial start, not physically or family-tested by Kid Activity Lab. Time, mess, strength, learning and safety outcomes are unknown.</p>
        </article>'''


def paper_bridge_handoff_card(activity, layout):
    return f'''        <article class="seo-activity {layout}" id="{esc(activity["slug"])}">
          <p class="challenge-label">Different stationary choice</p>
          <h2>{esc(activity["title"])}</h2>
          <p class="paper-bridge-choice-cue"><strong>Moving-toy road not provided.</strong></p>
          <p>Choose a DIFFERENT stationary-object test, or decline. It does not fulfill the old moving-toy or car-crossing job. This is not a finding that moving-toy bridges cannot work.</p>
          <p><strong>BEFORE handling or opening the card:</strong> an adult stays beside the setup and controls two low closed books. Use one sheet of paper and one intact large lightweight block or soft toy suitable for EVERY reachable child; no car, coins or marbles as this default. Choose this when the child can place gently and follow a stop cue. Skip for mouthing, uncontrolled younger reach or uncertain adult attention.</p>
          <p><strong>Stop:</strong> sliding books, thrown objects, mouthed or torn paper, climbing or wanting to leave. Remove loose paper pieces. The adult can place the object while the child points or watches, or end.</p>
          <p><a href="../cards/paper-bridge.html">Read the different stationary Paper Bridge card from the start</a>. Read its fit, parent and placement checks before starting; the linked guide adds the optional fold, rescue and cleanup.</p>
          <p>Research-backed choice, not family-tested by Kid Activity Lab. Time, mess, physical performance, learning and safety outcomes are unknown.</p>
          <p>Source context: <a href="https://www.sciencebuddies.org/stem-activities/build-best-bridge">Science Buddies</a> and <a href="https://science.anu.edu.au/engagement/science-lab-experiments-home-school/paper-bridge-challenge-science-strong-shapes">ANU</a> describe stationary loads and paper shapes, not this moving-toy road. Our large-object, low-book controls are editorial adaptations, not a source-tested exact setup.</p>
        </article>'''


def cup_doorway_pause_card(activity, layout):
    return f'''        <article class="seo-activity {layout}" id="{esc(activity["slug"])}">
          <p class="challenge-label">Cup doorway version paused</p>
          <h2>{esc(activity["title"])}</h2>
          <p class="cup-doorway-pause-cue"><strong>Do not start this version.</strong></p>
          <p>Our old six-cup doorway instructions do not establish the cup orientation, first support or toy clearance. Neither the top-cup step nor its open-gate rescue is a qualified start here. This is not a finding that no cup doorway can work.</p>
          <p>BEFORE handling, open the chosen activity and read its owned-material, adult-role, stop and collection checks for EVERY reachable child, or decline. Adult stays beside the setup. Skip for mouthing, uncertain fit or reach, or unavailable adult attention.</p>
          <p><a href="../cards/cup-tower.html">Different Cup Tower stacking</a>: two checked matching paper cups; no toy opening.</p>
          <p><a href="../cards/box-garage.html">Different one-car Box Garage</a>: DIFFERENT materials, an already-open box and a suitable owned car; ONE park-and-out job. Do not substitute cups into that recipe.</p>
          <p>Neither choice fulfills the paused cup-doorway job. Research-backed decision, not family-tested by Kid Activity Lab. Time, mess and physical outcomes are unknown.</p>
          <p>Research limits: <a href="https://discovere.org/engineering-activities/tallest-cup-tower/">DiscoverE's cup tower</a> and <a href="https://resourcehub.bostonchildrensmuseum.org/resources/cup-creations">Boston Children's Museum's cup challenges</a> describe other building tasks, not these missing doorway instructions.</p>
        </article>'''


def engineering_activity_card(activity):
    if activity.get("straw_bridge_handoff"):
        return straw_bridge_handoff_card(activity, "engineering-challenge")
    if activity.get("paper_bridge_handoff"):
        return paper_bridge_handoff_card(activity, "engineering-challenge")
    if activity.get("cup_doorway_pause"):
        return cup_doorway_pause_card(activity, "engineering-challenge")
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    link = ""
    if activity["url"]:
        link_text = activity.get("link_text", "Open the base activity card")
        link = f'<a class="small-link" href="{esc(activity["url"])}">{esc(link_text)}</a>'
    stop_html = f'''
          <div class="challenge-stop">
            <p><strong>Stop:</strong> {esc(activity["stop"])}</p>
            <p><strong>Parent check:</strong> {esc(activity["parent"])}</p>
          </div>'''
    early_stop = stop_html if activity.get("stop_before_action") else ""
    late_stop = "" if early_stop else stop_html
    source_note = ""
    if activity["slug"] in {"box-garage", "wind-tower-test", "car-ramp-distance-test"}:
        links = "; ".join(f'<a href="{esc(url)}">{esc(label)}</a>' for label, url in activity["sources"])
        source_note = f'<details><summary>Sources and testing status</summary><p>{links}.</p><p>{esc(activity["source_note"])}</p></details>'
    guide_handoff = (
        '<p><a href="../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start">Read the cardboard-ramp checks before handling</a></p>'
        if activity["slug"] == "car-ramp-distance-test" else ""
    )
    first_cue = (
        f'<p class="distance-start-cue"><strong>{esc(ACTIVITIES["car-ramp-distance-test"]["start_cue"])}</strong></p>'
        if activity["slug"] == "car-ramp-distance-test" else ""
    )
    return f'''        <article class="seo-activity engineering-challenge" id="{esc(activity["slug"])}">
          <div>
            <p class="challenge-label">Challenge</p>
            <h2>{esc(activity["title"])}</h2>{first_cue}{early_stop}{guide_handoff}
            <p class="challenge-mission"><strong>Kid mission:</strong> {esc(activity["mission"])}</p>
            <div class="source-tags">
              <span class="tag">Editorial range: ages 4-6</span>
            </div>
          </div>
          <div class="activity-materials"><strong>Need</strong>{esc(activity["materials"])}</div>
          <p><strong>Adult setup:</strong> {esc(activity["adult_role"])}</p>
          <ol class="card-steps">{steps}</ol>
          <div class="challenge-details">
            <p><strong>Test</strong>{esc(activity["test"])}</p>
            <p><strong>First change</strong>{esc(activity["redesign"])}</p>
            <p><strong>If the build stalls</strong>{esc(activity["rescue"])}</p>
          </div>{late_stop}
          {link}{source_note}
        </article>'''


def building_activity_card(activity):
    if activity.get("straw_bridge_handoff"):
        return straw_bridge_handoff_card(activity, "building-build")
    if activity.get("paper_bridge_handoff"):
        return paper_bridge_handoff_card(activity, "building-build")
    if activity.get("cup_doorway_pause"):
        return cup_doorway_pause_card(activity, "building-build")
    if activity.get("tile_build_pause"):
        return f'''        <article class="seo-activity building-build" id="{esc(activity["slug"])}">
          <p class="challenge-label">{esc(activity["job"])}</p>
          <h2>{esc(activity["title"])}</h2>
{tile_build_pause_choices(activity)}
          <p><a class="small-link" href="{esc(activity["url"])}">Why this build is paused</a></p>
        </article>'''
    if activity.get("checked_handoff"):
        return f'''        <article class="seo-activity building-build" id="{esc(activity["slug"])}">
          <p class="challenge-label">{esc(activity["job"])}</p>
          <h2>{esc(activity["title"])}</h2>
          <p>{esc(activity["materials"])}</p>
          <p><a class="small-link" href="{esc(activity["handoff_url"])}">{esc(activity["handoff_label"])}</a></p>
          <p><strong>Before starting:</strong> {esc(activity["parent"])}</p>
          <p>{esc(activity["mission"])}</p>
          <p>Research-backed, not family-tested by Kid Activity Lab. Time, mess and physical outcomes are unknown.</p>
        </article>'''
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    link = ""
    if activity["url"]:
        link_text = activity.get("link_text", "Open the base activity card")
        link = f'<a class="small-link" href="{esc(activity["url"])}">{esc(link_text)}</a>'
    stop_html = f'''
          <div class="challenge-stop">
            <p><strong>Stop:</strong> {esc(activity["stop"])}</p>
            <p><strong>Parent check:</strong> {esc(activity["parent"])}</p>
          </div>'''
    early_stop = stop_html if activity.get("stop_before_action") else ""
    late_stop = "" if early_stop else stop_html
    source_note = ""
    if activity["slug"] in {"blanket-river", "tube-sculpture", "block-tower"}:
        links = "; ".join(f'<a href="{esc(url)}">{esc(label)}</a>' for label, url in activity["sources"])
        source_note = f'<details><summary>Sources and testing status</summary><p>{links}.</p><p>{esc(activity["source_note"])}</p></details>'
    return f'''        <article class="seo-activity building-build" id="{esc(activity["slug"])}">
          <div>
            <p class="challenge-label">{esc(activity["job"])}</p>
            <h2>{esc(activity["title"])}</h2>{early_stop}
            <p class="challenge-mission"><strong>Kid mission:</strong> {esc(activity["mission"])}</p>
            <div class="source-tags">
              <span class="tag">Editorial preschool route; age 4 included</span>
            </div>
          </div>
          <div class="activity-materials"><strong>Need</strong>{esc(activity["materials"])}</div>
          <p><strong>Adult setup:</strong> {esc(activity["adult_role"])}</p>
          <ol class="card-steps">{steps}</ol>
          <div class="challenge-details build-rescue">
            <p><strong>If the build stalls</strong>{esc(activity["rescue"])}</p>
          </div>{late_stop}
          {link}{source_note}
        </article>'''


def indoor_activity_card(activity):
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    stop_html = f'''          <div class="challenge-stop">
            <p><strong>Stop:</strong> {esc(activity["stop"])}</p>
            <p><strong>Parent check:</strong> {esc(activity["parent"])}</p>
          </div>'''
    early_stop = f"{stop_html}\n" if activity.get("stop_before_action") else ""
    late_stop = "" if early_stop else f"{stop_html}\n"
    source_note = ""
    if activity["slug"] == "blanket-toy-crossing":
        links = "; ".join(f'<a href="{esc(url)}">{esc(label)}</a>' for label, url in activity["sources"])
        source_note = f'<details><summary>Sources and testing status</summary><p>{links}.</p><p>{esc(activity["source_note"])}</p></details>'
    return f'''        <article class="seo-activity indoor-start" id="{esc(activity["slug"])}">
          <div>
            <p class="challenge-label">{esc(activity["job"])}</p>
            <h2>{esc(activity["title"])}</h2>
{early_stop}            <p class="challenge-mission"><strong>Kid idea:</strong> {esc(activity["mission"])}</p>
            <div class="source-tags">
              <span class="tag">Editorial preschool route</span>
            </div>
          </div>
          <div class="activity-materials"><strong>Need</strong>{esc(activity["materials"])}</div>
          <p><strong>Adult setup:</strong> {esc(activity["adult_role"])}</p>
          <ol class="card-steps">{steps}</ol>
          <div class="challenge-details indoor-rescue">
            <p><strong>If it stalls</strong>{esc(activity["rescue"])}</p>
          </div>
{late_stop}          <a class="small-link" href="{esc(activity["url"])}">{esc(activity["link_text"])}</a>{source_note}
        </article>'''


def preschool_stem_lead_card(lead):
    steps = "".join(f"<li>{esc(step)}</li>" for step in lead["steps"])
    return f'''        <article class="stem-start" id="{esc(lead["slug"])}">
          <div class="stem-start-heading">
            <p class="challenge-label">{esc(lead["lane"])}</p>
            <h2>{esc(lead["title"])}</h2>
            <p class="challenge-mission"><strong>Kid mission:</strong> {esc(lead["mission"])}</p>
          </div>
          <div class="stem-start-body">
            <div class="activity-materials"><strong>Materials or substitute</strong>{esc(lead["materials"])}</div>
            <p class="stem-substitution"><strong>Substitution:</strong> {esc(lead["substitution"])}</p>
            <p class="stem-readiness"><strong>Readiness:</strong> {esc(lead["readiness"])}</p>
            <p><strong>Adult setup:</strong> {esc(lead["adult_role"])}</p>
            <ol class="card-steps">{steps}</ol>
            <div class="stem-stop"><strong>Stop and reset</strong><span>{esc(lead["stop"])}</span></div>
          </div>
        </article>'''


def preschool_stem_page_html(page):
    root = rel_root(page["path"])
    head_style = f'\n    <style>{page["head_style"]}</style>' if page.get("head_style") else ""
    chooser_links = "\n".join(
        f'''          <a href="{esc(choice["href"])}">
            <span class="stem-lane">{esc(choice["lane"])}</span>
            <strong>{esc(choice["action"])}</strong>
            <span>{esc(choice["summary"])}</span>
          </a>'''
        for choice in page["chooser"]
    )
    lead_html = "\n".join(preschool_stem_lead_card(lead) for lead in page["leads"])
    related_routes = "\n".join(
        f'''          <a href="{esc(url)}">
            <strong>{esc(title)}</strong>
            <span>{esc(body)}</span>
          </a>'''
        for title, body, url in page["related_routes"]
    )
    legacy_routes = "\n".join(
        f'<li><a href="{esc(url)}">{esc(title)}</a></li>'
        for title, url in page["legacy_routes"]
    )
    source_links = "\n".join(
        f'<li><a href="{esc(url)}">{esc(title)}</a></li>'
        for title, url in page["sources"]
    )
    image = page["image"]
    canonical = f"{BASE_URL}/{page['path']}"
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(page["title"])}</title>
    <meta name="description" content="{esc(page["description"])}">
    <link rel="canonical" href="{esc(canonical)}">
    <link rel="stylesheet" href="{root}styles.css?v=preschool-stem-front-door-1">{head_style}
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="{root}original/">Original</a>
          <a href="{root}cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero preschool-stem-hero">
        <p class="kicker">{esc(page["kicker"])}</p>
        <h1>{esc(page["h1"])}</h1>
        <p class="dek">{esc(page["intro"])}</p>
      </section>

      <section class="seo-page preschool-stem-page">
        <section class="stem-chooser" aria-labelledby="stem-chooser-title">
          <div class="section-heading">
            <h2 id="stem-chooser-title">{esc(page["chooser_title"])}</h2>
            <p>Choose by the action the child can take and the materials you can supervise now.</p>
          </div>
          <nav class="stem-mode-links" aria-label="Three preschool STEM activity starts">
{chooser_links}
          </nav>
        </section>

        <div class="stem-disclosure" role="note">
          <strong>Evidence note</strong>
          <p>{esc(page["evidence_note"])}</p>
        </div>

        <figure class="stem-visual">
          <img src="{esc(image["src"])}" alt="{esc(image["alt"])}" width="{esc(image["width"])}" height="{esc(image["height"])}">
          <figcaption>{esc(image["caption"])}</figcaption>
        </figure>

        <section class="stem-starts" aria-labelledby="stem-starts-title">
          <div class="section-heading">
            <p class="kicker">Three complete starts</p>
            <h2 id="stem-starts-title">Run one question, then stop</h2>
            <p>Use the readiness cue before the age label. Each start ends after one comparison; continuing is optional, not an expected outcome.</p>
          </div>
{lead_html}
        </section>

        <section class="related stem-routes" aria-labelledby="stem-routes-title">
          <h2 id="stem-routes-title">Go deeper by discipline</h2>
          <p>These pages own the longer science, engineering, math, and age-specific jobs. The broad chooser stays short.</p>
          <div class="stem-deeper-routes">
{related_routes}
          </div>
          <p class="stem-optional-label"><strong>Optional library routes</strong></p>
          <ul class="stem-optional-routes">
{legacy_routes}
          </ul>
        </section>

        <section class="related stem-sources" aria-labelledby="stem-sources-title">
          <h2 id="stem-sources-title">Research sources and limits</h2>
          <p>These sources support observing and comparing changes, testing and improving a build, and working with repeating patterns. They do not establish that Kid Activity Lab ran these exact setups or measured fit, safety, engagement, or learning outcomes.</p>
          <ul class="source-list">
{source_links}
          </ul>
        </section>
      </section>
    </main>

    <footer class="site-footer">
      <p><a href="{root}cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def engineering_page_html(page):
    root = rel_root(page["path"])
    image_warning = f'<p class="paper-bridge-image-warning"><strong>{esc(page["image_warning"])}</strong></p>' if page.get("image_warning") else ""
    tip_link = f'<p><a href="{esc(page["tip_link"][1])}">{esc(page["tip_link"][0])}</a></p>' if page.get("tip_link") else ""
    activity_html = "\n".join(
        engineering_activity_card(page_activity(page, key))
        for key in page["activities"]
    )
    chooser_rows = "\n".join(
        f'''            <tr>
              <td data-label="What is ready">{esc(situation)}</td>
              <td data-label="Start with">{chooser_pick_cell(pick)}</td>
              <td data-label="Adult role">{esc(adult_role)}</td>
            </tr>'''
        for situation, pick, adult_role in page["chooser"]
    )
    process_steps = "\n".join(
        f'<li><strong>{esc(label)}</strong><span>{esc(body)}</span></li>'
        for label, body in page["process_steps"]
    )
    related_routes = "\n".join(
        f'''          <a href="{esc(url)}">
            <strong>{esc(title)}</strong>
            <span>{esc(body)}</span>
          </a>'''
        for title, body, url in page["related_routes"]
    )
    source_links = "\n".join(
        f'<li><a href="{esc(url)}">{esc(title)}</a></li>'
        for title, url in page["sources"]
    )
    image = page["image"]
    canonical = f"{BASE_URL}/{page['path']}"
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(page["title"])}</title>
    <meta name="description" content="{esc(page["description"])}">
    <link rel="canonical" href="{esc(canonical)}">
    <link rel="stylesheet" href="{root}styles.css?v=engineering-arrival-1-paper-bridge-1-straw-1">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="{root}original/">Original</a>
          <a href="{root}cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero engineering-hero">
        <p class="kicker">{esc(page["kicker"])}</p>
        <h1>{esc(page["h1"])}</h1>
        <p class="dek">{esc(page["intro"])}</p>
      </section>

      <section class="seo-page engineering-page">
        <div class="callout">
          <strong>Start here:</strong> {esc(page["tip"])}{tip_link}
        </div>

        <div class="engineering-disclosure" role="note">
          <strong>Evidence note</strong>
          <p>{esc(page["evidence_note"])}</p>
        </div>

        {image_warning}
        <figure class="engineering-visual">
          <img src="{esc(image["src"])}" alt="{esc(image["alt"])}" width="{esc(image["width"])}" height="{esc(image["height"])}">
          <figcaption>{esc(image["caption"])}</figcaption>
        </figure>

        <section class="chooser" aria-labelledby="engineering-chooser-title">
          <h2 id="engineering-chooser-title">{esc(page["chooser_title"])}</h2>
          <div class="table-wrap seo-table" aria-label="{esc(page["chooser_label"])}">
            <table>
              <thead>
                <tr>
                  <th>What is ready</th>
                  <th>Start with</th>
                  <th>Adult role</th>
                </tr>
              </thead>
              <tbody>
{chooser_rows}
              </tbody>
            </table>
          </div>
        </section>

        <section class="engineering-process related" aria-labelledby="engineering-process-title">
          <h2 id="engineering-process-title">A preschool engineering loop</h2>
          <p>Use this loop for runnable challenges. For a different-card choice, read that card's checks before starting; a paused version is not a build instruction. The five-part structure is adapted from TERC Head Start on Engineering and HeadStart.gov; the short prompts are Kid Activity Lab editorial wording.</p>
          <ol>
{process_steps}
          </ol>
        </section>

        <section class="engineering-challenges" aria-labelledby="engineering-challenges-title">
          <div class="section-heading">
            <p class="kicker">Nine choices</p>
            <h2 id="engineering-challenges-title">Choose one problem to solve</h2>
            <p>Follow each route's checks first. Runnable challenges offer a test and optional first change; different-card choices and paused versions are not local recipes. No route promises to fit every child.</p>
          </div>
          <div class="seo-activity-grid" aria-label="Preschool engineering challenges">
{activity_html}
          </div>
        </section>

        <section class="related" aria-labelledby="engineering-routes-title">
          <h2 id="engineering-routes-title">Choose another route</h2>
          <p>Building play and broad STEM are useful neighboring jobs, but they are not the same search or parent decision as an engineering challenge.</p>
          <div class="related-routes">
{related_routes}
          </div>
        </section>

        <section class="related engineering-sources" aria-labelledby="engineering-sources-title">
          <h2 id="engineering-sources-title">Research sources and limits</h2>
          <p>These sources support an iterative problem-solving model for young children. They do not establish that Kid Activity Lab ran these exact setups or measured their fit, safety, engagement, or learning outcomes.</p>
          <ul class="source-list">
{source_links}
          </ul>
        </section>
      </section>
    </main>

    <footer class="site-footer">
      <p><a href="{root}cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def building_page_html(page):
    root = rel_root(page["path"])
    style_version = f"{CSS_VERSION}-paper-bridge-1-straw-1"
    image_warning = f'<p class="building-image-warning"><strong>{esc(page["image_warning"])}</strong></p>' if page.get("image_warning") else ""
    tip_link = f'<p><a href="{esc(page["tip_link"][1])}">{esc(page["tip_link"][0])}</a></p>' if page.get("tip_link") else ""
    head_style = f'\n    <style>{page["head_style"]}</style>' if page.get("head_style") else ""
    activity_html = "\n".join(
        building_activity_card(page_activity(page, key))
        for key in page["activities"]
    )
    chooser_rows = "\n".join(
        f'''            <tr>
              <td data-label="What is ready">{esc(material)}</td>
              <td data-label="Build job">{chooser_pick_cell(pick)}</td>
              <td data-label="Adult role">{esc(adult_role)}</td>
            </tr>'''
        for material, pick, adult_role in page["chooser"]
    )
    support_steps = "\n".join(
        f'<li><strong>{esc(label)}</strong><span>{esc(body)}</span></li>'
        for label, body in page["support_steps"]
    )
    related_routes = "\n".join(
        f'''          <a href="{esc(url)}">
            <strong>{esc(title)}</strong>
            <span>{esc(body)}</span>
          </a>'''
        for title, body, url in page["related_routes"]
    )
    source_links = "\n".join(
        f'<li><a href="{esc(url)}">{esc(title)}</a></li>'
        for title, url in page["sources"]
    )
    image = page["image"]
    canonical = f"{BASE_URL}/{page['path']}"
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(page["title"])}</title>
    <meta name="description" content="{esc(page["description"])}">
    <link rel="canonical" href="{esc(canonical)}">
    <link rel="stylesheet" href="{root}styles.css?v={style_version}">{head_style}
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="{root}original/">Original</a>
          <a href="{root}cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero building-hero">
        <p class="kicker">{esc(page["kicker"])}</p>
        <h1>{esc(page["h1"])}</h1>
        <p class="dek">{esc(page["intro"])}</p>
      </section>

      <section class="seo-page building-page">
        <div class="callout">
          <strong>Start here:</strong> {esc(page["tip"])}{tip_link}
        </div>

        <div class="building-disclosure" role="note">
          <strong>Evidence note</strong>
          <p>{esc(page["evidence_note"])}</p>
        </div>

        <div class="building-readiness" role="note">
          <strong>Choose for every child who can reach the build</strong>
          <p>{esc(page["readiness_note"])}</p>
        </div>

        {image_warning}
        <figure class="building-visual">
          <img src="{esc(image["src"])}" alt="{esc(image["alt"])}" width="{esc(image["width"])}" height="{esc(image["height"])}">
          <figcaption>{esc(image["caption"])}</figcaption>
        </figure>

        <section class="chooser" aria-labelledby="building-chooser-title">
          <h2 id="building-chooser-title">{esc(page["chooser_title"])}</h2>
          <div class="table-wrap seo-table" aria-label="{esc(page["chooser_label"])}">
            <table>
              <thead>
                <tr>
                  <th>What is ready</th>
                  <th>Build job</th>
                  <th>Adult role</th>
                </tr>
              </thead>
              <tbody>
{chooser_rows}
              </tbody>
            </table>
          </div>
        </section>

        <section class="building-support related" aria-labelledby="building-support-title">
          <h2 id="building-support-title">Support the build without supplying the design</h2>
          <p>The structure and spatial prompts below are Kid Activity Lab editorial wording informed by the named education and extension sources.</p>
          <ol>
{support_steps}
          </ol>
        </section>

        <section class="building-boundary related" aria-labelledby="building-boundary-title">
          <h2 id="building-boundary-title">Use the right route</h2>
          <p><strong>This page:</strong> open-ended structures and spaces made with materials already available.</p>
          <p><strong>Engineering:</strong> a problem, visible test, and one redesign. <a href="../collections/engineering-activities-for-4-year-olds.html">Open the preschool engineering chooser</a>.</p>
          <p><strong>Construction themes:</strong> classroom units about vehicles, tools, dramatic play, literacy, crafts, and printables. This page does not promise that curriculum.</p>
        </section>

        <section class="building-collection" aria-labelledby="building-collection-title">
          <div class="section-heading">
            <p class="kicker">Nine builds</p>
            <h2 id="building-collection-title">Choose one structure job</h2>
            <p>Use the rescue as a smaller finish, not as a promise that the activity will fit every child.</p>
          </div>
          <div class="seo-activity-grid" aria-label="Preschool building activities">
{activity_html}
          </div>
        </section>

        <section class="related" aria-labelledby="building-routes-title">
          <h2 id="building-routes-title">Choose another activity route</h2>
          <p>These neighboring pages support different activity goals: testing and redesigning, broader preschool STEM, or choosing something for an indoor moment.</p>
          <div class="related-routes">
{related_routes}
          </div>
        </section>

        <section class="related building-sources" aria-labelledby="building-sources-title">
          <h2 id="building-sources-title">Research sources and limits</h2>
          <p>These sources support open exploration, varied structures and materials, spatial questions, and a bounded adult role. They do not establish that Kid Activity Lab ran these setups or measured their fit, safety, engagement, or learning outcomes.</p>
          <ul class="source-list">
{source_links}
          </ul>
        </section>
      </section>
    </main>

    <footer class="site-footer">
      <p><a href="{root}cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def indoor_page_html(page):
    root = rel_root(page["path"])
    start_html = "\n".join(indoor_activity_card(activity) for activity in page["indoor_starts"])
    chooser_rows = "\n".join(
        f'''            <tr>
              <td data-label="Moment">{esc(moment)}</td>
              <td data-label="Start with">{chooser_pick_cell(pick)}</td>
              <td data-label="Space and materials">{esc(space)}</td>
              <td data-label="Adult role">{esc(adult_role)}</td>
            </tr>'''
        for moment, pick, space, adult_role in page["chooser"]
    )
    support_steps = "\n".join(
        f'<li><strong>{esc(label)}</strong><span>{esc(body)}</span></li>'
        for label, body in page["support_steps"]
    )
    rainy_rotation = "\n".join(
        f'''          <a href="{esc(url)}">
            <strong>{esc(label)}</strong>
            <span>{esc(body)}</span>
          </a>'''
        for label, body, url in page["rainy_rotation"]
    )
    related_routes = "\n".join(
        f'''          <a href="{esc(url)}">
            <strong>{esc(title)}</strong>
            <span>{esc(body)}</span>
          </a>'''
        for title, body, url in page["related_routes"]
    )
    source_links = "\n".join(
        f'''            <li>
              <a href="{esc(url)}">{esc(title)}</a>
              <span>{esc(limit)}</span>
            </li>'''
        for title, url, limit in page["sources"]
    )
    image = page["image"]
    canonical = f"{BASE_URL}/{page['path']}"
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(page["title"])}</title>
    <meta name="description" content="{esc(page["description"])}">
    <link rel="canonical" href="{esc(canonical)}">
    <link rel="stylesheet" href="{root}styles.css?v={CSS_VERSION}">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="{root}original/">Original</a>
          <a href="{root}cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero indoor-hero">
        <p class="kicker">{esc(page["kicker"])}</p>
        <h1>{esc(page["h1"])}</h1>
        <p class="dek">{esc(page["intro"])}</p>
      </section>

      <section class="seo-page indoor-page">
        <div class="callout">
          <strong>Start here:</strong> {esc(page["tip"])}
          <p><a href="#sock-target-roll">Read the bounded start</a></p>
        </div>

        <div class="indoor-disclosure" role="note">
          <strong>Evidence note</strong>
          <p>{esc(page["evidence_note"])}</p>
        </div>

        <div class="indoor-readiness" role="note">
          <strong>Check the real room and every child who can reach it</strong>
          <p>{esc(page["readiness_note"])}</p>
        </div>

        <figure class="indoor-visual">
          <img src="{esc(image["src"])}" alt="{esc(image["alt"])}" width="{esc(image["width"])}" height="{esc(image["height"])}">
          <figcaption>{esc(image["caption"])}</figcaption>
        </figure>

        <section class="chooser" aria-labelledby="indoor-chooser-title">
          <h2 id="indoor-chooser-title">{esc(page["chooser_title"])}</h2>
          <div class="table-wrap seo-table" aria-label="{esc(page["chooser_label"])}">
            <table>
              <thead>
                <tr>
                  <th>Moment</th>
                  <th>Start with</th>
                  <th>Space and materials</th>
                  <th>Adult role</th>
                </tr>
              </thead>
              <tbody>
{chooser_rows}
              </tbody>
            </table>
          </div>
        </section>

        <section class="indoor-rain related" aria-labelledby="indoor-rain-title">
          <p class="kicker">Rainy day is a context</p>
          <h2 id="indoor-rain-title">Rotate the job, not the page</h2>
          <p>Weather may be why everyone is inside, but the next useful choice is still movement, making or building, quieter play, or a game. Rain-themed crafts and weather learning are separate jobs and are not promised here.</p>
          <div class="indoor-rotation">
{rainy_rotation}
          </div>
        </section>

        <section class="indoor-support related" aria-labelledby="indoor-support-title">
          <h2 id="indoor-support-title">Make any choice easier to start</h2>
          <p>These four moves are Kid Activity Lab editorial guidance. They reduce the decision and setup, but they do not predict how a child will respond.</p>
          <ol>
{support_steps}
          </ol>
        </section>

        <section class="indoor-starts" aria-labelledby="indoor-starts-title">
          <div class="section-heading">
            <p class="kicker">Six bounded starts</p>
            <h2 id="indoor-starts-title">Choose one child-facing idea</h2>
            <p>Use the rescue as a smaller finish. Use the stop when the material, movement, room, or child no longer fits.</p>
          </div>
          <div class="seo-activity-grid" aria-label="Indoor activity starts for preschoolers">
{start_html}
          </div>
        </section>

        <section class="related" aria-labelledby="indoor-routes-title">
          <h2 id="indoor-routes-title">Choose a deeper route</h2>
          <p>Use these existing pages when the job is specifically a longer build, a standard-deck game, or finding something from materials already visible.</p>
          <div class="related-routes">
{related_routes}
          </div>
        </section>

        <section class="related indoor-sources" aria-labelledby="indoor-sources-title">
          <h2 id="indoor-sources-title">Research sources and limits</h2>
          <p>These sources support parent-job, category, and activity-shape decisions within the limits shown. They do not establish that Kid Activity Lab ran these setups or measured their fit, timing, mess, safety, engagement, or learning outcomes.</p>
          <ul class="source-list">
{source_links}
          </ul>
        </section>
      </section>
    </main>

    <footer class="site-footer">
      <p><a href="{root}cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def legacy_redirect_html(redirect):
    root = rel_root(redirect["path"])
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(redirect["title"])}</title>
    <meta name="description" content="{esc(redirect["description"])}">
    <meta http-equiv="refresh" content="0; url={esc(redirect["destination"])}">
    <link rel="canonical" href="{esc(redirect["canonical"])}">
    <link rel="stylesheet" href="{root}styles.css?v={CSS_VERSION}">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="{root}original/">Original</a>
          <a href="{root}cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero legacy-redirect">
        <p class="kicker">Page moved</p>
        <h1>{esc(redirect["h1"])}</h1>
        <p class="dek">Rainy day is now one context inside the preschool indoor chooser, alongside movement, making, building, pretend play, and games.</p>
        <p><a href="{esc(redirect["destination"])}">Open the indoor activities chooser</a></p>
      </section>
    </main>

    <footer class="site-footer">
      <p><a href="{root}cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def paper_straw_rocket_guide_html():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Paper Straw Rocket: A Parent-Led Activity | Kid Activity Lab</title>
    <meta name="description" content="Make a paper straw rocket with NASA's printable, adult setup and launch, a clear fit diagram, and checks for a stuck or leaking rocket. Printer required.">
    <link rel="icon" href="data:,">
    <link rel="canonical" href="https://kidactivitylab.com/articles/paper-straw-rocket.html">
    <link rel="stylesheet" href="../styles.css?v=paper-bridge-1">
    <style>
      body { background: #fff; }
      .rocket-guide { max-width: 760px; margin: 0 auto; }
      .rocket-guide h1 { font-size: 2.5rem; letter-spacing: 0; }
      .rocket-guide .hero { padding-bottom: 8px; }
      .rocket-guide .content { padding-top: 0; }
      .rocket-guide .start { border-top: 2px solid #176b62; margin-top: 20px; padding-top: 12px; }
      .rocket-guide .start p { margin: 8px 0; }
      .rocket-guide figure { margin: 24px 0; max-width: 650px; }
      .rocket-guide figure img { aspect-ratio: 9 / 10; object-fit: contain; }
      .rocket-guide figcaption { font-size: 0.9rem; }
      .rocket-guide section { scroll-margin-top: 7rem; }
      .rocket-guide .jump { display: flex; flex-wrap: wrap; gap: 8px 24px; }
      .rocket-guide .jump a { padding: 8px 0; }
      .rocket-guide a:focus-visible { outline: 3px solid #246b8f; outline-offset: 4px; }
      @media (max-width: 600px) { .rocket-guide h1 { font-size: 2rem; } }
      @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
    </style>
    <script type="application/ld+json">
      {"@context":"https://schema.org","@type":"Article","headline":"Paper Straw Rocket","datePublished":"2026-09-22","dateModified":"2026-09-22","author":{"@type":"Organization","name":"Kid Activity Lab"},"image":"https://kidactivitylab.com/assets/paper-straw-rocket/fit-air-path.png"}
    </script>
  </head>
  <body>
    <header class="site-header"><nav class="nav" aria-label="Main navigation">
      <a class="brand" href="/">Kid Activity Lab</a>
      <div class="nav-links"><a href="/">Home</a><a href="../original/">Original</a><a href="../cards.html">Cards</a></div>
    </nav></header>
    <main><article class="rocket-guide">
      <header class="hero">
        <p class="kicker">Prepare | count down | watch</p>
        <h1>Paper Straw Rocket</h1>
        <p class="dek">Turn a paper sleeve into a small rocket. An adult builds and launches; your child can decorate, count down or watch.</p>
        <div class="start">
          <p><strong>Printer required.</strong> Get ordinary printer paper, a pencil, scissors, tape and a straight plastic drinking straw that fits inside the paper tube.</p>
          <p><strong>Adult-led throughout:</strong> keep tools and the launcher with you. Choose a clear launch direction away from people and faces. If you cannot keep it clear, choose another activity.</p>
          <p><strong>Research-backed, not family-tested by Kid Activity Lab.</strong> This is not a child-launch or independent-play activity.</p>
        </div>
        <nav class="jump" aria-label="On this page"><a href="#prepare">Make the rocket</a><a href="#launch">First launch</a><a href="#rescue">Stuck or leaking?</a></nav>
      </header>
      <div class="content">
        <section id="prepare" aria-labelledby="prepare-title">
          <h2 id="prepare-title">Adult setup: one paper model</h2>
          <p><a href="https://d2pn8kiwq2w21t.cloudfront.net/documents/strawrocket_worksheet.pdf">Open NASA's rocket template (PDF)</a> and print page 1. Use its outlines, not the diagram below. No printer? Try our <a href="paper-helicopter-kids.html">paper helicopter</a> instead; it is a different activity, not a substitute rocket recipe.</p>
          <ol class="steps">
            <li><strong>Cut the parts.</strong> Cut out the body rectangle and both fin units, separating the fins at the middle scissors mark. A child can decorate the flat paper before the adult cuts.</li>
            <li><strong>Roll the body.</strong> Roll the rectangle lengthwise around the pencil and tape the long seam. Remove the pencil to check the straw: it must slide inside without large gaps. Remake a pinched or loose tube rather than force it. Remove the straw and put the pencil back for the next steps.</li>
            <li><strong>Add the fins.</strong> Tape each fin unit's center rectangle to an opposite side of the tube at its bottom opening. Nothing should extend below that end. Bend the four triangular fins apart into a cross when viewed from behind.</li>
            <li><strong>Seal the nose.</strong> With the pencil still inside, twist the paper at the other end around its tip. Tape the twisted nose closed, then remove the pencil. The bottom stays open.</li>
          </ol>
          <p>Put the pencil, scissors and loose scraps away. Check that the finished sleeve slides off the straw freely and that tape does not cover its opening. This version uses a paper sleeve, not a second straw or pipette. Do not add a hard tip, clips or weights.</p>
          <figure>
            <img src="../assets/paper-straw-rocket/fit-air-path.png" alt="Side cutaway: the straw enters the open bottom of a paper sleeve and ends before its taped, closed nose. Air moves from the straw into the sleeve. Rear view: four fins surround a clear center opening. Remove the pencil before launch." width="900" height="1000">
            <figcaption>Original KAL explanation, not to scale or a cutting template. The top cutaway omits fins so you can see the air path. Use NASA's printed outline for the parts. <a href="../assets/paper-straw-rocket/fit-air-path.png">Open the full-size diagram</a>.</figcaption>
          </figure>
        </section>
        <section id="launch" aria-labelledby="launch-title">
          <h2 id="launch-title">Count down, then watch</h2>
          <p>The adult checks the clear direction, holds the straw with the rocket pointing away from everyone, and blows outward through the straw once. The paper sleeve leaves; the adult keeps the straw. Never aim at a person, including during a fit check.</p>
          <p>Invite your child to count down or say, "Watch where the paper lands." Everyone waits outside the launch path until the adult lowers the straw and calls retrieval. Watching from a comfortable seat or declining is fine; no child needs to blow.</p>
          <p><strong>Stop</strong> if anyone enters the path, a child mouths the materials, a straw or paper part is damaged, or adult control cannot continue. Do not launch toward faces, chase while holding a straw in the mouth, or use suction to clear a jam. Keep all launch equipment with the adult between tries.</p>
        </section>
        <section id="rescue" aria-labelledby="rescue-title">
          <h2 id="rescue-title">Stuck or leaking?</h2>
          <p>First lower the launcher and take it away from the mouth. These are inspection suggestions, not guaranteed fixes. Do not blow harder to overcome a problem.</p>
          <dl class="bridge-troubleshooting">
            <div><dt>Sleeve stays stuck</dt><dd>Slide it off by hand. Check for pinched paper or tape catching the straw. Remake the same paper tube if it cannot slide freely; do not force or enlarge it while it is in the mouth.</dd></div>
            <div><dt>Air escapes; little movement</dt><dd>Inspect the nose and long seam for an opening. Retape an open seam, keeping the bottom clear. Replace torn paper. If the fit or seal remains unclear, end the trial.</dd></div>
          </dl>
        </section>
        <section id="finish" aria-labelledby="finish-title">
          <h2 id="finish-title">One more try, or finish</h2>
          <p>After a working start, repeat once with the same setup and ask, "Did it land in the same place?" No distance contest or worksheet is needed. The enclosed air can push the sleeve off the straw; this is a paper model, not an engine-powered rocket.</p>
          <p>Collect the rocket, straw, tape and paper offcuts. With younger siblings nearby, the adult manages the materials and retrieval; if that is not practical, stop. Preparation time, play duration and cleanup effort have not been measured.</p>
        </section>
        <section id="evidence" aria-labelledby="evidence-title">
          <h2 id="evidence-title">Sources and limits</h2>
          <p>The construction follows <a href="https://www.jpl.nasa.gov/edu/resources/project/make-a-straw-rocket/">NASA JPL's straw rocket</a> and linked template, checked September 21, 2026. Follow the webpage's taped-nose instruction even though the worksheet does not mention that tape. NASA describes school grades 4-8, not ages 4-8.</p>
          <p><a href="https://www.grc.nasa.gov/www/k-12/TRC/Rockets/paper_rocket.html">NASA Glenn's paper-rocket guidance</a>, checked the same day, supports leak checks and warns against aiming toward anyone because of eye injury risk. Its alternative nose and fin pattern are not used here.</p>
          <p>KAL's adult-only launch, child roles, stop/recovery sequence and diagram are editorial adaptations, not an age recommendation or safety certification. No physical or family test by KAL is recorded. Flight, comprehension, enjoyment, learning, repeatability, mess and safety outcomes remain unknown.</p>
        </section>
        <p><a href="../cards.html">Choose another activity</a></p>
      </div>
    </article></main>
    <footer class="site-footer"><p>Kid Activity Lab</p></footer>
  </body>
</html>
'''


def paper_helicopter_guide_html():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Paper Helicopter for Kids: Cut, Fold and Try | Kid Activity Lab</title>
    <meta name="description" content="Make one paper helicopter with adult preparation, a labeled cut-and-fold map, a drop-and-watch start and checks for a model that does not turn. No printer needed.">
    <link rel="icon" href="data:,">
    <link rel="canonical" href="https://kidactivitylab.com/articles/paper-helicopter-kids.html">
    <link rel="stylesheet" href="../styles.css?v=paper-bridge-1">
    <style>
      .helicopter-guide h1 { font-size: 2.5rem; letter-spacing: 0; }
      .helicopter-guide .content { padding-top: 0; }
      .helicopter-map { margin: 20px 0; max-width: 620px; }
      .helicopter-map img { aspect-ratio: 9 / 14; object-fit: contain; }
      .helicopter-map figcaption { font-size: 0.9rem; }
      .helicopter-guide details { margin: 18px 0; }
      .helicopter-guide summary { cursor: pointer; text-decoration: underline; }
      .helicopter-guide .content section[id] { scroll-margin-top: max(110px, 7rem); }
      @media (max-width: 600px) {
        .helicopter-guide h1 { font-size: min(2rem, 56px); }
        .helicopter-guide .content h2 { font-size: min(1.75rem, 48px); }
      }
    </style>
    <script type="application/ld+json">
      {"@context":"https://schema.org","@type":"Article","headline":"Paper Helicopter for Kids","datePublished":"2026-09-19","dateModified":"2026-09-19","author":{"@type":"Organization","name":"Kid Activity Lab"},"image":"https://kidactivitylab.com/assets/paper-helicopter/cut-fold-map.png"}
    </script>
  </head>
  <body>
    <header class="site-header"><nav class="nav" aria-label="Main navigation">
      <a class="brand" href="/">Kid Activity Lab</a>
      <div class="nav-links"><a href="/">Home</a><a href="../original/">Original</a><a href="../cards.html">Cards</a></div>
    </nav></header>
    <main><article class="bridge-article helicopter-guide">
      <header class="hero bridge-guide-hero">
        <p class="kicker">Fold | drop | notice</p>
        <h1>Paper Helicopter for Kids</h1>
        <p class="dek">Will folded paper turn as it falls? An adult prepares the model; your child can release it or watch.</p>
        <section class="bridge-start-panel" aria-labelledby="helicopter-start-title">
          <h2 id="helicopter-start-title">Before you start</h2>
          <p><strong>Get:</strong> ordinary paper, pencil and adult-controlled scissors. A ruler helps; no printer, clips or added weights.</p>
          <p><strong>Adult:</strong> mark, cut and fold using the map below. Clear a landing space away from faces, feet and younger children's reach.</p>
          <p><strong>Child:</strong> follow a release-not-throw demonstration. Say, "Let go and watch." The adult can do the releasing instead.</p>
          <p class="bridge-stop"><strong>Stop:</strong> if paper is mouthed, thrown toward people, scraps or scissors become accessible, or close supervision cannot continue. Stay on the floor; no climbing.</p>
        </section>
        <p><strong>Research-backed, not family-tested by Kid Activity Lab.</strong> Readiness and adult control matter more than an age label.</p>
        <p><a href="#prepare">Prepare the paper</a> · <a href="#drop">First drop</a> · <a href="#rescue">Not turning?</a></p>
      </header>
      <div class="content">
        <section id="prepare" aria-labelledby="prepare-title">
          <h2 id="prepare-title">Adult preparation: three cuts, then folds</h2>
          <p>Start with a rectangle about three times as tall as wide. With a ruler, use <strong>7 cm wide by 21 cm tall</strong>. Keep it upright. These are KAL's suggested proportions, not NASA measurements or a flight-tested design.</p>
          <ol class="steps">
            <li><strong>Mark before cutting.</strong> Put a dot halfway across the width, 8 cm below the top. Draw a center cut line from the top to this dot. Draw a shallow sloping fold from the dot to each outside edge, ending 8.5 cm below the top.</li>
            <li><strong>Mark the lower body.</strong> Halfway down the rectangle, draw a cut inward from each side through its outer third only. Leave the middle third uncut. From each cut endpoint draw a fold straight down to the bottom. Mark a base fold 2.5 cm above the bottom.</li>
            <li><strong>Make the three cuts.</strong> Cut down to the top dot, then inward to the two side endpoints. Do not connect the side cuts or extend the top cut into the body.</li>
            <li><strong>Fold the blades oppositely.</strong> On their sloping lines, bend one blade toward you and the other away, roughly a quarter-turn. They should stick out on opposite sides of the upright body, not lie flat against it.</li>
            <li><strong>Fold the body.</strong> Fold both lower side panels inward over the middle strip, one over the other. Fold the bottom up through all layers. Put scissors and scraps away before the child handles the model.</li>
          </ol>
          <details><summary>No ruler? Mark by halving the gaps</summary>
            <p>Use the short edge of an ordinary A4 or Letter sheet as the rectangle's height; estimate a width one-third as long. Use a spare straight paper edge to draw lines. Light edge pinches can locate halfway marks without creasing the whole model.</p>
            <ol>
              <li>Find halfway down. Find halfway between the top and that level, then halfway between this new level and the original halfway mark. Put the center dot there.</li>
              <li>Between the dot's level and the halfway level, halve the gap, then halve it again toward the dot. Put the two outside ends of the sloping folds at this level.</li>
              <li>At halfway down, estimate three equal widths for the two side-cut endpoints. Mark the base fold by halving the bottom half, then halving its lowest section again.</li>
            </ol>
            <p>This approximates the map; it is not an assurance that marking differences will work. If the marks remain confusing, pause rather than guess a cut.</p>
          </details>
          <figure class="helicopter-map">
            <img src="../assets/paper-helicopter/cut-fold-map.png" alt="Upright rectangle: center cut stops where two sloping blade folds meet. Two side cuts halfway down stop at the middle third. Side panels fold inward and the bottom folds up. No cut crosses the middle body." width="900" height="1400">
            <figcaption>Original KAL planning map. Dashed red lines are cuts ending at dots; solid green lines are folds. The black outline is the edge of the rectangle. Not a print-to-scale template.</figcaption>
          </figure>
        </section>
        <section id="drop" aria-labelledby="drop-title">
          <h2 id="drop-title">Let go and watch</h2>
          <p>The adult checks the folds, holds the lower body with the blades above it, and releases over the clear landing area without a push or twist. Keep both feet on the floor. Notice turning, fluttering or falling straight down; none is a required result.</p>
          <p>Invite one child to try while you stay beside them. Retrieve the model together before another release. A seated child can watch an adult release or try from a reachable height; lower drops may look different. Stop whenever continuing is unwanted.</p>
        </section>
        <section id="rescue" aria-labelledby="rescue-title">
          <h2 id="rescue-title">If it does not turn</h2>
          <p>Adult check: are the blades folded in opposite directions and free to move? Are both side panels folded in and the base folded up? Is the middle body still joined? Reset those folds and try one more release with the same paper and height.</p>
          <p>If the body is cut through, start with a fresh blank; do not patch it with clips or weights. If the model still does not turn, end the trial or compare what it did. Do not climb higher to force a result. These checks are suggestions, not guaranteed repairs.</p>
        </section>
        <section id="finish" aria-labelledby="finish-title">
          <h2 id="finish-title">One change, or finish here</h2>
          <p>For another experiment, the adult can fold the base up once more. Keep the paper and release height the same and ask, "What changed?" No stopwatch, race or written record is needed.</p>
          <p>Keep preparation materials with the adult during mixed-age play. Offer watching or choosing the next try instead of handling small scraps. Collect the model and every offcut when finished. Preparation time, play duration and cleanup effort have not been measured.</p>
        </section>
        <section id="evidence" aria-labelledby="evidence-title">
          <h2 id="evidence-title">Sources and limits</h2>
          <p><a href="https://www.jpl.nasa.gov/edu/resources/project/make-a-paper-mars-helicopter-2/">NASA JPL's paper helicopter project</a> and its <a href="https://d2pn8kiwq2w21t.cloudfront.net/documents/paperhelicopter_worksheet.pdf">worksheet geometry</a>, checked September 19, 2026, supply the folded-body approach and base-fold comparison. We omit elevated drops, clips and classroom measurement tasks. This falling paper model is not powered flight.</p>
          <p>KAL's proportions, no-ruler marking route, adult/child roles, recovery and stop wording are editorial adaptations. The <a href="https://www.cpsc.gov/s3fs-public/blk_media_5015_0.pdf">CPSC Art and Craft Safety Guide</a>, checked September 18, informs general supervision and tool control; it does not certify this activity.</p>
          <p>No family or physical flight test by KAL is recorded. Rotation, marking tolerance, comprehension, enjoyment, learning, repeatability, mess and safety outcomes are unknown. Ordinary paper is the default; cardstock and tissue are not established equivalents.</p>
        </section>
        <p><a href="../cards.html">Choose another activity</a></p>
      </div>
    </article></main>
    <footer class="site-footer"><p>Kid Activity Lab</p></footer>
  </body>
</html>
'''


def cup_tower_guide_html():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Paper Cup Tower for Kids: Start, Rebuild, Change | Kid Activity Lab</title>
    <meta name="description" content="Start a paper cup tower with two matching cups. Find clear adult setup, stacking versus nesting, collapse rescues, one-change ideas and cleanup boundaries.">
    <link rel="icon" href="data:,">
    <link rel="canonical" href="https://kidactivitylab.com/articles/paper-cup-tower-kids.html">
    <link rel="stylesheet" href="../styles.css?v=cup-tower-1">
    <script type="application/ld+json">
      {"@context":"https://schema.org","@type":"Article","headline":"Paper Cup Tower for Kids","datePublished":"2026-09-17","dateModified":"2026-10-27","author":{"@type":"Organization","name":"Kid Activity Lab"},"image":"https://kidactivitylab.com/assets/cup-tower/paper-cup-start.webp"}
    </script>
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links"><a href="/">Home</a><a href="../original/">Original</a><a href="../cards.html">Cards</a></div>
      </nav>
    </header>
    <main>
      <article class="bridge-article cup-tower-guide">
        <header class="hero bridge-guide-hero">
          <p class="kicker">Stack | notice | rebuild</p>
          <h1>Paper Cup Tower for Kids</h1>
          <p class="dek">Can two cups balance bottom-to-bottom? Try a tiny tower, take it apart, and decide what to change.</p>
          <section class="bridge-start-panel" aria-labelledby="cup-start-title">
            <h2 id="cup-start-title">Fit and start</h2>
            <p><strong>Try it when:</strong> your child can place a cup gently and follow a stop cue; an adult can stay beside the setup.</p>
            <p><strong>Get:</strong> two matching intact lightweight paper cups, one optional matching spare, and a clear firm level surface.</p>
            <p class="bridge-stop"><strong>Adult check and stop:</strong> check that the cups balance on a low surface away from edges and feet. Stay beside every child who can reach the setup; keep spare cups and loose pieces out of younger children's reach. Skip this activity if you cannot attend. Stop after mouthing, throwing, damaged cups, climbing, or unwanted collapse. Keep the build low and remove torn pieces.</p>
            <ol>
              <li><strong>Adult:</strong> put one cup upside down. Demonstrate a second cup right side up on it, with the two closed bottoms touching.</li>
              <li><strong>Child:</strong> remove the top cup, then try placing it back. Say, "Can you let go gently?"</li>
            </ol>
          </section>
          <p><strong>Research-backed, not family-tested by Kid Activity Lab.</strong> Cup fit and child readiness matter more than an age label.</p>
        </header>
        <figure class="hero-image">
          <img src="../assets/cup-tower/paper-cup-start.webp" alt="Two paper cups touching at their closed bottoms: the lower cup upside down and the upper cup upright, with one spare cup beside them" width="1672" height="941">
          <figcaption>AI-generated setup illustration, not a family-test photo or proof that your cups will balance.</figcaption>
        </figure>
        <div class="content">
          <section id="first-try" aria-labelledby="first-try-title">
            <h2 id="first-try-title">One small build, then reset</h2>
            <p>The adult first checks whether these cups can balance in the shown arrangement. Work on the floor or a low surface, away from edges and feet. Pick cups suitable for every child who can reach them; avoid heavy, cracked or sharp-edged substitutes.</p>
            <p><strong>Adult role:</strong> stay beside every child who can reach the setup; keep spare cups and loose pieces out of younger children's reach. Skip this activity if you cannot attend. Stop after mouthing, throwing, damaged cups, climbing, or unwanted collapse, and remove torn pieces. Do not turn the cups into steps or build near a face.</p>
            <ol class="steps">
              <li>Separate nested cups. Put the first cup opening-down, with its wide rim resting flat.</li>
              <li>Place the second cup opening-up, so its closed bottom rests on the first cup's closed bottom. Do not push one cup inside the other.</li>
              <li>Let go gently and notice whether it stays, leans or falls. An adult may guide the child's hand or model again.</li>
              <li>Lift off the top cup before rebuilding. There is no height target, race or requirement to continue.</li>
            </ol>
          </section>
          <section id="one-change" aria-labelledby="one-change-title">
            <h2 id="one-change-title">Choose one change</h2>
            <p>If the two-cup start works and another try is welcome, rebuild with the same cups on the same surface. Try adding the spare cup upside down on top, with its wide rim meeting the upper cup's rim. Keep it low; skip the addition if the cups wobble or cannot meet cleanly.</p>
            <p>Ask, "What moved when you let go?" Look for staying, leaning or falling, not a promised stronger or taller result. Then remove the top cup first and reset. Changing the number of cups is enough for one try; no ruler or written record is needed.</p>
          </section>
          <section id="rescue" aria-labelledby="rescue-title">
            <h2 id="rescue-title">If the build stalls</h2>
            <dl class="bridge-troubleshooting">
              <div><dt>Cups disappear inside each other</dt><dd>That is nesting. Separate them, turn the lower cup opening-down and show the two closed bottoms touching. Nesting can be the chosen play instead; it is not the same balance test.</dd></div>
              <div><dt>It falls straight away</dt><dd>Check for dents and a sloping or soft surface. Try a different matching pair. If they still cannot balance, place cups side by side and arrange a row rather than forcing a tower.</dd></div>
              <div><dt>Placement is difficult</dt><dd>Let the child choose where the base goes while the adult models the top placement. Return to one cup or arrange a row; no tall build is required.</dd></div>
              <div><dt>Falling is no longer welcome</dt><dd>Take the cups apart gently instead of knocking them down. End or switch activities when the child wants to stop.</dd></div>
            </dl>
          </section>
          <section id="fit" aria-labelledby="fit-title">
            <h2 id="fit-title">Make it fit the child and space</h2>
            <p><strong>Materials:</strong> the default is matching lightweight paper cups. Intact lightweight plastic cups of uniform size are another source-supported material, but the adult must recheck their shape and balance; they are not automatically interchangeable. Skip glass, metal cans and damaged cups.</p>
            <p><strong>Placement and reach:</strong> use a reachable firm low surface, with supported seating if helpful. One child can choose an arrangement while the adult places cups. For mixed ages, take turns with the same small set and keep the spare with the adult; do not give a younger child loose pieces just to keep them occupied.</p>
            <p><strong>Sound or attention:</strong> take cups apart rather than making a collapse, and offer one placement at a time. These are editorial options, not therapeutic guidance or evidence that an adaptation will work for a particular child.</p>
            <p><strong>Preparation:</strong> separate and inspect cups, clear the area, and demonstrate once. No cutting, glue, tape, measurement or recording is needed. Duration and mess have not been measured by Kid Activity Lab.</p>
          </section>
          <section id="cleanup" aria-labelledby="cleanup-title">
            <h2 id="cleanup-title">Finish with the cups accounted for</h2>
            <p>Remove the upper cups first. Collect the whole set together; the adult removes damaged cups and loose pieces promptly and stores the set out of younger children's reach. Do not reuse damaged cups for play. Supervision and these stop boundaries are not a safety assurance.</p>
          </section>
          <section id="evidence" aria-labelledby="evidence-title">
            <h2 id="evidence-title">Sources and limits</h2>
            <p>Sources rechecked October 27, 2026. Kid Activity Lab has not recorded a family test of this setup. Timing, comprehension, engagement, enjoyment, learning, repeatability, frustration, mess and safety outcomes remain unknown.</p>
            <ul>
              <li><a href="https://discovere.org/engineering-activities/tallest-cup-tower/">DiscoverE: Tallest Cup Tower</a> supplies the bottom-to-bottom demonstration and uniform paper/plastic cup materials. Its classroom competition uses a much larger set; this reduced, noncompetitive start is a KAL editorial adaptation.</li>
              <li><a href="https://www.education.com/activity/article/design-challenge-creating-a-cup-tower/">Education.com: Creating a Cup Tower</a> describes paper-cup redesign with height measurement and recording. We do not reproduce that measured lesson or promise its outcomes.</li>
              <li><a href="https://growingupnyc.cityofnewyork.us/brainbuilding/cup-tower/">Growing Up NYC: Cup Tower</a> supports adult demonstration and rebuild play with plastic cups, not this exact paper-cup quantity or geometry.</li>
            </ul>
            <p>The small-set sequence, readiness cues, scripts, rescues, adaptations, supervision and cleanup wording are editorial synthesis. The illustration does not establish physical performance. There is no guaranteed cup fit or child outcome.</p>
          </section>
          <section class="related" aria-labelledby="related-title">
            <h2 id="related-title">Another small build</h2>
            <ul>
              <li><a href="../cards/cup-tower.html">Compact Cup Tower card</a></li>
              <li><a href="paper-bridge-challenge-kids.html">Paper Bridge Challenge</a></li>
              <li><a href="cardboard-box-car-ramp-preschoolers.html">Cardboard Car Ramp</a></li>
            </ul>
          </section>
        </div>
      </article>
    </main>
    <footer class="site-footer"><p><a href="../cards.html">Back to activity cards</a></p></footer>
  </body>
</html>
'''


def ball_maze_guide_html():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Cardboard Ball Maze for Kids | Kid Activity Lab</title>
    <meta name="description" content="Make a no-cut cardboard ball maze with a shallow box lid, three chunky blocks, and one large lightweight ball. Get clear setup, rescue, stop, and reset steps.">
    <link rel="icon" href="data:,">
    <link rel="canonical" href="https://kidactivitylab.com/articles/cardboard-ball-maze-kids.html">
    <link rel="stylesheet" href="../styles.css?v=ball-maze-guide-3">
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "Cardboard Ball Maze for Kids",
        "description": "Make a no-cut cardboard ball maze with a shallow box lid, three movable chunky blocks, and one large lightweight ball.",
        "datePublished": "2026-09-14",
        "dateModified": "2026-09-14",
        "author": {
          "@type": "Organization",
          "name": "Kid Activity Lab"
        },
        "image": "https://kidactivitylab.com/assets/ball-maze/ball-maze-box-guide.webp"
      }
    </script>
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

    <main>
      <article class="maze-article">
        <header class="hero maze-guide-hero">
          <p class="kicker">Build - roll - change</p>
          <h1>Cardboard Ball Maze for Kids</h1>
          <p class="dek">Can you guide one big ball through three movable walls? Start with a wide path, tilt gently, then change one wall.</p>

          <section class="maze-start-panel" aria-labelledby="maze-start-title">
            <h2 id="maze-start-title">Fit and start</h2>
            <p><strong>Try it when:</strong> your child can move a chunky block and follow a stop cue. An adult can steady or tilt the lid if two-handed control is still difficult.</p>
            <p><strong>Get:</strong> one shallow intact box lid, three chunky blocks, and one large lightweight foam ball chosen by the adult for every child who can reach the setup.</p>
            <ol>
              <li><strong>Adult:</strong> put the lid flat in a clear floor or low-table space and keep control of the ball between runs.</li>
              <li><strong>Child:</strong> place three blocks as wide walls, then hold two sides and tilt gently to guide the ball through.</li>
            </ol>
            <p><strong>Mission:</strong> move the ball from one end of the lid to the other without lifting it by hand.</p>
            <p class="maze-stop"><strong>Stop:</strong> if the ball or a block goes in a mouth, is thrown, or leaves the clear area; if the lid is lifted near a face or shaken hard; or if cardboard or a block becomes damaged.</p>
          </section>
        </header>

        <figure class="hero-image">
          <img src="../assets/ball-maze/ball-maze-box-guide.webp" alt="An intact shallow cardboard lid with three loose chunky block walls, one large blue foam ball, and an adult hand steadying the edge" width="1672" height="941">
          <figcaption>AI-generated setup illustration. It shows the no-cut three-wall default; it is not a Kid Activity Lab family-test photo.</figcaption>
        </figure>

        <div class="content">
          <section id="first-run" aria-labelledby="first-run-title">
            <h2 id="first-run-title">Make one wide path</h2>
            <ol class="steps">
              <li>Put the empty lid flat. Check that it is intact, shallow, and easy for the child to hold at two sides.</li>
              <li>Place three chunky blocks flat inside as loose walls. Leave gaps much wider than the ball.</li>
              <li>The adult puts the large lightweight ball at one end, then moves both hands outside the rolling area.</li>
              <li>Hold two sides of the lid and tilt only enough to make the ball roll. Guide it around the walls to the other end.</li>
              <li>Put the lid flat. The adult takes control of the ball before the next run or cleanup.</li>
            </ol>
            <div class="callout">
              <strong>Adult boundary:</strong> Stay beside the setup, keep the lid below face level, and keep the surrounding path clear. The adult controls when the ball enters and leaves the lid. Stop and reset after hard shaking, throwing, mouthing, a spill, or damaged material.
            </div>
          </section>

          <section id="one-wall" aria-labelledby="one-wall-title">
            <h2 id="one-wall-title">Change one wall</h2>
            <p>Keep the same lid, ball, starting side, and two walls. Move only the third wall, then run the maze again. The visible comparison is the route the ball takes; no learning or engagement outcome is assumed.</p>
            <div class="maze-compare-grid">
              <section>
                <h3>First route</h3>
                <p>Keep all three walls far apart. Make one calm run from start to finish.</p>
              </section>
              <section>
                <h3>One change</h3>
                <p>Turn or move one wall while the lid is flat. Try the same starting side again.</p>
              </section>
            </div>
            <p><strong>Parent phrase:</strong> "Which wall should we move?" If the child wants to rearrange everything, let the comparison end and use the blocks for open maze building.</p>
          </section>

          <section id="troubleshooting" aria-labelledby="troubleshooting-title">
            <h2 id="troubleshooting-title">If the maze is not working</h2>
            <dl class="maze-troubleshooting">
              <div>
                <dt>The ball gets stuck</dt>
                <dd>Put the lid flat. Move one wall farther away, then restart from the same end.</dd>
              </div>
              <div>
                <dt>The path is too hard</dt>
                <dd>Remove one wall or line up all three as a simple zigzag with very wide gaps.</dd>
              </div>
              <div>
                <dt>The blocks slide too much</dt>
                <dd>Use wider, flatter blocks and gentler tilts. Loose walls are meant to move; do not add tape or glue.</dd>
              </div>
              <div>
                <dt>The lid tips or bends</dt>
                <dd>Stop. Use a smaller intact lid, keep it on the floor, or let the adult tilt while the child directs the route.</dd>
              </div>
              <div>
                <dt>The child is done</dt>
                <dd>Put the lid flat, let the adult remove the ball, and end the activity. Completing another run is optional.</dd>
              </div>
            </dl>
          </section>

          <section id="adapt" aria-labelledby="adapt-title">
            <h2 id="adapt-title">Change the role, not the promise</h2>
            <div class="maze-adapt-grid">
              <section>
                <h3>With a younger child nearby</h3>
                <p>The adult keeps the ball and spare blocks out of reach between runs. Use only pieces selected for every child who can reach the setup, and end the activity if mouthing or throwing begins.</p>
              </section>
              <section>
                <h3>If tilting is difficult</h3>
                <p>Keep the lid on a low surface. The child can place or point to walls while the adult makes the gentle tilt. This changes the motor role, not the maze mission.</p>
              </section>
            </div>
            <p>Specific sensory preferences, mobility needs, and assistive-technology requirements were not established by this research. Adjust sound, touch, posture, and participation with the child in front of you rather than treating the age label as a complete fit decision.</p>
          </section>

          <section id="cleanup" aria-labelledby="cleanup-title">
            <h2 id="cleanup-title">Reset and clean up</h2>
            <p>Put the lid flat. The adult removes and stores the ball first. Return the blocks, inspect the lid for torn or bent edges, and recycle it if it is damaged. Check the floor before a younger child returns.</p>
          </section>

          <section id="evidence" aria-labelledby="evidence-title">
            <h2 id="evidence-title">What this guide knows</h2>
            <p>Kid Activity Lab built this guide from current public activity references and editorial synthesis. Kid Activity Lab has not recorded a family test of this setup. Exact duration, mess, comprehension, engagement, enjoyment, learning, repeatability, frustration, and safety outcomes are unknown.</p>
            <p>PBS, KID Museum, Children's Home Society of California, and the Children's Museum of Southern Minnesota each document a box or tray maze with a rolling ball. Several source versions use fixed walls, craft tools, or small balls. The intact lid, loose chunky blocks, large lightweight ball, and three-wall default on this page are Kid Activity Lab's research-backed editorial variant, not a tested source outcome.</p>
            <ul>
              <li><a href="https://www.pbs.org/video/box-lid-mazes-with-engineering-full-steam-ahead-hdtadv/">PBS KidVision Pre-K: Box Lid Mazes</a></li>
              <li><a href="https://kid-museum.org/make-it/kid-arcade/">KID Museum: KID Arcade</a></li>
              <li><a href="https://chs-ca.org/chs-blog/games-and-activities-you-can-make-at-home/">Children's Home Society of California: At-home activities</a></li>
              <li><a href="https://www.cmsouthernmn.org/2020/03/29/ball-maze-cmsmathome/">Children's Museum of Southern Minnesota: Ball Maze</a></li>
            </ul>
          </section>

          <section class="related" aria-label="Related Ball Maze routes">
            <h2>Choose a shorter or broader route</h2>
            <ul>
              <li><a href="../cards/ball-maze-box.html">Use the compact Ball Maze Box card</a></li>
              <li><a href="../collections/engineering-activities-for-4-year-olds.html#ball-maze-box">Compare preschool engineering challenges</a></li>
              <li><a href="../collections/building-activities-for-4-year-olds.html">Browse preschool building activities</a></li>
            </ul>
          </section>
        </div>
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def tape_road_guide_html():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Painter's Tape Road for Kids | Kid Activity Lab</title>
    <meta name="description" content="Make one simple painter's tape road with a parking mission, a removable-board fallback, clear adult roles, direct stops, route changes, and cleanup steps.">
    <link rel="icon" href="data:,">
    <link rel="canonical" href="https://kidactivitylab.com/articles/painter-tape-road-kids.html">
    <link rel="stylesheet" href="../styles.css?v=tape-road-guide-1">
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "Painter's Tape Road for Kids",
        "description": "Make one short painter's tape road and parking place using an adult-selected surface or removable board.",
        "datePublished": "2026-09-15",
        "dateModified": "2026-09-15",
        "author": {
          "@type": "Organization",
          "name": "Kid Activity Lab"
        },
        "image": "https://kidactivitylab.com/assets/tape-road/painter-tape-road-guide.webp"
      }
    </script>
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

    <main>
      <article class="road-article">
        <header class="hero road-guide-hero">
          <p class="kicker">Choose - tape - drive</p>
          <h1>Painter's Tape Road for Kids</h1>
          <p class="dek">Make one short road and one parking place. The child drives; the adult chooses the surface, handles the tape, and clears it away.</p>

          <section class="road-start-panel" aria-labelledby="road-start-title">
            <h2 id="road-start-title">Fit and start</h2>
            <p><strong>Try it when:</strong> your child can push a large toy vehicle and follow a stop cue.</p>
            <p><strong>Get:</strong> surface-appropriate removable painter's tape chosen by the adult, plus one or two large intact toy vehicles selected for every child who can reach them.</p>
            <p><strong>Choose the surface:</strong> follow the tape maker's instructions. Test one strip in an inconspicuous area and remove it. If the floor or finish is unknown or unsuitable, use a large cardboard sheet, table, or tray the adult is willing to tape.</p>
            <ol>
              <li><strong>Adult:</strong> make one short road and a parking box.</li>
              <li><strong>Child:</strong> push one vehicle along the road and park it.</li>
            </ol>
            <p class="road-stop"><strong>Stop:</strong> for peeling, chewing, or wrapping tape; throwing or mouthing vehicles; leaving the activity area; or any change to the surface.</p>
          </section>
        </header>

        <figure class="hero-image">
          <img src="../assets/tape-road/painter-tape-road-guide.webp" alt="A short blue painter's tape road and parking box on a removable cardboard board with two large intact toy cars and an adult holding the tape roll" width="1672" height="941">
          <figcaption>AI-generated setup illustration. It shows the removable-board default; it is not a Kid Activity Lab family-test photo or proof of surface performance.</figcaption>
        </figure>

        <div class="content">
          <section id="one-road" aria-labelledby="one-road-title">
            <h2 id="one-road-title">Run one short road</h2>
            <ol class="steps">
              <li>The adult reads the tape guidance, checks the chosen surface, applies one test strip, and removes it.</li>
              <li>On the selected surface or removable board, the adult lays one broad tape route with one gentle turn.</li>
              <li>Add one parking box at the end. Put one adult-selected vehicle at the start.</li>
              <li>The child pushes the vehicle along the road and into the parking box.</li>
              <li>The adult keeps loose tape out of reach and stays close enough to stop the listed actions or a surface change.</li>
            </ol>
            <div class="callout">
              <strong>Keep the roles clear:</strong> the adult selects, applies, checks, and removes the tape. The child owns the drive-and-park mission.
            </div>
          </section>

          <section id="one-change" aria-labelledby="one-change-title">
            <h2 id="one-change-title">Change one short segment</h2>
            <p>Keep the same surface, vehicle, starting place, and parking box. The adult moves or adds one short segment, then the child drives the route again. Notice only the visible route change; no engagement or learning outcome is assumed.</p>
            <div class="road-compare-grid">
              <section>
                <h3>First route</h3>
                <p>Use one gentle turn and a parking box close enough to see from the start.</p>
              </section>
              <section>
                <h3>One change</h3>
                <p>Add a second turn or move the parking box. Keep the route visible as the same vehicle follows it.</p>
              </section>
            </div>
          </section>

          <section id="troubleshooting" aria-labelledby="troubleshooting-title">
            <h2 id="troubleshooting-title">If the road is not working</h2>
            <dl class="road-troubleshooting">
              <div>
                <dt>The tape lifts</dt>
                <dd>Stop. The adult removes the loose strip and either follows the product guidance for a different suitable surface or switches to an untaped vehicle route.</dd>
              </div>
              <div>
                <dt>The vehicle does not fit the parking box</dt>
                <dd>The adult widens the parking box or selects another large intact vehicle that can park inside it.</dd>
              </div>
              <div>
                <dt>The mission is unclear</dt>
                <dd>Point to the parking box and say, "Drive here." Remove extra vehicles and buildings.</dd>
              </div>
              <div>
                <dt>The route is too complex</dt>
                <dd>Return to one straight road and one parking box. A city is optional, not the starting requirement.</dd>
              </div>
              <div>
                <dt>The child is done</dt>
                <dd>End the drive. The adult removes the tape and stores the vehicles; another route is optional.</dd>
              </div>
            </dl>
          </section>

          <section id="adapt" aria-labelledby="adapt-title">
            <h2 id="adapt-title">Keep the same mission in a different space</h2>
            <div class="road-adapt-grid">
              <section>
                <h3>Small or seated route</h3>
                <p>Use a table, tray, or large cardboard sheet with one straight road. The child can push the vehicle from a seated position while the adult steadies the removable surface.</p>
              </section>
              <section>
                <h3>Younger child nearby</h3>
                <p>Select only large intact vehicles appropriate for every child who can reach the setup. Keep the tape roll and loose strips with the adult, and stop if mouthing or throwing begins.</p>
              </section>
            </div>
            <p>Specific sensory preferences, mobility needs, and assistive-technology requirements were not established by this research. Change the surface, posture, sound, or role with the child in front of you rather than treating an age label as a complete fit decision.</p>
          </section>

          <section id="cleanup" aria-labelledby="cleanup-title">
            <h2 id="cleanup-title">Let the adult close the activity</h2>
            <p>Park the vehicles and move them out of the work area. The adult removes the tape using the selected product's guidance, checks the surface, gathers every loose strip, and stores the tape and vehicles out of reach.</p>
          </section>

          <section id="evidence" aria-labelledby="evidence-title">
            <h2 id="evidence-title">What this guide knows</h2>
            <p>Kid Activity Lab built this guide from current public activity references, manufacturer guidance, public parent questions, and editorial synthesis. Kid Activity Lab has not recorded a family test of this setup. Exact duration, mess, comprehension, engagement, enjoyment, independence, learning, repeatability, frustration, surface performance, and safety outcomes are unknown.</p>
            <p>The Genius of Play documents a tape track and a table or tray alternative. 3M and FrogTape publish product-specific surface, testing, and removal guidance. Mississippi State Extension documents a masking-tape road as one block-play setup. Those sources do not establish that every tape suits every surface or that the Kid Activity Lab version was used successfully.</p>
            <ul>
              <li><a href="https://thegeniusofplay.org/tgop/genius/play-ideas-tips/play-ideas/tape-track.aspx">The Genius of Play: Tape Track</a></li>
              <li><a href="https://www.scotchblue.com/3M/en_US/p/d/b00035531/">3M ScotchBlue: product-specific surface and removal guidance</a></li>
              <li><a href="https://www.scotchblue.com/3M/en_US/scotchblue/your-questions/">3M ScotchBlue: painter's tape questions</a></li>
              <li><a href="https://www.frogtape.com/how-to-use/painters-tape">FrogTape: How to Use Painter's Tape</a></li>
              <li><a href="https://4h.extension.msstate.edu/resources/publications/block-play">Mississippi State University Extension: Block Play</a></li>
            </ul>
          </section>

          <section class="related" aria-label="Related Painter's Tape Road routes">
            <h2>Choose a shorter or broader route</h2>
            <ul>
              <li><a href="../cards/tape-road.html">Use the compact Tape Road card</a></li>
              <li><a href="../cards/tape-city.html">Add one building with the Tape City variation</a></li>
              <li><a href="../collections/indoor-activities-for-preschoolers.html#tape-road-delivery">Compare indoor activity jobs</a></li>
            </ul>
          </section>
        </div>
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="../cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def page_html(page):
    if page.get("preschool_stem_layout"):
        return preschool_stem_page_html(page)
    if page.get("indoor_layout"):
        return indoor_page_html(page)
    if page.get("engineering_layout"):
        return engineering_page_html(page)
    if page.get("building_layout"):
        return building_page_html(page)
    root = rel_root(page["path"])
    activity_html = "\n".join(activity_card(page_activity(page, key)) for key in page["activities"])
    rows = "\n".join(
        f'''            <tr>
              <td>{esc(page_activity(page, key)["title"])}</td>
              <td>{esc(page_activity(page, key)["time"])}</td>
              <td>{esc(page_activity(page, key)["mess"])}</td>
              <td>{esc(page_activity(page, key)["materials"])}</td>
            </tr>'''
        for key in page["activities"]
    )
    start_block = ""
    if page.get("start_block"):
        block = page["start_block"]
        start_block = f'''

        <section class="callout start-block">
          <h2>{esc(block["title"])}</h2>
          <p>{esc(block["body"])}</p>
          <p><a href="{esc(block["url"])}">{esc(block["link_text"])}</a></p>
        </section>'''
    chooser = ""
    if page.get("chooser"):
        chooser_rows = "\n".join(
            f'''            <tr>
              <td>{esc(situation)}</td>
              <td>{chooser_pick_cell(pick)}</td>
              <td>{esc(reason)}</td>
            </tr>'''
            for situation, pick, reason in page["chooser"]
        )
        chooser_title = page.get("chooser_title", "Tired-parent chooser")
        chooser_label = page.get("chooser_label", "Tired-parent activity chooser")
        chooser = f'''

        <section class="chooser">
          <h2>{esc(chooser_title)}</h2>
          <div class="table-wrap seo-table" aria-label="{esc(chooser_label)}">
            <table>
              <thead>
                <tr>
                  <th>Parent situation</th>
                  <th>Best pick</th>
                  <th>Why</th>
                </tr>
              </thead>
              <tbody>
{chooser_rows}
              </tbody>
            </table>
          </div>
        </section>'''
    extra_sections = start_block + chooser
    after_activity_sections = "".join(
        f'''

        <section class="related">
          <h2>{esc(section["title"])}</h2>
          <p>{esc(section["body"])}</p>
        </section>'''
        for section in page.get("after_activity_sections", [])
    )
    related = "".join(f"<li>{esc(query)}</li>" for query in page["related"])
    canonical = f"{BASE_URL}/{page['path']}"
    head_style = f'\n    <style>{page["head_style"]}</style>' if page.get("head_style") else ""
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(page["title"])}</title>
    <meta name="description" content="{esc(page["description"])}">
    <link rel="canonical" href="{esc(canonical)}">
    <link rel="stylesheet" href="{root}styles.css?v={CSS_VERSION}">{head_style}
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="/">Home</a>
          <a href="{root}original/">Original</a>
          <a href="{root}cards.html">Cards</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="hero">
        <p class="kicker">{esc(page["kicker"])}</p>
        <h1>{esc(page["h1"])}</h1>
        <p class="dek">{esc(page["intro"])}</p>
      </section>

      <section class="seo-page">
        <div class="callout">
          <strong>Quick pick:</strong> {esc(page["tip"])}
        </div>{extra_sections}

        <div class="table-wrap seo-table" aria-label="Activity chooser">
          <table>
            <thead>
              <tr>
                <th>Activity</th>
                <th>Time</th>
                <th>Mess</th>
                <th>Materials</th>
              </tr>
            </thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>

        <section class="seo-activity-grid" aria-label="Activity ideas">
{activity_html}
        </section>{after_activity_sections}

        <section class="related">
          <h2>Searches this page is built for</h2>
          <p>Parents often search these closely related phrases, so this page keeps the wording practical instead of clever.</p>
          <ul>
            <li>{esc(page["primary"])}</li>
            {related}
          </ul>
        </section>

        <section class="related">
          <h2>How to choose safely</h2>
          <p>Match the activity to the child in front of you, not just the age label. Use larger pieces when younger siblings are nearby, keep ramps and towers low, and supervise tape, pom poms, small blocks, water, rubber bands, or anything that can go in a mouth.</p>
        </section>
      </section>
    </main>

    <footer class="site-footer">
      <p><a href="{root}cards.html">Browse all activity cards</a></p>
    </footer>
  </body>
</html>
'''


def update_keyword_targets():
    out = ROOT / "data" / "seo_keyword_targets.csv"
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            lineterminator="\n",
            fieldnames=[
                "url",
                "page_type",
                "primary_keyword",
                "related_keywords",
                "evidence",
                "index_status",
                "first_2_month_impression_expectation",
            ],
        )
        writer.writeheader()
        for page in PAGES + MANUAL_SEO_TARGETS:
            writer.writerow(
                {
                    "url": "/" + page["path"],
                    "page_type": page["page_type"],
                    "primary_keyword": page["primary"],
                    "related_keywords": "; ".join(page["related"]),
                    "evidence": page.get(
                        "evidence",
                        "Google autocomplete variant observed 2026-06-26; SERP has broad roundup competitors.",
                    ),
                    "index_status": page.get("index_status", "index"),
                    "first_2_month_impression_expectation": page.get(
                        "first_2_month_impression_expectation",
                        "20-150 if indexed; higher only if Google trusts the new domain quickly.",
                    ),
                }
            )


def main():
    from contributor_pages import sync_contributor_pages

    for page in PAGES:
        path = SITE / page["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page_html(page))
    for redirect in LEGACY_REDIRECTS:
        path = SITE / redirect["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(legacy_redirect_html(redirect))
    rocket_path = SITE / "articles" / "paper-straw-rocket.html"
    rocket_path.parent.mkdir(parents=True, exist_ok=True)
    rocket_path.write_text(paper_straw_rocket_guide_html())
    helicopter_path = SITE / "articles" / "paper-helicopter-kids.html"
    helicopter_path.parent.mkdir(parents=True, exist_ok=True)
    helicopter_path.write_text(paper_helicopter_guide_html())
    cup_tower_path = SITE / "articles" / "paper-cup-tower-kids.html"
    cup_tower_path.parent.mkdir(parents=True, exist_ok=True)
    cup_tower_path.write_text(cup_tower_guide_html())
    ball_maze_path = SITE / "articles" / "cardboard-ball-maze-kids.html"
    ball_maze_path.parent.mkdir(parents=True, exist_ok=True)
    ball_maze_path.write_text(ball_maze_guide_html())
    tape_road_path = SITE / "articles" / "painter-tape-road-kids.html"
    tape_road_path.parent.mkdir(parents=True, exist_ok=True)
    tape_road_path.write_text(tape_road_guide_html())
    update_keyword_targets()
    sync_contributor_pages()
    print(f"generated {len(PAGES)} SEO pages and {len(LEGACY_REDIRECTS)} legacy redirects")


if __name__ == "__main__":
    main()
