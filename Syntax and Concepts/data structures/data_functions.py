def manage_account_info(action, key, value=None):
    person = {"name": "Navid", "age": 30, "city": "Toronto"}
    if action == "add" or action == "modify":
        person[key] = value 
        print(f"Updated info: {person}")
    elif action == "delete":
        if key in person: 
            del person[key]
            print(f"Delete info: {person}")
        else: 
            print(f"Key '{key}' not found.")
    else: 
        print("Invalid Action")
        
manage_account_info("add", "game", "overwatch")
