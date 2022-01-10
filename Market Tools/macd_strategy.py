# Import the required libraries
import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
from datetime import date
from pandas.core.frame import DataFrame
import yfinance as yf
import os
import pricing

def analyze_macd(signals_df:DataFrame):
  # Calculate the MACD and Signal Line Indicators
  # Calculate the short term exponential moving average (EMA)
  signals_df["short_ema"] = signals_df.Close.ewm(span=12, adjust=False).mean()

  # Calculate the long term exponential moving average (EMA)
  signals_df["long_ema"] = signals_df.Close.ewm(span=26, adjust=False).mean()

  # Calculate the MACD Line
  signals_df["macd"] = signals_df["short_ema"] - signals_df["long_ema"]

  # Calculate the Signal Line
  signals_df["signal line"] = signals_df["macd"].ewm(span=9, adjust=False).mean()

  # Create a column to hold the trading signal
  signals_df["Signal"] = 0.0
  
  # Generate the trading signal 0 or 1,
  # where 1 is the MACD greater than the signal line
  # and 0 is when the condition is not met
  signals_df["Signal"] = np.where(
      signals_df["macd"] > signals_df["signal line"], 1.0, 0.0
  )

  # Calculate the points in time when the Signal value changes
  # Identify trade entry (1) and exit (-1) points
  signals_df["Entry/Exit"] = signals_df["Signal"].diff()

  # Visualize exit position relative to close price
  exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
      color="yellow",
      marker="v",
      size=200,
      legend=False,
      ylabel="Price in $",
      width=1000,
      height=400)

  # Visualize entry position relative to close price
  entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
      color="purple",
      marker="^",
      size=200,
      legend=False,
      ylabel="Price in $",
      width=1000,
      height=400)

  # Visualize close price for the investment
  security_close = signals_df[['Close']].hvplot(
      line_color="lightgray",
      ylabel="Price in $",
      width=1000,
      height=400)

  # Visualize moving averages
  dmac_signal_lines = signals_df[["macd", "signal line"]].hvplot(
      ylabel="Price in $",
      width=1000,
      height=400)

  # Create the overlay plot
  entry_exit_plot = security_close * dmac_signal_lines * entry * exit

  return signals_df, entry_exit_plot

def backtest_macd(signals_df):
  # Set initial capital
  initial_capital = float(100000)

  # Set the share size
  share_size = 500