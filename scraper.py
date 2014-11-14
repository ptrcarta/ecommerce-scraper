#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# specify search and platforms

#specify looping time

# annotate the scraping time
