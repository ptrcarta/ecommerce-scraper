from kijiji import PageKijiji, ItemKijiji
from page import Container

def json_test():
    page = PageKijiji('auto')
    cont = Container(page.output())
    fp = open('json_test', 'w')
    fp.write(cont.to_JSON())

def json_test_simp():
    page = PageKijiji('thinkpad')
    cont = Container(page.output())
    print(cont.to_JSON())

from optparse import OptionParser
import sys

def parser_test():
    parser = OptionParser(usage="Usage: %prog -s\'search term\' -p\'platform\'")
    parser.add_option("-s", "--search", action="append", dest="search",
                    help="The keyword you want to search for")
    parser.add_option("-p", "--platform", action="append", dest="platform",
                    help="The platform that will be searched. must be the name of"
                    " a plugin module (example: for kijiji.py write kijiji)")
    parser.set_defaults(platform=['kijiji'])

    (option, args) = parser.parse_args(['-s', 'thinkpad', '-p',
        'kijiji', 'thinkpad'])
    if option.search == None:
        sys.stderr.write('You need to specify at least one search term')
        exit(code=1)
    print(option)
    print(args)

