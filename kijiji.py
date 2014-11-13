from item import Item
from page import Page

import json
import re

class ItemKijiji(Item):
    "container class for a kijiji item."

    @property
    def title(self):
        "Name of the article"
        return self._title

    @property
    def price(self):
        return re.sub('[^0-9]+.*', '', self._price)

    @property
    def link(self): 
        return "http://kijiji.it/annunci/" + \
        re.sub('/s-annuncio/', '', self._link)

    def to_JSON(self):
        return json.dumps({'price':self.price, 'title':self._title,
        'link':self.link, 'image':self._image}, indent=4)

    def parse_item(self):
        "Parse html and puts resulting items in a list of Item objects" 
        try:
            self._title = self._bsitem.find(attrs = 
            {'class':'srp-item-title'}).string
        except Exception:
            self._title = 'NA'

        try:
            self._price = self._bsitem.find(attrs = 
            {'class':'srp-item-price'}).string 
        except Exception:
            self._price = 'NA'

        try:
            # This one has to be converted in the non thumbnail one
            self._image = self._bsitem.find(attrs = 
            {'class':'srp-imagebox'})['data-imgsrc'] 
        except KeyError:
            self._image = None

        try:
            # Has to be tested
            self._link = self._bsitem.find(attrs = 
            {'class':'srp-item-link'})['href'] 
        except KeyError:
            self._link = None


class PageKijiji(Page):

    _items_attributes = {'class':'srp-item'}
    _url = 'http://m.kijiji.it/s-annunci/italia/{0}/c0-l0'


