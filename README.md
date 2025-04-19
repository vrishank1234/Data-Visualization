# Stock Data Visualization Project

This project fetches stock data from Alpha Vantage API and visualizes it using a web interface. The data is stored in a MySQL database and displayed using interactive charts.

## Prerequisites

- Python 3.11 or higher
- MySQL Server
- Homebrew (for macOS users)

## Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vrishank1234/Data-Visualization.git
   cd Data-Visualization/Harrier-project
   ```

2. **Install MySQL** (macOS)
   ```bash
   brew install mysql
   brew services start mysql
   ```
   After installation, set up MySQL root password:
   ```bash
   mysql_secure_installation
   ```

3. **Create MySQL Database**
   ```bash
   mysql -u root -p
   ```
   In MySQL prompt:
   ```sql
   CREATE DATABASE stock_db;
   exit;
   ```

4. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables**
   Create a `.env` file in the Harrier-project directory with the following content:
   ```
   API_URL=https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=YOUR_API_KEY
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DATABASE=stock_db
   ```
   Replace `YOUR_API_KEY` with your Alpha Vantage API key and `your_mysql_password` with your MySQL password.

## Running the Project

1. **Fetch and Store Data**
   ```bash
   python fetch_and_store.py
   ```
   This will fetch the stock data from Alpha Vantage API and store it in the MySQL database.

2. **Start the Web Application**
   ```bash
   python app.py
   ```
   The web application will start on `http://localhost:5000`. Open this URL in your browser to view the stock data visualization.

## Project Structure

- `fetch_and_store.py`: Script to fetch data from API and store in MySQL
- `app.py`: Flask web application for data visualization
- `templates/`: Directory containing HTML templates
- `requirements.txt`: Python dependencies
- `.env`: Environment variables configuration

## Troubleshooting

1. **MySQL Connection Issues**
   - Make sure MySQL service is running: `brew services list`
   - Verify MySQL credentials in `.env` file
   - Check if database exists: `mysql -u root -p -e "SHOW DATABASES;"`

2. **API Issues**
   - Verify your Alpha Vantage API key
   - Check API rate limits
   - Ensure internet connectivity

## Notes

- The project uses Alpha Vantage API for stock data. You might need to sign up for an API key at [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
- The free tier of Alpha Vantage API has rate limits. Check their documentation for details
- Make sure to keep your API key and database credentials secure
