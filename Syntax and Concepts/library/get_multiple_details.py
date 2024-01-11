import requests

def fetch_character_data(character_id):
    url = f'https://swapi.dev/api/people/{character_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch data')
        return None

def print_character_details(character_data):
    details = ['name', 'height', 'mass', 'hair_color', 'gender']
    for detail in details:
        print(f'{detail.title()})')

# Fetch and print details for Luke Skywalker (ID 1)
character_data = fetch_character_data(1)
if character_data:
    print_character_details(character_data)