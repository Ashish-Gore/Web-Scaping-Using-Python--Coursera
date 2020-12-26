import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_1116166.xml'
uh = urllib.request.urlopen(serviceurl)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')

sum = 0

for count in counts:
    sum = sum + int(count.text)
    
print(sum)