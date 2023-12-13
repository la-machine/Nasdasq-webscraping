# Candlestick Chart Flask App

This Flask application fetches financial data using the Nasdaq Data Link API and generates candlestick charts using Plotly.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Customization](#customization)
- [Collaborators](#colaborators)

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3
- Git

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/la-machine/Nasdasq-webscraping.git
   cd Nasdasq-webscraping
2. python -m venv venv:  
**- On windows:**
  - .\venv\Scripts\activate  
**- On mac/linux:**
  - source venv/bin/activate
3. pip install -r requirements.txt
## Usage:
Explaining how users can run the application.

```markdown
## Usage

Run the Flask application:
```bash
python app.py
```

## Endpoints: 
We have 2 endpoints which requires a symbol as pathvariable. 
They fetch data from the nasdaq and displays it in form of chandle stick using plotly

```markdown
## Endpoints

### Fetch Hourly Data
- **Endpoint:** `/nasdaq/<string:symbol>`
- **Method:** GET
- **Parameters:**
  - `symbol` (required): The Nasdaq stock symbol (e.g., `AAPL`).
- **Example:**
```
**For my case these are my endpoints :**
    http://127.0.0.1:5000/nasdaq/{symbol}

  http://127.0.0.1:5000/nasdaq/daily/{symbol}
## Customization:

```markdown
## Customization

You can customize the appearance of the candlestick chart and hover information in the `createChart` function within `app.py`. Update the `hovertext` list to change the hover text content.
```
## Colaborators:
 - **Developer**
   - **Name:**  *Youaleu TCHOUASSI Frank Loic*  
   - **Email:** *frankpythagore@gmail.com*  
 - **Surpervisor**
   - **Name:** *Mr Nwal Frank*  
   - **Email:** *franck.nwal@mobilehub.com*




