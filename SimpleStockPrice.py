import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")

#Define ticker symbol
tickerSymbol = 'GOOGL' #Google
# tickerSymbol = 'AAPL' #Apple
# tickerSymbol = 'AMZN' #Amazon
#Get info about ticker
tickerData = yf.Ticker(tickerSymbol)
#Find the prices over specified period of time
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
