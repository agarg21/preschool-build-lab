import csv
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE_URL = "https://kidactivitylab.com"
CSS_VERSION = "nav-stable-2"


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
        "title": "Paper Roll Drop",
        "url": "../cards/paper-roll-drop.html",
        "ages": "3-5",
        "time": "2 min",
        "mess": "low",
        "help": "medium",
        "materials": "paper roll, pom poms",
        "best_for": "fine motor practice, repetition, color naming",
        "steps": ["Tape or hold a tube.", "Drop a pom pom.", "Catch it.", "Try another color."],
        "parent": "Use large items if younger siblings are nearby.",
    },
    "pom-pom-drop": {
        "title": "Pom Pom Drop",
        "url": "../cards/pom-pom-drop.html",
        "ages": "3-5",
        "time": "3 min",
        "mess": "low",
        "help": "medium",
        "materials": "cardboard tube, pom poms",
        "best_for": "hand control, sorting, quiet play",
        "steps": ["Set up a tube.", "Drop pom poms.", "Catch them.", "Sort by color."],
        "parent": "Pom poms can be choking hazards.",
    },
    "magnetic-tile-house": {
        "title": "Magnetic Tile House",
        "url": "../cards/magnetic-tile-house.html",
        "ages": "3-6",
        "time": "3 min",
        "mess": "low",
        "help": "low",
        "materials": "magnetic tiles, small toy",
        "best_for": "spatial play, pretend play, quiet time",
        "steps": ["Make walls.", "Add a roof.", "Put a toy inside.", "Open the door."],
        "parent": "Do not use cracked magnetic tiles.",
    },
    "magnetic-tile-ideas": {
        "title": "Magnetic Tile Builds",
        "url": "../cards/magnetic-tile-ideas.html",
        "ages": "3-6",
        "time": "2 min",
        "mess": "low",
        "help": "low",
        "materials": "magnetic tiles",
        "best_for": "open-ended building, patterns, independent play",
        "steps": ["Pick tiles.", "Make a wall.", "Add a roof.", "Change the shape."],
        "parent": "Check magnets and tile edges before play.",
    },
    "block-tower": {
        "title": "Block Tower",
        "url": "../cards/block-tower.html",
        "ages": "3-6",
        "time": "2 min",
        "mess": "low",
        "help": "low",
        "materials": "blocks",
        "best_for": "counting, balance, quick resets",
        "steps": ["Stack blocks.", "Count them.", "Make it taller.", "Start over."],
        "parent": "Keep towers low around toddlers.",
    },
    "car-ramp-distance-test": {
        "title": "Car Ramp Distance Test",
        "url": "../cards/car-ramp-distance-test.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "low",
        "help": "medium",
        "materials": "ramp, tape, toy cars",
        "best_for": "early STEM, measuring, prediction",
        "steps": ["Roll a car.", "Mark where it stops.", "Try another car.", "Compare the marks."],
        "parent": "Keep the rolling area clear.",
    },
    "paper-plate-ramp": {
        "title": "Paper Plate Ramp",
        "url": "../cards/paper-plate-ramp.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "low",
        "help": "medium",
        "materials": "paper plate, car, books",
        "best_for": "ramp experiments, flexible building",
        "steps": ["Make a slope.", "Place a car.", "Let it roll.", "Change the ramp."],
        "parent": "Adult helps bend or tape the plate.",
    },
    "tape-train-tracks": {
        "title": "Tape Train Tracks",
        "url": "../cards/tape-train-tracks.html",
        "ages": "3-6",
        "time": "5 min",
        "mess": "low",
        "help": "low",
        "materials": "masking tape, toy trains",
        "best_for": "pretend play, floor maps, rainy days",
        "steps": ["Make tracks.", "Add a station.", "Drive the train.", "Change tracks."],
        "parent": "Test tape before sticking it down.",
    },
    "lego-color-tower": {
        "title": "LEGO or DUPLO Color Tower",
        "url": "../cards/lego-color-tower.html",
        "ages": "4-6",
        "time": "3 min",
        "mess": "low",
        "help": "medium",
        "materials": "LEGO or DUPLO",
        "best_for": "color sorting, counting, small builds",
        "steps": ["Pick a color.", "Stack bricks.", "Count them.", "Try another color."],
        "parent": "Use DUPLO if younger siblings are nearby.",
    },
    "duplo-games": {
        "title": "DUPLO Games",
        "url": "../cards/duplo-games.html",
        "ages": "3-5",
        "time": "3 min",
        "mess": "low",
        "help": "low",
        "materials": "DUPLO blocks",
        "best_for": "simple rules, matching, reset-friendly games",
        "steps": ["Pick blocks.", "Make a tiny game.", "Play one round.", "Switch the rule."],
        "parent": "Keep small LEGO away from younger kids.",
    },
    "tube-sculpture": {
        "title": "Tube Sculpture",
        "url": "../cards/tube-sculpture.html",
        "ages": "4-6",
        "time": "8 min",
        "mess": "medium",
        "help": "medium",
        "materials": "cardboard tubes, tape",
        "best_for": "building, art, vertical balance",
        "steps": ["Stack tubes.", "Tape gently.", "Make it taller.", "Start over."],
        "parent": "Adult helps if tubes need cutting.",
    },
    "tape-city": {
        "title": "Tape City",
        "url": "../cards/tape-city.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "low",
        "help": "low",
        "materials": "painter tape, cars, blocks",
        "best_for": "pretend play, maps, collaborative play",
        "steps": ["Make roads.", "Add buildings.", "Drive cars.", "Move the city."],
        "parent": "Test tape before sticking it down.",
    },
    "sock-ball-roll": {
        "title": "Sock Ball Roll",
        "url": "../cards/sock-ball-roll.html",
        "ages": "3-6",
        "time": "2 min",
        "mess": "low",
        "help": "low",
        "materials": "rolled socks, books",
        "best_for": "indoor gross motor, hallway play",
        "steps": ["Roll socks.", "Make a tunnel.", "Roll through.", "Move the tunnel."],
        "parent": "Use soft socks and keep feet off the books.",
    },
    "spoon-transfer": {
        "title": "Spoon Transfer",
        "url": "../cards/spoon-transfer.html",
        "ages": "3-5",
        "time": "2 min",
        "mess": "low",
        "help": "medium",
        "materials": "spoon, two bowls, large objects",
        "best_for": "fine motor practice, focus, hand control",
        "steps": ["Fill one bowl.", "Scoop one thing.", "Move it.", "Do it again."],
        "parent": "Use large non-choking objects.",
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
        "time": "5 min",
        "mess": "low",
        "help": "medium",
        "materials": "small box, toy cars",
        "best_for": "pretend play, toy car storage, naming",
        "steps": ["Open a box.", "Park cars.", "Make spaces.", "Drive out."],
        "parent": "Adult handles any cutting.",
    },
    "blanket-river": {
        "title": "Blanket River",
        "url": "../cards/blanket-river.html",
        "ages": "3-6",
        "time": "2 min",
        "mess": "low",
        "help": "medium",
        "materials": "blanket, blocks",
        "best_for": "pretend play, indoor movement, bridge building",
        "steps": ["Lay a blanket.", "Build a bridge.", "Cross the river.", "Move the bridge."],
        "parent": "No running on blankets.",
    },
    "sink-or-float-tray": {
        "title": "Sink or Float Tray",
        "url": "../cards/sink-or-float-tray.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "medium",
        "help": "medium",
        "materials": "shallow water tray, safe household objects",
        "best_for": "prediction, sorting, early science talk",
        "steps": ["Pick one object.", "Guess sink or float.", "Test it.", "Sort and try another."],
        "parent": "Use a shallow tray and stay next to water.",
    },
    "ice-melt-rescue": {
        "title": "Ice Melt Rescue",
        "url": "../cards/ice-melt-rescue.html",
        "ages": "4-6",
        "time": "8 min",
        "mess": "medium",
        "help": "medium",
        "materials": "ice cube, warm water, spoon, tray",
        "best_for": "temperature, observation, patient testing",
        "steps": ["Put ice on a tray.", "Touch with a spoon.", "Add warm drops.", "Watch it melt."],
        "parent": "Use warm water, not hot water.",
    },
    "magnet-hunt": {
        "title": "Magnet Hunt",
        "url": "../cards/magnet-hunt.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "low",
        "help": "medium",
        "materials": "large magnet, safe objects",
        "best_for": "sorting, prediction, material testing",
        "steps": ["Pick an object.", "Guess if it sticks.", "Try the magnet.", "Make two piles."],
        "parent": "Use one large magnet and avoid tiny magnets or batteries.",
    },
    "shadow-shape-match": {
        "title": "Shadow Shape Match",
        "url": "../cards/shadow-shape-match.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "low",
        "help": "medium",
        "materials": "flashlight, blocks, wall",
        "best_for": "light, shapes, cause and effect",
        "steps": ["Pick a block.", "Shine the light.", "Find the shadow.", "Move it closer."],
        "parent": "Do not shine flashlights into eyes.",
    },
    "foil-boat-test": {
        "title": "Foil Boat Test",
        "url": "../cards/foil-boat-test.html",
        "ages": "4-6",
        "time": "8 min",
        "mess": "medium",
        "help": "medium",
        "materials": "foil, water tray, pennies or blocks",
        "best_for": "buoyancy, engineering, redesign",
        "steps": ["Shape a foil boat.", "Float it.", "Add one piece.", "Change the boat."],
        "parent": "Use a shallow water tray and supervise small pieces.",
    },
    "straw-bridge": {
        "title": "Straw Bridge",
        "url": "../cards/straw-bridge.html",
        "ages": "4-6",
        "time": "8 min",
        "mess": "low",
        "help": "medium",
        "materials": "straws, tape, two cups",
        "best_for": "engineering, balance, testing strength",
        "steps": ["Put cups apart.", "Tape straws together.", "Make a bridge.", "Test one toy."],
        "parent": "Adult handles tape and keeps the bridge low.",
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
        "time": "6 min",
        "mess": "low",
        "help": "medium",
        "materials": "ramp, towel, foil, toy car",
        "best_for": "friction, prediction, toy car testing",
        "steps": ["Roll on a plain ramp.", "Add a towel.", "Try foil.", "Compare the rolls."],
        "parent": "Keep the ramp low and the rolling path clear.",
    },
    "wind-tower-test": {
        "title": "Wind Tower Test",
        "url": "../cards/wind-tower-test.html",
        "ages": "4-6",
        "time": "6 min",
        "mess": "low",
        "help": "medium",
        "materials": "blocks, paper fan",
        "best_for": "structure, stability, redesign",
        "steps": ["Build a tower.", "Fan it gently.", "See what falls.", "Build it wider."],
        "parent": "Keep towers low and fan gently.",
    },
    "pattern-path": {
        "title": "Pattern Path",
        "url": "../cards/pattern-path.html",
        "ages": "4-6",
        "time": "4 min",
        "mess": "low",
        "help": "low",
        "materials": "blocks, tiles, or paper squares",
        "best_for": "patterns, sequencing, early math",
        "steps": ["Pick two colors.", "Make a path.", "Say the pattern.", "Add one more."],
        "parent": "Use pieces too large to mouth if younger siblings are nearby.",
    },
    "measuring-tape-jumps": {
        "title": "Measuring Tape Jumps",
        "url": "../cards/measuring-tape-jumps.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "low",
        "help": "medium",
        "materials": "painter tape, toy, floor",
        "best_for": "measurement, comparing distance, active math",
        "steps": ["Make tape marks.", "Jump a toy.", "See where it lands.", "Try again."],
        "parent": "Use a toy jump, not kid jumping, in small rooms.",
    },
    "balance-scale-baskets": {
        "title": "Balance Basket Scale",
        "url": "../cards/balance-scale-baskets.html",
        "ages": "4-6",
        "time": "7 min",
        "mess": "low",
        "help": "medium",
        "materials": "hanger, two baskets, safe objects",
        "best_for": "weight, comparison, early math language",
        "steps": ["Add one object.", "Add another side.", "Watch it tilt.", "Try to balance."],
        "parent": "Adult sets up the hanger and supervises the scale.",
    },
    "color-mixing-cups": {
        "title": "Color Mixing Cups",
        "url": "../cards/color-mixing-cups.html",
        "ages": "4-6",
        "time": "6 min",
        "mess": "medium",
        "help": "medium",
        "materials": "clear cups, water, food coloring",
        "best_for": "prediction, color science, careful pouring",
        "steps": ["Fill two cups.", "Add two colors.", "Pour together.", "Name the new color."],
        "parent": "Use tiny drops and protect the table.",
    },
    "sound-shaker-match": {
        "title": "Sound Shaker Match",
        "url": "../cards/sound-shaker-match.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "low",
        "help": "medium",
        "materials": "closed containers, rice, blocks, pasta",
        "best_for": "sound, listening, matching evidence",
        "steps": ["Shake one container.", "Guess what is inside.", "Shake another.", "Match the sounds."],
        "parent": "Seal containers well and supervise small fillers.",
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
        "title": "Water Drop Race",
        "url": "../cards/water-drop-race.html",
        "ages": "4-6",
        "time": "5 min",
        "mess": "medium",
        "help": "medium",
        "materials": "wax paper, water drops, straw",
        "best_for": "surface tension, gentle breath control, observation",
        "steps": ["Put drops on wax paper.", "Blow gently.", "Race two drops.", "Try a bigger drop."],
        "parent": "Use gentle blowing and keep water away from electronics.",
    },
}


PAGES = [
    {
        "path": "ages/activities-for-3-year-olds-at-home.html",
        "page_type": "age",
        "primary": "activities for 3 year olds at home",
        "title": "Activities for 3 Year Olds at Home | Kid Activity Lab",
        "h1": "Activities for 3 year olds at home.",
        "kicker": "Age 3",
        "description": "Low-prep activities for 3 year olds at home using blocks, tape, cups, paper rolls, toy cars, and household materials.",
        "intro": "Three year olds usually do best with short, visible steps and activities that can be reset quickly. These picks avoid long craft instructions and start with things you probably already have out.",
        "tip": "Choose low-help ideas first: stacking, rolling, roads, tunnels, and simple pretend play.",
        "activities": ["cup-tower", "cardboard-car-ramp", "tape-road", "paper-roll-drop", "duplo-games", "block-tower", "magnetic-tile-house", "sock-ball-roll"],
        "related": ["games for 3 year olds at home", "fun activities for 3 year olds at home", "indoor activities for 3 year olds at home"],
    },
    {
        "path": "ages/activities-for-4-year-olds-at-home.html",
        "page_type": "age",
        "primary": "activities for 4 year olds at home",
        "title": "Activities for 4 Year Olds at Home | Kid Activity Lab",
        "h1": "Activities for 4 year olds at home.",
        "kicker": "Age 4",
        "description": "Easy activities for 4 year olds at home: building, pretend play, ramps, tape roads, blocks, magnetic tiles, and low-mess STEM prompts.",
        "intro": "Four year olds can handle a little more planning: make a road, test a ramp, build a bridge, or set up a tiny city. Keep the activity small enough that the child still owns the work.",
        "tip": "If you need one activity now, choose the cardboard ramp. If your child wants a challenge, open the original age-4 STEM test pack. If you need quiet pretend play, choose Tape City or Magnetic Tile Builds.",
        "chooser_title": "Start here by parent situation",
        "chooser_label": "Age 4 at-home chooser",
        "chooser": [
            ("I need a proven low-prep activity", ("Cardboard ramp parent guide", "../articles/cardboard-box-car-ramp-preschoolers.html"), "Google is already finding this page, and the setup is fast: cardboard, books, toy cars."),
            ("I want a 5-10 minute STEM challenge", ("Original age-4 STEM test pack", "../collections/original-stem-activities-for-4-year-olds.html"), "Five activities with parent jobs, kid steps, safety notes, and stop rules."),
            ("I want more STEM choices", ("STEM activities for 4 year olds", "../ages/stem-activities-for-4-year-olds.html"), "A broader chooser for ramps, bridges, shadows, towers, and water tests."),
            ("I need quiet pretend play", "Tape City or Magnetic Tile Builds", "Good for low-mess play when you can do one quick setup."),
        ],
        "activity_overrides": {
            "car-ramp-distance-test": {
                "title": "Cardboard ramp for toy cars",
                "url": "../articles/cardboard-box-car-ramp-preschoolers.html",
                "link_text": "Open ramp parent guide",
                "materials": "cardboard, books, toy cars",
                "steps": ["Lean cardboard on books.", "Roll one car.", "Change the ramp height.", "Mark where the car stops."],
                "parent": "Keep the ramp low and do not let kids climb on the setup.",
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
        "h1": "No-prep activities for preschoolers.",
        "kicker": "No prep",
        "description": "No-prep preschool activities parents can start quickly with household items: cups, blocks, toy cars, tape, socks, books, and cardboard.",
        "intro": "This page is for the moment when you need something now. The activities use visible materials, short steps, and quick cleanup. No printable, no long supply list, no complicated craft setup.",
        "tip": "If you have only two minutes, choose cups, blocks, socks, or a single toy car ramp.",
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
        "tip": "Clear one short floor lane, place a low empty basket at the far end, and roll two bundled socks toward it. Walk to reset. If throwing or running starts, stop and clear the lane.",
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
            ("I need one thing now", ("Soft-Sock Target Roll", "#sock-target-roll"), "One short, clear floor lane; bundled socks and a low basket", "Place the target, mark the roll line, and stay beside the lane"),
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
                "mission": "Roll a bundled pair of socks into a low basket, then walk it back to the same line.",
                "materials": "two bundled pairs of socks, one low empty laundry basket",
                "adult_role": "Place the basket on the floor at the end of a short clear lane. Choose the roll line and stay beside it.",
                "steps": ["Put one sock bundle on the floor.", "Roll it toward the basket.", "Walk to collect both bundles and reset."],
                "rescue": "Bring the basket closer or slide one sock bundle across the floor instead of aiming into it.",
                "stop": "Stop if socks are thrown, anyone runs through the lane, or another person or pet enters the target area.",
                "parent": "Clear stairs, doors, breakables, cords, furniture corners, and active walkways from the line before starting.",
                "url": "../cards/sock-ball-roll.html",
                "link_text": "Open the base sock-roll card",
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
                "stop": "Stop if paper or tape lifts, the path slides, running starts, or the route reaches a doorway or walkway.",
                "parent": "Check the floor and spacing yourself. Stay close enough to stop the route when the surface or movement no longer fits.",
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
                "slug": "blanket-toy-crossing",
                "title": "Blanket Toy Crossing",
                "job": "Pretend with a floor boundary",
                "mission": "Make a route that lets one large toy travel from one side of a flat blanket to the other.",
                "materials": "one blanket, large lightweight blocks or firm cushions, one large toy",
                "adult_role": "Spread the blanket flat in a clear area and state that the route is for the toy, not for feet.",
                "steps": ["Place one support near each blanket edge.", "Move the toy along or between the supports.", "Move the toy across and back once."],
                "rescue": "Lay the supports flat as a stepping path for the toy.",
                "stop": "Stop if the blanket bunches, anyone runs or climbs, or the setup enters a doorway or walkway.",
                "parent": "Keep the blanket flat, use only stable floor-level supports, and stay close enough to end the setup immediately.",
                "url": "../cards/blanket-river.html",
                "link_text": "Open the base blanket-river card",
            },
        ],
        "activities": ["tape-road", "tape-train-tracks", "sock-ball-roll", "blanket-river", "cardboard-car-ramp", "cup-tower", "magnetic-tile-house", "block-tower", "tape-city"],
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
        "h1": "Independent activities for preschoolers.",
        "kicker": "Independent play",
        "description": "Independent preschool activities with low-prep materials, simple steps, low mess, and parent check notes for safer quiet play.",
        "intro": "Independent does not mean unsupervised. It means the child can understand the work after a quick parent setup. The best picks have repeatable actions: stack, sort, park, build, roll, reset.",
        "tip": "Start the first round together, then leave one tiny challenge: build three towers, park all red cars, or make a house for one toy.",
        "activities": ["magnetic-tile-house", "magnetic-tile-ideas", "block-tower", "cup-tower", "duplo-games", "paper-roll-drop", "tape-road", "box-garage"],
        "related": ["independent work for preschoolers", "independent art activities for preschoolers", "independent learning activities for preschoolers"],
    },
    {
        "path": "collections/fine-motor-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "fine motor activities for preschoolers",
        "title": "Fine Motor Activities for Preschoolers | Kid Activity Lab",
        "h1": "Fine motor activities for preschoolers.",
        "kicker": "Fine motor",
        "description": "Fine motor activities for preschoolers using pom poms, paper rolls, blocks, tape, spoons, cups, and household objects.",
        "intro": "Fine motor practice does not have to look like worksheets. Preschoolers build hand strength and control while dropping, stacking, peeling, scooping, connecting, and balancing.",
        "tip": "Use large pieces first. If an item can fit in a mouth, treat it as a direct-supervision activity.",
        "activities": ["paper-roll-drop", "pom-pom-drop", "spoon-transfer", "lego-color-tower", "duplo-games", "magnetic-tile-ideas", "cup-tower", "tape-road"],
        "related": ["fine motor activities for preschoolers at home", "fine motor activities for preschoolers pdf", "fine motor activities for preschoolers printables"],
    },
    {
        "path": "collections/stem-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "stem activities for preschoolers",
        "title": "STEM Activities for Preschoolers | Kid Activity Lab",
        "h1": "STEM activities for preschoolers.",
        "kicker": "STEM",
        "description": "Simple STEM activities for preschoolers at home: ramps, bridges, towers, magnetic tile builds, measuring games, and engineering challenges.",
        "intro": "For preschoolers, STEM can be simple: build something, test it, notice what happened, and change one thing. These activities avoid long explanations and let the object do the teaching.",
        "tip": "Use the same prompt on every activity: What do you think will happen if we change one thing?",
        "activities": ["car-ramp-distance-test", "paper-bridge", "cardboard-car-ramp", "paper-plate-ramp", "cup-tower", "tube-sculpture", "magnetic-tile-ideas", "lego-color-tower"],
        "related": ["engineering activities for preschoolers", "science activities for preschoolers", "stem projects for preschoolers"],
    },
    {
        "path": "ages/stem-activities-for-4-year-olds.html",
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
            "body": "Best first pick: start with the Kid Activity Lab original test pack. It has five 5-10 minute activities with parent jobs, read-aloud kid steps, stop rules, and notes to capture what actually worked.",
            "link_text": "Open the original age-4 STEM test pack",
            "url": "../collections/original-stem-activities-for-4-year-olds.html",
        },
        "chooser": [
            ("I need low mess", "Ramp Detective or Shadow Builder", "Dry materials, fast reset, and easy to stop."),
            ("My child likes stories", "Bridge Rescue", "The toy crossing the river gives the test a reason."),
            ("I need movement but not chaos", "Windproof Tower", "Building and rebuilding gives energy a job."),
            ("We can handle water", "Tiny Boat Cargo Test", "High engagement, but needs close supervision."),
            ("It is almost bedtime", "Shadow Builder", "Calm, low mess, and easy to end after two shadows."),
        ],
        "activity_overrides": {
            "car-ramp-distance-test": {
                "title": "Ramp Detective car test",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#ramp-detective",
                "link_text": "Open in original test pack",
                "materials": "low ramp, towel or placemat, toy car",
                "best_for": "ramps, prediction, measuring",
                "steps": ["Roll on a plain ramp.", "Add one road surface.", "Guess what will happen.", "Mark where the car stops."],
            },
            "paper-bridge": {
                "title": "Bridge Rescue paper bridge",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#bridge-rescue",
                "link_text": "Open in original test pack",
                "best_for": "engineering, story play, testing strength",
            },
            "shadow-shape-match": {
                "title": "Shadow Builder",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#shadow-builder",
                "link_text": "Open in original test pack",
                "best_for": "light, shapes, calm cause and effect",
            },
            "wind-tower-test": {
                "title": "Windproof Tower",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#windproof-tower",
                "link_text": "Open in original test pack",
                "best_for": "structure, stability, redesign",
            },
            "foil-boat-test": {
                "title": "Tiny Boat Cargo Test",
                "url": "../collections/original-stem-activities-for-4-year-olds.html#tiny-boat-cargo-test",
                "link_text": "Open in original test pack",
                "materials": "foil, shallow water tray, large cargo pieces",
                "best_for": "buoyancy, water play, redesign",
                "steps": ["Shape a foil boat.", "Float it.", "Add one large passenger.", "Pinch the sides higher."],
                "parent": "Use one inch of water, large cargo only, and stay next to the tray.",
            },
            "ramp-texture-test": {
                "materials": "ramp, towel or paper, toy car",
                "steps": ["Roll on a plain ramp.", "Add a towel.", "Try paper or a placemat.", "Compare the rolls."],
            },
        },
        "activities": ["car-ramp-distance-test", "paper-bridge", "foil-boat-test", "magnet-hunt", "shadow-shape-match", "pattern-path", "wind-tower-test", "color-mixing-cups", "ramp-texture-test"],
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
        "description": "Choose preschool engineering activities with paper, foil, blocks, cups, straws, and toy cars. Each challenge includes a test and one redesign.",
        "intro": "Pick a small problem, give the child a clear mission, test the build, and change one thing. These research-backed challenges use household materials and show the adult job without taking over the design.",
        "tip": "Start with Paper Bridge: two low books, one sheet of paper, and one toy car. If the paper bends, fold it once and test again.",
        "engineering_layout": True,
        "evidence_note": "Kid Activity Lab created this chooser from current source and search research. We have not family-tested these setups. The age range, adult roles, rescue steps, and first changes are editorial guidance; timing, mess, engagement, learning, repeatability, and safety outcomes are unknown.",
        "image": {
            "src": "../assets/preschool-engineering/engineering-challenge-materials.webp",
            "alt": "Paper bridge, foil boat, cup tower, box-lid maze, straws, and painter tape arranged as engineering challenge materials.",
            "width": "1672",
            "height": "941",
            "caption": "Illustration of possible setups. This is not a Kid Activity Lab family-test photo.",
        },
        "chooser_title": "Choose by what is already out",
        "chooser_label": "Preschool engineering activity chooser",
        "chooser": [
            ("Paper and a toy car", ("Paper Bridge", "#paper-bridge"), "Set two low books in place, then let the child own the bridge."),
            ("A tray can get wet", ("Foil Boat", "#foil-boat-test"), "Stay beside the shallow tray and add large cargo one piece at a time."),
            ("Blocks or cups are ready", [("Wind Tower", "#wind-tower-test"), ("Cup Doorway", "#cup-tower")], "Keep the build low and run one gentle test."),
            ("Toy cars are the hook", [("Target Ramp", "#car-ramp-distance-test"), ("Box Garage", "#box-garage")], "Set the boundary or target; let the child decide the change."),
            ("The child wants more building", [("Straw Bridge", "#straw-bridge"), ("Ball Maze", "#ball-maze-box")], "Handle cutting or tape and leave the layout decisions to the child."),
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
                "materials": "one sheet of paper, two low books, one toy car",
                "mission": "Build a paper road that carries the car across the gap.",
                "adult_role": "Place two low, stable books on the floor and keep them from sliding.",
                "steps": ["Lay the paper across the books.", "Send the car across once.", "Look at where the paper bends."],
                "test": "Can the car cross without the paper dropping into the gap?",
                "redesign": "Fold the paper lengthwise once, then test the same car again.",
                "rescue": "Move the books closer together and keep the first sheet flat.",
                "stop": "Stop if the books slide, the child climbs on them, or the paper test is no longer welcome.",
                "parent": "Keep the bridge on the floor and use books the child can lift only with help.",
            },
            "straw-bridge": {
                "slug": "straw-bridge",
                "title": "Straw Bridge",
                "materials": "drinking straws, painter tape, two paper cups, one lightweight toy",
                "mission": "Join straws into a bridge that holds one toy between the cups.",
                "adult_role": "Handle any cutting and tear short pieces of tape before the build begins.",
                "steps": ["Put the cups a short distance apart.", "Join straws into one bridge deck.", "Set the toy in the middle."],
                "test": "Does the bridge stay across the cups while the toy rests on it?",
                "redesign": "Tape one more straw under the middle and test the same toy.",
                "rescue": "Move the cups closer or test without the toy first.",
                "stop": "Stop if straws or tape go in a mouth, a cup will not stay put, or the child wants to leave the build.",
                "parent": "Use paper or silicone straws when possible and keep all cut pieces accounted for.",
            },
            "foil-boat-test": {
                "slug": "foil-boat-test",
                "title": "Foil Boat",
                "materials": "foil, shallow tray, water, two large wooden blocks",
                "mission": "Shape a boat that floats while carrying two large cargo blocks.",
                "adult_role": "Add a shallow layer of water, place the tray on a wipeable surface, and stay beside it.",
                "steps": ["Pinch the foil into an open boat.", "Float the empty boat.", "Add the blocks one at a time."],
                "test": "Does the boat stay above the water with both blocks inside?",
                "redesign": "Pinch the sides higher or make the bottom wider, then test again.",
                "rescue": "Remove one block and widen the boat before the next try.",
                "stop": "Stop if foil or cargo goes in a mouth, water leaves the tray area, or the child moves away from the setup.",
                "parent": "Use large cargo only, keep water shallow, and empty the tray as soon as the activity ends.",
            },
            "paper-chain-test": {
                "slug": "paper-chain-test",
                "title": "Paper Chain Reach Test",
                "materials": "pre-cut paper strips, painter tape, one book",
                "mission": "Build a paper chain long enough to wrap around the book and meet at the top.",
                "adult_role": "Pre-cut wide strips and hold the book still while the child joins loops.",
                "steps": ["Make and tape one paper loop.", "Thread each new strip through the last loop.", "Wrap the chain around the book."],
                "test": "Do the two ends meet without pulling a loop apart?",
                "redesign": "Add one loop or replace the narrowest loop with a wider strip.",
                "rescue": "Use a smaller book or start with three large loops already joined.",
                "stop": "Stop if tape or strips go in a mouth, the book tips, or joining loops has become an adult-only job.",
                "parent": "Keep scissors out of the play area and use a light book with rounded corners.",
            },
            "wind-tower-test": {
                "slug": "wind-tower-test",
                "title": "Wind Tower",
                "materials": "six blocks, one folded-paper fan",
                "mission": "Build a six-block tower that stays up through three gentle fan waves.",
                "adult_role": "Keep the tower low and do the same three gentle fan waves for each test.",
                "steps": ["Build with all six blocks.", "Move hands away.", "Ask the adult to fan three times."],
                "test": "Is the tower still standing after the third fan wave?",
                "redesign": "Move the widest blocks to the bottom and test again.",
                "rescue": "Begin with four blocks and a base two blocks wide.",
                "stop": "Stop if blocks are thrown, stacked for climbing, or the child does not want another wind test.",
                "parent": "Use lightweight blocks and keep the tower below the child's shoulders.",
            },
            "car-ramp-distance-test": {
                "slug": "car-ramp-distance-test",
                "title": "Target Ramp",
                "materials": "low ramp, one toy car, painter tape target",
                "mission": "Change the ramp so the car stops as close as possible to the tape target.",
                "adult_role": "Set a low ramp on the floor, test the tape first, and keep the rolling lane clear.",
                "steps": ["Roll the car from the same starting spot.", "Put the target near where it stopped.", "Change one part of the ramp."],
                "test": "After the change, does the car stop closer to the target?",
                "redesign": "Raise or lower the ramp by one book and roll the same car again.",
                "rescue": "Move the target closer and use a shorter rolling lane.",
                "stop": "Stop if the ramp or books slide, cars leave the clear lane, or rolling becomes throwing.",
                "parent": "Keep the ramp away from stairs, feet, pets, and breakable objects.",
            },
            "ball-maze-box": {
                "slug": "ball-maze-box",
                "title": "Box-Lid Ball Maze",
                "materials": "shallow box lid, chunky blocks, one ping-pong ball",
                "mission": "Make a path that lets the ball travel from one corner to the opposite corner.",
                "adult_role": "Choose a shallow lid, confirm the ball is too large to swallow, and keep the lid on the floor or table.",
                "steps": ["Build walls inside the lid.", "Place the ball in one corner.", "Tilt the lid gently toward the goal."],
                "test": "Can the ball reach the opposite corner without getting trapped?",
                "redesign": "Move one wall to open the place where the ball stopped.",
                "rescue": "Use only three walls and make a wide path first.",
                "stop": "Stop if the ball goes in a mouth, blocks leave the lid, or tilting becomes shaking.",
                "parent": "Use one large lightweight ball, not a marble, bead, or other small sphere.",
            },
            "box-garage": {
                "slug": "box-garage",
                "title": "Two-Car Box Garage",
                "materials": "open small box, two toy cars, painter tape",
                "mission": "Design two parking bays and an exit wide enough for one car to roll out.",
                "adult_role": "Provide an already-open box, handle any cutting, and test tape on the box first.",
                "steps": ["Park both cars inside the box.", "Mark two bays with tape.", "Roll one car through the exit."],
                "test": "Do both cars fit, and can one leave without hitting the other?",
                "redesign": "Move one tape line or widen the exit, then park both cars again.",
                "rescue": "Use one car first and remove the bay lines.",
                "stop": "Stop if the box tears into sharp edges, tape goes in a mouth, or cutting would be needed during play.",
                "parent": "Adult handles all cutting and removes loose tape or torn cardboard immediately.",
            },
            "cup-tower": {
                "slug": "cup-tower",
                "title": "Cup Doorway",
                "materials": "six lightweight paper cups, one toy car",
                "mission": "Build a cup doorway that stands while the toy car drives through it.",
                "adult_role": "Choose light cups, set the build on the floor, and keep the car lane short.",
                "steps": ["Build two short cup walls.", "Place one cup across the top.", "Drive the car through the opening."],
                "test": "Can the car pass through without touching the cup walls?",
                "redesign": "Move the two walls farther apart and rebuild the top.",
                "rescue": "Remove the top cup and make a wide gate first.",
                "stop": "Stop if cups are thrown, crushed into sharp edges, or used as steps.",
                "parent": "Use empty lightweight cups only and keep the structure below the child's shoulders.",
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
        "description": "Simple science experiments for 4 year olds using water, ice, magnets, shadows, colors, sound, ramps, and household materials.",
        "intro": "The strongest science experiments for 4 year olds are short and observable. The child should be able to predict, test, notice, and try again without waiting for a long result.",
        "tip": "Pick experiments where the result is easy to see: sinking, floating, sticking, melting, mixing, rolling, or making a sound.",
        "activities": ["sink-or-float-tray", "ice-melt-rescue", "magnet-hunt", "shadow-shape-match", "color-mixing-cups", "sound-shaker-match", "water-drop-race", "ramp-texture-test"],
        "related": ["easy science experiments for 4 year olds", "science activities for 4 year olds at home", "preschool science experiments"],
    },
    {
        "path": "collections/math-activities-for-4-year-olds-at-home.html",
        "page_type": "collection",
        "primary": "math activities for 4 year olds at home",
        "title": "Math Activities for 4 Year Olds at Home | Kid Activity Lab",
        "h1": "Math activities for 4 year olds at home.",
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
        "description": "No-prep STEM activities for 4 year olds using cups, blocks, socks, paper, toy cars, flashlights, magnets, ramps, and household objects.",
        "intro": "This page is for the moment when you want STEM play without gathering a supply list. Most of these start with one object, one question, and one quick test.",
        "tip": "Choose the activity that matches what is already out: blocks, cups, toy cars, paper, socks, or a flashlight.",
        "activities": ["cup-tower", "block-tower", "sock-ball-roll", "paper-bridge", "magnet-hunt", "shadow-shape-match", "ramp-texture-test", "pattern-path", "tape-road"],
        "related": ["easy stem activities for kids", "no prep stem activities preschool", "quick stem activities for preschoolers"],
    },
    {
        "path": "collections/building-activities-for-4-year-olds.html",
        "page_type": "collection",
        "primary": "building activities for preschoolers",
        "title": "Building Activities for Preschoolers | Kid Activity Lab",
        "h1": "Building activities for preschoolers.",
        "route_label": "Building activities for 4 year olds",
        "kicker": "Preschool building | Age 4 route included",
        "description": "Choose preschool building activities with blocks, cups, magnetic tiles, paper, straws, tubes, and blankets. Start by material and the kind of structure a child wants to make.",
        "intro": "Choose what is already out, then give the child one structure job: make a place, build up, span a gap, shape a sculpture, or build big on the floor. These research-backed routes keep the design with the child and make the adult setup visible.",
        "tip": "Start with a low block home for one favorite toy. Put out six to ten large blocks, set the toy beside them, and ask: Where could the toy go?",
        "building_layout": True,
        "evidence_note": "Kid Activity Lab created this chooser from current source and search research. We have not family-tested these setups. The age-four route, material choices, adult roles, rescue steps, and stop boundaries are editorial guidance; timing, mess, engagement, learning, repeatability, and safety outcomes are unknown.",
        "readiness_note": "Choose materials that are appropriate for the youngest child who can reach the build. Remove cracked or damaged materials and any piece with an exposed magnet. If any child may mouth materials, stay within reach and watch continuously; skip straws, loose tape, and other loose pieces and use larger solid blocks instead.",
        "image": {
            "src": "../assets/preschool-building/building-material-chooser.webp",
            "alt": "Illustration of large blocks, paper cups, a paper bridge, a cardboard-tube sculpture, and a blanket path as preschool building material choices.",
            "width": "1672",
            "height": "941",
            "caption": "Illustrated material routes, not a Kid Activity Lab family-test photo or a product recommendation.",
        },
        "chooser_title": "Choose by what is ready and what to build",
        "chooser_label": "Preschool building activity chooser",
        "chooser": [
            ("Large blocks or tiles", [("Toy Home", "#magnetic-tile-house"), ("Wide-Base Tower", "#block-tower")], "Put out a small set and let the child decide the shape."),
            ("Paper cups", ("Cup Doorway", "#cup-tower"), "Keep the build on the floor and the toy lane short."),
            ("Paper, straws, or two low books", [("Paper Path", "#paper-bridge"), ("Straw Span", "#straw-bridge")], "Set the supports; handle cutting or tape."),
            ("Cardboard tubes and painter tape", ("Tube Sculpture", "#tube-sculpture"), "Prepare short tape pieces and leave the arrangement to the child."),
            ("Blanket and large blocks", ("Blanket Crossing", "#blanket-river"), "Clear the floor and keep the build for toys, not climbing."),
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
                "materials": "six to ten intact large magnetic tiles or blocks, one large toy",
                "mission": "Make a place with an opening where the toy can go inside and come back out.",
                "adult_role": "Choose intact pieces, place the toy beside them, and keep the build on the floor.",
                "steps": ["Make two side walls.", "Leave an opening for the toy.", "Add a back wall or roof if wanted."],
                "rescue": "Use three walls and leave the roof off.",
                "stop": "Stop if a tile is cracked, a magnet is exposed, or pieces are thrown or mouthed.",
                "parent": "Follow the toy maker's age guidance and remove damaged magnetic pieces immediately.",
            },
            "magnetic-tile-ideas": {
                "slug": "magnetic-tile-ideas",
                "title": "Connected Rooms",
                "job": "Enclose a space",
                "materials": "intact large magnetic tiles or blocks, two large toys",
                "mission": "Make two connected spaces so each toy has a place.",
                "adult_role": "Offer a small set of intact pieces and ask where an opening should go.",
                "steps": ["Make one open shape.", "Build a second shape beside it.", "Join them with a wall or doorway."],
                "rescue": "Make two flat outlines instead of standing walls.",
                "stop": "Stop if a piece breaks, magnets become visible, or the material no longer stays in the build area.",
                "parent": "Use pieces appropriate for the child and check edges and enclosed magnets before play.",
            },
            "block-tower": {
                "slug": "block-tower",
                "title": "Wide-Base Tower",
                "job": "Build up",
                "materials": "six to ten lightweight blocks",
                "mission": "Build upward from a base that is wider than the top.",
                "adult_role": "Set the blocks on the floor and keep the finished build below the child's shoulders.",
                "steps": ["Make a wide first level.", "Add a smaller level.", "Choose one block for the top."],
                "rescue": "Use two levels and call the wide base the finished build.",
                "stop": "Stop if blocks are thrown, used as steps, or stacked near a face, pet, or breakable object.",
                "parent": "Choose lightweight blocks. Keep the tower low and away from faces, overhead areas, walkways, pets, and breakable objects.",
            },
            "cup-tower": {
                "slug": "cup-tower",
                "title": "Cup Doorway",
                "job": "Make an opening",
                "materials": "six lightweight paper cups, one large toy car or figure",
                "mission": "Make a doorway wide enough for the toy to pass through.",
                "adult_role": "Use empty lightweight cups and place the toy on a short floor lane.",
                "steps": ["Make two short cup walls.", "Place one cup across the top.", "Move the toy through the opening."],
                "rescue": "Remove the top cup and make a wide gate first.",
                "stop": "Stop if cups are thrown, crushed into sharp edges, or used as steps.",
                "parent": "Discard torn cups and keep the structure below the child's shoulders.",
            },
            "paper-bridge": {
                "slug": "paper-bridge",
                "title": "Paper Path",
                "job": "Span a gap",
                "materials": "one sheet of paper, two low stable books, one lightweight toy",
                "mission": "Make a paper path that connects the two books for the toy.",
                "adult_role": "Place two low books on the floor and keep them from sliding.",
                "steps": ["Lay the paper across the books.", "Move the toy along the path.", "Fold or curve the edges if wanted."],
                "rescue": "Move the books closer until the paper reaches easily.",
                "stop": "Stop if books slide, the child climbs on them, or the paper is torn into sharp strips.",
                "parent": "Keep the supports low and use books the child moves only with adult help.",
            },
            "straw-bridge": {
                "slug": "straw-bridge",
                "title": "Straw Span",
                "job": "Join materials",
                "materials": "drinking straws, painter tape, two paper cups, one lightweight toy",
                "mission": "Join several straws into a path between the two cups.",
                "adult_role": "Handle any cutting and prepare short pieces of painter tape before the build.",
                "steps": ["Lay straws side by side.", "Join them with short tape pieces.", "Rest the span across the cups."],
                "rescue": "Use fewer straws and move the cups closer.",
                "stop": "Stop if straws splinter or bend into sharp ends, tape goes in a mouth, or cups slide.",
                "parent": "Use wide straws when possible and remove loose tape and damaged pieces promptly.",
            },
            "tube-sculpture": {
                "slug": "tube-sculpture",
                "title": "Tube Sculpture",
                "job": "Make a sculpture",
                "materials": "whole cardboard tubes, cardboard base, painter tape",
                "mission": "Arrange tubes into a shape that can stand on the cardboard base.",
                "adult_role": "Provide whole tubes and short tape pieces; handle all cutting.",
                "steps": ["Stand two tubes on the base.", "Add a tube beside or across them.", "Turn the sculpture and add one more piece."],
                "rescue": "Start with tubes lying flat in a connected shape.",
                "stop": "Stop if cardboard tears into sharp edges, tape is mouthed, or tubes are used as launchers or steps.",
                "parent": "Remove staples, rough edges, and loose tape before and during the build.",
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
                "job": "Build big on the floor",
                "materials": "one blanket, large blocks or cushions, one large toy",
                "mission": "Make a crossing that lets the toy travel from one side of the blanket to the other.",
                "adult_role": "Spread the blanket flat in a clear area and keep the route for toys rather than feet.",
                "steps": ["Place supports near each blanket edge.", "Join them with large blocks or a firm cushion.", "Move the toy across the route."],
                "rescue": "Make a stepping path for the toy instead of one raised crossing.",
                "stop": "Stop if anyone runs on the blanket, climbs on the build, or the setup blocks a doorway or walkway.",
                "parent": "Keep the blanket flat, use only stable floor-level supports, and take the route down after play.",
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


def activity_card(activity):
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    link = ""
    if activity["url"]:
        link_text = activity.get("link_text", "Open card")
        link = f'<a class="small-link" href="{esc(activity["url"])}">{esc(link_text)}</a>'
    return f'''        <article class="seo-activity">
          <div>
            <h2>{esc(activity["title"])}</h2>
            <p>{esc(activity["best_for"])}</p>
            <div class="source-tags">
              <span class="tag">{esc(activity["ages"])} years</span>
              <span class="tag">{esc(activity["time"])}</span>
              <span class="tag">{esc(activity["mess"])} mess</span>
              <span class="tag">{esc(activity["help"])} help</span>
            </div>
          </div>
          <div class="activity-materials"><strong>Need</strong>{esc(activity["materials"])}</div>
          <ol class="card-steps">{steps}</ol>
          <p class="activity-parent"><strong>Parent check:</strong> {esc(activity["parent"])}</p>
          {link}
        </article>'''


def engineering_activity_card(activity):
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    link = ""
    if activity["url"]:
        link = f'<a class="small-link" href="{esc(activity["url"])}">Open the base activity card</a>'
    return f'''        <article class="seo-activity engineering-challenge" id="{esc(activity["slug"])}">
          <div>
            <p class="challenge-label">Challenge</p>
            <h2>{esc(activity["title"])}</h2>
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
          </div>
          <div class="challenge-stop">
            <p><strong>Stop:</strong> {esc(activity["stop"])}</p>
            <p><strong>Parent check:</strong> {esc(activity["parent"])}</p>
          </div>
          {link}
        </article>'''


def building_activity_card(activity):
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    link = ""
    if activity["url"]:
        link_text = activity.get("link_text", "Open the base activity card")
        link = f'<a class="small-link" href="{esc(activity["url"])}">{esc(link_text)}</a>'
    return f'''        <article class="seo-activity building-build" id="{esc(activity["slug"])}">
          <div>
            <p class="challenge-label">{esc(activity["job"])}</p>
            <h2>{esc(activity["title"])}</h2>
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
          </div>
          <div class="challenge-stop">
            <p><strong>Stop:</strong> {esc(activity["stop"])}</p>
            <p><strong>Parent check:</strong> {esc(activity["parent"])}</p>
          </div>
          {link}
        </article>'''


def indoor_activity_card(activity):
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    return f'''        <article class="seo-activity indoor-start" id="{esc(activity["slug"])}">
          <div>
            <p class="challenge-label">{esc(activity["job"])}</p>
            <h2>{esc(activity["title"])}</h2>
            <p class="challenge-mission"><strong>Kid idea:</strong> {esc(activity["mission"])}</p>
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
          <div class="challenge-stop">
            <p><strong>Stop:</strong> {esc(activity["stop"])}</p>
            <p><strong>Parent check:</strong> {esc(activity["parent"])}</p>
          </div>
          <a class="small-link" href="{esc(activity["url"])}">{esc(activity["link_text"])}</a>
        </article>'''


def engineering_page_html(page):
    root = rel_root(page["path"])
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
      <section class="hero engineering-hero">
        <p class="kicker">{esc(page["kicker"])}</p>
        <h1>{esc(page["h1"])}</h1>
        <p class="dek">{esc(page["intro"])}</p>
      </section>

      <section class="seo-page engineering-page">
        <div class="callout">
          <strong>Start here:</strong> {esc(page["tip"])}
        </div>

        <div class="engineering-disclosure" role="note">
          <strong>Evidence note</strong>
          <p>{esc(page["evidence_note"])}</p>
        </div>

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
          <p>Use the same loop for every challenge. The five-part structure is adapted from TERC Head Start on Engineering and HeadStart.gov; the short prompts are Kid Activity Lab editorial wording.</p>
          <ol>
{process_steps}
          </ol>
        </section>

        <section class="engineering-challenges" aria-labelledby="engineering-challenges-title">
          <div class="section-heading">
            <p class="kicker">Nine challenges</p>
            <h2 id="engineering-challenges-title">Choose one problem to solve</h2>
            <p>Run one test and one first change. The rescue is a smaller version, not a promise that the activity will fit every child.</p>
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
      <section class="hero building-hero">
        <p class="kicker">{esc(page["kicker"])}</p>
        <h1>{esc(page["h1"])}</h1>
        <p class="dek">{esc(page["intro"])}</p>
      </section>

      <section class="seo-page building-page">
        <div class="callout">
          <strong>Start here:</strong> {esc(page["tip"])}
        </div>

        <div class="building-disclosure" role="note">
          <strong>Evidence note</strong>
          <p>{esc(page["evidence_note"])}</p>
        </div>

        <div class="building-readiness" role="note">
          <strong>Choose for every child who can reach the build</strong>
          <p>{esc(page["readiness_note"])}</p>
        </div>

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


def page_html(page):
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
    for page in PAGES:
        path = SITE / page["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page_html(page))
    for redirect in LEGACY_REDIRECTS:
        path = SITE / redirect["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(legacy_redirect_html(redirect))
    update_keyword_targets()
    print(f"generated {len(PAGES)} SEO pages and {len(LEGACY_REDIRECTS)} legacy redirects")


if __name__ == "__main__":
    main()
