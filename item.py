class Item:
    "container class for an item."

    def __init__(self, bsitem):
        #sublcass type ?
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
       
