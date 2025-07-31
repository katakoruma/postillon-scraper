#%%%%%%%%%%%%%%%%
import requests, json, pickle
from itertools import product

#%%%%%%%%%%%%%%%%

id = 1000
y,m = 2020, 4
save = False

url = lambda year, month, id:f'https://www.der-postillon.com/{year}/{month:02d}/newsticker-{id}.html'
path = '/Users/leon/Boxcryptor/sciebo/code/Python_encrypted/postillon_newsticker_crawler/ticker.pkl'

#html_export = requests.get(url(y,m))
#html_export.raise_for_status()

ids = 1500,2050
date_list = list(product(reversed(list(range(2020, 2024))), reversed(list(range(1, 13)))))

#%%%%%%%%%%%%%%%%

ticker_dict = {}


def append_ticker(export, year, month, id):

    split1 = export.text.split('<p>+++')
    split2 = export.text.split('+++</p>\n')

    ticker = split1[1:-1]
    ticker.append(split2[-2])

    ticker = [text.replace('+++', '').replace('<p>', '').replace('</p>', '').replace('\n', '') for text in ticker]
    ticker = [text[1:-1] for text in ticker]

    print(ticker)

    ticker_dict[id] = {'date': (year, month), 'ticker': ticker, 'n_ticker': len(ticker)}




id = max(ids)-1

while id in range(ids[0],ids[1]):

    for year,month in date_list:

        while id in range(ids[0],ids[1]):

            print(year,month,id)

            html_export = requests.get(url(year,month,id))
            
            if html_export.ok:
                print('success')

                try:
                    append_ticker(html_export, year, month, id)
                except:
                    print('Something went wrong with ', id)

                id -= 1
                continue
            else:
                break

    del year ; del month
    id -= 1


#%%%%%%%%%%%%%%%%

if save:

    with open(path, 'wb') as fp:
        pickle.dump(ticker_dict, fp)

#%%%%%%%%%%%%%%%%
