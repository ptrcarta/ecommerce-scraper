from kijiji import PageKijiji, ItemKijiji
from page import Container

def json_test():
    page = PageKijiji('thinkpad')
    cont = Container(page.output())
    fp = open('json_test', 'w')
    fp.write(cont.to_JSON())

def json_test_simp():
    page = PageKijiji('thinkpad')
    cont = Container(page.output())
    print(cont.to_JSON())
