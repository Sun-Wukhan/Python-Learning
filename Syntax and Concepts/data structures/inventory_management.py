def manage_inventory(action, item=None, quantity=None):
    inventory = {"apples": 10, "bananas": 5, "oranges": 7}
    
    if action == "add" or action == "update": 
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Updated Inventory: {inventory}")
    elif action == "remove":
        if item in inventory: 
            del inventory[item]
            print(f"Removed Item: {item}")
        else: 
            print(f"Item {item} not found")
    elif action == "view":
        print(f"Current Inventory: {inventory}")
    else:
        print("No Valid Action Was Specified")


manage_inventory("add", "pears", 3)
manage_inventory("update", "apples", 5)
manage_inventory("remove", "bananas")
manage_inventory("view")