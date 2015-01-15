#!/usr/bin/python
#
# Copyright (c) 2015 Davide Gessa <gessadavide@gmail.com>
import os
import sys
import urllib2 as ul2

f = open ('APIKEY', 'r')
API_KEY = f.read ().replace ('\n', '').replace ('\r', '')
f.close ()

DEST_DIR = "/var/www/data/bitcoinmap/btcde"
BASE_URL = 'https://bitcoinapi.de/v1/'+API_KEY+'/'
ENDS = [ 'trades.json', 'orderbook.json', 'rate.json' ]


for e in ENDS:
	data = ul2.urlopen (BASE_URL+e).read ()
	f = open (DEST_DIR+e, 'w')
	f.write (data)
	f.close ()
