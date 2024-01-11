import requests 
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

def analyze_data(data):
    if data: 
        df = pd.DataFrame(data)
        print("First 5 rows of the data:")
        print(df.head())
    else:
        print("No data to analyze")

# Example URL from JSONPlaceholder
data_url = "https://jsonplaceholder.typicode.com/posts"
data = fetch_data(data_url)
analyze_data(data)