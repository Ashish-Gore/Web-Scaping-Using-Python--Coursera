
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0
tags = soup('span', {'class': 'comments'})
for tag in tags:
    count = count + 1
    total = total + int(tag.contents[0])
    
print("Count: ", count)
print("Sum:   ", total)