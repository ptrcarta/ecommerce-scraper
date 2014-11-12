import json

class Item:
    "container class for ebay item."
    def __init__(self, bsitem):
        "bsitem is div with class=srp-item"
        self._bsitem = bsitem
        self.parse_item()

    def to_JSON(self):
        args= dict()
        args.update({'price':self._price, 'title':self._title, 'link':self._link, 'image':self._image})
        return json.dumps(args, indent=4)

    def __str__(self):
        return self.to_JSON()

    def parse_item(self):
        "Parse html and puts resulting items in a list of Item objects"
        try:
            self._title = self._bsitem.find(attrs = {'class':'srp-item-title'}).string
        except:
            self._title = 'NA'
        try:
            self._price = self._bsitem.find(attrs = {'class':'srp-item-price'}).string # This one has to be sanitized (convert to int or NaN if no price listed
        except:
            self._price = 'NA'
        try:
            self._image = self._bsitem.find(attrs = {'class':'srp-imagebox'})['data-imgsrc'] # This one as to be converted in the non thumbnail one
        except KeyError:
            self._image = 'NA'
        try:
            self._link = self._bsitem.find(attrs = {'class':'srp-item-link'})['href'] # Has to be prepended with domain name
        except KeyError:
            self._link = 'NA'


