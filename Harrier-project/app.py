from flask import Flask, render_template, jsonify
import pandas as pd
from sqlalchemy import create_engine, URL
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# MySQL config
url_object = URL.create(
    "mysql+mysqlconnector",
    username=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    database=os.getenv("MYSQL_DATABASE"),
)
engine = create_engine(url_object)

@app.route("/")
def index():
    return render_template("chart.html")

@app.route("/data")
def get_data():
    df = pd.read_sql("SELECT * FROM stock_data", engine)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    # Make sure these columns exist and are correctly typed
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)

    df = df.sort_values("timestamp")

    # Format for Highcharts candlestick: [timestamp, open, high, low, close]
    data = df[["timestamp", "open", "high", "low", "close"]].copy()
    data["timestamp"] = data["timestamp"].astype(int) // 10**6  # Convert to JS timestamp (ms)
    candle_data = data.values.tolist()

    return jsonify(candle_data)


if __name__ == "__main__":
    app.run(debug=True)
