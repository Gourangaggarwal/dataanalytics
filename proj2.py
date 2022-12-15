# Import libraries
import random
import os
import numpy as np #liner algebra(mean)
import pandas as pd #data processing, csv I/O
import pandas_datareader as web

# Date
import datetime as dt
from datetime import date, timedelta, datetime

# EDA
import matplotlib.pyplot as plt
#from matplotlib.pylab import rcParams
import plotly.express as px # interactive charts
from matplotlib.ticker import ScalarFormatter
import plotly.graph_objects as go #To construct network graphs
#from plotly.subplots import make_subplots #To make multiple plots
import seaborn as sns



# compute moving averages
from typing import Self

#To avoid printing of un necessary Deprecation warning and future warnings
import warnings
warnings.filterwarnings("ignore")

import streamlit as st #web development
from PIL import Image

#merging all the data csv of cryptocurrencies
df = pd.DataFrame()
for file in os.listdir(r'Data' ) :
    if file.endswith(".csv"):
        df = pd.concat([df , pd.read_csv(os.path.join("Data", file),infer_datetime_format=True)], axis=0 )

#data cleaning
df.reset_index(drop=True, inplace=True)
df.drop('SNo',axis=1 ,inplace=True)
#df.drop('Unnamed: 0',axis=1 ,inplace=True)

#start = dt.datetime(2015, 1, 1)
#end = dt.datetime.now()
df['Date']=pd.to_datetime(df['Date']).dt.date


st.set_page_config(page_title = 'Crypto Data Dashboard',
    page_icon = '✅',
    layout="wide") 

tokens = {'XEM', 'EOS', 'XMR', 'DOT', 'USDC', 'UNI', 'BNB', 'MIOTA', 'AAVE',
            'SOL', 'BTC', 'ADA', 'USDT', 'ATOM', 'LINK', 'LTC', 'XRP', 'ETH',
            'TRX', 'XLM', 'CRO', 'DOGE', 'WBTC'}

#dashboard title
st.title("""
            # Cryptocurrency Dashboard Application
            Visually show data on crypto(**'XEM', 'EOS', 'XMR', 'DOT', 'USDC', 'UNI', 'BNB', 'MIOTA', 'AAVE',
            'SOL', 'BTC', 'ADA', 'USDT', 'ATOM', 'LINK', 'LTC', 'XRP', 'ETH',
            'TRX', 'XLM', 'CRO', 'DOGE', 'WBTC'**)from 1st January 2015 onwards.
         """)


image = Image.open("crypto_image3.png")
st.image(image, use_column_width = True)


    
st.markdown('***')
st.sidebar.header("User Input Filters")

def get_input():
    crypto_symbol = st.sidebar.selectbox('Tokens', tokens)
    start_date = st.sidebar.text_input("Start Date", "2015-01-01")
    end_date = st.sidebar.text_input("End Date", "2022-12-12")
    
    return start_date, end_date, crypto_symbol



def get_crypto_name(symbol):
    symbol = symbol.upper()
#    if symbol in df['Symbol'].unique() :
#        return df['Name']
#    else:
#        return "None"
    if symbol == "BTC":
        return "Bitcoin"
    elif symbol == "ETH":
        return "Etherium"
    elif symbol == "DOGE":
        return "Dogecoin"
    elif symbol == "XEM":
        return "NEM"         
    elif symbol == "EOS":
        return "EOS" 
    elif symbol == "XMR":
        return "Monero" 
    elif symbol == "DOT":
        return "Polkadot"
    elif symbol == "USDC":
        return "USD Coin"
    elif symbol == "UNI":
        return "Uniswap"
    elif symbol == "BNB":
        return "Binance Coin"         
    elif symbol == "MIOTA":
        return "IOTA" 
    elif symbol == "AAVE":
        return "Aave" 
    elif symbol == "SOL":
        return "Solana"
    elif symbol == "ADA":
        return "Cardano"         
    elif symbol == "USDT":
        return "Tether" 
    elif symbol == "ATOM":
        return "Cosmos" 
    elif symbol == "LINK":
        return "ChainLink"
    elif symbol == "LTC":
        return "Litecoin"
    elif symbol == "XRP":
        return "XRP"
    elif symbol == "TRX":
        return "Tron"         
    elif symbol == "XLM":
        return "Stellar" 
    elif symbol == "CRO":
        return "Crypto.com Coin" 
    elif symbol == "WBTC":
        return "Wrapped Bitcoin"  
    else:
        return "None"


def get_data(symbol, start, end):
    symbol = symbol.upper()
#       currency = df.groupby(['Symbol'])
#       currency_data = df[df['Symbol'].isin(currency)]
#       dt_cryptoname = pd.DataFrame 
    if symbol == "BTC":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Bitcoin.csv") 
    elif symbol == "":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Bitcoin.csv")
     
    elif symbol == "ETH":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Ethereum.csv")
     
    elif symbol == "DOGE":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Dogecoin.csv")
     
    elif symbol == "XEM":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_NEM.csv")
     
    elif symbol == "EOS":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_EOS.csv")
     
    elif symbol == "XMR":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Monero.csv")
     
    elif symbol == "DOT":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Polkadot.csv")
     
    elif symbol == "USDC":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_USDCoin.csv")
    elif symbol == "UNI":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Uniswap.csv") 
    elif symbol == "BNB":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_BinanceCoin.csv") 
    elif symbol == "MIOTA":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Iota.csv") 
    elif symbol == "AAVE":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Aave.csv") 
    elif symbol == "SOL":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Solana.csv") 
    elif symbol == "ADA":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Cardano.csv")
    elif symbol == "USDT":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Tether.csv") 
    elif symbol == "ATOM":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Cosmos.csv") 
    elif symbol == "LINK":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_ChainLink.csv")   
    elif symbol == "LTC":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Litecoin.csv") 
    elif symbol == "XRP":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_XRP.csv") 
    elif symbol == "TRX":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Tron.csv") 
    elif symbol == "XLM":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_Stellar.csv") 
    elif symbol == "CRO":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_CryptocomCoin.csv") 
    elif symbol == "WBTC":
        dt_cryptoname = pd.read_csv("/Users/gourang/Desktop/uni/python_project/Data/coin_WrappedBitcoin.csv")
    else:
        dt_cryptoname = pd.DataFrame (columns= [ 'Name' , 'Symbol' , 'Date', 'High' , 'Low', 'Open' , 'Close', 'Volume' , 'Marketcap'] )


    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    dt_cryptoname = dt_cryptoname.set_index(pd.DatetimeIndex(dt_cryptoname['Date'].values))
    return dt_cryptoname.loc[start:end]

start, end, symbol = get_input()

dcrypto = pd.DataFrame(data = get_data(symbol, start, end))
crypto_name = get_crypto_name(symbol)


#1st graph depicting the biggest cryptocurrencies by their market value.

plt.figure(figsize=(18,10))
ax = df.groupby(['Symbol'])['Marketcap'].last().sort_values(ascending=False).head(5).sort_values().plot(kind='barh')
ax.set_xlabel("Market Cap (in billion USD)")
ax.ticklabel_format( style='plain', axis='x')
plt.title("Top 5 Cryptocurrencies by Market Cap", fontsize=20)
st.header("Historical Data from the World of Crypto")
st.pyplot(plt)



st.header(crypto_name + " Data")
st.write(dcrypto)
st.header(crypto_name + "Data Statistics")
st.write(dcrypto.describe())

st.header(crypto_name + "Data Close Price")
st.line_chart(dcrypto['Close'])

st.header(crypto_name + "Data Volume")
st.bar_chart(dcrypto['Volume'])

st.header(crypto_name + "Data Market Cap")
st.bar_chart(dcrypto['Marketcap'])


fig = go.Figure( data = [go.Candlestick ( 
                            x = dcrypto['Date'], 
                            open = dcrypto['Open'],  
                            high = dcrypto['High'],  
                            low=dcrypto['Low'],  
                            close=dcrypto['Close'], 
                            increasing_line_color = 'green' , 
                            decreasing_line_color = 'red' ) ])

st.header(crypto_name + "Data Candlestick")
st.plotly_chart(fig)

#area plot based on the highest valiues of crypto daily.
area = px.area(data_frame= df , x = "Date" ,y= "High", line_group="Name" , color = "Name" , 
    color_discrete_sequence=px.colors.qualitative.Alphabet_r,title = 'Area Plot for TOP Cryptocurrencies')

area.update_xaxes(
    title_text = 'Date',rangeslider_visible = True,rangeselector = dict(buttons = list([dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

area.update_yaxes(title_text = 'Price in USD', ticksuffix = '$')
area.update_layout(showlegend = True,title = {'text': 'Area Plot for TOP Cryptocurrencies','y':0.9,'x':0.5,'xanchor': 'center',
                                              'yanchor': 'top'})

st.header("All Crypto Daily High")
st.plotly_chart(area, use_container_width=True)
#area plot based on the marketcaps of crypto daily.
area = px.area(data_frame = df,y  = "Marketcap" , x = "Date" , line_group="Name", color = "Name",
    color_discrete_sequence=px.colors.qualitative.Alphabet, title = 'Market Cap Change of all Cryptocurrencies')

area.update_xaxes(title_text = 'Date',rangeslider_visible = True,rangeselector = dict(buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

area.update_yaxes(title_text = 'Percentage Change ', ticksuffix = '%')
area.update_layout(showlegend = True,title = {'text': 'Market Cap Change of all Cryptocurrencies','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
st.header("All Crypto Daily Marketcap")
st.plotly_chart(area, use_container_width=True)

# special expander objects
st.sidebar.markdown('***')
with st.sidebar.expander('Help'):
    st.markdown('''
                    - Select token of your choice.
                    - Interactive plots can be zoomed or hovered to retrieve more info.
                    - Plots can be downloaded using Plotly tools.''')


# Plotting Graphs of Closing Prices of Top 4 Cryptocurrencies as per Market Cap
dx = df.copy()
top_4_currency_names = dx.groupby(['Symbol'])['Marketcap'].last().sort_values(ascending=False).head(4).index
top_4_currency_names_except_first=dx[dx['Symbol']!='BTC'].groupby(['Symbol'])['Marketcap'].last().sort_values(ascending=False).head(4).index
top_4_currency_names_except_first_two=dx[(dx['Symbol']!='BTC') & (dx['Symbol']!='ETH')].groupby(['Symbol'])['Marketcap'].last().sort_values(ascending=False).head(4).index
top_4_currency_names_except_first_two_three_four=dx[(dx['Symbol']!='BTC') & (dx['Symbol']!='ETH')& (dx['Symbol']!='USDT')& (dx['Symbol']!='BNB')].groupby(['Symbol'])['Marketcap'].last().sort_values(ascending=False).head(4).index


data_top_4_currencies = dx[dx['Symbol'].isin(top_4_currency_names)]
top_4_currencies_after_BTC = dx[dx['Symbol'].isin(top_4_currency_names_except_first)]
top_4_currencies_after_BTC_ETH = dx[dx['Symbol'].isin(top_4_currency_names_except_first_two)]
top_4_currencies_after_BTC_ETH_USDT_BNB = dx[dx['Symbol'].isin(top_4_currency_names_except_first_two_three_four)]



plt.figure(figsize=(20,25))
plt.subplot(4,1,1)
grid= sns.lineplot(data= data_top_4_currencies, x="Date", y="Close", hue='Symbol')
plt.title("Closing Prices of Top 4 Cryptocurrencies", fontsize=20)
plt.legend(loc='upper left')

plt.subplot(4,1,2)
grid1= sns.lineplot(data= top_4_currencies_after_BTC, x="Date", y="Close", hue='Symbol')
plt.title("Closing Prices of Top 4 Cryptocurrencies except BTC", fontsize=20)
plt.legend(loc='upper left')

plt.subplot(4,1,3)
grid2 = sns.lineplot(data= top_4_currencies_after_BTC_ETH,x="Date", y="Close", hue='Symbol')
plt.title("Closing Prices of Top 4 Cryptocurrencies except BTC & ETH", fontsize=20)
plt.legend(loc='upper left')

plt.subplot(4,1,4)
grid3 = sns.lineplot(data= top_4_currencies_after_BTC_ETH_USDT_BNB,x="Date", y="Close", hue='Symbol')
plt.title("Closing Prices of Top 4 Cryptocurrencies except BTC, ETH & USDT", fontsize=20)
plt.legend(loc='upper left')

st.pyplot(plt)



