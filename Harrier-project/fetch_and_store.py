import os
import requests
import pandas as pd
from sqlalchemy import create_engine, URL
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = os.getenv("API_URL")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    raw_data = response.json()

    time_series = raw_data.get("Time Series (5min)", {})

    # Convert time series to DataFrame
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.reset_index(inplace=True)
    df.rename(columns={"index": "timestamp"}, inplace=True)

    # Clean column names (e.g., "1. open" -> "open")
    df.columns = [col.split(". ")[-1] if ". " in col else col for col in df.columns]

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Add metadata: stock symbol
    meta_data = raw_data.get("Meta Data", {})
    df["symbol"] = meta_data.get("2. Symbol", "N/A")

    return df


def store_data(df):
    url_object = URL.create(
        "mysql+mysqlconnector",
        username=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE,
    )

    engine = create_engine(url_object)

    # Save cleaned DataFrame to MySQL
    df.to_sql("stock_data", engine, if_exists="replace", index=False)
    print("✅ Data stored successfully in MySQL database.")


if __name__ == "__main__":
    try:
        df = fetch_data()
        store_data(df)
    except Exception as e:
        print("❌ Error:", e)
