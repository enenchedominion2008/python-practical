shoping_list = []
while True :
    listing = input("input what you want to buy : ")

    if listing == "done":
        break
    shoping_list.append(listing)
    if len(shoping_list) > 10 :
        print("you have reach your maximum amount try again later")
        break
    print(f"here  you ordered {len(shoping_list)} items  {shoping_list} ")