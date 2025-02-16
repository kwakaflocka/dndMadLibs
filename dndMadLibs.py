import random
import re

races = ["Human", "Elf", "Dwarf", "Orc", "Halfling", "Tiefling", "Gnome", "Dragonborn"]
classes = ["Fighter", "Wizard", "Rogue", "Cleric", "Bard", "Ranger", "Paladin", "Sorcerer"]
personalities = [
    "Brave and fearless", "Cunning and sly", "Honorable and just", "Reckless and impulsive",
    "Loyal but stubborn", "Kind-hearted but naive", "Calculating and ambitious", "Sarcastic and witty"
]
weapons = ["Longsword", "Dagger", "Battleaxe", "Shortbow", "Magic Staff", "Crossbow", "Spear", "Warhammer"]
starting_equipment = ["Traveler's Pack", "Rope & Grappling Hook", "Potion of Healing", "Lantern & Oil", "Lockpicks"]

background_templates = [
    "I grew up in a {place} where I {occupationVerb} as a {occupationNoun}. One day, my life changed forever when {lifeChangingEvent}.",
    "I was raised by {guardianWhoRaisedYou} who taught me {skill}. However, I left home when {tragicEvent}.",
    "Once, I was a {job}, but {tragedy} forced me to start a new life as an adventurer.",
    "I wandered the {landscape} alone until I met {mentor}, who trained me in {training}.",
    "My family was known for {legacy}, but I chose to follow my own path after {lifeChangingEvent}."
]

def madlibs_background():
    """Generates a Mad Libs-style background by asking the user for inputs."""
    template = random.choice(background_templates)
    
    # Use regular expressions to find placeholders (words between {})
    blanks = re.findall(r'\{([^}]+)\}', template)
    
    filled_values = {}
    print("\nLet's create your backstory! Fill in the blanks:")

    # Fill in blanks by asking the user for input. If input is empty, use a default value.
    for blank in blanks:
        value = input(f"Enter a {blank}: ").strip()
        filled_values[blank] = value if value else f"mysterious {blank}"

    # Replace placeholders in the template with the filled values
    for blank, value in filled_values.items():
        template = template.replace(f"{{{blank}}}", value)

    return template

def freestyle_background():
    """Allows the user to describe their background freely."""
    print("\nDescribe your background:")
    return input("> ").strip() or "A mysterious past filled with adventure and secrets."

def choose_option(prompt, options):
    """Prompts the user to choose an option or select 'random'."""
    while True:
        print(f"\n{prompt}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("0. Random")

        choice = input("Enter a number: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice <= len(options):
                return random.choice(options) if choice == 0 else options[choice - 1]
        
        print("Invalid choice, please enter a valid number.")

def choose_or_describe(prompt, options):
    """Allows the user to describe their own option or pick a random one."""
    print(f"\n{prompt}")
    print("Type your own description OR enter 'random' to get a random one.")

    user_input = input("> ").strip()
    return random.choice(options) if user_input.lower() == "random" else user_input

def generate_character():
    """Generates a full D&D character with user-selected or random attributes."""
    name = input("\nEnter your character's name: ").strip()
    while not name:
        print("Character name cannot be empty!")
        name = input("Enter your character's name: ").strip()

    race = choose_option("Choose your race:", races)
    char_class = choose_option("Choose your class:", classes)
    personality = choose_or_describe("Describe your personality or type 'random':", personalities)
    background_style = input("\nChoose your background style (random, freestyle, madlibs): ").strip().lower()

    if background_style == 'madlibs':
        background = madlibs_background()
    elif background_style == 'freestyle':
        background = freestyle_background()
    else:
        background = "I grew up in a quiet village, but my destiny called me to adventure."

    # Generate random weapon and starting equipment
    weapon = random.choice(weapons)
    equipment = random.choice(starting_equipment)

    # Character data
    character = {
        "Name": name,
        "Race": race,
        "Class": char_class,
        "Personality": personality,
        "Weapon": weapon,
        "Starting Equipment": equipment,
    }

    # Print the character details
    print("\n--- Your Character ---")
    for key, value in character.items():
        if isinstance(value, dict):
            print(f"{key}: {', '.join([f'{k}: {v}' for k, v in value.items()])}")
        else:
            print(f"{key}: {value}")

    # Print the background followed by the character summary
    print(f"\nBackground: I was born as a {character['Race']}.  {background} Now, I am a {character['Class']} and go by {character['Name']}. I am known for being {character['Personality']}.")

    return character

if __name__ == "__main__":
    print("D&D Character Generator\n")
    while True:
        char = generate_character()

        if input("\nGenerate another character? (y/n): ").strip().lower() != "y":
            break
