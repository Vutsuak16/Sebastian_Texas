__name__ = "vutsuak"

import urllib2
import BeautifulSoup as bs4



site = "http://nyti.ms/1QYHX77"
hdr = {'User-Agent': 'Mozilla/5.0'}
p = urllib2.build_opener(urllib2.HTTPCookieProcessor).open(site)
soup = bs4.BeautifulSoup(p)
content = ""
author = ""
date = ""
title=""
t = soup.title.string.split('|')[0]
for i in t:
    if i=="-":
        break
    title+=i
print title

