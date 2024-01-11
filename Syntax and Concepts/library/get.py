import requests 

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else: 
        print("Failed to fetch Data")
        return None

data_url = "https://swapi.dev/api/people/11"
data = fetch_data(data_url)