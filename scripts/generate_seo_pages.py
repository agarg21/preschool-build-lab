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
        "title": "Indoor Activities for Preschoolers | Kid Activity Lab",
        "h1": "Indoor activities for preschoolers.",
        "kicker": "Indoor play",
        "description": "Indoor preschool activities for home: low-mess building, toy car roads, blocks, ramps, blanket rivers, and quiet independent play ideas.",
        "intro": "Indoor activities need to fit real rooms: low noise, low mess, no running path through the house. These options work on a floor, table, hallway, or small play area.",
        "tip": "Use tape roads, block builds, and low ramps when you need movement without chaos.",
        "activities": ["tape-road", "tape-train-tracks", "sock-ball-roll", "blanket-river", "cardboard-car-ramp", "cup-tower", "magnetic-tile-house", "block-tower", "tape-city"],
        "related": ["indoor activities for 3 year olds at home", "indoor activities for 4 year olds at home", "screen free activities for kids indoors"],
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
        "primary": "building activities for 4 year olds",
        "title": "Building Activities for 4 Year Olds | Kid Activity Lab",
        "h1": "Building activities for 4 year olds.",
        "kicker": "Building",
        "description": "Building activities for 4 year olds with blocks, cups, magnetic tiles, paper bridges, straw bridges, towers, tubes, boxes, and blanket rivers.",
        "intro": "Building activities are a natural STEM entry point for 4 year olds because the result is right in front of them. The goal is not a perfect craft; it is a structure they can change and test.",
        "tip": "Give one constraint: build across a gap, build taller than a hand, build a home for one toy, or build something that stays up in wind.",
        "activities": ["magnetic-tile-house", "magnetic-tile-ideas", "block-tower", "cup-tower", "paper-bridge", "straw-bridge", "tube-sculpture", "wind-tower-test", "blanket-river"],
        "related": ["preschool building activities", "construction activities for preschoolers", "building stem activities for preschoolers"],
    },
    {
        "path": "collections/rainy-day-activities-for-preschoolers.html",
        "page_type": "collection",
        "primary": "rainy day activities for preschoolers",
        "title": "Rainy Day Activities for Preschoolers | Kid Activity Lab",
        "h1": "Rainy day activities for preschoolers.",
        "kicker": "Rainy day",
        "description": "Rainy day preschool activities for home: indoor roads, ramps, towers, magnetic tile builds, paper roll drops, and low-mess pretend play.",
        "intro": "Rainy-day activities need to absorb energy without turning the room upside down. These are small, resettable ideas that work when everyone is stuck inside.",
        "tip": "Rotate between one movement idea, one building idea, and one quiet idea.",
        "activities": ["tape-road", "tape-train-tracks", "cardboard-car-ramp", "sock-ball-roll", "blanket-river", "magnetic-tile-house", "paper-roll-drop", "cup-tower", "tape-city"],
        "related": ["rainy day activities for kids at home", "rainy day activities for toddlers", "indoor activities for preschoolers"],
    },
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


def page_html(page):
    if page.get("engineering_layout"):
        return engineering_page_html(page)
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
    update_keyword_targets()
    print(f"generated {len(PAGES)} SEO pages")


if __name__ == "__main__":
    main()
