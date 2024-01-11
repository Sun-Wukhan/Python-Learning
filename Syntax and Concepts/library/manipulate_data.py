import pandas as pd 

def analyze_data(data):
    if data: 
        df = pd.DataFrame(data)
        print("First 5 rows of the data:")
        print(df.head())
    else:
        print("No data to analyze")

analyze_data(data)