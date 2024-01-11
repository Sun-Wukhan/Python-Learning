import requests

def fetch_character_data():
    url = "https://swapi.dev/api/people/1/"
    response = requests.get(url)
    if response.status_code == 200:
    
        return response.json()
    else: 
        print("FAILED TO FETCH")
        return None 

# Fetch data for character with ID 1

def print_out_values(): 
    character_data = fetch_character_data()
    if character_data:
        print(character_data.get("height", "N/A"))
    else:
        print("No data to print.")
        
print_out_values()
    