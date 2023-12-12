from flask import Flask, jsonify, render_template
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO
import base64
import nasdaqdatalink

app = Flask(__name__)

# ... (other route handlers and configurations)

@app.route('/nasdaq/<string:symbol>', methods=['GET'])
def getDataBySymbol(symbol):
    nasdaqdatalink.ApiConfig.api_key = 'ezAZLmmy5CTsihbLTVEz'
    mydata = nasdaqdatalink.Dataset(f'WIKI/{symbol}').data(params={'start_date': '2001-01-01', 'end_date': '2010-01-01', 'collapse': 'hourly', 'transformation': 'rdiff', 'rows': 4})
    if mydata is None:
        return jsonify({'error': 'Task not found'}), 404

    chart_html = createChart(mydata.to_pandas(), symbol)
    return render_template('chart_template.html', chart_html=chart_html)

# ... (other route handlers and configurations)

def createChart(data, symbol):
    # Convert the data to a pandas DataFrame
    df = data

    # Create a Matplotlib figure
    fig, ax = plt.subplots()

    # Plot the 'Adj. Close' values against the date
    ax.plot(df.index, df['Adj. Close'], label='Adj. Close', color='blue')
    ax.set_title(f'{symbol} Candlestick Chart')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.legend()

    # Save the Matplotlib figure to a BytesIO object
    img = BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(img)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()

    # Close the Matplotlib figure to free up resources
    plt.close(fig)

    # Return the base64-encoded image for embedding in HTML
    return f'<img src="data:image/png;base64,{img_base64}" alt="{symbol} Candlestick Chart">'

if __name__ == '__main__':
    app.run(debug=True)
