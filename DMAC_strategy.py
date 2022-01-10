# %% [markdown]
# # DMAC Trading Strategy Algorithm

# %% [markdown]
# ## Import the Libraries and Create a DataFrame

# %%
# Import the required libraries
import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
from datetime import date
import yfinance as yf
import os

# %% [markdown]
# ## Retrieve the Historical Stock Data

# %%
# Set the Start and End Dates for Yahoo Finance API
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# %%
# Load_data function to retrieve historical information
def load_data(ticker):
  data = yf.download(ticker, START, TODAY)
  #data.reset_index(inplace = True)
  
  return data

# %% [markdown]
# ## Create Signals DF

# %%
# Create Signals DF
signals_df = load_data("KEYS")
signals_df

# %% [markdown]
# ## Plot the Signals Line

# %%
# Use hvplot to visualize the data
signals_df.Close.hvplot()

# %% [markdown]
# ## Calculate the SMA for the Short and Long Windows

# %%
# Set the variables for short window and long window periods
short_window = 50
long_window = 100

# %% [markdown]
# ## Define two new DataFrame columns, named “SMA50” and “SMA100”

# %%
# Generate the short and long window simple moving averages (50 and 100 days, respectively)
signals_df["SMA50"] = signals_df.Close.rolling(window=short_window).mean()
signals_df["SMA100"] = signals_df.Close.rolling(window=long_window).mean()

# Review the DataFrame
display(signals_df.head())
display(signals_df.tail())

# %% [markdown]
# ## Identify the Trading Signals

# %%
# Create a column to hold the trading signal
signals_df["Signal"] = 0.0
signals_df

# %%
# Generate the trading signal 0 or 1,
# where 1 is the short-window (SMA50) greater than the long-window (SMA100)
# and 0 is when the condition is not met
signals_df["Signal"][short_window:] = np.where(
    signals_df["SMA50"][short_window:] > signals_df["SMA100"][short_window:], 1.0, 0.0
)

# Review the DataFrame
signals_df.tail(10)

# %% [markdown]
# ## Find the Crossover Points

# %%
# Calculate the points in time when the Signal value changes
# Identify trade entry (1) and exit (-1) points
signals_df["Entry/Exit"] = signals_df["Signal"].diff()

# Review the DataFrame
signals_df.loc["2015-12-03":"2015-12-13"]

# %% [markdown]
# ## Plot the Data

# %%
# Visualize exit position relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
    color="yellow",
    marker="v",
    size=200,
    legend=False,
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
exit

# %%
# Visualize entry position relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
    color="purple",
    marker="^",
    size=200,
    legend=False,
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
entry

# %%
# Visualize close price for the investment
security_close = signals_df[['Close']].hvplot(
    line_color="lightgray",
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
security_close

# %%
# Visualize moving averages
moving_avgs = signals_df[["SMA50", "SMA100"]].hvplot(
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
moving_avgs

# %%
# Create the overlay plot
entry_exit_plot = security_close * moving_avgs * entry * exit

# Show the plot
entry_exit_plot.opts(
    title="Apple - SMA50, SMA100, Entry and Exit Points"
)

# %% [markdown]
# ## Backtest the Algorithm

# %%
# Set initial capital
initial_capital = float(100000)

# Set the share size
share_size = 500

# Buy a 500 share position when the dual moving average crossover Signal equals 1 (SMA50 is greater than SMA100)
# Sell a 500 share position when the dual moving average crossover Signal equals 0 (SMA50 is less than SMA100)
signals_df['Position'] = share_size * signals_df['Signal']

# Determine the points in time where a 500 share position is bought or sold
signals_df['Entry/Exit Position'] = signals_df['Position'].diff()

# Multiply the close price by the number of shares held, or the Position
signals_df['Portfolio Holdings'] = signals_df.Close * signals_df['Position']

# Subtract the amount of either the cost or proceeds of the trade from the initial capital invested
signals_df['Portfolio Cash'] = initial_capital - (signals_df.Close * signals_df['Entry/Exit Position']).cumsum()

# Calculate the total portfolio value by adding the portfolio cash to the portfolio holdings (or investments)
signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']

# Calculate the portfolio daily returns
signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

# Calculate the portfolio cumulative returns
signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1

# Print the DataFrame
signals_df

# %% [markdown]
# ## Interpret the Backtesting Results

# %%
# Visualize exit position relative to total portfolio value
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Portfolio Total'].hvplot.scatter(
    color='yellow',
    marker='v',
    size=200,
    legend=False,
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize entry position relative to total portfolio value
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Portfolio Total'].hvplot.scatter(
    color='purple',
    marker='^',
    size=200,
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize the value of the total portfolio
total_portfolio_value = signals_df[['Portfolio Total']].hvplot(
    line_color='lightgray',
    ylabel='Total Portfolio Value',
    xlabel='Date',
    width=1000,
    height=400
)

# Overlay the plots
portfolio_entry_exit_plot = total_portfolio_value * entry * exit
portfolio_entry_exit_plot.opts(
    title="Apple Algorithm - Total Portfolio Value",
    yformatter='%.0f'
)


