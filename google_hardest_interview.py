__name__ = "vutsuak"

import urllib2
import BeautifulSoup as bs4

html = urllib2.urlopen('http://www.inc.com/business-insider/google-hardest-interview-questions.html')

soup = bs4.BeautifulSoup(html)
content = ""
author = ""
date = ""

title = soup.title.string.split('|')[0]

for i in soup.findAll('a'):
    link = i.get('href')
    if link is not None:
        link = link.split('/')
        if "author" in link:
            author = link[-1]

for i in soup.findAll('h3'):
    content += str(i.string) + "\n"
for i in soup.findAll('span'):
    if i.string is not None:
        k = i.string.split(" ")
        if "Published" in k:
            date = i.string

print title
print author
print date
# print content
# print videos  , videos link wasnt there in the site
