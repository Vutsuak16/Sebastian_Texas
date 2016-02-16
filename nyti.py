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
title = ""
l = []
t = soup.title.string.split('|')[0]
for i in t:
    if i == "-":
        break
    title += i

for i in soup.findAll("time"):
    date = i.string
    break

for node in soup.findAll('p'):
    l.append(''.join(node.findAll(text=True)))

author = l[2][0:16]

for i in soup.findAll('p', {'class': 'story-body-text story-content'}):
    if i.string is not None:
        content += i.string + "\n"
print title
print date
print author
print content
