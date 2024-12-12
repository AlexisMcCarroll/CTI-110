import random

# Function to create a character by asking for details
def create_character():
    # Gather the character's details from the player
    name = input("Enter the character's name: ")
    health = int(input(f"Enter {name}'s health: "))
    strength = int(input(f"Enter {name}'s strength: "))
    inventory = ["Health Potion", "Elixir"]  # Set initial items
    weapon = ["Power Axe"]  # Set initial weapon
    magic = input("Enter the character's magical powers: ")

    # Create a dictionary to store the character's details
    character = {
        "Name": name,
        "Health": health,
        "Strength": strength,
        "Items": inventory,
        "Weapons": weapon,
        "Powers": magic,
    }
    return character

# Function to display character stats
def show_stats(character):
    print(f"\nStats for {character['Name']}:")
    print("🐱‍🏍🎈⚔")
    print(f"Health: {character['Health']}")
    print(f"Strength: {character['Strength']}")
    print(f"Items: {character['Items']}")
    print(f"Weapons: {character['Weapons']}")
    print(f"Powers: {character['Powers']}\n")

# Function to create a villain with random attributes
def create_villain():
    name = "Johnny the Menace"
    health = random.randint(50, 100)  # Random health between 50 and 100
    strength = random.randint(10, 20)  # Random strength between 10 and 20
    inventory = ["Small Health Potion"]  # Villain's item
    weapon = ["Power Axe"]  # Villain's weapon
    magic = "fireball"  # Villain's magic power

    # Create a dictionary to store the villain's details
    character = {
        "Name": name,
        "Health": health,
        "Strength": strength,
        "Items": inventory,
        "Weapons": weapon,
        "Powers": magic,
    }
    return character

# Function to simulate an attack
def attack(attacker, victim):
    damage = random.randint(1, attacker["Strength"])  # Random damage based on attacker's strength
    victim["Health"] -= damage  # Decrease the victim's health
    print(f'{attacker["Name"]} attacks {victim["Name"]} for {damage} damage!')
    print(f'{victim["Name"]} now has {victim["Health"]} health.\n')

def use_ability(attacker, victim):
    if attacker["Powers"] == "fireball":
        damage = random.randint(20, 40)
        victim["Health"] -= damage
        print(f'{attacker["Name"]} uses Fireball and deals {damage} damage to {victim["Name"]}!')
    elif attacker["Powers"] == "shield":
        attacker["Shielded"] = True
        print(f'{attacker["Name"]} uses Shield and will take reduced damage next turn!')
    elif attacker["Powers"] == "heal":
        heal_amount = random.randint(15, 30)
        attacker["Health"] += heal_amount
        print(f'{attacker["Name"]} uses Heal and recovers {heal_amount} health!')
    print()
    
# Function to heal a character using an item
def heal(character, item):
    if item == "Health Potion":
        heal_amount = random.randint(15, 30)  # Random healing for Health Potion
        character["Health"] += heal_amount
        character["Items"].remove(item)  # Remove the item from inventory
        print(f'{character["Name"]} uses a Health Potion and heals for {heal_amount} health!')
    elif item == "Elixir":
        heal_amount = random.randint(20, 40)  # Random healing for Elixir
        character["Health"] += heal_amount
        character["Items"].remove(item)  # Remove the item from inventory
        print(f'{character["Name"]} uses an Elixir and heals for {heal_amount} health!')
    elif item == "Small Health Potion":
        heal_amount = random.randint(5, 15)  # Random healing for Small Health Potion
        character["Health"] += heal_amount
        character["Items"].remove(item)  # Remove the item from inventory
        print(f'{character["Name"]} uses a Small Health Potion and heals for {heal_amount} health!')
    print(f'{character["Name"]} now has {character["Health"]} health.\n')

# Function to let the player choose an item to use from their inventory
def use_item(character):
    if character["Items"]:
        print(f"\n{character['Name']}'s Inventory: {character['Items']}")
        item = input("Select an item to use: ").strip()  # Allow the player to choose an item
        if item in character["Items"]:
            heal(character, item)  # Heal the character using the selected item
        else:
            print("Invalid item. No item used.\n")
    else:
        print("No items available in inventory.\n")

# Function to handle the battle between the player's character and the villain
def battle(char1, johnny):
    print("\nThe battle starts now!")
    while char1["Health"] > 0 and johnny["Health"] > 0:
        # Player's Turn
        print("\n--- Your Turn ---")
        action = input("Would you like to 'attack', 'use item', or 'use special powers'? ").strip().lower()

        if action == "use item":
            use_item(char1)  # Player uses an item
        elif action == "attack":
            attack(char1, johnny)  # Player attacks the villain
        elif action == "use special powers":
            use_ability(char1, johnny)  # Player uses special powers
        else:
            print("Invalid action. Skipping turn...\n")
            continue  # Skip the turn if the input is invalid

        # Check if the villain is defeated
        if johnny["Health"] <= 0:
            print(f'{johnny["Name"]} is defeated! {char1["Name"]} wins!\n')
            break

        # Villain's Turn
        print("\n--- Enemy's Turn ---")
        if johnny["Health"] <= 30 and "Small Health Potion" in johnny["Items"]:
            heal(johnny, "Small Health Potion")  # Villain heals if health is low
        else:
            # Villain chooses an action
            action = random.choice(["attack", "use ability"])
            if action == "attack":
                attack(johnny, char1)  # Villain attacks
            else:
                use_ability(johnny, char1)  # Villain uses special powers

        # Check if the player is defeated
        if char1["Health"] <= 0:
            print(f'{char1["Name"]} is defeated! {johnny["Name"]} wins!\n')
            break

# Main function to start the game
def main():
    print("The game is about to begin...\n")
    char1 = create_character()  # Create the player's character
    show_stats(char1)  # Display character stats
    
    johnny = create_villain()  # Create the villain
    show_stats(johnny)  # Display villain stats
    
    battle(char1, johnny)  #Start the battle between the player's character and the villain

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
