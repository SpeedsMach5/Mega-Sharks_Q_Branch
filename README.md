# Stock Forecaster and Strategy Analyzer
Forescast future prices of securities using Facebook Prophet and Analyze different trading strategies using backtesting.

---

## Technologies

This project leverages python 3.7 with the following packages:

**[Streamlit Library](https://docs.streamlit.io/)** - Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.<br>

**[datetime.date Library](https://docs.python.org/3/library/datetime.html)** - The datetime module supplies classes for manipulating dates and times. (class datetime.date -
An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Attributes: year, month, and day.)<br>

**[fbprophet.plot Library](https://facebook.github.io/prophet/docs/quick_start.html)** - Prophet follows the sklearn model API. We create an instance of the Prophet class and then call its fit and predict methods.<br>

**[Plotly Library](https://plotly.github.io/plotly.py-docs/generated/plotly.html)** - Plotly’s Python API allows users to programmatically access Plotly’s server resources.<br>

**[Holoviews Library](https://holoviews.org/index.html)** - HoloViews is an open-source Python library designed to make data analysis and visualization seamless and simple.<br>

**[Matplotlib Library](https://matplotlib.org/)** - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.<br>

**[Numpy Library](https://numpy.org/)** - NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.<br>

**[Pandas Library](https://pandas.pydata.org/)** - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.<br>

**[hvplot Library](https://hvplot.holoviz.org/)** - A high-level plotting API for the PyData ecosystem built on HoloViews.<br>

**[Pathlib Library](https://pathlib.readthedocs.io/en/pep428/)** - This module offers a set of classes featuring all the common operations on paths in an easy, object-oriented way.<br>

**[yfinance Library](https://pypi.org/project/yfinance/)** - yfinance is **not** affiliated, endorsed, or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.<br>

**[OS Library](https://docs.python.org/3/library/os.html)** - This module provides a portable way of using operating system dependent functionality.<br>

**[Backtrader Library](https://www.backtrader.com/)** - backtrader allows you to focus on writing reusable trading strategies, indicators and analyzers instead of having to spend time building infrastructure.<br>

---

## Installation Guide

Before running the application first install the following dependencies:

To install Streamlit, run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install streamlit
```

To verify installation, run the following code in your git terminal:

```python
pip list streamlit
```

Verify installation:

![Streamlit List](images/streamlit_list.png)

This package installed version 1.3.1

Next, to install DateTime, run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install DateTime
```

The next package to install is FB Prophet. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install fbprophet
```

Verify installation:

![FBProphet List](images/fbprophet_list.png)

This package installed version 0.7.1

Next, we need to install the plotly package. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install plotly
```

Verify installation by running the following command in your terminal:

```python
conda list plotly
```

![Plotyly List](images/plotly_list.png)

The next package to install is holoviews. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install holoviews
```

Verify installation by running the following command in your terminal:

```python
conda list holoviews
```

![Holoviews List](images/holoviews_list.png)

The next package to install is matplotlib. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install matplotlib
```

Verify installation by running the following command in your terminal:

```python
conda list matplotlib
```

![matplotlib List](images/matplotlib_list.png)

The next package to install is numpy. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install numpy
```

Verify installation by running the following command in your terminal:

```python
conda list numpy
```

![numpy List](images/numpy_list.png)

The next package to install is numpy. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install pandas
```

Verify installation by running the following command in your terminal:

```python
conda list pandas
```

![pandas List](images/pandas_list.png)

The next package to install is numpy. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install hvplot
```

Verify installation by running the following command in your terminal:

```python
conda list hvplot
```

![hvplot List](images/hvplot_list.png)

The next package to install is numpy. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install pathlib
```

Verify installation by running the following command in your terminal:

```python
conda list pathlib
```

![pathlib List](images/pathlib_list.png)

The next package to install is yfinance. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install yfinance
```

Verify installation by running the following command in your terminal:

```python
conda list yfinance
```

![yfinance List](images/yfinance_list.png)

The last package to install is backtrader. Run this command in your git terminal. Make sure you are in the development environment where you would like to install it:

```python
pip install backtrader
```

Verify installation by running the following command in your terminal:

```python
conda list backtrader
```

![backtrader List](images/backtrader_list.png)

---

## Usage

To use the 'Stock Forecaster and Strategy Analyzer' application, simply clone the repository and run **Streamlit.py** in your terminal. 

You can also run the application by clicking on the following link:

**[Streamlit.py](https://share.streamlit.io/speedsmach5/market_tools/main/Streamlit.py)**

Step 1: Select the ticker you want to forecast and analyze:

![Select Ticker](images/choose_ticker.png)

For this explanation, we will be using Tesla (Ticker: TSLA)

Step 2: Select the strategies you want to analyze:

![Select Strategies](images/select_strategy.png)

For this example, we will use all 4 strategies. (DMAC, MACD, EMA/SMA Crossover, Buy the Dip)

Step 3: Select the number of prediction days you want to forecast:

![Prediction Days](images/prediction_days.png)

Step 4: Run Analysis:

![Run Analysis](images/run_analysis.png)

