import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load API URL
load_dotenv()
API_URL = os.getenv("API_URL")

# Fetch data from API
def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

# Store data in SQL DB (SQLite here)
def store_data(data):
    df = pd.DataFrame(data)
    
    # Create a connection to SQLite DB (or change URL for PostgreSQL/MySQL)
    engine = create_engine('sqlite:///db/data.db')
    df.to_sql('posts', engine, if_exists='replace', index=False)
    print("Data stored successfully in DB.")

if __name__ == "__main__":
    data = fetch_data()
    store_data(data)
