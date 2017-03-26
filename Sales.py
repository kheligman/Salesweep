__author__ = 'Kathryn'

import requests
from bs4 import BeautifulSoup
from dominate.tags import *
from Item import Item

keyword = 'Girth'
list = []
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:

        #SmartPak
        url = 'https://www.smartpakequine.com/search/Searcha?parameters=%2Fall%2F0%2Fbrowse%2F1%2Fi%2F1%2Fisvip%2F1%2Fpc%2F542%2Fsegment%2Fproduct%2Fsort%2Fbest_sellers'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div',{'class':'product-name'}):
            for link2 in link.findAll('a'):
                name = link2.getText()
                href = link2.get('href')

                if keyword in name:
                    item = Item(name, href)
                    #item = Item.make_item(name,href)
                    list.append(item)
        page += 1

        #Dover
        page = 1
        url = 'http://www.doversaddlery.com/Category.aspx?c=8000&pgsize=all&pgnum=1'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div',{'class':'product-single'}):
            for link2 in link.findAll('div',{'class':'name'}):
                for link3 in link2.findAll('a'):
                    name = link2.getText()
                    href = link3.get('href')

                    if keyword in name:
                        item = Item(name, href)
                        #item = Item.make_item(name,href)
                        list.append(item)
        page += 1


       # print(html(body(h1('Hello, World!'))))

def make_html():
    for item in list:
        print(item)


trade_spider(1)
make_html()