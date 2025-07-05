import tkinter as tk
from tkinter import ttk
import random

# -----------------------------------------------------------------------------
# Title: D&D 5th Edition random Viking character generater v1.0
# Description: A script to generate detailed Norse-themed D&D characters.
# Author: Volmarr Wyrd with the aid of ChatGPT v4 o1-preview
# License: MIT License
# Copyright (c) 2024 Volmarr Wyrd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------
#
# D&D 5th Edition random Viking character generater v1.0
# Created by Volmarr Wyrd with the aid of ChatGPT v4 o1-preview, Sept-24-2024.
# This script reqiures Python 3 or later.
# The script uses pyperclip for clipboard functionality.Install it using pip install pyperclip if you want the clipboard feature.
# Copy the code and save it into a text file named norse_character_generator.py
# Run the script from terminal using:  python norse_character_generator.py

# Gender options
genders = ["Male", "Female", "Random"]

# Gender-specific name components
male_name_prefixes = [
	"As", "Bjorn", "Eirik", "Gunn", "Half", "Ing", "Knut", "Leif", "Magn",
	"Olaf", "Ragn", "Sig", "Thor", "Ulf", "Val", "Har", "Er", "Ivar", "Loki",
	"Magnar", "Njal", "Odin", "Rolf", "Tor", "Vidar", "Wotan", "Yng", "Fenr",
	"Arne", "Bjarne", "Dag", "Egil", "Finn", "Gunnar", "Hakon", "Jarl", "Ketil",
	"Lars", "Morten", "Nicolai", "Orvar", "Per", "Roar", "Sten", "Trygve", "Ulrik",
	"Viggo", "Yrjö", "Aegir", "Alv", "Anund", "Arvid", "Asgeir", "Balder", "Berg", "Birger", "Brand", "Bryn", "Dagfinn", "Eilif",  "Eindride", "Einar", "Erling", "Eyvind", "Folke", "Frey", "Frode", "Geir", "Gorm", "Gudmund", "Gunvald", "Haldor", "Hall", "Harald", "Helgi", "Hjalmar", "Holger", "Ingvar", "Isak", "Jorund", "Kare", "Leik", "Lodin", "Mads", "Nils", "Odd", "Oleg", "Olof", "Orm", "Rune", "Sigurd", "Sindre", "Skarde", "Snorri", "Stig", "Styr", "Svein", "Sven", "Thorbjorn", "Thorgrim", "Thorin", "Thorkel", "Thorvald", "Torben", "Torsten", "Vigfus", "Yngve", "Bjarki", "Dagur", "Eysteinn", "Fridleif", "Geirmund", "Geirrod", "Grim", "Gudbrand", "Hallfred", "Havar", "Havard", "Herleif", "Hoder", "Hrolf", "Hrothgar", "Idar", "Jens", "Jon", "Kjartan", "Kol", "Magnus", "Oddleif", "Ofeig", "Ole", "Oystein", "Ragnvald", "Sigbjorn", "Sigmund", "Sindri", "Skeggi", "Stigandr", "Styrkar", "Svend", "Thangbrand", "Thorfinn", "Thorleif", "Thorolf", "Thorsteinn", "Thrain", "Ulfar", "Ulfhedin", "Vebjorn", "Viglund", "Volund", "Bjornolf", "Brandr", "Egil", "Eldgrim", "Erik", "Gisli", "Gudleif", "Hafgrim", "Hauk", "Hjalti", "Holmgeir", "Ingolf", "Ivarr", "Ketil", "Ketill", "Leifr", "Ormarr", "Ragnar", "Sigtrygg", "Skapti", "Skuli", "Steinarr", "Thangbrandr", "Thorarin", "Thorgeir", "Thorir", "Thorkell", "Thorleikr", "Thormod", "Thorstein", "Tyr", "Valdemar", "Vidkunn", "Yngvar", "Atli", "Audun", "Beinir", "Eirikr", "Gardar", "Gauti", "Gest", "Glum", "Grettir", "Halli", "Haraldur", "Hring", "Illugi", "Ingi", "Ingimund", "Koll", "Kolli", "Kolskegg", "Lambi", "Modolf", "Njall", "Olvir", "Ornolf", "Sigfus", "Sigmundr", "Sigurdur", "Skarphedin", "Stein", "Styrmir", "Sveinn", "Thidrandi", "Thorbrand", "Thord", "Thorgrimr", "Thorodd", "Throst", "Ulfketill", "Valgard", "Vestar", "Vigleik", "Vilhjalmr", "Floki", "Geirleif", "Gestur", "Hrafn", "Hrani", "Ingolfur", "Kollgrim", "Njord", "Ottar", "Steinn", "Thangbrandur", "Thjodolf", "Torfi", "Vilhjalmur", "Yngvi", "Aleifr", "Armod", "Aslak", "Asvald", "Bersi", "Bodvar", "Borgar", "Bruni", "Brynjolf", "Dagr", "Eilifr", "Eindridi", "Eyvindr", "Finnbogi", "Fridthjof", "Geirmundr", "Geirstein", "Gellir", "Grani", "Grimkell", "Grimolf", "Guthormr", "Hafgrimr", "Halfdan", "Hallvard", "Hedin", "Herjolf", "Hermundr", "Hoskuld", "Hrafnkel", "Hrollaug", "Hrut", "Ingimundr", "Isleif", "Ketilbjorn", "Kolbein", "Kormakr", "Kveldulf", "Ljot", "Mord", "Naddodd", "Oddr", "Onundr", "Ormr", "Ozurr", "Rafn", "Ref", "Skomlr", "Sokki", "Starkadr", "Steinar", "Steinbjorn", "Steinolf", "Stigandi", "Svala", "Theodolf", "Thjostolf", "Thorgils", "Thrand", "Ulfhedinn", "Vagn", "Vebrand", "Vestein", "Yngvarr", "Asmund", "Freyr", "Balder", "Bragi", "Forseti", "Heimdall", "Hodr", "Mimir", "Vili", "Ve", "Vidar", "Vali", "Kvasir", "Buri", "Bor", "Meili", "Magni", "Modi", "Fjolnir", "Sigi", "Hunding", "Sinfjotli", "Helgi", "Guttorm", "Jormunrek", "Volsung"
	# Add more prefixes as needed
]

female_name_prefixes = [
	"Fre", "Gud", "Hilda", "Astrid", "Hel", "Kari", "Sif", "Urd", "Yrsa",
	"Eir", "Frigg", "Sigr", "Thora", "Inga", "Liv", "Saga", "Embla", "Alva",
	"Idun", "Nanna", "Skadi", "Runa", "Gun", "Brynh", "Solveig", "Gunnhild",
	"Asta", "Birgit", "Dagny", "Eira", "Freya", "Gerda", "Hanna", "Ingrid",
	"Johanna", "Kirsten", "Lena", "Marta", "Nina", "Oda", "Randi", "Signe",
	"Tove", "Vigdis", "Ylva", "Alf", "Arn", "Asa", "Aud", "Bod", "Dis", "Ey", "Fri", "Ger", "Gro", "Hall", "Hrefn", "Jor", "Lof", "Ragn", "Unn", "Vigg", "Yng", "Hlin", "Eost", "Full", "Lag", "Skog", "Gol", "Skuld", "Mist", "Geir", "Hrist", "Rot", "Trim", "Vor", "Sjo", "Syn", "Var", "Hjor", "Inge", "Svan", "Thur", "Ase", "Dag", "Ran", "Edl", "Gry", "Idon", "Lin", "Revn", "Agnet", "Anj", "Ann", "Carin", "Cecil", "Dort", "Elis", "Gret", "Hann", "Krist", "Lail", "Mal", "Marga", "Mat", "Pern", "Ren", "Sof", "Ulrik", "Vive", "Agn", "Alvh", "Aria", "Brun", "Dagn", "Elfr", "Eyd", "Frig", "Gull", "Ingr", "Kat", "Lut", "Mard", "Nid", "Osk", "Rind", "Sjof", "Torh", "Valk", "Yrs", "Alva", "Birg", "Dagm", "Eldr", "Eydis", "Finna", "Gerd", "Gerse", "Gull", "Her", "Herfr", "Herv", "Idon", "Kris", "Laga", "Lif", "Modi", "Nott", "Olga", "Ragna", "Rev", "Sefa", "Sigyn", "Siri", "Siv", "Thora", "Torny", "Valkyr", "Yr"
	# Add more prefixes as needed
]

male_name_suffixes = [
	"ar", "bjorn", "finn", "gard", "ing", "kell", "lief", "mund",
	"nar", "olf", "rad", "sten", "thor", "ulf", "vard", "wulf", "brand",
	"fast", "grim", "hall", "jorn", "kel", "laug", "magn", "nir", "or",
	"rik", "sten", "tul", "vald", "win", "yng", "heim", "svar",
	"ulfsson", "sson", "valdr", "skegg", "svard", "bjornsson", "arn",
	"gautr", "hard", "ketil", "lang", "leikr", "rand", "sig", "sverre",
	"trygg", "vard", "vik", "yr"
	# Add more suffixes as needed
]

female_name_suffixes = [
	"dottir", "hild", "dis", "frid", "gunn", "heid", "laug", "lif",
	"ny", "runa", "linn", "skuld", "disa", "bera", "unn", "frida",
	"gerd", "ing", "katla", "lin", "unnr", "veig", "sol", "ny",
	"bjorg", "drifa", "elva", "finna", "gisla", "helga", "ingrid",
	"jora", "kaisa", "lina", "maren", "nora", "olve", "rogn", "saga",
	"tora", "ursula", "vigdis", "ylva"
	# Add more suffixes as needed
]

nicknames = [
	"the Brave", "the Strong", "Ironhand", "Stormcaller", "Wolfheart", "Dragonbane",
	"Skullsplitter", "Shadowwalker", "Bearclaw", "Whisperwind", "Thunderfist",
	"Eagle Eye", "the Swift", "Iceblood", "Sea Wolf", "the Wise", "Firebeard",
	"Stoneheart", "Longstrider", "the Silent", "Windrider", "the Cunning",
	"Bonebreaker", "Deepwalker", "Nightblade", "Dawnbringer", "Frostfang", "the Bold",
	"Shieldmaiden", "Battle-Maiden", "Iron Maiden", "Mistress of Blades",
	"Ironhide", "Stormbreaker", "Bloodaxe", "Silver Tongue", "Grim",
	"One-Eye", "Fireheart", "Whiteshield", "Goldhair", "Blackthorn",
	"Steelheart", "Stonefist", "Hawkeye", "Ironjaw", "Runesinger",
	"Spiritwalker", "Windwhisper", "Dragonheart", "Thunderstrike", "Frostbeard", "Bloodwolf", "Ironshield", "Stormbringer", "Thunderwalker", "Sea Serpent", "Bearkiller", "Redbeard", "Stoneaxe", "Battleborn", "Dragon Slayer", "Oathkeeper", "Silverhand", "Firewalker", "Windseer", "Frostblade", "Nightstalker", "Icebreaker", "Wolfslayer", "Ironfoot", "Ravensong", "Skysplitter", "Farseer", "Blackhelm", "Stormeye", "Steelbrow", "Ghostblade", "Wildhammer", "Duskbringer", "Lightbringer", "Darkbane", "Runemaster", "Ironbrow", "Oakenshield", "Strongarm", "Redhawk", "Stonebreaker", "Darkblade", "Icewind", "Frostwolf", "Wolfbane", "Swordbreaker", "Hammerhand", "Stonefoot", "Shadowstrike", "Flamebearer", "Windrunner", "Firestorm", "Ironbear", "Wildheart", "Battlehammer", "Nightshade", "Stormborn", "Blacksword", "Eagleheart", "Wolfclaw", "Seaborn", "Ironhawk", "Stonewall", "Thunderwolf", "Skybreaker", "Ironfang", "Stonehelm", "Darkwolf", "Silvereye", "Flamesong", "Dragonrider", "Windsong", "Shadowhunter", "Ironhorn", "Stormrider", "Ravenclaw", "Dawnslayer", "Nightwind", "Stonehammer", "Ironfist", "Wildspear", "Stormhammer", "Thunderblade", "Ghostwolf", "Fireforge", "Windcaller", "Silverblade", "Wolfstorm", "Stormwolf", "Ironclaw", "Shadowblade", "Stonewolf", "Thunderclaw", "Windslayer", "Firewolf", "Wildblade", "Iceclaw", "Ghostbear", "Ironblade", "Stormclaw", "Shadowfang", "Stoneclaw", "Windblade", "Fireclaw", "Wolfblade", "Stormbear", "Ironhammer", "Thunderhammer", "Shadowhammer", "Stonebear", "Windhammer", "Firehammer", "Dragonhammer", "Wolfhammer", "Stormblade", "Ironaxe", "Thunderaxe", "Shadowaxe", "Stoneaxe", "Windaxe", "Fireaxe", "Dragonaxe", "Wolfaxe", "Stormarrow", "Ironarrow", "Thunderarrow", "Shadowarrow", "Stonearrow", "Windarrow", "Firearrow", "Dragonarrow", "Wolfarrow", "Stormspear", "Ironspear", "Thunderspear", "Shadowspear", "Stonespear", "Windspear", "Firespear", "Dragonspear", "Wolfspear", "Stormshield", "Ironshield", "Thundershield", "Shadowshield", "Stoneshield", "Windshield", "Fireshield", "Dragonshield", "Wolfshield", "Stormbow", "Ironbow", "Thunderbow", "Shadowbow", "Stonebow", "Windbow", "Firebow", "Dragonbow", "Wolfbow", "Stormsong", "Ironsong", "Thundersong", "Shadowsong", "Stonesong", "Windsong", "Firesong", "Dragonsong", "Wolfsong", "Stormwalker", "Ironwalker", "Thunderwalker", "Shadowwalker", "Stonewalker", "Windwalker", "Firewalker", "Dragonwalker", "Wolfwalker", "Stormrider", "Ironrider", "Thunderrider", "Shadowrider", "Stonerider", "Windrider", "Firerider", "Dragonrider", "Wolfrider", "Stormseeker", "Ironseeker", "Thunderseeker", "Shadowseeker", "Stoneseeker", "Windseeker", "Fireseeker", "Dragonseeker", "Wolfseeker", "Stormcaller", "Ironcaller", "Thundercaller", "Shadowcaller", "Stonecaller", "Windcaller", "Firecaller", "Dragoncaller", "Wolfcaller", "Stormhunter", "Ironhunter", "Thunderhunter", "Shadowhunter", "Stonehunter", "Windhunter", "Firehunter", "Dragonhunter", "Wolfhunter", "Stormweaver", "Ironweaver", "Thunderweaver", "Shadowweaver", "Stoneweaver", "Windweaver", "Fireweaver", "Dragonweaver", "Wolfweaver", "Stormbringer", "Ironbringer", "Thunderbringer", "Shadowbringer", "Stonebringer", "Windbringer", "Firebringer", "Dragonbringer", "Wolfbringer", "Stormsinger", "Ironsinger", "Thundersinger", "Shadowsinger", "Stonesinger", "Windsinger", "Firesinger", "Dragonsinger", "Wolfsinger", "Stormwielder", "Ironwielder", "Thunderwielder", "Shadowwielder", "Stonewielder", "Windwielder", "Firewielder", "Dragonwielder", "Wolfwielder", "Stormwatcher", "Ironwatcher", "Thunderwatcher", "Shadowwatcher", "Stonewatcher", "Windwatcher", "Firewatcher", "Dragonwatcher", "Wolfwatcher", "Stormguard", "Ironguard", "Thunderguard", "Shadowguard", "Stoneguard", "Windguard", "Fireguard", "Dragonguard", "Wolfguard", "Stormsword", "Ironsword", "Thundersword", "Shadowsword", "Stonesword", "Windsword", "Firesword", "Dragonsword", "Wolfsword", "Stormhelm", "Ironhelm", "Thunderhelm", "Shadowhelm", "Stonehelm", "Windhelm", "Firehelm", "Dragonhelm", "Wolfhelm", "Stormbane", "Ironbane", "Thunderbane", "Shadowbane", "Stonebane", "Windbane", "Firebane", "Dragonbane", "Wolfbane", "Shieldbreaker", "Rageborn", "Bloodfang", "Ironblood", "Stormborn", "Thundershield", "Oathbreaker", "Bonecrusher", "Icewalker", "Earthshaker", "Warbringer", "Soulreaper", "Ironwind", "Frostbreaker", "Stormrunner", "Windrider", "Spearbreaker", "Shadowstorm", "Wolfstar", "Fireblade", "Thunderstrike", "Darkstar", "Goldentooth", "Frostborn", "Ironhide", "Wraithblade", "Deathweaver", "Spellbreaker", "Doomhammer", "Windshadow", "Firestorm", "Stoneblood", "Ironstorm", "Frostfire", "Stormgazer", "Windshadow", "Ironmantle", "Bloodclaw", "Stormsong", "Firestone", "Thunderstone", "Dragonfire", "Ironforge", "Shadowsteel", "Firesong", "Wolfwind", "Stormtamer", "Icemantle", "Darkheart", "Skywatcher", "Runecaller", "Whisperblade", "Starseer", "Nightwhisper", "Windwhisper", "Ironrage", "Soulbinder", "Stormforge", "Ironshield", "Thunderfury", "Grimfist", "Darkwind", "Fireeye", "Wolfwing", "Stormwolf", "Icewolf", "Shadowwolf", "Bloodaxe", "Frosthammer", "Ironhammer", "Stormcloaked", "Thunderlord", "Fireborn", "Ghostwalker", "Ironmind", "Stonehelm", "Windreaver", "Dragonborn", "Wolfblood", "Stormflame", "Ironwrath", "Thunderwrath", "Firewrath", "Dragonwrath", "Wolfwrath"
	# Add more nicknames as needed
]

# Define Norse-themed races
norse_races = [
	"Human",
	"Dwarf",
	"Elf",
	"Half-Elf",
	"Goliath",  # Represents giants from Norse myths
	"Half-Orc",
	# Removed Tiefling, Aasimar, Firbolg, Tabaxi
]

# Race options including 'Random'
race_options = ["Random"] + norse_races

classes = [
	"Barbarian",
	"Cleric",
	"Druid",
	"Fighter",
	"Ranger",
	"Paladin",
	"Warlock",
	"Skald",  # Norse bard
	"Runecaster",
	"Sorcerer",
	"Monk",
	"Rogue",
	"Berserker",
	"Shaman",
	"Valkyrie",
	"Seer",
	"Hunter",
	"Mystic",
	"Witch",
	"Explorer",
	# Add more classes as needed
]

backgrounds = [
	"Sailor",
	"Soldier",
	"Outlander",
	"Folk Hero",
	"Noble",
	"Hermit",
	"Acolyte",
	"Guild Artisan",
	"Mercenary",
	"Hunter",
	"Skald",
	"Trader",
	"Raider",
	"Explorer",
	"Blacksmith",
	"Shipwright",
	"Farmer",
	"Fisher",
	"Navigator",
	"Herbalist",
	"Healer",
	"Mystic",
	"Scholar",
	"Miner",
	"Leatherworker",
	"Beastmaster",
	"Carpenter",
	"Messenger",
	"Scout",
	"Seer",
	"Shepherd",
	"Chieftain's Child",
	"Rebel",
	"Guardian",
	"Wanderer",
	"Weapon Smith",
	"Armorer",
	"Woodcutter",
	"Alchemist",
	"Runesmith",
	"Archivist",
	"Scribe",
	"Sentinel",
	"Caretaker",
	"Historian",
	"Artisan",
	"Storyteller",
	"Diplomat",
	"Enchanter",
	"Geomancer",
	"Beekeeper",
	# Add more backgrounds as needed
]

alignments = [
	"Lawful Good",
	"Neutral Good",
	"Chaotic Good",
	"Lawful Neutral",
	"True Neutral",
	"Chaotic Neutral",
	"Lawful Evil",
	"Neutral Evil",
	"Chaotic Evil",
]

skills = [
	"Athletics",
	"Survival",
	"Perception",
	"Intimidation",
	"History",
	"Stealth",
	"Nature",
	"Animal Handling",
	"Insight",
	"Medicine",
	"Religion",
	"Sleight of Hand",
	"Acrobatics",
	"Investigation",
	"Arcana",
	"Deception",
	"Performance",
	"Persuasion",
	"Endurance",
	"Tracking",
	"Cooking",
	"Sailing",
	"First Aid",
	"Herbalism",
	"Blacksmithing",
	"Leatherworking",
	"Woodworking",
	"Runecraft",
	"Cartography",
	"Appraisal",
	"Climbing",
	"Fishing",
	"Horsemanship",
	# Add more skills as needed
]

# Historical Viking weapons and equipment
equipment = [
	"Battleaxe",
	"Shield",
	"Longbow",
	"Shortbow",
	"Chain Mail",
	"Leather Armor",
	"Handaxe",
	"Warhammer",
	"Javelin",
	"Greatsword",
	"Longsword",
	"Dagger",
	"Helmet",
	"Spear",
	"Throwing Axe",
	"Seax Knife",
	"Viking Sword",
	"Round Shield",
	"Mail Shirt",
	"Cloak",
	"Drinking Horn",
	"Fishing Net",
	"Horned Helmet",
	"Wooden Shield",
	"Iron Spear",
	"Fur Cloak",
	"Travel Boots",
	"Iron Gauntlets",
	"Quiver of Arrows",
	"Rope",
	"Torch",
	"Flint and Steel",
	"Waterskin",
	"Herbal Poultices",
	"Compass",
	"Map Scroll",
	"Horn",
	"Tent",
	"Bedroll",
	"Fishing Rod",
	"Hunting Trap",
	"Herbalism Kit",
	"Smith's Tools",
	"Carpenter's Tools",
	"Navigator's Tools",
	"Drum",
	"Lyre",
	"Runestone",
	"Engraved Arm Ring",
	# Add more equipment as needed
]

traits = [
	"Brave",
	"Resilient",
	"Stoic",
	"Fierce",
	"Loyal",
	"Cunning",
	"Honorable",
	"Vengeful",
	"Superstitious",
	"Ambitious",
	"Generous",
	"Hot-tempered",
	"Quiet",
	"Optimistic",
	"Pessimistic",
	"Reckless",
	"Disciplined",
	"Pragmatic",
	"Idealistic",
	"Sarcastic",
	"Determined",
	"Curious",
	"Charming",
	"Wise",
	"Resourceful",
	"Fearless",
	"Stubborn",
	"Independent",
	"Adventurous",
	"Protective",
	"Observant",
	"Eloquent",
	"Hardworking",
	"Kind-hearted",
	"Reserved",
	"Meticulous",
	"Bold",
	"Innovative",
	"Daring",
	"Perceptive",
	"Empathetic",
	"Compassionate",
	"Tenacious",
	"Versatile",
	"Tactful",
	"Persistent",
	"Humorous",
	"Steadfast",
	"Mysterious",
	"Insightful",
	"Unpredictable",
	"Adaptable",
	"Faithful",
	"Zealous",
	"Intuitive",
	"Patient",
	"Rational",
	"Adaptable",
	"Adventurous",
	"Alert",
	"Amiable",
	"Analytical",
	"Artistic",
	"Attentive",
	"Bold",
	"Calm",
	"Charming",
	"Compassionate",
	"Confident",
	"Conscientious",
	"Creative",
	"Curious",
	"Decisive",
	"Dependable",
	"Determined",
	"Diligent",
	"Disciplined",
	"Eloquent",
	"Empathetic",
	"Energetic",
	"Enthusiastic",
	"Fair",
	"Faithful",
	"Fearless",
	"Flexible",
	"Focused",
	"Forgiving",
	"Forthright",
	"Friendly",
	"Frugal",
	"Generous",
	"Gentle",
	"Hardworking",
	"Honest",
	"Imaginative",
	"Independent",
	"Industrious",
	"Innovative",
	"Insightful",
	"Intelligent",
	"Intuitive",
	"Inventive",
	"Kind",
	"Knowledgeable",
	"Leader",
	"Meticulous",
	"Observant",
	"Optimistic",
	"Organized",
	"Perceptive",
	"Perseverant",
	"Persuasive",
	"Practical",
	"Precise",
	"Protective",
	"Prudent",
	"Quick-witted",
	"Rational",
	"Reflective",
	"Reliable",
	"Reserved",
	"Respectful",
	"Responsible",
	"Sensible",
	"Sensitive",
	"Sincere",
	"Skilled",
	"Strategic",
	"Strong-willed",
	"Supportive",
	"Talented",
	"Thoughtful",
	"Tolerant",
	"Trustworthy",
	"Understanding",
	"Unyielding",
	"Vigilant",
	"Visionary",
	"Warm",
	"Wary",
	"Witty",
	"Zealous",
	"Stoic",
	"Austere",
	"Patient",
	"Stoic",
	"Bold",
	"Chivalrous",
	"Competitive",
	"Cooperative",
	"Courageous",
	"Cultured",
	"Daring",
	"Debonair",
	"Decorous",
	"Deep",
	"Dignified",
	"Disciplined",
	"Educated",
	"Efficient",
	"Elegant",
	"Empirical",
	"Esthetic",
	"Focused",
	"Gallant",
	"Gracious",
	"Heroic",
	"Idealistic",
	"Impartial",
	"Incisive",
	"Insightful",
	"Intense",
	"Jovial",
	"Leaderly",
	"Leisurely",
	"Logical",
	"Lyrical",
	"Mature",
	"Moderate",
	"Moral",
	"Objective",
	"Passionate",
	"Polished",
	"Principled",
	"Profound",
	"Prudent",
	"Punctual",
	"Purposeful",
	"Rational",
	"Realistic",
	"Reserved",
	"Resourceful",
	"Respectful",
	"Responsive",
	"Reverential",
	"Sage",
	"Scholarly",
	"Scrupulous",
	"Selfless",
	"Seraphic",
	"Serious",
	"Skillful",
	"Sophisticated",
	"Stable",
	"Steadfast",
	"Stoic",
	"Studious",
	"Suave",
	"Subtle",
	"Tasteful",
	"Teacherly",
	"Thorough",
	"Tolerant",
	"Unfoolable",
	"Upright",
	"Venturesome",
	"Vivacious",
	"Well-read",
	"Worldly",
	"Zealous",
	"Accommodating",
	"Ambitious",
	"Adept",
	"Affable",
	"Approachable",
	"Articulate",
	"Assertive",
	"Astute",
	"Authentic",
	"Balanced",
	"Benevolent",
	"Candid",
	"Charismatic",
	"Civilized",
	"Communicative",
	"Compelling",
	"Competent",
	"Composed",
	"Consistent",
	"Cordial",
	"Courageous",
	"Courteous",
	"Creative",
	"Decent",
	"Dedicated",
	"Dependable",
	"Diplomatic",
	"Discerning",
	"Discreet",
	"Dynamic",
	"Earnest",
	"Easygoing",
	"Educated",
	"Effective",
	"Efficient",
	"Emotional",
	"Empathetic",
	"Encouraging",
	"Enduring",
	"Enterprising",
	"Exuberant",
	"Fair-minded",
	"Firm",
	"Focused",
	"Frank",
	"Friendly",
	"Fun-loving",
	"Generous",
	"Gentle",
	"Good-natured",
	"Gregarious",
	"Hardworking",
	"Helpful",
	"Honorable",
	"Humble",
	"Humorous",
	"Idealistic",
	"Impartial",
	"Incisive",
	"Incorruptible",
	"Individualistic",
	"Innovative",
	"Insightful",
	"Intelligent",
	"Intuitive",
	"Inventive",
	"Joyful",
	"Just",
	"Knowledgeable",
	"Level-headed",
	"Light-hearted",
	"Logical",
	"Lovable",
	"Loyal",
	"Mannerly",
	"Merciful",
	"Methodical",
	"Modest",
	"Neat",
	"Objective",
	"Open-minded",
	"Optimistic",
	"Orderly",
	"Organized",
	"Original",
	"Passionate",
	"Patient",
	"Perceptive",
	"Persistent",
	"Philosophical",
	"Playful",
	"Polite",
	"Practical",
	"Precise",
	"Principled",
	"Profound",
	"Prudent",
	"Purposeful",
	"Quiet",
	"Rational",
	"Realistic",
	"Reflective",
	"Relaxed",
	"Reliable",
	"Reserved",
	"Respectful",
	"Responsible",
	"Responsive",
	"Reverent",
	"Romantic",
	"Sage",
	"Scholarly",
	"Secure",
	"Self-critical",
	"Self-reliant",
	"Self-sufficient",
	"Sensitive",
	"Sentimental",
	"Serious",
	"Shrewd",
	"Simple",
	"Sociable",
	"Spontaneous",
	"Steady",
	"Stoic",
	"Subtle",
	"Sympathetic",
	"Systematic",
	"Tasteful",
	"Teacherly",
	"Thoughtful",
	"Trusting",
	"Unassuming",
	"Understanding",
	"Unpredictable",
	"Unsentimental",
	"Valiant",
	"Versatile",
	"Vivacious",
	"Warm",
	"Well-bred",
	"Well-mannered",
	"Well-rounded",
	"Wise",
	"Witty",
	"Youthful"
	# Add more traits as needed
]

ideals = [
	"Honor",
	"Freedom",
	"Power",
	"Tradition",
	"Glory",
	"Knowledge",
	"Survival",
	"Justice",
	"Faith",
	"Balance",
	"Courage",
	"Loyalty",
	"Revenge",
	"Peace",
	"Wisdom",
	"Destiny",
	"Strength",
	"Wealth",
	"Family",
	"Community",
	"Innovation",
	"Harmony",
	"Respect",
	"Sacrifice",
	"Independence",
	"Equality",
	"Compassion",
	"Truth",
	"Discipline",
	"Honor Among Thieves",
	"Redemption",
	"Perfection",
	"Liberty",
	"Order",
	"Protection",
	"Self-Reliance",
	"Endurance",
	"Adventure",
	"Fate",
	"Balance with Nature",
	"Honor. I will uphold the traditions and codes of my ancestors.",
	"Courage. Fear will not stop me from doing what is right.",
	"Glory. I seek to earn a place among the legends.",
	"Justice. All wrongs must be righted, no matter the cost.",
	"Freedom. Every person deserves to chart their own destiny.",
	"Loyalty. My comrades come before anything else.",
	"Knowledge. Understanding the world is the key to mastering it.",
	"Strength. Power is the path to respect and influence.",
	"Wisdom. With wisdom comes true understanding.",
	"Faith. The gods guide my actions and decisions.",
	"Destiny. I am meant for greatness.",
	"Balance. All things must be kept in equilibrium.",
	"Compassion. Helping others is my greatest calling.",
	"Revenge. Those who wronged me will pay dearly.",
	"Redemption. I seek to atone for past mistakes.",
	"Duty. My responsibilities define who I am.",
	"Peace. Conflict brings nothing but sorrow.",
	"Innovation. New ideas and inventions drive progress.",
	"Tradition. The old ways are the best ways.",
	"Adventure. Life is nothing without excitement.",
	"Survival. I will do whatever it takes to stay alive.",
	"Wealth. Accumulating riches is my primary goal.",
	"Power. I aim to become a force to be reckoned with.",
	"Order. Society functions best when laws are upheld.",
	"Chaos. Rules are meant to be challenged.",
	"Family. My loved ones are the most important thing to me.",
	"Nature. The natural world must be preserved.",
	"Artistry. Creativity is the essence of the soul.",
	"Honor in Battle. A warrior's death is the greatest glory.",
	"Self-Improvement. Every day is an opportunity to grow.",
	"Community. We are stronger together than alone.",
	"Truth. Deception is the root of all evil.",
	"Patience. Good things come to those who wait.",
	"Charity. I have a duty to help those less fortunate.",
	"Fairness. Everyone deserves a fair chance.",
	"Ambition. I will not rest until I achieve my goals.",
	"Leadership. I strive to be a guiding light for others.",
	"Destiny's Call. I am driven by forces beyond my understanding.",
	"Exploration. There are always new horizons to discover.",
	"Spirituality. My faith shapes my actions and beliefs.",
	"Protection. It is my duty to defend the weak.",
	"Vengeance. Justice must be served for past wrongs.",
	"Legacy. I want to be remembered long after I'm gone.",
	"Independence. I rely on no one but myself.",
	"Humility. Pride leads to downfall.",
	"Equality. All beings deserve respect and dignity.",
	"Discipline. Through discipline comes mastery.",
	"Resilience. Adversity only makes me stronger.",
	"Harmony. Living in peace with others is paramount.",
	"Sacrifice. I am willing to give up much for a greater cause.",
	"Efficiency. Waste not, want not.",
	"Curiosity. The pursuit of knowledge drives me.",
	"Optimism. There's always hope for a better tomorrow.",
	"Pragmatism. Practical solutions are better than idealistic ones.",
	"Fame. I want my name to be known throughout the lands.",
	"Love. Affection and relationships give life meaning.",
	"Humor. Laughter is the best remedy.",
	"Cunning. Intelligence and strategy win over brute force.",
	"Redemption. No one is beyond saving.",
	"Honor Among Thieves. Even criminals have a code.",
	"Mercy. Compassion should temper justice.",
	"Glory of the Gods. All deeds are for the deities' honor.",
	"Discovery. Uncovering hidden truths excites me.",
	"Balance of Nature. Disturbing nature brings disaster.",
	"Fate. I accept whatever destiny has in store.",
	"Mastery. Achieving excellence is my life's work.",
	"Familial Duty. My family's needs come before my own.",
	"Strength of Will. Mental fortitude conquers all obstacles.",
	"Anonymity. I prefer to stay unnoticed.",
	"Rebellion. Authority must be questioned.",
	"Serenity. Inner peace is the ultimate goal.",
	"Simplicity. A simple life is a happy life.",
	"Purity. Corruption must be cleansed.",
	"Harmony with Nature. Living in tune with the environment.",
	"Justice for All. Everyone deserves justice.",
	"Devotion. My cause is everything to me.",
	"Destiny Weaver. I believe we make our own fate.",
	"Invention. Creating new things brings me joy.",
	"Surpassing Limits. Boundaries are meant to be broken.",
	"Preservation. The old ways must not be forgotten.",
	"Stewardship. It's our duty to care for the world.",
	"Might Makes Right. Strength determines authority.",
	"Liberty. No one should be oppressed.",
	"Adaptability. Survival requires flexibility.",
	"Eternal Vigilance. Constant watchfulness is necessary.",
	"Honest Work. There's dignity in labor.",
	"Unity. Divided we fall.",
	"Seeker of Truth. Lies are unacceptable.",
	"Karma. Actions bring consequences.",
	"Destiny of Kings. Leadership is my birthright.",
	"Transcendence. I seek to rise above the mundane.",
	"Retribution. Punishment must fit the crime.",
	"Sanctity of Life. All life is precious.",
	"Balance of Power. No one should hold too much power.",
	"Preservation of Knowledge. Learning must be protected.",
	"Altruism. Helping others is its own reward.",
	"Overcoming Fear. Courage is facing one's fears.",
	"Egalitarianism. All are equal in the eyes of the gods.",
	"Self-Reliance. Dependence is a weakness.",
	"Open-Mindedness. New ideas lead to progress.",
	"Justice over Law. The spirit of the law is more important than the letter.",
	"Spiritual Enlightenment. I seek higher understanding.",
	"Purging Evil. Darkness must be eradicated.",
	"Innovation. Stagnation leads to decay.",
	"Moderation. Excess leads to ruin.",
	"Duty to the Throne. The ruler's word is absolute.",
	"Environmentalism. Protecting the earth is paramount.",
	"Knowledge is Power. Learning is the path to control.",
	"Perfection. I strive for flawlessness in all I do.",
	"Destiny's Instrument. I am a tool of fate.",
	"Strength Through Adversity. Hardship builds character.",
	"Harmony Among Races. Cooperation brings prosperity.",
	"Defiance. I resist those who try to control me.",
	"Spiritual Journey. Life is a quest for spiritual growth.",
	"Equality Before the Law. No one is above justice.",
	"Quest for Immortality. I seek to transcend mortality.",
	"Redemption of Others. I help others find their way.",
	"Excellence. Mediocrity is unacceptable.",
	"Freedom of Expression. Everyone should speak their mind.",
	"Divine Will. My actions are guided by higher powers.",
	"Escape. I am running from my past.",
	"Contentment. Happiness comes from appreciating what you have.",
	"Endurance. I will outlast any challenge.",
	"Fraternity. Brotherhood is thicker than blood.",
	"Conquest. I aim to expand my influence.",
	"Mystery. Some things are better left unknown.",
	"Heritage. My lineage defines me.",
	"Asceticism. Material possessions are meaningless.",
	"Deception. Information is best kept secret.",
	"Fortune Favors the Bold. Taking risks leads to rewards.",
	"Prophecy. I am fulfilling a foretold destiny."
	# Add more ideals as needed
]

# Age ranges for each race
# (Add this to your data definitions)

age_ranges = {
	"Human": (15, 80),
	"Dwarf": (40, 350),
	"Elf": (100, 750),
	"Half-Elf": (20, 180),
	"Goliath": (15, 100),
	"Half-Orc": (14, 75),
	# Add other races and their age ranges as needed
}

# Hit dice for each class
# (Add this to your data definitions)

hit_dice_dict = {
	"Barbarian": 12,
	"Bard": 8,
	"Cleric": 8,
	"Druid": 8,
	"Fighter": 10,
	"Monk": 8,
	"Paladin": 10,
	"Ranger": 10,
	"Rogue": 8,
	"Sorcerer": 6,
	"Warlock": 8,
	"Wizard": 6,
	# Include your custom classes with appropriate hit dice
	"Skald": 8,
	"Shaman": 8,
	"Berserker": 12,
	"Valkyrie": 10,
	"Seer": 6,
	"Mystic": 8,
	"Witch": 8,
	"Hunter": 10,
	"Runecaster": 8,
	"Explorer": 8,
	# Add other classes as needed
}

bonds = [
	"Family",
	"Clan",
	"Gods",
	"Homeland",
	"Mentor",
	"Comrades",
	"Loved One",
	"Oath",
	"Artifact",
	"Destiny",
	"Lost Love",
	"Childhood Friend",
	"Ancient Prophecy",
	"Forgotten Kingdom",
	"Ship",
	"Honor Debt",
	"Sacred Grove",
	"Ancestral Weapon",
	"Mystical Rune",
	"Fallen Comrade",
	"Secret Society",
	"Hidden Village",
	"Endangered Species",
	"Lost Relic",
	"Cursed Treasure",
	"Mystic Order",
	"Protective Spirit",
	"Sacred Duty",
	"Forbidden Love",
	"Eternal Rival",
	"Old Grudge",
	"The People",
	"Nature's Balance",
	"Ancient Enemy",
	"Family Heirloom",
	"Broken Promise",
	"Lost Sibling",
	"Guardian Spirit",
	"The Sea",
	"The Stars",
	"I will avenge my family's death, no matter the cost.",
	"My sword is a family heirloom, and I must honor it.",
	"I am the last of my tribe, and I must keep their memory alive.",
	"I owe my life to the warrior who saved me in battle.",
	"My loyalty to my chieftain is unwavering.",
	"I seek to prove myself worthy of joining the gods in Valhalla.",
	"The ancient runes guide my path, and I must decipher their meaning.",
	"I must protect my homeland from all threats.",
	"A mystical seer foretold a great destiny for me.",
	"I am searching for my long-lost sibling.",
	"My clan's honor depends on my actions.",
	"I made a vow to a dying comrade that I intend to keep.",
	"The spirits of my ancestors watch over me.",
	"I am driven to find the mythical city of Asgard.",
	"I protect a sacred artifact with my life.",
	"I am haunted by visions of a coming apocalypse.",
	"I owe a blood debt to a mysterious stranger.",
	"My mentor was slain by a monster; I will hunt it down.",
	"I am bound to serve a powerful druid who saved me.",
	"I have sworn to recover a stolen relic of great importance.",
	"My village was destroyed, and I seek to rebuild it.",
	"I seek the approval of the gods through my deeds.",
	"I promised to deliver a message to a faraway land.",
	"I am cursed until I fulfill an ancient prophecy.",
	"I bear the mark of a secret society.",
	"I search for the cure to a deadly disease afflicting my people.",
	"My best friend was taken by raiders; I will rescue them.",
	"I inherited a map to a hidden treasure.",
	"I must uphold the treaty between humans and mystical beings.",
	"A dragon destroyed my home; I seek vengeance.",
	"I have a recurring dream that I believe is a divine message.",
	"I am searching for the truth about my mysterious lineage.",
	"I carry a letter from a lost love.",
	"I owe my success to the generosity of a stranger.",
	"I am determined to end a long-standing feud between clans.",
	"My actions are guided by the teachings of a sacred text.",
	"I wear an amulet that holds a secret power.",
	"I was betrayed by someone I trusted; I seek to understand why.",
	"I must safeguard the last remaining member of a royal line.",
	"I protect the entrance to a sacred grove.",
	"I seek to restore my family's lost honor.",
	"I have a debt to repay to the dwarves of the mountain.",
	"I am on a quest to find a legendary weapon.",
	"I am compelled to protect the innocent wherever I go.",
	"I am the guardian of ancient knowledge.",
	"I swore an oath to a deity to complete a holy mission.",
	"I am the keeper of a dangerous secret.",
	"I strive to live up to the reputation of a famous ancestor.",
	"I rescued a creature who now accompanies me.",
	"I am linked to a powerful artifact that chose me.",
	"I seek to end the reign of a tyrannical ruler.",
	"I was given a vision of a great catastrophe that I must prevent.",
	"I must find the missing pieces of an ancient artifact.",
	"I owe allegiance to a secret order.",
	"I am haunted by the ghost of someone I failed to save.",
	"I promised to protect a child who is key to a prophecy.",
	"I am driven to master a rare form of magic.",
	"I seek redemption for a past misdeed.",
	"I am on a pilgrimage to sacred sites.",
	"I carry the legacy of a fallen hero.",
	"I am the only one who knows the location of a hidden realm.",
	"I must deliver a warning to a distant kingdom.",
	"I am bound to serve the rightful heir to the throne.",
	"I seek to uncover the truth behind a local legend.",
	"I protect a portal between worlds.",
	"I must prevent an ancient evil from rising again.",
	"I am searching for a teacher to help me control my powers.",
	"I promised to find the lost library of the ancients.",
	"I bear the burden of a family curse.",
	"I am determined to make a name for myself.",
	"I seek to unite warring factions against a common enemy.",
	"I was given a mission by a dying god.",
	"I owe my survival to a creature many consider a myth.",
	"I am connected to a powerful elemental force.",
	"I aim to map uncharted territories.",
	"I am the chosen guardian of a sacred text.",
	"I must recover my stolen memories.",
	"I seek to free a loved one from imprisonment.",
	"I was exiled and strive to earn my way back home.",
	"I am on a quest to break an unbreakable enchantment.",
	"I vowed to destroy a corrupt artifact.",
	"I am followed by a mysterious figure whose intentions are unclear.",
	"I must find the ingredients for a life-saving elixir.",
	"I am searching for signs of the old gods.",
	"I was given a riddle that I must solve.",
	"I protect a hidden village from discovery.",
	"I carry a key with no lock.",
	"I seek to learn the fate of an expedition that vanished.",
	"I am driven to perfect a craft or skill.",
	"I must keep a powerful item out of the wrong hands.",
	"I was tasked with guarding a powerful prisoner.",
	"I strive to prevent a prophecy from coming true.",
	"I am connected by fate to a person I've never met.",
	"I seek to restore balance to a disrupted natural order.",
	"I promised to help a spirit find peace.",
	"I was entrusted with a message that could change everything.",
	"I am searching for the origins of a mysterious artifact.",
	"I am bound to serve an ancient tree that grants me power.",
	"I seek to avenge the destruction of a sacred place.",
	"I was saved by magic and now must repay that debt.",
	"I protect a secret passage known only to me.",
	"I am followed by a loyal animal companion.",
	"I must return a lost relic to its rightful place.",
	"I seek to understand strange powers that have awakened within me.",
	"I have visions of events yet to come.",
	"I am dedicated to preserving a nearly extinct art form.",
	"I was given a task by a celestial being.",
	"I aim to recover the lost songs of my people.",
	"I am driven to find the one who betrayed me.",
	"I protect an heirloom that others wish to steal.",
	"I must find a way to communicate with an otherworldly being.",
	"I am searching for a place seen only in dreams.",
	"I was told I am the key to preventing a great disaster.",
	"I am determined to solve the mystery of my birth.",
	"I must find the missing pages of an ancient tome.",
	"I seek to learn the language of dragons.",
	"I carry the hopes of my village on my shoulders.",
	"I am the guardian of a sacred flame.",
	"I must protect a royal family member in disguise.",
	"I am driven to clear my family's tarnished name.",
	"I have a friendly rivalry with another adventurer.",
	"I owe my life to a community that took me in.",
	"I seek to recover artifacts stolen from my homeland.",
	"I am on a mission to prevent a war.",
	"I carry a prophecy that others seek to exploit.",
	"I must repay a life debt to an unexpected ally.",
	"I am the only one who knows the way to a hidden sanctuary.",
	"I am searching for the lost heir to a fallen kingdom.",
	"I vowed to protect the descendants of an ancient line.",
	"I seek to harness the power of a rare natural phenomenon."
	# Add more bonds as needed
]

flaws = [
	"Greedy",
	"Arrogant",
	"Impulsive",
	"Stubborn",
	"Vengeful",
	"Fearful",
	"Jealous",
	"Obsessive",
	"Cowardly",
	"Distrustful",
	"Overconfident",
	"Blunt",
	"Secretive",
	"Prideful",
	"Wrathful",
	"Superstitious",
	"Lazy",
	"Pessimistic",
	"Reckless",
	"Addictive Personality",
	"Quick to Anger",
	"Easily Distracted",
	"Overprotective",
	"Self-Doubting",
	"Materialistic",
	"Judgmental",
	"Envious",
	"Manipulative",
	"Gullible",
	"Mistrustful",
	"Dishonest",
	"Cruel",
	"Paranoid",
	"Sarcastic",
	"Selfish",
	"Unforgiving",
	"Impatient",
	"Narrow-Minded",
	"Melancholic",
	"Anxious",
	"Indecisive",
	"Withdrawn",
	"Resentful",
	"Workaholic",
	"Perfectionist",
	"Cynical",
	"Fatalistic",
	"Hot-headed",
	"Aloof",
	"Greedy for Power",
	"Obsessed with Revenge",
	"Neglectful",
	"Distracted by the Past",
	"Cowardly",
	"Vain",
	"Hot-tempered",
	"Reckless",
	"Pessimistic",
	"Distrustful",
	"Superstitious",
	"Envious",
	"Secretive",
	"Inflexible",
	"Indecisive",
	"Overconfident",
	"Gullible",
	"Selfish",
	"Judgmental",
	"Manipulative",
	"Lazy",
	"Dishonest",
	"Blunt",
	"Obsessive",
	"Paranoid",
	"Jealous",
	"Short-sighted",
	"Aloof",
	"Moody",
	"Withdrawn",
	"Clumsy",
	"Forgetful",
	"Impatient",
	"Disorganized",
	"Distracted",
	"Egotistical",
	"Miserly",
	"Cynical",
	"Unreliable",
	"Melancholic",
	"Hypochondriac",
	"Overly Cautious",
	"Fearful",
	"Nosy",
	"Overindulgent",
	"Absent-minded",
	"Easily Bored",
	"Intolerant",
	"Workaholic",
	"Restless",
	"Sarcastic",
	"Suspicious",
	"Prideful",
	"Unforgiving",
	"Vengeful",
	"Fickle",
	"Gluttonous",
	"Insecure",
	"Anxious",
	"Overprotective",
	"Detached",
	"Domineering",
	"Rebellious",
	"Self-doubting",
	"Self-destructive",
	"Clingy",
	"Daydreamer",
	"Defiant",
	"Emotionally Distant",
	"Fanatical",
	"Fatalistic",
	"Hedonistic",
	"Ill-tempered",
	"Inarticulate",
	"Indifferent",
	"Insensitive",
	"Intimidating",
	"Irresponsible",
	"Martyr Complex",
	"Merciless",
	"Obnoxious",
	"Opinionated",
	"Perfectionist",
	"Possessive",
	"Prejudiced",
	"Quick-tempered",
	"Regretful",
	"Rigid",
	"Ruthless",
	"Scheming",
	"Self-centered",
	"Self-critical",
	"Shy",
	"Spiteful",
	"Tactless",
	"Unassertive",
	"Weak-willed",
	"Hypocritical",
	"Misanthropic",
	"Obsessive-Compulsive",
	"Distrustful",
	"Overzealous",
	"Wasteful",
	"Imprudent",
	"Pessimistic",
	"Defeatist",
	"Volatile",
	"Hard-hearted",
	"Materialistic",
	"Ungrateful",
	"Uncooperative",
	"Impressionable",
	"Complacent",
	"Compulsive Liar",
	"Resentful",
	"Procrastinator",
	"Callous",
	"Easily Distracted",
	"Unambitious",
	"Vindictive",
	"Apathetic",
	"Greedy",
	"Melodramatic",
	"Overly Competitive",
	"Nosy",
	"Perfectionist",
	"Overly Sentimental",
	"Untrustworthy",
	"Cowardly",
	"Self-righteous",
	"Impulsive",
	"Blames Others",
	"Close-minded",
	"Cold",
	"Cruel",
	"Cynical",
	"Disloyal",
	"Dogmatic",
	"Egotistical",
	"Envious",
	"Fanatical",
	"Foolhardy",
	"Grudge-bearing",
	"Hostile",
	"Immature",
	"Impatient",
	"Intolerant",
	"Jealous",
	"Mean-spirited",
	"Moody",
	"Narcissistic",
	"Obsessive",
	"Paranoid",
	"Pessimistic",
	"Prejudiced",
	"Reckless",
	"Rude",
	"Sadistic",
	"Self-indulgent",
	"Spiteful",
	"Suspicious",
	"Unpredictable",
	"Violent",
	"Weak-willed",
	"Workaholic",
	"Xenophobic",
	"Zealous",
	"Overemotional",
	"Lacks Confidence",
	"Overly Ambitious",
	"Prone to Addictions",
	"Fear of Failure",
	"Lustful",
	"Obsessed with Power",
	"Easily Deceived",
	"Haunted by the Past",
	"Afraid of Commitment",
	"Clumsy",
	"Deceptive",
	"Easily Flustered",
	"Emotionally Fragile",
	"Gambler",
	"Greedy for Recognition",
	"Insensitive to Others",
	"Loner",
	"Obsessed with Death",
	"Overly Serious",
	"Prone to Nightmares",
	"Refuses Help",
	"Seeks Approval",
	"Self-Sacrificing",
	"Talkative",
	"Trouble Making Decisions",
	"Unhealthy Obsessions",
	"Withdrawn",
	"Won't Admit Mistakes",
	"Fear of the Unknown",
	"Perfectionist",
	"Overly Idealistic",
	"Easily Angered",
	"Fear of Intimacy",
	"Aversion to Authority",
	"Superstitious",
	"Obsessed with Revenge",
	"Poor Judge of Character",
	"Restless",
	"Obsessive Cleaner",
	"Fear of Being Alone",
	"Guilt-ridden",
	"Emotionally Unstable",
	"Overly Critical",
	"Prone to Exaggeration",
	"Stubbornly Independent",
	"Avoids Conflict",
	"Denial of Reality",
	"Needs Constant Validation",
	"Cannot Keep Secrets",
	"Addicted to Thrills",
	"Easily Offended",
	"Uncouth",
	"Low Self-Esteem",
	"Overly Suspicious",
	"Excessively Curious",
	"Unworldly",
	"Fear of Change",
	"Emotionally Dependent",
	"Lacks Direction",
	"Excessively Modest",
	"Overly Serious",
	"Overly Romantic",
	"Afraid of Confrontation",
	"Fear of Failure",
	"Lacks Ambition",
	"Lives in the Past",
	"Avoids Responsibility",
	"Dependent on Others",
	"Easily Tempted",
	"Fearful of Conflict",
	"Obsessive Hoarder",
	"Pathological Liar",
	"Fear of Rejection",
	"Unwilling to Forgive",
	"Overly Obedient",
	"Lacks Empathy",
	"Afraid of Commitment",
	"Cannot Handle Criticism",
	"Obsessed with Wealth",
	"Easily Led",
	"Puts Others First to a Fault",
	"Compulsive Gambler",
	"Cannot Keep a Promise",
	"Fearful of Supernatural",
	"Addicted to Danger",
	"Craves Attention",
	"Difficulty Trusting Others",
	"Excessively Proud",
	"Holds Grudges",
	"Lacks Imagination",
	"Needs to Be in Control",
	"Obsessed with Appearance",
	"Overly Competitive",
	"Rigid Thinking",
	"Seeks Approval from Everyone",
	"Unwilling to Take Risks"
	# Add more flaws as needed
]

personality_traits = [
	"I face problems head-on.",
	"I enjoy a good drink.",
	"I am haunted by memories of war.",
	"I have a strong sense of fair play.",
	"I never back down from a challenge.",
	"I see omens in every event.",
	"I am always calm, no matter what.",
	"I am driven by wanderlust.",
	"I am incredibly slow to trust.",
	"I work hard to play hard.",
	"I am quick to anger.",
	"I hide my emotions.",
	"I am full of inspiring tales.",
	"I ask a lot of questions.",
	"I am always polite and respectful.",
	"I am confident in my abilities.",
	"I take great pride in my work.",
	"I value honesty above all.",
	"I believe that actions speak louder than words.",
	"I am always willing to help others.",
	"I am fascinated by ancient mysteries.",
	"I prefer solitude.",
	"I am very protective of my friends.",
	"I hold grudges.",
	"I laugh loudly and often.",
	"I keep my thoughts to myself.",
	"I am fiercely loyal to my clan.",
	"I often dream of past battles.",
	"I enjoy the simple things in life.",
	"I have a poetic side few see.",
	"I am skeptical of magic and sorcery.",
	"I live by a code of honor.",
	"I am driven to seek out new experiences.",
	"I have little respect for those who avoid risk.",
	"I judge people by their actions, not their words.",
	"I treasure a memento of my past.",
	"I am slow to trust members of other races.",
	"I don't like to bathe.",
	"I bluntly say what others are hinting at or hiding.",
	"I enjoy being strong and like breaking things.",
	"I have a lesson for every situation, drawn from observing nature.",
	"I feel far more comfortable around animals than people.",
	"I express myself through song and verse.",
	"I use polysyllabic words to convey the impression of great erudition.",
	"I am always picking things up, absently fiddling with them.",
	"I am utterly serene, even in the face of disaster.",
	"I quote (or misquote) sacred texts and proverbs.",
	"I am tolerant of other faiths and respect the worship of other gods.",
	"I enjoy fine food, drink, and high society among my patrons.",
	"I pay lip service to the local gods.",
	"I am quietly studying the creatures around me.",
	"I am obsessed with collecting stories and legends.",
	"I am always polite and respectful.",
	"I am haunted by a past memory and sleep poorly.",
	"I have no room for caution in a life lived to the fullest.",
	"I don't talk about the thing that torments me.",
	"I expect danger around every corner.",
	"I refuse to become a victim, and will not allow others to be victimized.",
	"I feel tremendous empathy for all who suffer.",
	"I have a dark calling that puts me above the law.",
	"I would rather make a new friend than a new enemy.",
	"I'm a hopeless romantic, always searching for that 'special someone'.",
	"I am deeply connected to the spirits of my ancestors.",
	"I see the world as a puzzle to be solved.",
	"Possesses an unquenchable thirst for adventure, always seeking new horizons and uncharted territories to explore, believing that a life without discovery is no life at all.",
	"Holds an unwavering belief in the wisdom of the old gods, frequently consulting ancient runes and omens to guide decisions both trivial and significant.",
	"Exhibits a fierce and fiery temperament, quick to anger when honor is challenged, yet equally quick to forgive when apologies are made with sincerity.",
	"Carries a deep reverence for nature, feeling a strong connection to the forests, mountains, and seas, often spending time alone to commune with the spirits of the wild.",
	"Known for a silver tongue and sharp wit, capable of weaving words into compelling tales and songs that inspire allies and confound enemies.",
	"Harbors a solemn sense of duty to protect the weak and uphold justice, believing that true strength is demonstrated through acts of kindness and fairness.",
	"Haunted by vivid dreams and visions of past and future battles, sometimes experiencing moments of prophetic insight that influence their actions.",
	"Maintains a stoic demeanor in the face of adversity, rarely showing fear or doubt, and serving as a pillar of strength for those around them.",
	"Possesses an insatiable curiosity about the mysteries of the world, fascinated by magic, the supernatural, and the unknown forces that shape destiny.",
	"Deeply values loyalty and camaraderie, viewing their companions as family and willing to lay down their life to protect them.",
	"Embraces the warrior's code of honor, adhering strictly to principles of fairness in combat, and showing respect to worthy opponents.",
	"Driven by a personal quest to avenge a past wrong, channeling all efforts toward settling old scores and restoring personal or familial honor.",
	"Enjoys the pleasures of life to the fullest, indulging in feasts, drink, and celebration, believing that joy and revelry are as important as valor in battle.",
	"Believes that one's fate is woven by the Norns and accepts life's events with graceful resignation, seeing each moment as a thread in a grand tapestry.",
	"Displays a cunning and strategic mind, often devising clever plans and tactics that outsmart adversaries, valuing brains as much as brawn.",
	"Feels a strong connection to the sea, considering it both a friend and a foe, and possesses exceptional skills in navigation and shipcraft.",
	"Exhibits a generous and hospitable nature, always willing to share resources with those in need and welcoming strangers with open arms.",
	"Holds an unwavering optimism, maintaining hope even in the bleakest situations, and inspiring others to see the light amid darkness.",
	"Possesses a rebellious spirit, challenging traditional norms and authority, and advocating for individual freedom and self-determination.",
	"Has a penchant for storytelling, collecting tales from different lands and cultures, and sharing them to preserve history and entertain others.",
	"Guided by a strong moral compass, often acting as the voice of reason and mediator in disputes, striving for peace over conflict when possible.",
	"Obsessed with achieving eternal glory, seeking deeds that will ensure their name is remembered long after they are gone.",
	"Respects the wisdom of elders and actively seeks their counsel, valuing the knowledge passed down through generations.",
	"Displays an uncanny ability to remain calm under pressure, thinking clearly and acting decisively when situations become dire.",
	"Holds a secret fascination with the arcane arts, perhaps dabbling in magic or maintaining friendships with practitioners, despite societal skepticism.",
	"Fiercely protective of personal secrets and past, revealing little about themselves, which adds an air of mystery and intrigue.",
	"Believes strongly in the power of fate and destiny, often interpreting coincidences as signs and acting upon them with conviction.",
	"Exhibits a strong sense of humor, often using laughter to lift spirits and defuse tense situations, believing that mirth is a powerful weapon against despair.",
	"Lives by a strict personal code of ethics, which may differ from societal norms, and refuses to compromise these principles under any circumstances.",
	"Demonstrates exceptional craftsmanship or artistry, taking pride in creating works of beauty and utility, and seeing this as a form of personal expression.",
	"Carries a burden of guilt or regret over a past action, seeking redemption through acts of bravery or sacrifice.",
	"Feels a profound connection to animals, possibly having a trusted animal companion, and often preferring their company to that of other people.",
	"Values knowledge and learning, perhaps being self-taught or having studied under a mentor, and seeks to expand their understanding of the world.",
	"Exhibits an adventurous culinary palate, eager to try new foods and beverages, and possibly skilled in cooking traditional dishes.",
	"Has a strong competitive streak, turning even mundane activities into contests, and striving to be the best in all endeavors.",
	"Displays a nurturing side, taking younger or less experienced individuals under their wing, and offering guidance and protection.",
	"Believes in the interconnectedness of all things, seeing patterns and relationships others might miss, and contemplating the deeper meanings of events.",
	"Possesses an iron will and determination, refusing to give up even when faced with insurmountable odds, and inspiring others to do the same.",
	"Has a penchant for collecting trinkets and souvenirs from travels, each item holding sentimental value and a story.",
	"Harbors a deep-seated wanderlust, finding it difficult to stay in one place for long, and constantly seeking new experiences and challenges.",
	"Values silence and reflection, often spending time in solitude to meditate or contemplate, and may come across as reserved or introspective.",
	"Is deeply superstitious, carrying charms or performing rituals to ward off bad luck, and interpreting signs in the environment as omens.",
	"Exhibits a sarcastic wit and sharp tongue, often making cutting remarks that can both amuse and offend, and uses humor as a defense mechanism.",
	"Believes that actions speak louder than words, often leading by example rather than giving orders, and respects those who do the same.",
	"Has a soft spot for the underdog, instinctively siding with those who are oppressed or disadvantaged, and fighting against injustice.",
	"Possesses a deep love for music and poetry, perhaps playing an instrument or composing verses, and sees artistic expression as vital to the soul.",
	"Is known for their resourcefulness, able to make do with limited supplies and finding creative solutions to problems.",
	"Harbors a secret desire for peace and tranquility, perhaps dreaming of settling down someday, despite the demands of a warrior's life.",
	"Sees life as a grand game or challenge, approaching situations with a playful attitude, and enjoying outsmarting opponents in unexpected ways.",
	"Feels a strong connection to the night sky, perhaps studying the stars or feeling inspired by their vastness, and contemplates humanity's place in the cosmos.",
	"Believes in honoring promises and oaths above all else, considering one's word as a binding contract that must not be broken.",
	"Displays an innate empathy, able to sense the emotions of others, and often offering comfort or support to those in distress.",
	"Is driven by an insatiable desire for knowledge about the mystical and arcane, seeking out seers, sorcerers, and ancient texts in pursuit of hidden truths.",
	"Maintains an impeccable sense of honor in dealings, refusing to engage in deceit or treachery, even when such tactics might offer an advantage.",
	"Possesses an infectious enthusiasm and zest for life, lifting the spirits of those around them and approaching each day as a new adventure.",
	"Has a deep-rooted fear or phobia that influences behavior, perhaps stemming from a past trauma, and must be confronted to achieve personal growth.",
	"Believes that true strength comes from unity, striving to bring people together and fostering a sense of community and shared purpose.",
	"Is fiercely independent, valuing personal freedom above all else, and resisting any attempts to control or constrain their actions.",
	"Shows reverence for the cycles of life and death, perhaps participating in rituals to honor the deceased, and acknowledging the transient nature of existence.",
	"Possesses a strong sense of justice, unwilling to stand by while others are mistreated, and often stepping in to defend those who cannot defend themselves.",
	"Is guided by a personal mantra or philosophy, often quoting it in times of hardship, and using it as a compass to navigate moral dilemmas.",
	"Exhibits a deep love for storytelling, not just as entertainment but as a means of preserving history and teaching valuable lessons to others.",
	"Feels a strong kinship with mythical creatures or legends, perhaps believing they have a special connection or destiny intertwined with such beings.",
	"Is driven by a desire to leave a lasting legacy, undertaking grand projects or quests that will ensure they are remembered for generations to come.",
	"Holds a pragmatic view of the world, focusing on practical solutions and often eschewing ideals or emotions that may cloud judgment.",
	"Has an insatiable appetite for challenges, intentionally seeking out difficult tasks to test their limits and prove their capabilities.",
	"Is adept at reading people, picking up on subtle cues and body language, and often knowing what others are thinking or feeling without words.",
	"Believes in the importance of tradition and rituals, participating in cultural ceremonies with great enthusiasm and encouraging others to do the same.",
	"Possesses a hidden artistic talent, such as carving intricate designs, weaving, or metalworking, seeing beauty in craftsmanship.",
	"Is motivated by a desire to make amends for past mistakes, perhaps seeking forgiveness or attempting to right a previous wrong.",
	"Holds a fascination with the concept of fate versus free will, often pondering the extent to which their actions shape destiny.",
	"Is known for their meticulous attention to detail, whether in planning, crafting, or combat, believing that precision leads to excellence.",
	"Exhibits a nurturing side, taking care of animals or tending to the wounded, and valuing the preservation of life whenever possible.",
	"Believes that dreams hold significant meaning, keeping a journal of nightly visions and seeking interpretations from shamans or elders.",
	"Possesses a rebellious streak against the gods themselves, questioning divine authority and forging their own path regardless of omens or decrees.",
	"Finds solace in the simplicity of nature, preferring the quiet of the wilderness over the bustle of settlements, and often retreating into the wilds.",
	"Is haunted by a mysterious past, with gaps in memory or secrets that even they are not fully aware of, driving a quest for self-discovery.",
	"Shows a remarkable resilience in the face of hardship, recovering quickly from setbacks and using failures as lessons for future success.",
	"Believes that music and rhythm are integral to combat, perhaps fighting to a personal cadence or using drums and chants to inspire allies.",
	"Is deeply spiritual, not just in worship but in daily life, seeing the divine in all things and acting with a sense of sacred purpose.",
	"Exhibits a keen sense of humor even in dire situations, using laughter to cope with danger and to bond with companions.",
	"Possesses a strong sense of responsibility, feeling accountable for the welfare of others and sometimes bearing burdens that are not theirs to carry.",
	"Is fascinated by foreign cultures and customs, eager to learn from others and perhaps integrating new practices into their own life.",
	"Believes that true wisdom comes from experience, valuing firsthand knowledge over hearsay or theoretical learning.",
	"Has a natural affinity for leadership, often taking charge in group situations, and inspiring confidence through decisive actions.",
	"Views life as a series of tests set by the gods, approaching challenges as opportunities to prove worthiness and earn favor."
	# Add more personality traits as needed
]

# Gender-specific appearance descriptions
male_appearance_descriptions = [
	"Tall and imposing stature with a weathered face.",
	"Lean and agile, with piercing eyes that seem to look into the soul.",
	"Muscular build, with numerous battle scars adorning the arms.",
	"Long braided hair and beard, adorned with beads and small trinkets.",
	"Short-cropped hair with intricate tattoos covering the scalp.",
	"Wears a cloak made from wolf fur, symbolizing prowess as a hunter.",
	"Has a distinctive limp from an old injury, but it doesn't slow movement.",
	"Eyes are a striking shade of blue, uncommon among their people.",
	"Missing an ear, a souvenir from a fierce battle.",
	"Always wears a hood, keeping features hidden and mysterious.",
	"Hands are calloused from years of wielding weapons.",
	"Carries a small charm or amulet, a token from a loved one.",
	"Face is painted with traditional war paint.",
	"Hair is wild and untamed, reflecting a free spirit.",
	"Wears a necklace of animal teeth collected over the years.",
	"Scar across the left eye, vision unaffected but intimidating.",
	"Clothing is simple but well-maintained, preferring function over form.",
	"Often seen sharpening weapons, ever prepared for battle.",
	"Walks with a confident stride, exuding authority.",
	"Eyes hold a distant look, as if always lost in thought.",
	"Broad shoulders and a sturdy frame, built for endurance.",
	"Dark hair streaked with gray, showing signs of wisdom and age.",
	"Wears a helm adorned with raven feathers.",
	"Has a tattoo of a serpent winding up his arm.",
	"Beard braided into intricate patterns.",
	"One eye covered by an eye-patch, adding to his mysterious aura.",
	"Armor is dented and worn, showing years of use.",
	"Carries a large round shield painted with his clan's emblem.",
	"Voice is deep and resonant, commanding attention.",
	"Skin is tanned from years spent at sea.",
	"Eyes sparkle with mischief and hidden knowledge.",
	"Has a missing finger, lost during a crafting accident.",
	"Always seen with a pipe, puffing aromatic smoke.",
	"Wears a ring on every finger, each with its own story.",
	"Hair is tied back with a leather cord, keeping it out of his face.",
	"Wears a belt made from intertwined leather and metal.",
	"Has a slight limp but moves with surprising speed when needed.",
	"Face is stern, rarely showing emotion.",
	"Laugh lines around the eyes hint at a once jovial nature.",
	"Cloak is lined with fur, offering warmth in cold climates.",
	"Eyes are a piercing green, rare among his people.",
	"Hands are adorned with runic tattoos.",
	"Walks with the aid of a carved staff.",
	"Features are sharp and angular, giving a hawk-like appearance.",
	"Always wears a bandana or headband.",
	"Armor is polished to a shine, reflecting a disciplined nature.",
	"Keeps a small journal tucked into his belt.",
	"Ears are pierced with simple metal hoops.",
	"Has a deep, jagged scar running down his cheek.",
	"Carries a weathered map, edges frayed from use.",
	"Often seen whittling wood during moments of rest.",
	"He stands tall and broad-shouldered, with a mane of thick, golden hair that falls to his shoulders, often bound by leather cords to keep it from his piercing blue eyes. His beard is full and well-groomed, braided into two strands adorned with small bronze beads. His weathered skin bears the marks of many voyages, and intricate knotwork tattoos wrap around his muscular arms, telling tales of his adventures.",
	"His raven-black hair is cut short on the sides but left long on top, swept back from his forehead. A single braid hangs by his temple, signifying his family's lineage. His deep-set grey eyes are sharp and observant beneath heavy brows. A neatly trimmed beard frames his strong jawline, and a small scar cuts across his left cheek, a souvenir from past battles.",
	"He possesses a striking appearance with fiery red hair cascading down his back, often tied into a loose ponytail. His beard is thick and untamed, woven with beads made from bone and horn. His green eyes are bright and fierce, reflecting the untamed spirit of the northern forests. His skin is fair, dotted with freckles, and his hands are calloused from years of wielding axe and oar.",
	"His long, sandy blonde hair is often tied back with a simple leather thong, revealing a high forehead and keen blue eyes that seem to hold the wisdom of the seas. His face is clean-shaven, uncommon among his peers, highlighting his strong cheekbones and the faint lines etched from years of laughter and song. A silver earring in the shape of a wolf's head adorns his left ear.",
	"He has a rugged and weather-beaten face, with dark brown hair cut shoulder-length and kept loose. His beard is thick and bushy, braided into a single plait down the center. His hazel eyes are warm but carry a hint of melancholy. His skin bears the tan of long days under the sun, and his arms are marked with tattoos depicting dragons and mythical beasts.",
	"His appearance is commanding, with short-cropped black hair and a beard that is meticulously groomed. His dark eyes are intense and seem to pierce into the soul. A thin, silver circlet rests upon his brow, denoting his status among his people. His skin is olive-toned, and a thin scar traces along his jawline, a reminder of youthful duels.",
	"He sports long, flaxen hair that flows freely, often catching the wind as he sails. His beard is a cascade of golden curls, adorned with small metal rings etched with runes. His blue eyes are as clear as the summer sky, and his face carries a perpetual smile. His physique is lean but muscular, honed by years of navigating treacherous waters.",
	"His auburn hair is wild and unkempt, matching his fiery spirit. His beard is thick and reaches his chest, woven into intricate braids. His green eyes are bright and full of mischief, set beneath a brow often furrowed in thought. Tattoos of knotwork and symbols of protection cover his neck and extend down his back.",
	"He has a clean-shaven head, a practical choice for battle, revealing a head tattooed with intricate patterns symbolizing his clan and achievements. His beard is long and dark, tied at the end with a leather cord. His eyes are a deep brown, nearly black, and his gaze is steady and unwavering. His skin is marked by scars from numerous battles, each one a badge of honor.",
	"His hair is a mix of greys and blacks, showing the wisdom of his years. He keeps it long, tied back in a simple knot. His beard is full but neatly trimmed, with silver strands glinting in the light. His blue eyes are sharp, taking in everything around him with the experience of a seasoned warrior. A wolf pelt cloak drapes over his broad shoulders.",
	"He has short, sandy hair and a closely cropped beard, both lightened by the sun. His skin is weathered and tanned, evidence of countless voyages at sea. His eyes are a piercing grey, always scanning the horizon. A simple bronze torc circles his neck, and his arms are adorned with arm rings signifying victories and alliances.",
	"His dark brown hair is styled in braids along the sides, leaving the top loose to fall around his face. His beard is medium length, braided with beads of silver. His green eyes are calm and contemplative, reflecting a thoughtful nature. His skin is fair, with a few battle scars visible on his forearms. He wears a simple pendant of Thor's hammer around his neck.",
	"He is tall and imposing, with a shaved head and a thick red beard that reaches his chest. His beard is braided and bound with iron rings. His eyes are a light blue, almost icy in appearance, contrasting with his ruddy complexion. Tattoos of knotwork cover his scalp, making a bold statement of his warrior status.",
	"His light brown hair is shoulder-length and often pulled back, revealing a high forehead and intelligent eyes of hazel. His beard is neatly trimmed, a rarity among his peers. His face is unmarred by scars, suggesting cunning over brute force. A small silver earring in the shape of a raven adorns his ear, symbolizing wisdom.",
	"He has thick black hair that falls just below his ears, often tousled by the wind. His beard is short and well-kept. His eyes are dark brown, almost black, and hold a quiet intensity. His olive-toned skin suggests a heritage from distant lands. He wears a leather band around his forehead, decorated with simple knotwork patterns.",
	"He possesses a mane of curly blonde hair, wild and untamed. His beard is equally full, often with bits of leaves or twigs caught within, as he spends much time in the forests. His green eyes sparkle with humor and a zest for life. His skin is tanned, and his hands are rough from labor. He often wears simple clothing, favoring practicality over adornment.",
	"His grey hair is kept short, and his beard is full and untrimmed, showing his age and experience. His blue eyes are clear and sharp, undimmed by the years. His face is deeply lined, and a large scar runs from his forehead down to his cheek, a testament to his survival in battle. He carries himself with the confidence of a seasoned leader.",
	"He has reddish-brown hair styled into several braids that fall over his shoulders. His beard is long and braided, adorned with bronze beads shaped like animals. His eyes are a warm brown, and his face often bears a friendly smile. His skin is fair, and he has a tattoo of a serpent winding around his left arm.",
	"He sports a distinctive look with one side of his head shaved and the other left with long, dark hair that he ties back. His beard is trimmed short. His eyes are a striking grey, and a small scar crosses his right eyebrow. He wears a leather choker with a pendant in the shape of a bear's claw.",
	"He has thick, wavy hair the color of chestnuts, usually kept under a simple woolen cap. His beard is medium length, with two small braids on either side. His hazel eyes are observant and kind. His skin is freckled from sun exposure, and he often has a smudge of dirt or soot from his work as a blacksmith.",
	"He possesses a bald head and a neatly trimmed goatee, giving him a distinguished appearance. His eyes are a deep blue, and his gaze is thoughtful. His skin is fair, and he bears a tattoo of a compass rose on the back of his neck. He dresses in well-made clothing, reflecting his status as a successful trader.",
	"His long, silver hair flows freely down his back, a sign of his advanced years. His beard is equally long, braided and bound with golden rings. His eyes are a faded blue, still sharp with wisdom. His skin is lined but carries a healthy glow. He wears a cloak made of rich fabrics, denoting his high rank.",
	"He has sandy blonde hair styled into tight braids along his scalp, leaving the rest to fall freely. His beard is short and squared. His green eyes are bright and mischievous. His skin is lightly tanned, and he has a tattoo of runes along his collarbone. He often wears a smirk, hinting at a clever mind.",
	"His hair is a dark brown, cut short for practicality. His beard is full but kept tidy. His eyes are a rich brown, warm and inviting. His skin is olive-toned, with a few scars visible on his arms. He wears simple clothing, preferring function over form, and carries a small pouch of herbs at his belt.",
	"He has thick black hair that he keeps in a topknot, with the sides of his head shaved. His beard is long and braided, adorned with iron beads. His eyes are a cold blue, and his face is stern. His skin is pale, and he has tattoos of interlocking knots covering his arms and neck.",
	"He sports wavy blonde hair that he often lets fall freely, framing his strong features. His beard is trimmed short. His eyes are a deep blue, almost indigo, and his smile is warm. His skin is fair, with a few freckles across his nose. He wears a simple leather bracelet on his wrist.",
	"He has auburn hair cut to medium length, with a slight wave. His beard is thick and reaches just below his chin, often tied with a leather cord. His green eyes are alert and sharp. His skin is tanned from long days outdoors. He carries himself with the ease of someone comfortable in both forests and battlefields.",
	"He possesses jet-black hair that he keeps neatly trimmed. His beard is short and neatly maintained. His eyes are dark brown, nearly black, and he often appears deep in thought. His skin is a light olive tone, and he wears a small silver chain around his neck. He dresses simply but with an air of quiet dignity.",
	"He has a mane of thick, grey hair, showing the passage of time. His beard is long and full, with beads of wood and bone woven into it. His eyes are a piercing grey, still sharp despite his age. His skin is weathered, and he bears numerous scars. He wears a cloak made from wolf pelts.",
	"He sports short, light brown hair and a clean-shaven face, unusual among his peers. His eyes are a clear blue, and his features are youthful. His skin is fair, and he has a tattoo of a raven on his forearm. He often wears a simple tunic and trousers, favoring mobility.",
	"He has long, dark blonde hair pulled back into a braid. His beard is medium length, braided at the chin. His eyes are a warm brown, and his face is friendly. His skin is lightly tanned, and he wears a simple leather necklace with a small pendant in the shape of a ship.",
	"He possesses a distinctive look with his reddish hair shaved on one side and left long on the other, often braided. His beard is thick and unkempt. His green eyes are bright and full of energy. His skin is freckled, and he has a tattoo of a dragon curling around his neck.",
	"He has black hair cut short and a full beard that is neatly trimmed. His eyes are a deep brown, almost black, and his gaze is intense. His skin is olive-toned, and he bears a scar across his nose. He wears a silver arm ring engraved with knotwork designs.",
	"He sports light brown hair that he keeps in several small braids. His beard is short and trimmed. His eyes are hazel, shifting between green and brown. His skin is fair, and he often has a smudge of dirt from his work as a carpenter. He wears simple clothing, with a tool belt at his waist.",
	"He has thick, dark hair that falls to his shoulders, often pulled back during work. His beard is full and reaches his chest, adorned with beads of horn. His eyes are a sharp grey, and his face bears the marks of past battles. His skin is tanned, and he wears a bear claw necklace.",
	"He possesses long, silver hair that he keeps tied back. His beard is equally long, often braided. His eyes are a piercing blue, still vibrant despite his age. His skin is lined but healthy, and he carries himself with the grace of a seasoned warrior. He wears a cloak adorned with fur trim.",
	"He has short, sandy blonde hair and a neatly trimmed beard. His eyes are a light blue, almost grey. His skin is fair, and he bears a tattoo of Thor's hammer on his upper arm. He wears simple clothing but takes pride in keeping it well-maintained.",
	"He sports a shaved head and a full, dark beard that is braided. His eyes are a deep brown, and his gaze is intense. His skin is olive-toned, and he has tattoos of knotwork covering his arms. He wears a leather necklace with a pendant shaped like a wolf's head.",
	"He has thick, curly brown hair that he often ties back. His beard is full but kept tidy. His eyes are a warm brown, and his smile is friendly. His skin is tanned, and he often smells of the sea. He wears simple clothing suitable for sailing.",
	"He possesses long, golden hair that falls in loose waves. His beard is short and neatly trimmed. His eyes are a clear blue, and his features are sharp. His skin is fair, and he wears a silver ring on his finger. He dresses in finely made clothing, reflecting his status.",
	"He has short, black hair and a clean-shaven face. His eyes are a piercing grey, and his expression is serious. His skin is pale, and he bears a scar across his cheek. He wears a simple iron pendant around his neck.",
	"He sports shoulder-length brown hair and a medium-length beard. His eyes are green, and his face is often lit with a smile. His skin is lightly tanned, and he has a tattoo of an eagle on his arm. He wears simple clothing, favoring comfort.",
	"He possesses a bald head and a neatly trimmed beard. His eyes are a deep blue, and his gaze is thoughtful. His skin is fair, and he wears a silver earring. He dresses in practical clothing, suitable for travel.",
	"He has long, dark hair that he keeps loose. His beard is thick and reaches his chest. His eyes are a dark brown, and his expression is often stern. His skin is tanned, and he bears tattoos of knotwork on his arms. He wears a leather arm band.",
	"He sports short, blonde hair and a clean-shaven face. His eyes are a light green, and his smile is warm. His skin is fair, and he wears a simple necklace. He dresses in well-made clothing, reflecting his trade.",
	"He has thick, black hair that he keeps tied back. His beard is short and neatly trimmed. His eyes are a sharp grey, and his face is stern. His skin is olive-toned, and he wears a silver ring on his finger. He dresses simply but with an air of authority.",
	"He possesses long, brown hair that falls freely. His beard is full and unkempt. His eyes are a warm brown, and his smile is friendly. His skin is tanned, and he often wears a simple hat. He dresses in practical clothing suitable for farming.",
	"He has short, grey hair and a neatly trimmed beard. His eyes are a piercing blue, and his gaze is sharp. His skin is weathered, and he bears numerous scars. He wears a cloak made from animal hides.",
	"He sports shoulder-length blonde hair and a full beard. His eyes are a deep blue, and his expression is serious. His skin is fair, and he wears a leather bracelet. He dresses in practical clothing, suitable for hunting.",
	"He possesses a shaved head and a thick beard. His eyes are a dark brown, and his gaze is intense. His skin is pale, and he bears tattoos of dragons on his arms. He wears a silver chain around his neck.",
	"He has long, red hair that he keeps in braids. His beard is thick and braided. His eyes are a bright green, and his smile is mischievous. His skin is freckled, and he wears a leather necklace.",
	"He sports short, brown hair and a clean-shaven face. His eyes are a warm brown, and his smile is friendly. His skin is fair, and he wears simple clothing. He often carries a satchel of tools.",
	"He possesses thick, black hair that he keeps short. His beard is full and neatly trimmed. His eyes are a piercing blue, and his expression is serious. His skin is olive-toned, and he wears a silver pendant.",
	"He has shoulder-length blonde hair and a full beard. His eyes are a light blue, and his smile is warm. His skin is fair, and he wears a leather bracelet. He dresses in practical clothing, suitable for travel.",
	"He sports a bald head and a thick, grey beard. His eyes are a sharp grey, and his gaze is stern. His skin is weathered, and he wears a cloak made from animal hides. He carries himself with authority.",
	"He possesses long, dark hair that he keeps tied back. His beard is short and neatly trimmed. His eyes are a deep brown, and his smile is friendly. His skin is olive-toned, and he wears a simple necklace.",
	"He has short, blonde hair and a clean-shaven face. His eyes are a light green, and his expression is serious. His skin is fair, and he wears a leather bracelet. He dresses in practical clothing, suitable for work.",
	"He sports thick, brown hair that he keeps in a topknot. His beard is full and reaches his chest. His eyes are a warm brown, and his smile is friendly. His skin is tanned, and he wears a simple necklace.",
	"He possesses a shaved head and a neatly trimmed beard. His eyes are a piercing blue, and his gaze is thoughtful. His skin is fair, and he wears a silver earring. He dresses in practical clothing, suitable for sailing.",
	"He has long, black hair that he keeps loose. His beard is thick and unkempt. His eyes are a dark brown, and his expression is stern. His skin is tanned, and he bears tattoos of knotwork on his arms.",
	"He sports short, blonde hair and a clean-shaven face. His eyes are a light green, and his smile is warm. His skin is fair, and he wears a simple necklace. He dresses in well-made clothing.",
	"He possesses thick, black hair that he keeps tied back. His beard is short and neatly trimmed. His eyes are a sharp grey, and his face is stern. His skin is olive-toned, and he wears a silver ring."
	# Add more male appearances as needed
]

female_appearance_descriptions = [
	"Graceful and tall, with long flowing hair that catches the wind.",
	"Eyes as sharp as a hawk's, missing nothing in her surroundings.",
	"Muscular and athletic build, evidence of rigorous training.",
	"Hair braided intricately, adorned with flowers or beads.",
	"Wears a cloak made from bear fur, symbolizing strength.",
	"Face painted with symbols of protection and power.",
	"Carries herself with regal bearing, hinting at noble birth.",
	"Scar across her forearm, a reminder of past battles.",
	"Wears a necklace with a pendant shaped like a raven.",
	"Eyes are a deep green, reflecting the forests she loves.",
	"Clothing is practical yet well-crafted, indicating artisan skills.",
	"Hair is cut short, emphasizing her no-nonsense attitude.",
	"Often seen with a flower tucked behind her ear.",
	"Skin is lightly freckled from time spent outdoors.",
	"Has a tattoo of intertwined knots on her wrist.",
	"Voice is melodic, captivating those who hear her speak.",
	"Carries a staff adorned with feathers and ribbons.",
	"Eyes are bright and inquisitive, full of curiosity.",
	"Wears a silver circlet, suggesting a connection to the divine.",
	"Armor is sleek and fitted, allowing for agile movement.",
	"Wears earrings shaped like tiny axes.",
	"Hair shimmers with hints of silver, despite her youth.",
	"Carries a satchel filled with herbs and remedies.",
	"Hands are nimble and delicate, yet strong.",
	"Has a birthmark shaped like a crescent moon.",
	"Walks with quiet grace, moving almost silently.",
	"Wears bracelets that jingle softly with each movement.",
	"Eyes hold a hint of sadness, betraying past hardships.",
	"Often seen reading a worn, leather-bound book.",
	"Laugh is infectious, lifting the spirits of those around her.",
	"Cloak is embroidered with patterns of stars and constellations.",
	"Has a small, intricate tattoo behind her ear.",
	"Carries a dagger strapped to her thigh.",
	"Wears boots laced up to the knee, perfect for long journeys.",
	"Hair is dyed in streaks of red and gold.",
	"Has a gentle smile that puts others at ease.",
	"Wears a ring on a chain around her neck.",
	"Eyes change color slightly depending on the light.",
	"Wields a bow almost as tall as she is.",
	"Wears a belt with various pouches and tools.",
	"Has a small scar above her eyebrow, barely noticeable.",
	"Wears a pendant in the shape of a tree.",
	"Voice has a calming effect on those who hear it.",
	"Clothing features intricate embroidery of leaves and vines.",
	"Often seen gazing at the horizon, lost in thought.",
	"Wears fingerless gloves for better grip on her weapons.",
	"Hair is styled in elaborate updos for special occasions.",
	"Has a collection of rings on her fingers, each unique.",
	"Eyes reflect the colors of the sea.",
	"Carries a shield emblazoned with her family's crest.",
	"She has long, flowing golden hair that cascades over her shoulders like a shimmering waterfall, framing a face with piercing blue eyes that reflect the depths of the northern seas. Her skin is fair and smooth, with a hint of rose in her cheeks, and she moves with the grace of a snow leopard across the tundra.",
	"Her raven-black hair is intricately braided with silver threads and small runic charms, falling over a cloak woven from the midnight sky. Her emerald eyes hold a mysterious glint, and her lips curve into a knowing smile that hints at untold secrets.",
	"She possesses a striking beauty marked by fiery red hair that falls in wild curls down her back, reminiscent of flames dancing in the hearth. Her freckled skin tells tales of days spent under the open sky, and her eyes sparkle with mischief and the promise of adventure.",
	"Her ice-blonde hair is pulled back into a sleek knot adorned with a single hawk feather, highlighting high cheekbones and a strong jawline. Her grey eyes are as stormy as the winter seas, and her gaze carries both wisdom and a hint of melancholy.",
	"She exudes an aura of enchantment, with silvery hair that seems to glow under the moonlight and eyes of a deep violet hue. Intricate tattoos of ancient symbols trace along her arms and neck, suggesting a deep connection to the mystical arts.",
	"Her warm brown hair is styled in intricate braids intertwined with beads of amber and bone. Her olive skin is kissed by the sun, and her eyes are a rich hazel flecked with gold, mirroring the autumn forests of her homeland.",
	"She has a fierce and captivating presence, with jet-black hair cut sharply at her shoulders and eyes as dark as the deepest night. A delicate scar traces her left cheek, adding to her allure and hinting at battles fought and survived.",
	"Her long, wavy hair is the color of ripe wheat, crowned with a circlet of wildflowers that complement her rosy complexion. Her blue-green eyes reflect the serenity of tranquil fjords, and her laughter is as light and refreshing as a summer breeze.",
	"She embodies an ethereal beauty, with alabaster skin and hair as white as freshly fallen snow, flowing freely down to her waist. Her eyes are a startling icy blue, almost translucent, giving her an otherworldly appearance.",
	"Her chestnut hair is gathered into a loose braid draped over one shoulder, adorned with feathers and small wooden charms. Her green eyes are bright and inquisitive, set beneath delicately arched brows, and her smile is warm and inviting.",
	"She cuts a striking figure in dark attire, with deep burgundy hair that falls in loose waves around her face. Her eyes are a smoldering amber, and her lips are painted with a hint of plum. Silver rings adorn her fingers, each etched with runes.",
	"Her appearance is captivatingly mysterious, with long, dark hair framing a pale face marked by intricate, swirling designs painted in ash. Her eyes are a luminous grey, and she wears layers of flowing garments that move like shadows around her.",
	"She has sun-kissed skin and honey-blonde hair that catches the light, braided with strands of gold thread. Her eyes are a clear sky blue, radiating confidence and a zest for life. A pendant shaped like a sun hangs around her neck.",
	"Her ebony hair is styled into elaborate braids that form a crown atop her head, interwoven with strands of copper. Her dark brown eyes are intense and soulful, and a subtle tattoo of a crescent moon graces her forehead.",
	"She possesses a haunting beauty, with straight, silver-grey hair that falls like a veil around her. Her pale skin contrasts sharply with her dark attire, and her violet eyes seem to pierce into one's very soul. She wears a cloak that billows like mist.",
	"Her auburn hair is cropped short, highlighting her strong features and the intricate knotwork tattoos that adorn the sides of her head. Her eyes are a fierce green, and she carries herself with the confidence of a seasoned warrior.",
	"She exudes elegance, with long, silky black hair pulled back into a high ponytail, revealing delicate ears adorned with silver cuffs. Her eyes are a deep ocean blue, and her movements are graceful and purposeful, like a dancer or a blade in motion.",
	"Her appearance is both enchanting and intimidating, with wild, dark curls that frame her face and cascade down her back. Her eyes are a striking silver-grey, and dark, smoky makeup accentuates their intensity. She wears layered garments adorned with occult symbols.",
	"She has an air of mysticism, with pale blonde hair that she wears loose, allowing it to flow freely in the wind. Her eyes are a serene green, and she often has a distant look, as if gazing into realms unseen by others. She wears simple yet elegant robes in earthy tones.",
	"Her fiery red hair is styled into intricate braids adorned with small bones and feathers, giving her a fierce and wild appearance. Her eyes are a piercing blue, and war paint marks her face in bold lines. She carries herself with the pride of a seasoned huntress.",
	"She is enveloped in an aura of dark enchantment, with long, straight black hair that falls like a shadow around her. Her pale skin is contrasted by deep crimson lips, and her eyes are a hauntingly beautiful shade of dark green. She wears layers of dark fabrics embellished with metallic accents.",
	"Her golden-brown hair is tied back with leather cords, revealing a strong face with sharp features. Her hazel eyes are keen and observant, and a subtle scar runs across her right eyebrow. She dresses in practical attire suited for travel and survival.",
	"She has a captivating presence, with platinum blonde hair styled into an intricate updo adorned with pearls. Her blue eyes sparkle with intelligence and wit, and her attire is a blend of elegance and practicality, featuring fine fabrics and subtle armor pieces.",
	"Her dark brown hair is left unbound, cascading over her shoulders like a waterfall. Her eyes are a warm amber, and her smile is gentle yet enigmatic. She wears a cloak of deep green, embroidered with patterns of leaves and vines.",
	"She embodies the essence of a seeress, with long, silvery hair adorned with small charms and amulets. Her eyes are a pale blue, almost white, and seem to see beyond the physical realm. She wears layers of flowing garments in shades of grey and blue.",
	"Her look is striking and edgy, with deep purple hair cut in asymmetrical layers and a single braid adorned with silver beads. Her eyes are dark and intense, lined with kohl, and her lips are painted a deep berry color. Tattoos of ancient symbols trace along her arms.",
	"She has a timeless beauty, with wavy chestnut hair that falls to her mid-back. Her eyes are a deep, soulful brown, and her skin carries a warm, golden hue. She dresses in garments that blend traditional designs with subtle embellishments.",
	"Her appearance is otherworldly, with alabaster skin and hair that shimmers with shades of blue and silver. Her eyes are a luminescent turquoise, and she wears delicate jewelry crafted from shells and pearls. She moves with a fluid grace reminiscent of water.",
	"She possesses a fierce elegance, with long black hair pulled back into a tight braid. Her eyes are a sharp grey, and her features are accented with subtle, dark markings. She wears armor crafted with intricate designs, reflecting both functionality and artistry.",
	"Her strawberry-blonde hair is worn in loose waves, and a simple circlet rests upon her brow. Her green eyes are bright and full of life, and her cheeks are rosy. She wears light, flowing dresses that allow ease of movement and reflect her free spirit.",
	"She has a dark and mysterious allure, with charcoal-black hair that contrasts sharply with her pale complexion. Her eyes are a deep, captivating violet, and she wears dark attire accented with silver and gemstones. She exudes confidence and a touch of danger.",
	"Her sandy blonde hair is styled into multiple braids adorned with small seashells, hinting at a life by the sea. Her blue-grey eyes are calm and thoughtful, and she wears practical clothing suitable for sailing, with a touch of feminine flair.",
	"She exudes an aura of ancient wisdom, with silver hair that falls straight and smooth. Her eyes are a pale green, almost translucent, and her face bears delicate tattoos of runic symbols. She wears robes in shades of white and silver, and carries a staff adorned with crystals.",
	"Her look is bold and unapologetic, with fiery orange hair styled into a mohawk and sides shaved to reveal intricate knotwork tattoos. Her eyes are a striking amber, and she wears leather armor accented with metal spikes and chains.",
	"She has an ethereal beauty, with long, flaxen hair that glows softly in the sunlight. Her eyes are a gentle blue, and her skin seems to radiate warmth. She wears simple garments of natural fabrics, and often has flowers woven into her hair.",
	"Her appearance is both elegant and fierce, with dark brown hair pulled back into a high ponytail. Her sharp cheekbones and strong jawline are accented by minimalistic jewelry. Her attire is sleek and functional, designed for agility and speed.",
	"She embodies the spirit of the wild, with untamed auburn hair adorned with feathers and beads. Her green eyes are bright and alert, and her face is marked with subtle patterns of war paint. She wears clothing made from furs and leathers.",
	"Her look is mysterious and enchanting, with deep blue-black hair that seems to blend into the shadows. Her eyes are a luminous silver, and she wears dark, flowing garments adorned with intricate embroidery and subtle metallic accents.",
	"She has a regal bearing, with platinum blonde hair styled into an elaborate braid crown. Her eyes are a piercing blue, and her features are refined and symmetrical. She wears finely crafted clothing accented with embroidery and jewels.",
	"Her appearance is striking, with crimson hair that falls in thick curls around her face. Her eyes are a deep emerald green, and her lips are naturally rosy. She wears clothing in rich colors, and her accessories feature gemstones and intricate metalwork.",
	"She exudes a dark charm, with jet-black hair cut into a sharp bob that frames her face. Her eyes are a deep brown, almost black, and she wears dark eyeliner that accentuates their intensity. Her attire is layered, featuring textures like lace and leather.",
	"Her golden hair is styled into loose braids that fall over her shoulders. Her blue eyes are bright and inquisitive, and her smile is warm and genuine. She wears simple yet well-made clothing, suitable for both travel and social gatherings.",
	"She possesses a haunting beauty, with pale skin and hair the color of moonlight. Her eyes are a soft grey, and she often appears lost in thought. She wears flowing garments in shades of white and silver, and carries a book of ancient lore.",
	"Her look is bold and fierce, with dark hair pulled back into tight braids. Her eyes are a striking hazel, and her face is adorned with war paint in intricate designs. She wears armor that is both functional and decorated with symbols of her clan.",
	"She has an air of mystery, with long, straight hair of a deep mahogany hue. Her eyes are a warm brown, flecked with gold, and her skin has a natural glow. She wears jewelry made from natural materials like wood and stone.",
	"Her appearance is enchanting, with soft curls of blonde hair and eyes the color of the sea after a storm. She wears dresses that flow like water, in hues of blue and green, and her demeanor is calm and soothing.",
	"She exudes confidence, with short, spiky hair dyed a deep indigo. Her eyes are a sharp blue, and she has a small nose piercing. Her attire is modern and edgy, incorporating traditional elements in unconventional ways.",
	"She has a serene presence, with long, silken hair of a rich chestnut color. Her eyes are gentle and kind, a soft brown that reflects compassion. She wears simple robes in earthy tones, and often carries herbs and healing supplies.",
	"Her look is dramatic and intense, with dark hair styled into elaborate braids and adorned with metallic beads. Her eyes are a vivid green, and dark makeup accentuates their brightness. She wears layers of dark fabrics with intricate patterns.",
	"She embodies a free spirit, with sun-streaked blonde hair that is left loose and wild. Her eyes are a bright blue, and her skin is tanned from time spent outdoors. She wears light, comfortable clothing and often goes barefoot.",
	"Her appearance is both delicate and strong, with pale skin and hair of a soft ash blonde. Her eyes are a clear grey, and she wears minimal jewelry. Her attire is simple but well-crafted, reflecting a balance between functionality and elegance.",
	"She has a captivating aura, with long black hair that shines with hints of blue under certain light. Her eyes are a deep brown, almost black, and her features are accented with subtle makeup. She wears clothing that is both stylish and practical.",
	"Her fiery red hair is her most striking feature, cascading down her back in loose waves. Her green eyes sparkle with mischief, and her smile is infectious. She wears clothing in vibrant colors, reflecting her lively personality.",
	"She exudes an air of wisdom beyond her years, with silver-streaked hair and eyes that shift between blue and grey. Her face bears the faint lines of time, adding to her dignified appearance. She wears robes adorned with symbols of knowledge and learning.",
	"Her appearance is edgy and unconventional, with hair dyed a deep teal and styled into an undercut. Her eyes are a bright blue, and she has several ear piercings. She wears a mix of traditional and modern clothing, creating a unique and bold style.",
	"She has a natural beauty, with wavy brown hair and hazel eyes that reflect the colors of the forest. Her skin is lightly freckled, and she often wears a crown of leaves or flowers. Her clothing is made from natural fabrics and dyes.",
	"She possesses a haunting allure, with pale skin and dark hair that contrasts sharply. Her eyes are a piercing blue, and she wears dark attire accented with lace and subtle embroidery. She carries herself with grace and confidence.",
	"Her look is both fierce and elegant, with braided blonde hair adorned with small metal rings. Her eyes are a sharp grey, and her attire blends armor with flowing fabrics, reflecting her dual roles as a warrior and a leader.",
	"She embodies a mystical presence, with hair that transitions from dark brown to a deep purple at the ends. Her eyes are a captivating hazel, and she wears layers of jewelry featuring crystals and symbols. Her attire is flowing and layered.",
	"Her appearance is warm and inviting, with curly auburn hair and eyes that are a soft brown. Her smile is genuine, and her laughter is infectious. She wears comfortable clothing in earthy tones, and often has a satchel of supplies at her side.",
	"She has a bold and striking look, with shaved sides and a long braid of dark hair down her back. Her eyes are a deep green, and she has a tattoo of a raven on her neck. Her attire is functional, featuring leather and metal accents.",
	"She exudes elegance, with long, straight blonde hair and eyes the color of honey. Her skin is fair, and she wears finely crafted dresses adorned with subtle embroidery. She carries herself with poise and confidence.",
	"Her appearance is edgy and mysterious, with dark hair styled into a messy bob. Her eyes are a smoky grey, and she wears dark eyeliner that accentuates their intensity. Her attire is layered, featuring a mix of textures and dark colors.",
	"She possesses a timeless beauty, with soft brown hair pulled back into a simple bun. Her eyes are a warm hazel, and her features are gentle and refined. She wears modest clothing, reflecting a focus on inner qualities over outward appearances.",
	"Her look is captivating and unique, with hair dyed a deep forest green and styled in loose waves. Her eyes are a bright amber, and she wears minimal makeup. Her attire incorporates natural elements like feathers and leaves."
	# Add more female appearances as needed
]

# Background stories
background_stories = [
	"Grew up in a small village near the coast, spending days fishing and nights listening to tales of sea serpents.",
	"Was raised by a single parent after losing the other to a mysterious illness, fueling a desire to learn about healing.",
	"Joined a band of mercenaries at a young age, honing skills in combat and strategy.",
	"Trained under a renowned blacksmith, mastering the art of forging weapons.",
	"Lost their home to a raid, now seeking revenge against those responsible.",
	"Spent years traveling to distant lands, gathering knowledge and artifacts.",
	"Was chosen by the village elders to be the guardian of ancient runes.",
	"Has no memory of early childhood, carrying only a pendant as a clue to the past.",
	"Saved a noble's life, gaining favor but also unwanted attention.",
	"Witnessed a celestial event that was interpreted as a sign of great destiny.",
	"Left home to escape an arranged marriage, seeking freedom and adventure.",
	"Trained as a skald, preserving history through songs and stories.",
	"Was the sole survivor of a shipwreck, believing the gods spared them for a purpose.",
	"Discovered a hidden talent for magic, despite skepticism from peers.",
	"Dedicated life to hunting down a legendary beast that terrorizes the land.",
	"Served as a bodyguard for a powerful chieftain, learning the intricacies of politics.",
	"Spent time living among elves, adopting some of their ways and knowledge.",
	"Was cursed by a seer, and now seeks a way to break it.",
	"Accidentally unleashed a dark force and is now trying to atone.",
	"Trained in isolation in the mountains, emerging only when the homeland needed protection.",
	"Born under a rare comet, believed to have a special destiny.",
	"Worked as a navigator on long sea voyages, mapping uncharted territories.",
	"Descendant of a legendary hero, striving to live up to the name.",
	"Raised by wolves after being lost in the woods as a child.",
	"Apprenticed to a mysterious hermit who taught ancient secrets.",
	"Former member of a secretive order, left due to ideological differences.",
	"Disguised true identity to escape a dark past.",
	"Inherited a debt from family, now working to repay it.",
	"Found an ancient artifact that speaks in dreams.",
	"Fled from a collapsing kingdom, seeking a new start.",
	"Was a respected healer in the village before a tragic event.",
	"Lived among the dwarves, learning their crafting techniques.",
	"Escaped slavery and vowed to fight oppression.",
	"Was blessed (or cursed) by a trickster god.",
	"Trained as a hunter, protecting the village from wild beasts.",
	"Spent years searching for a sibling lost in war.",
	"Once part of a notorious pirate crew, now reformed.",
	"Guarded sacred groves, maintaining balance with nature.",
	"Embarked on a quest given by a dying mentor.",
	"Has visions of the future, often cryptic and unsettling.",
	"Dedicated to translating ancient texts, unlocking forgotten knowledge.",
	"Fought in a great war and carries the weight of those lost.",
	"Discovered a conspiracy within the royal court.",
	"Raised in a monastery, learning discipline and inner peace.",
	"Exiled from homeland due to false accusations.",
	"Believes to be the reincarnation of a legendary figure.",
	"Hunted by a powerful enemy for reasons unknown.",
	"Seeks to understand the meaning of a recurring dream.",
	"Wandered the land as a storyteller, collecting tales.",
	"Born during a fierce storm that lashed the coastal village, the child's arrival was seen as a sign from Thor himself. The village elders spoke of a destiny intertwined with the elements. Growing up among fishermen and warriors, the individual learned to read the sea and sky, becoming adept at navigating treacherous waters. One fateful day, a colossal sea serpent emerged from the depths, attacking the village fleet. Displaying remarkable courage, the young sailor led a daring defense, driving the beast away. This act of bravery set the individual on a path to explore distant lands, seeking knowledge about the mythical creatures of the deep and aiming to protect seafarers from similar threats.",

	"Raised in a secluded mountain hamlet, the individual was surrounded by towering peaks and ancient forests whispered to be inhabited by spirits. From an early age, a unique ability to communicate with animals became apparent, earning respect and awe from the community. When a neighboring clan encroached upon sacred lands, threatening to disrupt the balance of nature, the individual negotiated a peaceful resolution by mediating between the spirits and the intruders. This success sparked a journey to become a guardian of the wild, traveling across the Norse lands to preserve the harmony between humans and the natural world.",

	"Descended from a line of esteemed blacksmiths, the individual inherited a forge renowned for crafting weapons of legendary quality. One day, a mysterious traveler brought rare meteoric iron to the workshop, requesting the creation of a sword destined for a hero. Upon completing the weapon, the blacksmith discovered that it possessed magical properties, resonating with a strange energy. Realizing the responsibility that came with such power, the individual embarked on a quest to ensure the sword reached the rightful owner, facing challenges that tested both skill and moral compass.",

	"Growing up in a port city bustling with merchants from distant lands, the individual was fascinated by tales of far-off places and exotic goods. Apprenticing under a seasoned trader, the young merchant quickly mastered the art of negotiation and navigation. An encounter with a foreign mystic resulted in the acquisition of an enchanted compass that pointed toward one's deepest desire. Using this artifact, the merchant set sail to discover new trade routes and uncover the mysteries hinted at in old sagas, all while navigating the treacherous politics of rival trading guilds.",

	"Orphaned at a young age and raised by the village Volva—a wise seer—the individual was taught the ancient arts of divination and rune casting. A recurring vision of a great calamity prompted the seer to send the apprentice on a journey to gather sacred artifacts that could prevent the foretold disaster. Armed with knowledge and a deep connection to the spiritual realm, the individual set out to navigate the complexities of prophecy, encountering allies and adversaries influenced by the whims of the gods.",

	"Born into a clan of renowned warriors known for their berserker fury, the individual struggled with the uncontrollable rage that ran in the bloodline. Seeking a different path, a pilgrimage was undertaken to a distant temple dedicated to Balder, the god of light and purity. There, through meditation and discipline, the individual learned to channel inner turmoil into a source of strength without losing control. Returning home, a new philosophy was introduced to the clan, emphasizing balance and honor over sheer aggression, leading to a cultural shift that impacted the entire region.",

	"Hailing from a family of esteemed skalds, the individual possessed a natural talent for storytelling and music. During a journey to a royal court, an ancient manuscript was discovered in a hidden alcove of a dilapidated monastery. The text contained forgotten sagas and hymns that held clues to lost relics of the gods. Realizing the significance, a quest began to decode the manuscripts, recover the relics, and preserve the rich history of the Norse people before it faded into obscurity.",

	"Raised in a fishing village constantly threatened by raids, the individual witnessed the harsh realities of survival. Determined to bring about change, time was devoted to studying the art of shipbuilding and defense strategies. Innovating a new design, a fleet of agile and resilient ships was constructed, enabling the village to repel attackers effectively. This ingenuity caught the attention of a powerful Jarl, who requested assistance in fortifying other settlements, leading the individual into a role as a respected strategist and defender of the realm.",

	"Growing up near ancient ruins said to be remnants of the giants, the individual was captivated by the mysteries of the past. An insatiable curiosity led to the discovery of a hidden chamber containing relics and inscriptions. Deciphering the texts revealed a portal to Jotunheim, the land of giants. Faced with the ethical dilemma of exploring forbidden realms, a decision was made to embark on an expedition, aiming to learn from the giants and bridge understanding between worlds, all while avoiding the wrath of those who deemed such knowledge taboo.",

	"Born under the shadow of a volcano believed to be a gateway to Muspelheim, the realm of fire, the individual developed a fascination with elemental forces. After a volcanic eruption threatened nearby settlements, a journey began to understand and perhaps appease the fire giants rumored to dwell within. Along the way, mastery over fire was sought—not to wield destructively but to harness for protection and advancement, challenging the traditional fears and superstitions held by the Norse people.",

	"Living in a region where the boundary between Midgard and the Fae realms was thin, the individual often encountered creatures of folklore. One day, a pact was made with an elf who granted a charm allowing passage between worlds. Tasked with retrieving a stolen artifact critical to maintaining balance between realms, the individual navigated the complexities of both human and fae societies, striving to prevent a catastrophic rift that could unleash chaos upon both worlds.",

	"An apprentice to a renowned healer, the individual learned the secrets of herbs and the body. When a mysterious illness swept through the land, defying all known remedies, a quest was undertaken to find the mythical Well of Urd, whose waters were said to cure any ailment. Facing trials set by the Norns themselves, the individual had to confront personal weaknesses and make sacrifices, all to bring back a cure that could save countless lives.",

	"Growing up in a family of sailors, the individual was at home on the sea. During a routine voyage, the ship was attacked by pirates, and survival hinged on quick thinking and bravery. After commandeering the pirate ship, a decision was made to turn to privateering, targeting those who preyed on the innocent. This path led to a reputation as a folk hero among coastal communities and a thorn in the side of unscrupulous merchants and raiders.",

	"Living in the far north where nights can last for months, the individual developed a deep appreciation for the stars and celestial events. Discovering a comet that appeared to move against the known patterns, further study revealed it to be a harbinger of significant change. Sharing this knowledge with seers and leaders, the individual became a key advisor in preparing for the challenges foretold by the stars, blending astronomy with prophecy.",

	"From a young age, the individual showed an uncanny ability to forge bonds with animals, especially ravens. Interpreted as a blessing from Odin, this gift led to a role as a messenger and spy during times of conflict. Gathering intelligence with the help of avian allies, crucial information was relayed to leaders, altering the outcomes of battles and negotiations. This unique position required balancing loyalty, secrecy, and the burden of knowledge.",

	"Descended from a line of Jarl's, the individual was expected to lead but found greater passion in the quiet of the forests and the art of tracking. When a sacred artifact was stolen from the village by a rival clan, a solo mission was undertaken to retrieve it. Using skills in stealth and wilderness survival, the artifact was recovered, preventing war. This act redefined leadership in the eyes of the community, emphasizing wisdom and cunning over traditional displays of power.",

	"Growing up near a sacred grove dedicated to Freyja, the individual often participated in rituals celebrating love and fertility. When a prolonged drought threatened the region, the community looked to the gods for answers. Receiving visions during meditation, a pilgrimage was undertaken to seek out an ancient relic believed to restore balance. Along the journey, the individual faced trials that tested faith, compassion, and determination, ultimately leading to a deeper understanding of the interconnectedness of all things.",

	"An adept musician and poet, the individual traveled from village to village, sharing stories and songs. During one such journey, a chance encounter with a mysterious stranger led to the acquisition of a magical instrument capable of influencing emotions. Realizing the potential for both great good and harm, a commitment was made to use this gift to heal old wounds between feuding clans, promote unity, and preserve the rich cultural heritage of the Norse people.",

	"Working as an apprentice rune carver, the individual uncovered a set of ancient runes that did not match any known language. Obsessively studying them, it was discovered that they were keys to unlocking gates between realms. Recognizing the dangers of such power falling into the wrong hands, the individual set out to secure the runes, encountering others who sought them for their own purposes. This quest became a race against time to prevent potential catastrophe.",

	"Born in a border region frequently contested by warring clans, the individual witnessed the toll of endless conflict. Choosing a path of diplomacy, efforts were made to understand the roots of the disputes. Through courageous acts and unwavering commitment, ceasefires were brokered, and dialogues opened. This journey highlighted the challenges of peacekeeping in a culture that often glorified war, requiring the individual to navigate complex social and political landscapes.",

	"Growing up hearing whispers of dragons inhabiting distant mountains, the individual dreamed of seeing one. Gathering a small group of like-minded adventurers, an expedition was organized to seek out these mythical creatures. The journey was fraught with peril—treacherous terrain, harsh weather, and skepticism. Upon finally encountering a dragon, instead of engaging in battle, communication was established, leading to revelations about the ancient bonds between dragons and the Norse people.",

	"Living in a village known for its skilled archers, the individual excelled beyond all others. Invited to compete in a grand tournament hosted by a distant king, the archer faced competitors from across the realms. Amidst the competition, a plot to assassinate the king was uncovered. Using exceptional skills, the archer thwarted the attempt, earning favor and an appointment as a royal guard. This new role opened doors to influence and responsibilities previously unimagined.",

	"An artisan skilled in metalwork, the individual discovered a vein of unusual ore that shimmered with an inner light. Forging it into jewelry revealed that the items granted protective qualities to the wearer. When word spread, demand grew, attracting the attention of both noble patrons and jealous rivals. Balancing the desire to help others with the risks of greed and exploitation became a central challenge, prompting a journey to safeguard the source of the ore and its gifts.",

	"Raised among farmers, the individual led a simple life until a raiding party destroyed the village. Left with nothing, a vow was made to prevent others from suffering the same fate. Training in combat and survival, the individual became a protector of the vulnerable, establishing safe havens and teaching communities how to defend themselves. This path transformed a life of quiet anonymity into one of purpose and widespread respect.",

	"Fascinated by the legends of the World Tree, Yggdrasil, the individual sought to find a physical manifestation of it. After years of searching, a sacred grove was discovered where the veil between worlds was thin. Communing with spirits and gaining insights into the nature of existence, a commitment was made to protect this place from those who would exploit its power. This guardianship required constant vigilance and a willingness to confront both physical and spiritual threats.",

	"In a culture that valued physical strength, the individual stood out for exceptional intellect and ingenuity. Inventing devices and tactics that improved daily life and warfare, the individual often faced skepticism and resistance. A breakthrough came when a designed defense system saved a village from invasion. Recognition followed, but so did increased scrutiny. The journey then became about proving that innovation and tradition could coexist, enhancing the Norse way of life.",

	"Born during a rare celestial alignment, the individual was believed to have a special connection to the gods. This belief was reinforced by a natural aptitude for predicting weather and natural events. When signs pointed to a looming natural disaster, efforts were made to warn and prepare the communities. Facing disbelief and opposition, the individual had to find ways to convince others, demonstrating leadership and resolve in the face of impending calamity.",

	"Growing up among traders, the individual learned multiple languages and customs. During a voyage to distant lands, a fateful encounter with Eastern mystics introduced new philosophies and knowledge of arcane arts. Returning home, attempts to integrate these ideas met resistance. Committed to expanding horizons, the individual embarked on a mission to bridge cultures, fostering understanding and cooperation, and enriching the Norse world with new perspectives.",

	"An adept hunter, the individual was known for tracking elusive prey. One day, tracks of an unknown creature were found, leading deep into uncharted forests. The pursuit led to the discovery of a hidden enclave where ancient beings dwelled. Learning that these beings were guardians of nature threatened by encroaching settlements, a choice was made to become an intermediary, advocating for balance between human expansion and the preservation of the natural world.",

	"Inheriting a debt from a family member, the individual was compelled to serve a powerful and unscrupulous Jarl. Witnessing the suffering caused by the Jarl's actions, a plan was devised to undermine and expose the corruption. This involved gathering evidence, rallying support from oppressed villagers, and navigating dangerous political waters. The journey was fraught with personal risk but driven by a desire for justice and the well-being of the community.",

	"Possessing an innate talent for magic, the individual kept it hidden due to fear of persecution. When a neighboring village was cursed, causing crops to wither and livestock to perish, a decision was made to use these abilities to lift the affliction. Success brought both gratitude and suspicion, forcing the individual to confront societal fears about magic. This path led to becoming a mediator between the mystical and mundane worlds, striving to dispel ignorance and promote harmony.",

	"A skilled navigator, the individual was part of an expedition to map unknown territories. After being separated from the crew during a storm, an island was discovered that was not on any chart. The island held relics and ruins of a forgotten civilization with advanced knowledge. Realizing the potential impact on the world, the individual faced the dilemma of revealing the discovery or preserving the island's secrets to prevent exploitation.",

	"Growing up in a clan divided by internal strife, the individual sought to understand the root causes of the discord. Through patience and empathy, dialogues were facilitated between factions, uncovering misunderstandings and external manipulations. This effort not only healed the clan but also set an example for other groups facing similar challenges. The journey emphasized the power of communication and the importance of unity in the face of adversity.",

	"An orphan taken in by a group of traveling performers, the individual mastered various arts—music, acrobatics, illusion. While performing at a royal court, a conspiracy to overthrow the king was uncovered. Using performance skills to gather information and discreetly alert loyalists, the plot was thwarted. This experience propelled the individual into a life of covert operations, using talents to protect realms from hidden threats while maintaining the guise of an entertainer.",

	"Living near a glacier rumored to hold ancient spirits, the individual experienced vivid dreams that felt more like memories. Investigating the source, a hidden cavern was found containing artifacts from a bygone era. Touching one triggered a flood of ancestral memories, revealing a lineage connected to powerful elemental beings. Embracing this heritage, a mission began to harness these abilities responsibly, addressing environmental imbalances and guiding others toward respect for nature.",

	"A scholar dedicated to studying the Eddas and Sagas, the individual sought to separate myth from historical fact. During research, a code within the texts was discovered, pointing to locations of significant cultural artifacts. Embarking on an intellectual and physical quest, the individual aimed to recover these items to preserve cultural heritage. The journey involved deciphering complex puzzles and overcoming challenges that tested both mind and body.",

	"From a young age, the individual had an affinity for forging connections between disparate groups—warriors, artisans, farmers. Recognizing the strengths each brought, efforts were made to form a cooperative community that could withstand external threats and thrive internally. This initiative faced skepticism but gradually proved successful, setting a model for societal organization that balanced individual talents with collective well-being.",

	"While exploring coastal caves, the individual found an ancient ship preserved within—a vessel unlike any known design. Sensing its importance, restoration began in secret. Upon completion, it was discovered that the ship possessed magical properties, capable of traversing not just seas but realms. Faced with the enormity of this discovery, the individual had to decide whether to share this knowledge, how to use the ship, and the implications it held for understanding the world.",

	"An apprentice to a stern but wise elder, the individual learned the art of stone carving, creating runestones that told stories and preserved history. When the elder passed away, a hidden workshop was revealed, containing incomplete works and secrets. Taking up the mantle, the individual dedicated life to finishing these works, uncovering forgotten histories, and ensuring that the lessons and tales of the past would endure for future generations.",

	"In a dream, the individual was visited by a deity who bestowed a quest to retrieve a lost relic crucial for maintaining cosmic balance. Awakening with a tangible token from the dream—a feather, a gem, or a fragment of metal—the individual set out to fulfill this divine mandate. Along the way, encounters with skeptics, rivals, and allies shaped the journey, testing faith and commitment to a cause that few could comprehend.",

	"Possessing a unique ability to sense shifts in the fabric of reality, the individual noticed increasing disturbances that others could not perceive. Investigating these anomalies led to the discovery of rifts between worlds, through which entities were beginning to cross. Recognizing the threat, a mission was undertaken to seal these rifts, requiring knowledge of magic, negotiation with otherworldly beings, and the courage to face the unknown.",

	"Born into a family of renowned warriors, the individual felt out of place due to a contemplative nature and interest in philosophy. During a period of intense personal reflection, a pilgrimage was undertaken to sacred sites, seeking meaning and purpose. Along the way, wisdom was gained from various mentors—seers, hermits, sages—culminating in a personal enlightenment. Returning home, a new path was forged that combined martial prowess with spiritual insight, influencing others to seek balance in their lives."
	# Add more background stories as needed
]

# Spellcasting classes with their spells and cantrips
# (Add this to your data definitions)

spellcasting_classes = {
	"Cleric": {
    	"spells": ["Cure Wounds", "Bless", "Shield of Faith", "Guiding Bolt", "Spiritual Weapon", "Lesser Restoration", "Prayer of Healing", "Silence", "Hold Person", "Spiritual Guardians"],
    	"cantrips": ["Sacred Flame", "Thaumaturgy", "Guidance", "Light", "Resistance"],
	},
	"Druid": {
    	"spells": ["Entangle", "Faerie Fire", "Goodberry", "Healing Word", "Thunderwave", "Moonbeam", "Flaming Sphere", "Barkskin", "Spike Growth", "Heat Metal"],
    	"cantrips": ["Druidcraft", "Produce Flame", "Shillelagh", "Thorn Whip", "Guidance"],
	},
	"Sorcerer": {
    	"spells": ["Magic Missile", "Shield", "Burning Hands", "Mage Armor", "Sleep", "Scorching Ray", "Invisibility", "Mirror Image", "Web", "Detect Thoughts"],
    	"cantrips": ["Fire Bolt", "Prestidigitation", "Ray of Frost", "Mage Hand", "Light"],
	},
	"Wizard": {
    	"spells": ["Detect Magic", "Identify", "Magic Missile", "Shield", "Burning Hands", "Charm Person", "Find Familiar", "Feather Fall", "Magic Weapon", "Levitate"],
    	"cantrips": ["Fire Bolt", "Mage Hand", "Light", "Prestidigitation", "Ray of Frost"],
	},
	"Warlock": {
    	"spells": ["Armor of Agathys", "Arms of Hadar", "Hex", "Hellish Rebuke", "Witch Bolt", "Darkness", "Invisibility", "Mirror Image", "Misty Step", "Shatter"],
    	"cantrips": ["Eldritch Blast", "Mage Hand", "Chill Touch", "Minor Illusion", "Prestidigitation"],
	},
	"Bard": {
    	"spells": ["Charm Person", "Healing Word", "Thunderwave", "Sleep", "Detect Magic", "Hold Person", "Silence", "Enhance Ability", "Heat Metal", "Shatter"],
    	"cantrips": ["Vicious Mockery", "Mage Hand", "Minor Illusion", "Prestidigitation", "Message"],
	},
	# Add other spellcasting classes and their spells/cantrips
}

# Personality descriptions
personality_descriptions = [
	"A natural leader who inspires others through courage and determination.",
	"A quiet observer who speaks only when necessary but offers profound insights.",
	"Hot-tempered and quick to action, often leaping before looking.",
	"A jovial soul who enjoys the company of others and the pleasures of life.",
	"Deeply spiritual, often contemplating the will of the gods and fate.",
	"Skeptical of strangers, but fiercely loyal to those who earn trust.",
	"Calculating and strategic, always planning several steps ahead.",
	"Driven by a thirst for knowledge, constantly seeking new information.",
	"Haunted by past mistakes, seeking redemption through noble deeds.",
	"An idealist who believes in the inherent good of people and strives for justice.",
	"Pragmatic and resourceful, making the best out of any situation.",
	"An adventurer at heart, always looking for the next thrill.",
	"Cynical and sarcastic, often using humor to mask deeper emotions.",
	"Gentle and compassionate, with a strong desire to help others.",
	"Bold and confident, sometimes bordering on arrogance.",
	"Prefers solitude, finding peace in nature and quiet places.",
	"Highly superstitious, seeing signs and omens in everyday occurrences.",
	"Mysterious and enigmatic, revealing little about personal thoughts.",
	"Ambitious and driven, always striving to improve and achieve more.",
	"A pacifist at heart, preferring diplomacy over conflict.",
	"Cheerful and optimistic, lifting the spirits of those around them.",
	"Intensely focused, sometimes to the point of obsession.",
	"Witty and clever, enjoys engaging in verbal sparring.",
	"Deeply empathetic, feeling the pain of others as their own.",
	"Stoic and reserved, rarely showing emotions openly.",
	"Reckless and daring, thrives in dangerous situations.",
	"Patient and methodical, believing slow and steady wins the race.",
	"Self-doubting, often questioning own abilities despite evidence of success.",
	"Innovative thinker, always looking for new solutions to problems.",
	"Traditionalist, holding firmly to the ways of ancestors.",
	"Charismatic and charming, easily winning people over.",
	"Brooding and intense, with a hidden past.",
	"Joyful and free-spirited, dislikes being tied down.",
	"Detail-oriented, noticing things others often miss.",
	"Easily bored, constantly seeking new challenges.",
	"Noble and honorable, adhering to a strict moral code.",
	"Secretive, keeping personal matters closely guarded.",
	"Vengeful, never forgetting a slight or wrongdoing.",
	"Enigmatic, with motives that are difficult to discern.",
	"Protective of loved ones, willing to do anything for them.",
	"Unpredictable, keeping others guessing about next moves.",
	"Analytical, approaching situations with logic and reason.",
	"Dreamer, often lost in thoughts and imagination.",
	"Gruff exterior hides a kind and caring heart.",
	"Loyal to a fault, sometimes to own detriment.",
	"Strong sense of duty, prioritizing obligations above all else.",
	"Peaceful and contemplative, avoiding conflict when possible.",
	"Obsessed with a personal quest, driving every action.",
	"Resentful of authority, preferring to forge own path.",
	"Fearless in the face of danger, sometimes recklessly so.",
	"Generous, sharing wealth and resources freely.",
	# Add more personality descriptions as needed
]

def roll_dice():
	"""Simulate rolling four 6-sided dice and summing the top three."""
	rolls = [random.randint(1, 6) for _ in range(4)]
	return sum(sorted(rolls)[1:])

def generate_ability_scores():
	"""Generate ability scores using the standard rolling method."""
	return {stat: roll_dice() for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]}

def generate_name(gender):
	"""Generate a random name by combining prefixes and suffixes based on gender."""
	if gender == "Male":
    	first_name = random.choice(male_name_prefixes) + random.choice(male_name_suffixes)
	elif gender == "Female":
    	first_name = random.choice(female_name_prefixes) + random.choice(female_name_suffixes)
	else:  # Random
    	gender = random.choice(["Male", "Female"])
    	return generate_name(gender)
	nickname = random.choice(nicknames)
	return f"{first_name} '{nickname}'", gender

def generate_character(selected_race, selected_level, selected_gender, min_age=None, max_age=None):
	"""Generate a character dictionary with all necessary fields."""
	character = {}
	character["Name"], character["Gender"] = generate_name(selected_gender)
	character["Level"] = selected_level

	# Adjusted race selection
	if selected_race == "Random":
    	if random.random() < 0.9:
        	character_race = "Human"
    	else:
        	other_races = [race for race in norse_races if race != "Human"]
        	character_race = random.choice(other_races)
	else:
    	character_race = selected_race
	character["Race"] = character_race

	# Generate Age based on race or user-provided range
	if min_age is not None and max_age is not None:
    	character["Age"] = random.randint(min_age, max_age)
	else:
    	if character["Race"] in age_ranges:
        	min_age_default, max_age_default = age_ranges[character["Race"]]
        	character["Age"] = random.randint(min_age_default, max_age_default)
    	else:
        	# Default age range if race not found
        	character["Age"] = random.randint(15, 80)

	# ... rest of your code remains unchanged ...

	character["Class"] = random.choice(classes)

	# Assign spells and cantrips if the class is a spellcaster
	selected_class = character["Class"]

	if selected_class in spellcasting_classes:
    	# Determine number of spells and cantrips based on level
    	num_spells = min(len(spellcasting_classes[selected_class]["spells"]), character["Level"] + 1)
    	num_cantrips = min(len(spellcasting_classes[selected_class]["cantrips"]), 2 + character["Level"] // 4)

    	# Randomly select spells and cantrips
    	character["Spells"] = random.sample(spellcasting_classes[selected_class]["spells"], num_spells)
    	character["Cantrips"] = random.sample(spellcasting_classes[selected_class]["cantrips"], num_cantrips)
	else:
    	character["Spells"] = []
    	character["Cantrips"] = []

	character["Background"] = random.choice(backgrounds)
	character["Alignment"] = random.choice(alignments)
	character["Ability Scores"] = generate_ability_scores()

	# Calculate hit dice and hit points
	if selected_class in hit_dice_dict:
    	hit_die = hit_dice_dict[selected_class]
	else:
    	hit_die = 8  # Default hit die if class not found

	character["Hit Die"] = f"d{hit_die}"

	# Calculate total hit points
	con_modifier = (character["Ability Scores"]["CON"] - 10) // 2
	# First level full hit die plus CON modifier
	total_hp = hit_die + con_modifier

	# For subsequent levels, add average hit die roll plus CON modifier
	for level in range(2, character["Level"] + 1):
    	average_hp = (hit_die // 2) + 1  # Average roll for hit die
    	total_hp += average_hp + con_modifier

	character["Hit Points"] = total_hp
	character["Skills"] = random.sample(skills, 4)
	character["Proficiencies"] = ["Common", "Norse"]
	character["Equipment"] = random.sample(equipment, 5)
	character["Personality Traits"] = random.sample(personality_traits, 3)
	character["Ideals"] = random.choice(ideals)
	character["Bonds"] = random.choice(bonds)
	character["Flaws"] = random.choice(flaws)
	character["Features"] = ["Feature: " + random.choice(traits)]
	character["Traits"] = random.choice(traits)
	if character["Gender"] == "Male":
    	character["Appearance"] = random.choice(male_appearance_descriptions)
	else:
    	character["Appearance"] = random.choice(female_appearance_descriptions)
	character["Background Story"] = random.choice(background_stories)
	character["Personality Description"] = random.choice(personality_descriptions)
	return character

def display_character(character):
	"""Format the character dictionary into a string."""
	output = ""
	output += f"Name: {character['Name']}\n"
	output += f"Gender: {character['Gender']}\n"
	output += f"Race: {character['Race']}\n"
	output += f"Class: {character['Class']} (Level {character['Level']})\n"
	output += f"Background: {character['Background']}\n"
	output += f"Alignment: {character['Alignment']}\n\n"
	output += f"Age: {character['Age']}\n"
	output += f"Hit Die: {character['Hit Die']}\n"
	output += f"Hit Points: {character['Hit Points']}\n\n"
	output += "Ability Scores:\n"
	for stat, score in character["Ability Scores"].items():
    	output += f"  {stat}: {score}\n"
	output += "\nSkills: " + ", ".join(character["Skills"]) + "\n"
	output += "Proficiencies: " + ", ".join(character["Proficiencies"]) + "\n"
	output += "Equipment: " + ", ".join(character["Equipment"]) + "\n\n"
	# Display Spells and Cantrips if the character has any
	if character["Spells"]:
    	output += "Spells:\n"
    	for spell in character["Spells"]:
        	output += f"  - {spell}\n"
    	output += "\n"

	if character["Cantrips"]:
    	output += "Cantrips:\n"
    	for cantrip in character["Cantrips"]:
        	output += f"  - {cantrip}\n"
    	output += "\n"

	output += "Personality Traits:\n"
	for trait in character["Personality Traits"]:
    	output += f"  - {trait}\n"
	output += f"Ideals:\n  - {character['Ideals']}\n"
	output += f"Bonds:\n  - {character['Bonds']}\n"
	output += f"Flaws:\n  - {character['Flaws']}\n"
	output += "\nAppearance Description:\n  " + character["Appearance"] + "\n"
	output += "\nBackground Story:\n  " + character["Background Story"] + "\n"
	output += "\nPersonality Description:\n  " + character["Personality Description"] + "\n"
	output += "\nFeatures:\n  " + "\n  ".join(character["Features"]) + "\n"
	output += f"Additional Traits:\n  - {character['Traits']}\n"
	return output

# ... rest of your code ...

def generate_button_clicked():
	selected_race = race_var.get()
	selected_level = level_var.get()
	selected_gender = gender_var.get()
	if selected_gender == "Random":
    	selected_gender = random.choice(["Male", "Female"])

	# Get min_age and max_age from the GUI entries
	min_age_input = min_age_var.get()
	max_age_input = max_age_var.get()

	# Initialize min_age and max_age as None
	min_age = None
	max_age = None

	# Validate level
	try:
    	level = int(selected_level)
    	if level < 1 or level > 20:
        	raise ValueError
	except ValueError:
    	output_text.delete(1.0, tk.END)
    	output_text.insert(tk.END, "Please enter a valid level between 1 and 20.")
    	return

	# Validate min_age and max_age if provided
	try:
    	if min_age_input and max_age_input:
        	min_age = int(min_age_input)
        	max_age = int(max_age_input)
        	if min_age > max_age:
            	raise ValueError("Minimum age cannot be greater than maximum age.")
    	elif min_age_input or max_age_input:
        	raise ValueError("Please enter both minimum and maximum age, or leave both blank.")
	except ValueError as e:
    	output_text.delete(1.0, tk.END)
    	output_text.insert(tk.END, "Please enter valid age ranges.\n" + str(e))
    	return

	# Generate character
	character = generate_character(selected_race, level, selected_gender, min_age, max_age)
	character_sheet = display_character(character)
	output_text.delete(1.0, tk.END)
	output_text.insert(tk.END, character_sheet)

def copy_to_clipboard():
	root.clipboard_clear()
	root.clipboard_append(output_text.get(1.0, tk.END))

# Setup the main window
root = tk.Tk()
root.title("Norse-Themed D&D Character Generator")

# Race selection
race_label = ttk.Label(root, text="Select Race:")
race_label.pack(pady=5)

race_var = tk.StringVar()
race_dropdown = ttk.Combobox(root, textvariable=race_var, values=race_options, state="readonly")
race_dropdown.current(0)  # Default to "Random"
race_dropdown.pack(pady=5)

# Level selection
level_label = ttk.Label(root, text="Select Level (1-20):")
level_label.pack(pady=5)

level_var = tk.StringVar(value='1')
level_entry = ttk.Entry(root, textvariable=level_var)
level_entry.pack(pady=5)

# Gender selection
gender_label = ttk.Label(root, text="Select Gender:")
gender_label.pack(pady=5)

gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=genders, state="readonly")
gender_dropdown.current(2)  # Default to "Random"
gender_dropdown.pack(pady=5)

# Age range selection
age_range_label = ttk.Label(root, text="Enter Age Range (Optional):")
age_range_label.pack(pady=5)

# Frame to hold min_age and max_age entries side by side
age_frame = ttk.Frame(root)
age_frame.pack(pady=5)

min_age_var = tk.StringVar()
min_age_entry = ttk.Entry(age_frame, textvariable=min_age_var, width=10)
min_age_entry.pack(side=tk.LEFT, padx=5)
min_age_entry.insert(0, "")  # Default empty

to_label = ttk.Label(age_frame, text="to")
to_label.pack(side=tk.LEFT)

max_age_var = tk.StringVar()
max_age_entry = ttk.Entry(age_frame, textvariable=max_age_var, width=10)
max_age_entry.pack(side=tk.LEFT, padx=5)
max_age_entry.insert(0, "")  # Default empty

# Generate button
generate_button = ttk.Button(root, text="Generate Character", command=generate_button_clicked)
generate_button.pack(pady=10)

# Copy to clipboard button
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Output text area
output_text = tk.Text(root, width=80, height=40)
output_text.pack(pady=5)

# Start the GUI event loop
root.mainloop()
