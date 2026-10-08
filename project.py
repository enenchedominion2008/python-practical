resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3},
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []


def find_resource(rid):
    """Return the resource dictionary with this ID, or None."""
    for r in resources:
        if r["id"] == rid:
            return r
    return None


def get_positive_int(prompt):
    """Keep asking until the user enters a whole number greater than 0."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("That is not a whole number. Try again.")


def get_nonempty(prompt):
    """Keep asking until the user types something that is not blank."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty.")


def loan_balance(fellow_id, resource_id):
    """Units this fellow currently has on loan for this resource."""
    return sum(
        rec["borrowed"] - rec["returned"]
        for rec in borrow_records
        if rec["fellow_id"] == fellow_id and rec["resource_id"] == resource_id
    )


def currently_borrowed(resource_id):
    """Units of this resource currently out on loan, across all fellows."""
    return sum(
        rec["borrowed"] - rec["returned"]
        for rec in borrow_records
        if rec["resource_id"] == resource_id
    )


def print_resource(r):
    print(f"{r['id']} | {r['name']} | {r['category']} | {r['available']}/{r['total']} available")



def add_resource():
    rid = get_nonempty("New resource ID: ").upper()
    if find_resource(rid) is not None:
        print(f"Rejected: ID {rid} already exists.")
        return
    name = get_nonempty("Name: ")
    category = get_nonempty("Category: ")
    total = get_positive_int("Total units: ")
    resources.append(
        {"id": rid, "name": name, "category": category, "total": total, "available": total}
    )
    print(f"Added {name} ({rid}).")


def list_resources():
    if not resources:
        print("No resources yet.")
        return
    for r in resources:
        print_resource(r)


def borrow():
    fellow_id = input("Fellow ID: ").strip().upper()
    if fellow_id not in fellows:
        print("Rejected: unknown fellow ID.")
        return

    resource_id = input("Resource ID: ").strip().upper()
    resource = find_resource(resource_id)
    if resource is None:
        print("Rejected: unknown resource ID.")
        return

    qty = get_positive_int("Quantity: ")
    if qty > resource["available"]:
        print(f"Rejected: only {resource['available']} unit(s) of {resource['name']} available.")
        return

    resource["available"] -= qty
    borrow_records.append(
        {"fellow_id": fellow_id, "resource_id": resource_id, "borrowed": qty, "returned": 0}
    )
    print(f"{fellows[fellow_id]} borrowed {qty} x {resource['name']}.")


def return_item():
    fellow_id = input("Fellow ID: ").strip().upper()
    if fellow_id not in fellows:
        print("Rejected: unknown fellow ID.")
        return

    resource_id = input("Resource ID: ").strip().upper()
    resource = find_resource(resource_id)
    if resource is None:
        print("Rejected: unknown resource ID.")
        return

    on_loan = loan_balance(fellow_id, resource_id)
    if on_loan == 0:
        print(f"Rejected: {fellows[fellow_id]} has no {resource['name']} on loan.")
        return

    qty = get_positive_int("Quantity to return: ")
    if qty > on_loan:
        print(f"Rejected: {fellows[fellow_id]} only has {on_loan} on loan.")
        return

    remaining = qty
    for rec in borrow_records:
        if rec["fellow_id"] == fellow_id and rec["resource_id"] == resource_id:
            outstanding = rec["borrowed"] - rec["returned"]
            take = min(remaining, outstanding)
            rec["returned"] += take
            remaining -= take
            if remaining == 0:
                break
    resource["available"] += qty
    print(f"{fellows[fellow_id]} returned {qty} x {resource['name']}.")


def search_by_name():
    term = get_nonempty("Search name: ").lower()
    matches = [r for r in resources if term in r["name"].lower()]
    if not matches:
        print("No matching resources.")
        return
    for r in matches:
        print_resource(r)


def filter_by_category():
    category = get_nonempty("Category: ").lower()
    matches = [r for r in resources if r["category"].lower() == category]
    if not matches:
        print("No resources in that category.")
        return
    for r in matches:
        print_resource(r)


def report():
    total_units = sum(r["total"] for r in resources)
    available_units = sum(r["available"] for r in resources)
    borrowed_units = sum(rec["borrowed"] - rec["returned"] for rec in borrow_records)

    print("----- REPORT -----")
    print(f"Total units:     {total_units}")
    print(f"Available units: {available_units}")
    print(f"Borrowed units:  {borrowed_units}")

    low = [r for r in resources if r["available"] < 3]
    if low:
        print("Low stock (fewer than 3 available):")
        for r in low:
            print(f"  {r['name']} ({r['available']})")
    else:
        print("Low stock: none")

    per_resource = {r["id"]: currently_borrowed(r["id"]) for r in resources}
    highest = max(per_resource.values(), default=0)
    if highest == 0:
        print("Most borrowed: nothing is currently borrowed")
    else:
        leaders = [r for r in resources if per_resource[r["id"]] == highest]
        names = ", ".join(r["name"] for r in leaders)
        label = "Most borrowed" if len(leaders) == 1 else "Most borrowed (tie)"
        print(f"{label}: {names} ({highest})")
    print("------------------")



# MENU
def main():
    while True:
        print("\n=== Campus Resource Manager ===")
        print("1) Add resource")
        print("2) List resources")
        print("3) Borrow")
        print("4) Return")
        print("5) Search by name")
        print("6) Filter by category")
        print("7) Report")
        print("8) Exit")
        choice = input("Choose >> ").strip()

        if choice == "1":
            add_resource()
        elif choice == "2":
            list_resources()
        elif choice == "3":
            borrow()
        elif choice == "4":
            return_item()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            filter_by_category()
        elif choice == "7":
            report()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print(f"'{choice}' is not a valid option. Choose 1 to 8.")


if __name__ == "__main__":
    main()