#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from item import Item

from urllib.request import urlopen
from bs4 import BeautifulSoup

# configuration
keyword = 'thinkpad'

url = {'kijiji_mobile':'http://m.kijiji.it/s-annunci/italia/{0}/c0-l0',
        'ebay-annunci':'http://annunci.ebay.it/elettronica/computer-e-software'
        '/{0}/?entry_point=sb',
        }

items_attributes = {'kijiji_mobile':{'class':'srp-item'},
                    'ebay-annunci':{'class':'search-results-list-item'}} #this is for the k site. other formats need different attributes

items_sanitize_attributes = {'kijiji_mobile':{'class':''},
                            'ebay-annunci':{'class':['is-urgent-ad','is-topad-list-item']}} 


page = urlopen(url)
if page.status != 200:
    pass # continue, also need to wait, and notify after a number of failed attempts

content = BeautifulSoup(page)
items = content.find_all(attrs = items_attributes['ebay-annunci'])

sanitize_items(items, 
item_catalog = list()
for item in items:
    item = Item(item)
    item_catalog.append(item)

for i in item_catalog:
    print(i)
