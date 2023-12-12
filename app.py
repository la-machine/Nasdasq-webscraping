from flask import Flask, jsonify, request
import plotly.graph_objects as go
import plotly.io as pio
import nasdaqdatalink
# Create a Flask web application

app = Flask(__name__)
# Define an endpoint to fetch hourly data for a given Nasdaq symbol
@app.route('/nasdaq/<string:symbol>', methods=['GET'])
def getDataBySymol(symbol):
    nasdaqdatalink.ApiConfig.api_key = 'ezAZLmmy5CTsihbLTVEz'
    # Fetch hourly data for the specified symbol
    mydata = nasdaqdatalink.Dataset(f'WIKI/{symbol}').data(params={'start_date':'2001-01-01', 'end_date':'2010-01-01','collapse': 'hourly', 'transformation': 'rdiff', 'rows': 4})
    # If no data is found, return a 404 error
    if mydata is None:
        return jsonify({'error': 'Task not found'}), 404
    # Create and show a candlestick chart for the fetched data
    createChart(mydata.to_pandas(), symbol)
    # Return the fetched data in JSON format
    return jsonify({'mydata': mydata.to_pandas().to_dict(orient='records')})
# Define an endpoint to fetch daily data for a given Nasdaq symbol
@app.route('/nasdaq/daily/<string:symbol>', methods=['GET'])
def getDataBySymolDaily(symbol):
    nasdaqdatalink.ApiConfig.api_key = 'ezAZLmmy5CTsihbLTVEz'
    mydata = nasdaqdatalink.Dataset(f'WIKI/{symbol}').data(params={'collapse': 'daily', 'transformation': 'rdiff', 'rows': 4})
    if mydata is None:
        return jsonify({'error': 'Task not found'}), 404
    createChart(mydata.to_pandas(), symbol)
    return jsonify({'mydata': mydata.to_pandas().to_dict(orient='records')})
# Function to create a candlestick chart using Plotly
def createChart(data,symbol):
    # Convert the data to a pandas DataFrame
    df = data
    # Identify if each candlestick represents a gain or loss
    is_profit = df['Adj. Close'] > df['Adj. Open']
    # Create a list for hover text, indicating Gain or Loss
    hovertext = ['Gain' if profit else 'Loss' for profit in is_profit]

    # # Create candlestick chart with hover text and info
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Adj. Open'],
                                         high=df['Adj. High'],
                                         low=df['Adj. Low'],
                                         close=df['Adj. Close'],
                                         hovertext=hovertext,
                                         hoverinfo="text")
                          ])

    # Update layout
    fig.update_layout(title=f'{symbol} Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Stock Price',
                      xaxis_rangeslider_visible=False)

    # Show the chart in the browser
    fig.show()
# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
