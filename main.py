# import requests
# from decouple import config
# import nasdaqdatalink
# import pandas as pd
# import matplotlib.pyplot as plt

# NASDAQ_API = config('NASDAQ_API')

# data = nasdaqdatalink.get("RATEINF")


# nasdaqdatalink.ApiConfig.api_key = 'ezAZLmmy5CTsihbLTVEz'
# data = nasdaqdatalink.Dataset('EIA/PET_RWTC_D').data()
# pd.DataFrame(data.to_list())
# tables = [f"WIFI/{region}" for region in pd.DataFrame(data.to_list())[5].to_list()]
# tables.sort()
# print(pd.DataFrame(data.to_list()))
# db = nasdaqdatalink.Database('RATING')
# print(db)
# ds = db.datasets()
# pd.DataFrame(ds.to_list())
# tables = [f"RATING/{region}" for region in pd.DataFrame(ds.to_list())[1].to_list()]
# print(pd.DataFrame(ds.to_list())[1].to_list())
# db = nasdaqdatalink.Database.all()
# print(db.to_list())

# mydata = nasdaqdatalink.get_table('ZACKS/FC', ticker='AAPL')
# mydata = nasdaqdatalink.get_table('SHARADAR/SEP', ticker=['AAPL','TSLA'])
# mydata = nasdaqdatalink.get("WIKI/AMZN", returns="json")
# mydata = nasdaqdatalink.get_table('SHARADAR/TICKERS', table='SEP', ticker='AAPL')
# mydata = nasdaqdatalink.get_table('SHARADAR/METRICS', ticker='AAPL')
# mydata = nasdaqdatalink.get("WIKI/AMZN", returns="json")
# mydata = nasdaqdatalink.get_table("ZACKS/CDN", ticker='AAPL')
# print(mydata.data_fields())
# symbol = 'AAPL'
# dataset_data = nasdaqdatalink.Dataset(f'WIKI/{symbol}').data(params={'collapse':'hourly', 'transformation':'rdiff', 'rows':4 })
# mydata = nasdaqdatalink.Dataset(f'WIKI/AAPL').data(
#     params={'collapse': 'daily', 'transformation': 'rdiff', 'rows': 4})

# print(mydata.to_pandas())

# def getDataBySymol(symbol):
#     nasdaqdatalink.ApiConfig.api_key = 'ezAZLmmy5CTsihbLTVEz'
#     # mydata = nasdaqdatalink.Datatable("ZACKS/FC").data(params={'ticker': [symbol, 'MSFT']})
#     mydata = nasdaqdatalink.get_table('SHARADAR/SEP', ticker = symbol)
#     print(mydata)


# def plot_stock_data(symbol, dates, prices):
#     plt.figure(figsize=(10, 6))
#     plt.plot(dates, prices, label=symbol)
#     plt.title(f'Stock Prices for {symbol}')
#     plt.xlabel('Date')
#     plt.ylabel('Closing Price')
#     plt.legend()
#     plt.show()

# symbol = 'TSLA'
# getDataBySymol(symbol)



# dates = getNasdaqData(symbol)

# db = nasdaqdatalink.Database('RATEINF')
# print(db)
# db.data_fields()
# 
# ds = db.datasets()
# pd.DataFrame(ds.to_list())
import plotly.graph_objects as go
import plotly.io as pio
# import plotly.express as px
import pandas as pd

# Your data
data = {
    "mydata": [
        {
            "Adj. Close": 27.194834346234,
            "Adj. High": 27.495556960336,
            "Adj. Low": 26.937934984871,
            "Adj. Open": 27.208970879376,
            "Adj. Volume": 161141400.0,
            "Close": 211.61,
            "Ex-Dividend": 0.0,
            "High": 213.95,
            "Low": 209.611,
            "Open": 211.72,
            "Split Ratio": 1.0,
            "Volume": 23020200.0
        },
        {
            "Adj. Close": 26.872264362731,
            "Adj. High": 27.337484817026,
            "Adj. Low": 26.8247142058,
            "Adj. Open": 27.325918562638,
            "Adj. Volume": 111301400.0,
            "Close": 209.1,
            "Ex-Dividend": 0.0,
            "High": 212.72,
            "Low": 208.73,
            "Open": 212.63,
            "Split Ratio": 1.0,
            "Volume": 15900200.0
        },
        {
            "Adj. Close": 27.198689764364,
            "Adj. High": 27.244954781918,
            "Adj. Low": 26.770738351987,
            "Adj. Open": 26.837565599566,
            "Adj. Volume": 103021100.0,
            "Close": 211.64,
            "Ex-Dividend": 0.0,
            "High": 212.0,
            "Low": 208.31,
            "Open": 208.83,
            "Split Ratio": 1.0,
            "Volume": 14717300.0
        },
        {
            "Adj. Close": 27.081999108977,
            "Adj. High": 27.418448597746,
            "Adj. Low": 27.059894711701,
            "Adj. Open": 27.390175531463,
            "Adj. Volume": 88102700.0,
            "Close": 210.732,
            "Ex-Dividend": 0.0,
            "High": 213.35,
            "Low": 210.56,
            "Open": 213.13,
            "Split Ratio": 1.0,
            "Volume": 12586100.0
        }
    ]
}

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data["mydata"])

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Adj. Open'],
                                     high=df['Adj. High'],
                                     low=df['Adj. Low'],
                                     close=df['Adj. Close'])])

# Update layout
fig.update_layout(title='Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  xaxis_rangeslider_visible=False)
# fig = px.line(df, x=df.index, y="Adj. Close", title='Stock Prices Over Time')


# Show the chart in the browser
fig.show()
# fig.write_html('candlestick.html')

# Open the HTML file in the default web browser
# pio.show(fig, filename='candlestick_chart.html')