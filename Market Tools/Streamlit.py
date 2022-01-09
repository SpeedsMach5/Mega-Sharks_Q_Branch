import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objects as go
import pandas as pd
import os

#CONFIGURATION
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
TICKER_LIST_PATH = 'data/constituents_symbols.txt'
STRATEGY_LIST_PATH = 'data/strategies.txt'

status = st.text("")

# UTILITY FUNCTIONS
def get_listbox_data(file_path):
    """Retrieves a list of data from a carriage return-delimited file

    Opens the file specified by the file path and returns a list of its contents.

    Parameters
    ----------
    file_path: str, required
        The path of the file containing the list of items
    
    """

    with open(file_path, "r") as file:
        content = file.read()
        content = content.split("\n")
        return content

# DATA FUNCTIONS
def load_data_for_ticker(tickers, start_date, end_date):
    """Retrieves pricing historical pricing data for a list of tickers

    Utilizes yfinance to return pricing data between a start and end date.

    Parameters
    ----------
    tickers: str, required
        A list of ticker symbols
    
    start_date: str, required
        Download start date string (YYYY-MM-DD) or _datetime
    
    end_date: str, required
        Download end date string (YYYY-MM-DD) or _datetime.
    
    """
    data = yf.download(tickers, start_date, end_date)
    data.reset_index(inplace = True)
    return data

def run_analysis():
    """Runs and displays the different sections of the financial analysis

    Any code that needs to be run should have its own function and
    be called from here.  This is the main launch pad.  Order matters.

    Parameters
    ----------
    tickers: str, required
        A list of ticker symbols
    
    start_date: str, required
        Download start date string (YYYY-MM-DD) or _datetime
    
    end_date: str, required
        Download end date string (YYYY-MM-DD) or _datetime.
    
    """

    display_parameter_section()
    data = display_ticker_data_section(ticker_selectbox, START, TODAY)
    display_forecasting_section(data)
    display_sentiment_indicators_section()


def display_parameter_section():
    """Displays a summary of the user-selected parameters
    
    """
    st.subheader("Parameters")
    st.write('Summary of parameter selections:')
    st.markdown('- Tickers: ' + ticker_selectbox)
    st.markdown('- Strategies: ' + str(strategy_listbox))
    st.markdown('- Prediction days: ' + str(n_day))

#@st.cache(suppress_st_warning=True)
def display_ticker_data_section(tickers, start_date, end_date, tail_records=5):
    """Retrieves and displays the Open, High, Low, Close prices 
    
    Retrieves and displays the Open, High, Low, and Close prices for the last
    X records in the DataFrame.

    Parameters
    ----------
    tickers: str, required
        A list of ticker symbols
    
    start_date: str, required
        Download start date string (YYYY-MM-DD) or _datetime
    
    end_date: str, required
        Download end date string (YYYY-MM-DD) or _datetime.
    
    tail_records: int, optional (Default = 5)
        Specifies the number of records to display

    """

    st.subheader(f"Ticker Data: Last {tail_records} Closes")
    status = st.info("Loading...")
    data = load_data_for_ticker(ticker_selectbox, start_date, end_date)
    status.empty()
    st.write(data.tail(tail_records))
    return data

#@st.cache(suppress_st_warning=True)
def display_forecasting_section(data):
    """Displays forecasting data

    Parameters
    ----------
    data: DataFrame, required
        Open, High, Low, Close data for a ticker
    
    """
    st.subheader("Forecasting")
    status = st.info("Loading...")

    df_train = data[["Date", "Close"]]
    df_train = df_train.rename(columns={"Date":"ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period, freq='D')
    forecast = m.predict(future)

    st.warning("Note: These are probable outcomes, not an actual crystal ball")
    st.write(forecast.tail())

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    fig2 = m.plot_components(forecast)
    st.write(fig2)
    status.empty()

def display_sentiment_indicators_section():
    st.subheader("Sentiment Indicators")
    sentiment_status = st.info("Loading...")

    # SENTIMENT CODE HERE

    sentiment_status.empty()


# Linear Sidebar UI
st.sidebar.subheader('Analysis Parameters')

status.text = "Loading ticker list"
ticker_list = get_listbox_data(TICKER_LIST_PATH)
ticker_selectbox = st.sidebar.selectbox("1. Choose a ticker", ticker_list)
st.sidebar.markdown('____')

strategy_list = get_listbox_data(STRATEGY_LIST_PATH)
strategy_listbox = st.sidebar.multiselect("2. Choose one or more trading strategies", strategy_list)
st.sidebar.markdown('____')

n_day = st.sidebar.slider("3. Choose number of prediction days", 1,10)
period = n_day*10
st.sidebar.markdown('____')

st.sidebar.button('4. Run Analysis',help='Click to run analysis.', on_click=run_analysis)
