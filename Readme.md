# Finance AI Agent with Stock Analysis

## Overview
This project provides an AI-powered Finance Agent capable of analyzing and visualizing stock market data using the PHI framework and Yahoo Finance APIs. The application supports features like fetching historical stock data, generating candlestick charts with moving averages, providing analyst recommendations, and displaying company news. The project is designed for financial analysis and is user-friendly.

## Features
- **Stock Summary**: Fetch and save detailed stock summary information.
- **Candlestick Chart**: Generate a candlestick chart with 20-day and 50-day moving averages.
- **Buy/Sell Recommendation**: Provide a recommendation based on moving average crossover analysis.
- **Historical Data**: Save stock historical data to a CSV file.
- **Company Profile**: Extract and save the sector and industry of the company.
- **Financials**: Retrieve and save the financial statements of the company.
- **Analyst Recommendations**: Display and save analyst recommendations.
- **Major Holders**: Save details of the major shareholders of the company.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dhananjaypatil/finance-ai-agent.git
   ```

2. **Set Up Environment**:
   - Create a `.env` file in the root directory.
   - Add your PHI API key to the `.env` file:
     ```
     PHI_API_KEY=your_phi_api_key
     ```

3. **Install Dependencies**:
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python playground.py
   ```

## Usage

### Querying Stock Information
1. Run the application.
2. Enter the stock name (e.g., `TCS.NS`) when prompted.
3. The application will:
   - Save the stock's summary to a `.txt` file.
   - Generate a candlestick chart with moving averages and a buy/sell recommendation.
   - Save historical data, profile, financials, analyst recommendations, and holders to respective files.

### Visualizing Stock Data
- The candlestick chart will include:
  - 20-day moving average (green line).
  - 50-day moving average (blue line).
  - A buy/sell recommendation displayed in the chart title.

### Accessing Saved Data
- All files (e.g., summary, historical data, profile, etc.) will be saved in the current working directory with the stock name as a prefix.

## File Outputs
| File Name                        | Description                                       |
|----------------------------------|---------------------------------------------------|
| `<stock_name>_Summary.txt`       | Stock summary details.                           |
| `<stock_name>_Chart.png`         | Candlestick chart with moving averages.          |
| `<stock_name>_Historical_Data.csv` | Historical stock data.                           |
| `<stock_name>_Profile.csv`       | Company sector and industry.                     |
| `<stock_name>_Financials.csv`    | Company financials.                              |
| `<stock_name>_Analysis.txt`      | Analyst recommendations.                         |
| `<stock_name>_Holders.txt`       | Major shareholders.                              |

## Key Components

### Finance AI Agent
The Finance AI Agent is configured using the PHI framework with the following tools:
- **YFinanceTools**: Fetch stock price, analyst recommendations, stock fundamentals, and company news.
- **Groq Model**: Used for generating insights and analyzing stock data.

### Stock Query Function
The `query_stock_info` function performs the following:
- Fetches stock information and saves relevant details.
- Generates candlestick charts with moving averages.
- Provides a buy/sell recommendation based on moving averages crossover.

### Playground
The PHI Playground serves as an interactive environment to interactive and query stock data.

## Example
1. Input stock name: `TCS.NS`
2. Generated output:
   - Summary: Saved to `TCS_Summary.txt`
   - Chart: Saved to `TCS_Chart.png`
   - Historical Data: Saved to `TCS_Historical_Data.csv`
   - Financials: Saved to `TCS_Financials.csv`
   - Analyst Recommendations: Saved to `TCS_Analysis.txt`
   - Major Holders: Saved to `TCS_Holders.txt`

## Dependencies
- `phi`
- `yfinance`
- `mplfinance`
- `pandas`
- `python-dotenv`

