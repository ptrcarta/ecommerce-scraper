from bs4 import BeautifulSoup
from urllib.request import urlopen #revise to change User-Agent

class Page:

    _sanitize_attributes = {'None':'None'}
    _items_attributes = dict()
    _url = 'url'

    def __init__(self, search_term, location=''):
        self._search = search_term
        self._location = location
        self._url = self._url.format(self._search)
        self.fetch_page()
        self.sanitize()

    def fetch_page(self):
        page = urlopen(self._url)
        if page.status != 200:
            raise Exception # we'll see later
        self._content = BeautifulSoup(page)

    def sanitize(self):
        delitems = self._content.find_all(attrs = self._sanitize_attributes)
        for i in delitems:
            i.extract()
        delitems = self._content.find_all(attrs = self._sanitize_attributes)
        if len(delitems) != 0:
            raise Exception('Could not sanitize the page completely')

    def output(self):
        items = self._content.find_all(attrs = self._items_attributes)
        return items

    def get(self):
        self.fetch_page()
        self.sanitize()
        return self.output()


import time

class Item:
    "container class for an item."

    def __init__(self, bsitem):
        self._scrape_time = time.time()
        self._bsitem = bsitem
        self.parse_item()

    @property
    def title(self):
        "Name of the article"
        pass

    @property
    def price(self):
        "Price of the thing"
        pass
    
    @property
    def link(self): 
        "link to the page with the article"
        pass

    @property
    def image(self): 
        "Image that goes with other info"
        pass

    def to_JSON(self):
        pass

    def __str__(self):
        return self.to_JSON()

    def parse_item(self):
        "Turns the beautifulsoup into semantic data"
        pass

import json

class Container():
    def __init__(self, list):
        self._list = list

    def to_JSON(self):
        json_string = '{\n'
        for num in range(len(self._list)):
            json_string += '"Item_{0}": '.format(num)
            json_string += self._list[num].to_JSON()
            if num != len(self._list) - 1:
                json_string += ',\n'
        json_string += '\n}' 
        return json_string

    def add(self, list):
        "adds the items to the container and checks for dupes"
        for i in range(len(self._list)): # The following lines remove dupes
            j = len(list) - 1
            while j >= 0:
                if self._list[i].link == list[j].link:
                    del list[j]
                    break
                j -= 1
        length = len(list)
        self._list = list + self._list
        return length
