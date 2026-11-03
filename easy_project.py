print("====== Welcome to A Lost Island!\n The shorelines are vast, the secrets are deep, and your survival story starts right now.\n Whether you are here to map out uncharted territories, uncover ancient mysteries,\n or simply survive the night, a grand adventure awaits you.\n Keep your wits sharp, explorer—the island is watching! ========")
name = input("YOUR NAME: ")
print(f"<<<< welcome {name.capitalize()} \n your adventure begins >>>>")
energy = 5
location = "Beach"
inventory = []
print("current player status")
print(f"-------- enegry >> {energy} ----------")
print(f"------- current location >> {location} --------")
print(f"--------inventory >> {len(inventory)} ---------")
while True:
    print(f"current location {location} current energy {energy}")
    print("(1) look around")
    print("(2) move")
    print("(3) quit")
    options = input("choose >> ")
    if options.strip() == "3" :
        print('GAME OVER')
        break
    if options  not in ("1","2","3") :
        energy -= 1
        if energy < 1 :
            print("you are out of energy")
            print("GAME OVER")
            break
        print("you typed an invalid input and your energy has been cosumed choose the correct option")
        print(f"current enegry >> {energy}")
    if options.strip() == "1" :
        print(f"current location === {location} ===")
        print(f"a beautiful beach\n with birds flying over the waters moving with the waves\n accompanied by a soft breeze")
