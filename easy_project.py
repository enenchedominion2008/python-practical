connections = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

print("====== Welcome to A Lost Island!\n The shorelines are vast, the secrets are deep, and your survival story starts right now.\n Whether you are here to map out uncharted territories, uncover ancient mysteries,\n or simply survive the night, a grand adventure awaits you.\n Keep your wits sharp, explorer—the island is watching! ========")
name = input("YOUR NAME: ")
print(f"<<<< welcome {name.capitalize()} \n your adventure begins >>>>")
limit = 5
location = "Beach"
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
    if option == "3" :
        print('GAME OVER')
        break
    elif option == "1" :
        print(f"current location === {location} ===")
        print("Waves crash softly against the shore as gulls cry overhead.")
        print("A rusted lantern lies half-buried in the sand, its glass still intact.")
        print(">>> HINT: That lantern might be useful later. <<<")
    elif option == "2" :
       print(f"""where do you want to go to"
       (1) Jungle
       (2) Cave
       (3) Old Bridge
       (4)Lighthouse
       (5) Beach""")
       location = input("choose where you want to go to: ")
        print("not among the options please choose the correct option")
        continue
       destinations = connections[location]
       print(destinations)
    else :
        print("== you are puting the wrong input pls select the correct option")