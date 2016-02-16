__name__ = "vutsuak"

import urllib2
import BeautifulSoup as bs4

site = "http://bit.ly/1TVjbrf"
p = urllib2.urlopen(site)
html = p.read().decode('euc-kr')  # encoding specified
soup = bs4.BeautifulSoup(html)
content = ""
author = ""
date = ""
title = ""
l = []

title = soup.title.string

for i in soup.findAll('span', {'class': 't11'}):
    date = i.string
    break

for i in soup.findAll('div',{'id':'articleBodyContents'}):
    print ''.join(i.findAll(text=True))