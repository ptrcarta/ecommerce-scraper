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
        if len(delitems) != 0:
            raise Exception('Could not sanitize the page completely')

    def output(self):
        items = self._content.find_all(attrs = self._items_attributes)
        return items
