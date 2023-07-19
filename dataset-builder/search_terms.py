# TODO:
# 1. Download images from Google Image Search
# 2. Resize images to 300x300
# 3. Save images to a folder
# 4. Rename files with a counter, each file will have the label as the folder it is in
# 5. Create a CSV file with the filename and label
CSGO_SKIN_NAMES: list[str] = []

ak_names = [
    "Redline",
    "Bloodsport",
    "Vulcan",
    "Gold Arabesque",
    "Asiimov",
    "Fire Serpent",
    "Case Hardened",
    "Safari Mesh",
    "Wild Lotus",
    "The Empress",
    "Fuel Injector",
    ]

awp_names = [
    "Redline",
    "Lightning Strike",
    "Graphite",
    "Dragon Lore",
    "Fade",
    "Medusa",
    "Gungnir",
    "Oni Taiji",
    "Hyper Beast",
    "Neo-Noir",
]

m4a4_names = [
    "Howl",
    "Asiimov",
    "Desolate Space",
    "Neo-Noir",
    "Buzz Kill",
    "Hellfire",
    "The Battlestar",
]

m4a1_names = [
    "Hyper Beast",
    "Knight",
    "Golden Coil",
    "Hot Rod",
    "Mecha Industries",
    "Chantico's Fire",
    "Blue Phosphor",
    "Decimator",
    "Emphorosaur-S"
]

galil_names = [
    "Aqua Terrace",
    "Chatterbox",
    "Amber Fade",
    "Cerberus",
    "Eco",
]

ssg08_names = [
    "Abyss",
    "Blood in the Water",
    "Acid Fade",
    "Big Iron",
]

glock_names = [
    "Fade",
    "Water Elemental",
    "Dragon Tattoo",
    "Candy Apple",
    "Bullet Queen",
    "Gamma Doppler",
]

usp_names = [
    "Printstream",
    "Neo-Noir",
    "Cortex",
    "Cyrex",
    "Kill Confirmed",
    "Monster Mashup",
]

CSGO_SKIN_NAMES.extend([f"AK-47 | {name}" for name in ak_names] )
CSGO_SKIN_NAMES.extend([f"AWP | {name}" for name in awp_names] )
CSGO_SKIN_NAMES.extend([f"M4A4 | {name}" for name in m4a4_names] )
CSGO_SKIN_NAMES.extend([f"M4A1-S | {name}" for name in m4a1_names] )
CSGO_SKIN_NAMES.extend([f"Galil AR | {name}" for name in galil_names] )
CSGO_SKIN_NAMES.extend([f"SSG 08 | {name}" for name in ssg08_names] )
CSGO_SKIN_NAMES.extend([f"Glock-18 | {name}" for name in glock_names] )
CSGO_SKIN_NAMES.extend([f"USP-S | {name}" for name in usp_names] )