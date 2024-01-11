import requests 
import pandas as pd  

def fetch_data(url): 
    response = requests.get(url)
    if response.status_code == 200: 
        print(response.json())
        return response.json()
    else:
        print("Incorrect URL Or some other Error has occured")
        return None 

def analyze_data(data): 
    if data and 'results' in data: 
        df = pd.DataFrame(data['results'])
        print("Star Wars Characters: ")
        print(df[['name', 'species']])
    else:
        print("No data to analyze")
    
data_url = "https://swapi.dev/api/people/"
data = fetch_data(data_url)
analyze_data(data)