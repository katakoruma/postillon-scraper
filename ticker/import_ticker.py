import json, pickle
from pprint import pprint

path = '/Users/leon/Boxcryptor/sciebo/code/Python_encrypted/postillon_newsticker_crawler/ticker.pkl'

with open(path, 'rb') as json_data:
    ticker = pickle.load(json_data)
    json_data.close()


pprint(ticker)