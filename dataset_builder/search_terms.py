# TODO:
# 1. Download images from Google Image Search
# 2. Resize images to 300x300
# 3. Save images to a folder
# 4. Rename files with a counter, each file will have the label as the folder it is in
# 5. Create a CSV file with the filename and label
CSGO_SKIN_NAMES: list[tuple[str, str, str]] = []

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
    "Emphorosaur-S",
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

CSGO_SKIN_NAMES.extend([("ak", name, "AK-47") for name in ak_names])
CSGO_SKIN_NAMES.extend([("awp", name, "AWP") for name in awp_names])
CSGO_SKIN_NAMES.extend([("m4a4", name, "M4A4") for name in m4a4_names])
CSGO_SKIN_NAMES.extend([("m4a1s", name, "M4A1-S") for name in m4a1_names])
CSGO_SKIN_NAMES.extend([("galil", name, "Galil AR") for name in galil_names])
CSGO_SKIN_NAMES.extend([("scout", name, "SSG 08") for name in ssg08_names])
CSGO_SKIN_NAMES.extend([("glock", name, "Glock-18") for name in glock_names])
CSGO_SKIN_NAMES.extend([("usp", name, "USP-S") for name in usp_names])
