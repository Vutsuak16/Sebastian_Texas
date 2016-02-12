__name__ = "vutsuak"

import urllib2
import BeautifulSoup as bs4

html = urllib2.urlopen('http://www.inc.com/business-insider/google-hardest-interview-questions.html')

soup = bs4.BeautifulSoup(html)
content = ""
author = ""

title = soup.title.string.split('|')[0]

for i in soup.findAll('a'):
    link = i.get('href')
    if link is not None:
        link = link.split('/')
        if "author" in link:
            author = link[-1]

for i in soup.findAll('h3'):
    content += str(i.string) + "\n"

# print title
print author
# print date
# print content
# print videos
