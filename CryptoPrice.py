# This app is for practice. Insights gained is not financial advice of any sort.
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

st.set_page_config(layout="wide")

image = Image.open('crypto.jpg')

st.image(image, width = 500)

st.title('Crypto Price App')
st.markdown("""
Cryptocurrency prices for the top 100 cryptocurrency from the **CoinMarketCap**!

""")

expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:** [CoinMarketCap](http://coinmarketcap.com).
* **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf).
""")

col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

col1.header('Input Options')

currency_price_unit = col1.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))
