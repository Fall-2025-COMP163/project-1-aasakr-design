"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Abdelrahman Sakr
Date: October 28, 2025

AI Usage: [Document any AI assistance used]
Ai helped with debugging and optimizing the code structure."""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    """
    level = 1
    gold = 100

    # Get starting stats
    strength, magic, health = calculate_stats(character_class, level)

    # Build character as dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


def calculate_stats(character_class, level):
    """
    Calculates stats based on class and level.
    Uses simple formulas and basic math.
    """
    # Start with default values
    strength = 5
    magic = 5
    health = 100

    if character_class == "Warrior":
        strength = 10 + level * 2
        magic = 3 + level
        health = 120 + level * 5
    elif character_class == "Mage":
        strength = 3 + level
        magic = 12 + level * 3
        health = 80 + level * 4
    elif character_class == "Rogue":
        strength = 7 + level * 2
        magic = 7 + level * 2
        health = 90 + level * 3
    elif character_class == "Cleric":
        strength = 6 + level * 2
        magic = 10 + level * 2
        health = 110 + level * 4

    return strength, magic, health

def save_character(character, filename):
    """
    Saves character info to a text file
    """
    file = open(filename, "w")

    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")

    file.close()

def load_character(filename):
    """
    Loads character info from a file and returns a dictionary
    """
    character = {}

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            key = parts[0]
            value = parts[1]

            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)

    return character


def display_character(character):
    """
    Prints out the character info neatly
    """
    print("=== CHARACTER SHEET ===")
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Strength:", character["strength"])
    print("Magic:", character["magic"])
    print("Health:", character["health"])
    print("Gold:", character["gold"])

def level_up(character):
    """
    Increases character level by 1 and updates stats
    """
    character["level"] = character["level"] + 1

    # Recalculate stats using the same function
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

# Main program for testing
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    name = input("Enter character name: ")
    char_class = input("Enter class (Warrior, Mage, Rogue, Cleric): ")

    # Create and show the character
    char = create_character(name, char_class)
    display_character(char)

    # Save character
    filename = name.lower() + "_save.txt"
    save_character(char, filename)
    print("Character saved as", filename)
