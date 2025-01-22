from phi.agent import Agent
import phi.api
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.playground import Playground, serve_playground_app
import yfinance as yf
import mplfinance as mpf
import pandas as pd
import os

# Load environment variables from .env file
load_dotenv()

# Set PHI API key
phi.api = os.getenv("PHI_API_KEY")

# Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="gemma2-9b-it"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display the stock data, including:",
        "- Analyst recommendations",
        "- Stock fundamentals",
        "- Relevant company news",
        "Make sure to include any sources for the data.",
        "give the stock name and news about the stock and their sources"
    ],
    show_tool_calls=True,
    markdown=True,
)

import yfinance as yf
import pandas as pd
import mplfinance as mpf
import os

def query_stock_info(stock_name):
    """
    Fetch and save specific details for the given stock from Yahoo Finance.
    """
    stock = yf.Ticker(stock_name)
    stock_name = stock_name[:-3] if stock_name.endswith(".NS") else stock_name
    
    # File names
    summary_file = f"{stock_name}_Summary.txt"
    chart_file = f"{stock_name}_Chart.png"
    historical_data_file = f"{stock_name}_Historical_Data.csv"
    profile_file = f"{stock_name}_Profile.csv"
    financials_file = f"{stock_name}_Financials.csv"
    analysis_file = f"{stock_name}_Analysis.txt"
    holders_file = f"{stock_name}_Holders.txt"  

    # Summary
    try:
        summary = stock.info
        with open(summary_file, "w", encoding="utf-8") as file:
            file.write("### Summary ###\n")
            for key, value in summary.items():
                file.write(f"{key}: {value}\n")
        print(f"Summary saved to {summary_file}")
    except Exception as e:
        print(f"Error saving summary: {e}")

    # Candlestick Chart with Moving Averages and Buy/Sell Recommendation
    try:
        hist = stock.history(period="6mo")

        if 'Volume' not in hist.columns:
            hist['Volume'] = 0  # Set to 0 if no volume data available

        hist['MA50'] = hist['Close'].rolling(window=50).mean()
        hist['MA20'] = hist['Close'].rolling(window=20).mean()

        # Determine Buy/Sell recommendation based on moving averages crossover
        latest_20ma = hist['MA20'].iloc[-1]
        latest_50ma = hist['MA50'].iloc[-1]
        
        recommendation = "Hold"
        if latest_20ma > latest_50ma:
            recommendation = "Buy"
        elif latest_20ma < latest_50ma:
            recommendation = "Sell"

        # Prepare the data for candlestick chart
        hist_data = hist[['Open', 'High', 'Low', 'Close', 'Volume']]
        
        # Customize the chart with moving averages and recommendation text
        add_plot = [
            mpf.make_addplot(hist['MA50'], color='blue', linestyle='--', width=1.5, panel=0),
            mpf.make_addplot(hist['MA20'], color='green', linestyle='-.', width=1.5, panel=0),
        ]

        # Plot the candlestick chart
        mpf.plot(
                hist_data,
                type='candle',
                style='charles',
                title=f"{stock_name} Stock Price Chart (1 Year)\nRecommendation: {recommendation}",
                ylabel="Price (₹)",
                addplot=add_plot,
                figsize=(25, 10),
                volume=True,
                savefig=chart_file,
                show_nontrading=False,  
                panel_ratios=(6, 2),    
                tight_layout=True,
                update_width_config=dict(candle_linewidth=0.7, volume_linewidth=0.6),
            )

        print(f"Candlestick chart with moving averages and recommendation saved to {chart_file}")
    except Exception as e:
        print(f"Error saving chart: {e}")

    # Historical Data
    try:
        hist.to_csv(historical_data_file)
        print(f"Historical Data saved to {historical_data_file}")
    except Exception as e:
        print(f"Error saving historical data: {e}")

    # Profile
    try:
        profile = {
            "Sector": summary.get("sector", "N/A"),
            "Industry": summary.get("industry", "N/A")
        }
        profile_df = pd.DataFrame([profile])
        profile_df.to_csv(profile_file, index=False)
        print(f"Profile saved to {profile_file}")
    except Exception as e:
        print(f"Error saving profile: {e}")

    # Financials
    try:
        financials = stock.financials
        financials.to_csv(financials_file)
        print(f"Financials saved to {financials_file}")
    except Exception as e:
        print(f"Error saving financials: {e}")

    # Analysis
    try:
        analysis = stock.recommendations
        with open(analysis_file, "w", encoding="utf-8") as file:
            if analysis is not None:
                file.write("### Analyst Recommendations ###\n")
                file.write(analysis.to_string())
                print(f"Analysis saved to {analysis_file}")
            else:
                file.write("No analysis data available.")
                print("No analysis data available.")
    except Exception as e:
        print(f"Error saving analysis: {e}")

    # Holders
    try:
        holders = stock.major_holders
        with open(holders_file, "w", encoding="utf-8") as file:
            file.write("### Major Holders ###\n")
            file.write(holders.to_string())
        print(f"Holders saved to {holders_file}")
    except Exception as e:
        print(f"Error saving holders: {e}")

# Playground app
app = Playground(agents=[finance_agent]).get_app()

if __name__ == "__main__":
    stock_name = input("Enter the stock name: ").strip()
    query = query_stock_info(stock_name)
    serve_playground_app("playground:app", reload=True)
#TCS.NS stock open priceand company news
