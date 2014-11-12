import json
import re

class Item:
    "container class for ebay item."
    def __init__(self, bsitem):
        "bsitem is div with class=srp-item" # This werks because beautifulsoup has been imported in the main file
        self._bsitem = bsitem
        self.parse_item()

    @property
    def price(self):
        return re.sub('[^0-9]+.*', '', self._price)

    @property
    def link(self): 
        return "http://ecommercewebsite.it/annunci/" + re.sub('/s-annuncio/', '', self._link)

    def to_JSON(self):
        return json.dumps({'price':self.price, 'title':self._title, 'link':self.link, 'image':self._image}, indent=4)

    def __str__(self):
        return self.to_JSON()

    def parse_item(self):
        "Parse html and puts resulting items in a list of Item objects" 
        try:
            self._title = self._bsitem.find(attrs = {'class':'srp-item-title'}).string
        except Exception:
            self._title = 'NA'
        try:
            self._price = self._bsitem.find(attrs = {'class':'srp-item-price'}).string # This one has to be sanitized (convert to int or NaN if no price listed
        except Exception:
            self._price = 'NA'
        try:
            self._image = self._bsitem.find(attrs = {'class':'srp-imagebox'})['data-imgsrc'] # This one as to be converted in the non thumbnail one
        except KeyError:
            self._image = 'NA'
        try:
            self._link = self._bsitem.find(attrs = {'class':'srp-item-link'})['href'] # Has to be prepended with domain name
        except KeyError:
            self._link = 'NA'


