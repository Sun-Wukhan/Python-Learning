def manage_inventory(action, item=None, quantity=0):
    inventory = {"apples": 10, "bananas": 5, "oranges": 7}

    if action == "add":
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Updated Inventory: {inventory}")
    elif action == "update":
        if item in inventory: 
            new_quantity = inventory[item] + quantity
            if new_quantity <= 0: 
                del inventory[item]
                print(f"Inventory: {inventory} is less than 0.")
            else: 
                inventory[item] = new_quantity
                print(f"new updated amount: {inventory}")
    elif action == "remove":
        if item in inventory: 
            del inventory[item]
            print(f"Removed '{item}'. Current inventory: {inventory}")
        else: 
            print(f"CANNOT FIND ITEM: {item}")
    elif action == "view":
        print(inventory)
    else: 
        print("Invalid action")

manage_inventory("add", "pears", 3)
manage_inventory("update", "apples", -5)
manage_inventory("remove", "bananas")
manage_inventory("update", "pears", -3)  # This should remove 'pears' from inventory
manage_inventory("view")