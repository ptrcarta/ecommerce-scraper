#! /usr/bin/env python3

from optparse import OptionParser
import sys

parser = OptionParser(usage="Usage: %prog -s\'search term\' -p\'platform\'")

parser.add_option("-s", "--search", action="append", dest="search",
                help="The keyword you want to search for")
parser.add_option("-p", "--platform", action="append", dest="platform",
                help="The platform that will be searched. must be the name of"
                " a plugin module (example: for kijiji.py write kijiji)")
parser.add_option("-l", "--location", action="append", dest="location",
                help="The geographical location for the item "
                "//not yet implemented//")

(option, args) = parser.parse_args()

if option.search == None:
    sys.stderr.write('You need to specify at least a search term\n')
    exit(code=1)
if option.platform == None:
    sys.stderr.write('You need to specify at least a search term\n')
    exit(code=1)

### Plugin Loading System ###

import importlib 
for module in option.platform:
    module = 'pl.' + module
    try:
        modules = {module:importlib.import_module(module.lower())}
    except ImportError:
        sys.stderr.write('Could not import module {0}\n'.format(module))
        exit(code=1)


searchers = []
for search in option.search:
    for platform in option.platform:
        searchers.append(getattr(modules['pl.'+platform.lower()],
                        'Page' + platform.capitalize())(search))

### Main loop ###
from pl.page import Container
from time import sleep

while True:
    cont = Container(option.search[0])
    i = 0
    for search in searchers:
        i += cont.add(search.get())
    print(i)
    sleep(60)
