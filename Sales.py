__author__ = 'Kathryn'

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.smartpakequine.com/sale--view-all-equine-542pc?ck=m'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class':'imageLink'}):
            href = link.get('href')
            print(href)
        page += 1

trade_spider(1)