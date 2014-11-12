#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from item import Item

from urllib.request import urlopen
from bs4 import BeautifulSoup

# configuration
keyword = 'thinkpad'
url = 'http://m.kijiji.it/s-annunci/italia/{0}/c0-l0'.format(keyword)

#while True:

page = urlopen(url)
if page.status != 200:
    pass # continue, also need to wait, and notify after a number of failed attempts

content = BeautifulSoup(page)
items = content.find_all(attrs = {'class':'srp-item'})
item_catalog = list()

for item in items:
    item = Item(item)
    item_catalog.append(item)

for i in item_catalog:
    print(i)

