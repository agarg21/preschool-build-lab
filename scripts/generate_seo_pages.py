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
        "tip": "A good 4-year-old page should mix pretend play with early problem solving.",
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
        "title": "STEM Activities for 4 Year Olds | Kid Activity Lab",
        "h1": "STEM activities for 4 year olds.",
        "kicker": "Age 4 STEM",
        "description": "Simple STEM activities for 4 year olds at home: ramps, bridges, sink-or-float tests, magnets, patterns, towers, and low-prep experiments.",
        "intro": "Four year olds learn STEM best when the question is visible: Will it roll farther? Will it float? Will the bridge hold? These activities keep the setup small and give the child something real to test.",
        "tip": "Use one question per activity: What do you think will happen, and what changed when we tried again?",
        "activities": ["car-ramp-distance-test", "paper-bridge", "sink-or-float-tray", "magnet-hunt", "shadow-shape-match", "pattern-path", "wind-tower-test", "color-mixing-cups", "ramp-texture-test"],
        "related": ["easy stem activities for 4 year olds", "stem activities for 4 year olds at home", "science activities for 4 year olds"],
    },
    {
        "path": "collections/engineering-activities-for-4-year-olds.html",
        "page_type": "collection",
        "primary": "engineering activities for 4 year olds",
        "title": "Engineering Activities for 4 Year Olds | Kid Activity Lab",
        "h1": "Engineering activities for 4 year olds.",
        "kicker": "Engineering",
        "description": "Age-4 engineering activities with paper bridges, straw bridges, foil boats, towers, ramps, box garages, and simple redesign prompts.",
        "intro": "Engineering for a 4 year old is build, test, change one thing, and test again. These ideas use simple materials and avoid projects that depend on perfect cutting or adult-only construction.",
        "tip": "After the first try, ask for one redesign: wider, taller, stronger, flatter, or slower.",
        "activities": ["paper-bridge", "straw-bridge", "foil-boat-test", "paper-chain-test", "wind-tower-test", "car-ramp-distance-test", "ball-maze-box", "box-garage", "cup-tower"],
        "related": ["preschool engineering activities", "engineering activities for preschoolers", "stem engineering activities for preschoolers"],
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


def esc(value):
    return html.escape(value or "", quote=True)


def rel_root(path):
    depth = len(Path(path).parent.parts)
    return "../" * depth


def activity_card(activity):
    steps = "".join(f"<li>{esc(step)}</li>" for step in activity["steps"])
    link = ""
    if activity["url"]:
        link = f'<a class="small-link" href="{esc(activity["url"])}">Open card</a>'
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


def page_html(page):
    root = rel_root(page["path"])
    activity_html = "\n".join(activity_card(ACTIVITIES[key]) for key in page["activities"])
    rows = "\n".join(
        f'''            <tr>
              <td>{esc(ACTIVITIES[key]["title"])}</td>
              <td>{esc(ACTIVITIES[key]["time"])}</td>
              <td>{esc(ACTIVITIES[key]["mess"])}</td>
              <td>{esc(ACTIVITIES[key]["materials"])}</td>
            </tr>'''
        for key in page["activities"]
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
        <a class="brand" href="{root}index.html">Kid Activity Lab</a>
        <div class="nav-links">
          <a href="{root}index.html">Home</a>
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
        </div>

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
        </section>

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
        for page in PAGES:
            writer.writerow(
                {
                    "url": "/" + page["path"],
                    "page_type": page["page_type"],
                    "primary_keyword": page["primary"],
                    "related_keywords": "; ".join(page["related"]),
                    "evidence": "Google autocomplete variant observed 2026-06-26; SERP has broad roundup competitors.",
                    "index_status": "index",
                    "first_2_month_impression_expectation": "20-150 if indexed; higher only if Google trusts the new domain quickly.",
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
