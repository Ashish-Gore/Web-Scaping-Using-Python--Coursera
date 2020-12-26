from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

repeat = 7
position = 18
url = 'http://py4e-data.dr-chuck.net/known_by_Shayne.html'

while repeat > 0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')

    url=tags[position - 1].get('href', None)
    repeat = repeat - 1
    print(url);

print(re.findall('by_(.*).html', url))