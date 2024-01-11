def manage_library(action, title=None, status=0):
    library = {"1984": "available", "To Kill a Mockingbird": "checked out", "The Great Gatsby": "available"}

    if action == "add": 
        library[title] = status
        print(f"Book Added: {title} - {status}. Updated library: {library}")
    elif action == "update":
        if title in library:
            library[title] = status
            print(f"Updated '{title}' status to '{status}'.")
        else: 
            print(f"Title not found")
    elif action == "remove":
        if title in library: 
            del library[title]
            print(f"Removed '{title}'. Updated library: {library}")
        else: 
            print(f"Book '{title}' not found.")
    elif action == "view":
        for key, value in library.items():
            print(f"{key} and {value}")
    else: 
        print("Invalid")

# manage_library("add", "Brave New World", "available")
# manage_library("update", "1984", "checked out")
# manage_library("remove", "To Kill a Mockingbird")
manage_library("view")