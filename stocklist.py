import requests
from bs4 import BeautifulSoup
import pprint


def req_rows():
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	stock_list = []
	for idx in range(0, 26):
		url = 'http://eoddata.com/stocklist/NYSE/{}.htm'.format(alphabet[idx])
		res = requests.get(url)
		soup = BeautifulSoup(res.text, 'html.parser')
		rows = soup.select('.ro, .re')
		for idx, item in enumerate(rows):
			code = rows[idx].select('td')[0].getText()
			name = rows[idx].select('td')[1].getText()
			high = float(rows[idx].select('td')[2].getText().replace(',', ''))
			low = float(rows[idx].select('td')[3].getText().replace(',', ''))
			close = float(rows[idx].select('td')[4].getText().replace(',', ''))
			volume = float(rows[idx].select('td')[5].getText().replace(',', ''))
			change = float(rows[idx].select('td')[6].getText().replace(',', ''))
			stock_list.append({'code': code, 'name': name, 'high': high, 'low':low, 'close':close, 'volume':volume, 'change':change})
	return stock_list

f = open("demofile3.txt", "w")
f.write(str(req_rows()))
f.close()
#pprint.pprint(req_rows())

#pprint.pprint(rows[0].select('td')[1].getText())
#pprint.pprint(pprint.pprint(rows[idx].select('td')[0].getText()))
