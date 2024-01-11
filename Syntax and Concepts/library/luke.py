import requests 

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200: 
        print(response.json())
        return response.json()
    else: 
        print("No Data Found")
        return None 

def analyze_data(data):
    film_urls = character.data.get("films", [])
    