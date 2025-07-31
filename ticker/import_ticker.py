import json, pickle
from pprint import pprint

path = 'ticker.pkl'

with open(path, 'rb') as json_data:
    ticker = pickle.load(json_data)
    json_data.close()


pprint(ticker)