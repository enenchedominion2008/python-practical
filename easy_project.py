connections = {
    "beach": ["jungle"],
    "jungle": ["beach", "cave"],
    "cave": ["jungle", "old bridge"],
    "old bridge": ["cave", "lighthouse"],
    "lighthouse": ["old bridge"]
}

print("====== Welcome to A Lost Island!\n The shorelines are vast, the secrets are deep, and your survival story starts right now.\n Whether you are here to map out uncharted territories, uncover ancient mysteries,\n or simply survive the night, a grand adventure awaits you.\n Keep your wits sharp, explorer—the island is watching! ========")
name = input("YOUR NAME: ")
print(f"<<<< welcome {name.capitalize()} \n your adventure begins >>>>")

limit = 5
location = "beach"
inventory = []

print("current player status")
print(f"--------inventory >> {len(inventory)} ---------")

while True:
    print(f"""
current location <<<{location}>>>
 current energy ==={limit}===
(1) look around
(2) move
(3) quit
""")
    options = input("choose >> ")
    option = options.strip()

    if option == "3":
        print('GAME OVER')
        break

    elif option == "1":
        print(f"current location === {location} ===")
        if location == "beach":
            print("Waves crash softly against the shore as gulls cry overhead.")
            print("A rusted lantern lies half-buried in the sand, its glass still intact.")
            if "lantern" not in inventory:
                inventory.append("lantern")
                print(">>> You picked up the lantern. <<<")
            else:
                print(">>> You already have the lantern. <<<")
        elif location == "jungle":
            print("Vines hang thick between the trees.")
            if "rope" not in inventory:
                inventory.append("rope")
                print(">>> You found a coil of rope! <<<")
            else:
                print(">>> You already have the rope. <<<")
        elif location == "cave":
            print("Damp stone. The old bridge creaks to the north.")
        elif location == "old bridge":
            print("Rope planks sway. The lighthouse looms ahead.")
        elif location == "lighthouse":
            print("A dark beacon waits for a flame. Type 4 to light it.")
        print(f">>> inventory now: {inventory} <<<")

    elif option == "2":
        destinations = connections[location]

        print("Available destinations:")
        number = 1
        for place in destinations:
            print(number, place)
            number += 1

        choice = input("Choose your number >> ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(destinations):
            selected = destinations[int(choice) - 1]

            # Special rule: cannot go to lighthouse without rope
            if selected == "lighthouse" and "rope" not in inventory:
                print("The old bridge is broken — you need rope to cross. (No energy lost.)")
            else:
                location = selected
                limit -= 1
                print(f"You travel to {location}. Energy: {limit}")

                if limit <= 0:
                    print("You collapse from exhaustion. GAME OVER.")
                    break
        else:
            print("Invalid destination — you stay put (no energy lost).")

    elif option == "4":
        if location == "lighthouse" and "lantern" in inventory:
            print(f" {name.capitalize()} lights the beacon! The rescue boat sees you. YOU WIN!")
            break
        elif location == "lighthouse":
            print("You have no lantern — you cannot light the beacon.")
        else:
            print("There is no beacon here to light.")