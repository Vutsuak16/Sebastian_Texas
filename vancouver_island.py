__name__ = "vutsuak"

import urllib2
import BeautifulSoup as bs4

site = "http://www.cnn.com/2016/02/10/world/vancouver-island-human-foot/index.html"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site, headers=hdr)
page = urllib2.urlopen(req)
html = urllib2.urlopen(site)
soup = bs4.BeautifulSoup(html)
content = ""
author = ""
date = ""

t = soup.title.string.split(" ")[0:6]
title = ""
for i in range(len(t)):
    title += t[i] + " "
l = []
for node in soup.findAll('p'):
    l.append(''.join(node.findAll(text=True)))

for i in range(7, len(l)):
    content += l[i] + "\n"
author = l[3]
date = l[5]
print title
print author
print date
print content
# print videos
