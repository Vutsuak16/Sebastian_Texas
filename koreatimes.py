__name__ = "vutsuak"

import urllib2
import BeautifulSoup as bs4

html = urllib2.urlopen('http://www.koreatimes.co.kr/www/news/nation/2016/02/116_197716.html')
soup = bs4.BeautifulSoup(html)
content = ""
author = ""
date = ""
l=[]
title = soup.title.string.split('|')[0]

for i in soup.findAll('div', {'id': 'startts'}):
    content += str(i.string) + "\n"
ct = 0
for i in soup.findAll('span'):
    if i.string is not None:
        ct += 1
        if ct > 3:
            content += str(i.string) + "\n"
        if "Posted" in i.string.split(" "):
            date = i.string

for node in soup.findAll('span'):
        l.append(''.join(node.findAll(text=True)))

author= l[4]
print title
print author
print date
print content
# print videos
