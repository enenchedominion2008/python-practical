shoping_list = []
while True :
    listing = input("input your what you want to buy : ")

    if listing == "done":
        break
    shoping_list.append(listing)
    print(f"here is your order {shoping_list}")
