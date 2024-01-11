def manage_person_info(action, key, value=None):
    person = {"name": "Navid", "age": 30, "city": "Toronto"}

    if action == "add" or action == "modify":
        person[key] = value
        print(f"Updated info: {person}")
    elif action == "delete":
        if key in person:
            del person[key]
            print(f"Deleted '{key}'. Updated info: {person}")
        else:
            print(f"Key '{key}' not found.")
    else:
        print("Invalid action.")

# Test the function
manage_person_info("add", "email", "navid_khan@icloud.com")
manage_person_info("modify", "age", 31)
manage_person_info("delete", "city")