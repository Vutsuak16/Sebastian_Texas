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

title = soup.title.string.split(" ")[0:6]
t = ""
for i in range(len(title)):
    t += title[i] + " "

for i in soup.findAll("p",{"class":"update-time"}):
     if i.string is not None:
         print i.string

print t
#print author
# print date
# print content
# print videos
