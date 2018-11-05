import json
import os
import unittest

import print_data

def _read_test_input(filename):
    basepath = os.path.dirname(__file__)
    filepath = os.path.join(basepath, 'testdata', filename)
    return open(filepath).read()

def _read_golden_output(filename):
    basepath = os.path.dirname(__file__)
    filepath = os.path.join(basepath, 'testdata', filename)
    return json.loads(open(filepath).read())

class ScrapeTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_scrapes_bitcoin_snapshot(self):
        self.assertEqual(
            _read_golden_output('bitcoin-golden.json'),
            print_data.scrape_coinmarketcap_markets_html(
                _read_test_input('bitcoin.html')
                )
            )
