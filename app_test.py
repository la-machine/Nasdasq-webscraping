import unittest
from flask import Flask
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_getDataBySymbol(self):
        response = self.app.get('/nasdaq/AAPL')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('mydata', data)
        self.assertIsInstance(data['mydata'], list)
        self.assertGreater(len(data['mydata']), 0)

        required_keys = ['Adj. Close', 'Adj. High', 'Adj. Low', 'Adj. Open', 'Adj. Volume', 'Close', 'Ex-Dividend',
                         'High', 'Low', 'Open', 'Split Ratio', 'Volume']
        for entry in data['mydata']:
            for key in required_keys:
                self.assertIn(key, entry)

        for entry in data['mydata']:
            self.assertIsInstance(entry['Close'], (int, float))

    def test_getDataBySymbolDaily(self):
        response = self.app.get('/nasdaq/daily/AAPL')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
