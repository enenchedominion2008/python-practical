print("====== Welcome to A Lost Island!\n The shorelines are vast, the secrets are deep, and your survival story starts right now.\n Whether you are here to map out uncharted territories, uncover ancient mysteries,\n or simply survive the night, a grand adventure awaits you.\n Keep your wits sharp, explorer—the island is watching! ========")
name = input("YOUR NAME: ")
print(f"<<<< welcome {name.capitalize()} \n your adventure begins >>>>")
energy = 5
location = "Beach"
inventory = []
while True:
    print(f"current location {location} current energy {energy}")
    print("(1) look around")
    print("(2) move")
    print("(3) quit")
    options = input("choose >> ")
    if options == "3" :
        print('GAME OVER')
        break
