import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/comments_1116167.json'
uh = urllib.request.urlopen(serviceurl)

data = uh.read()
info = json.loads(data)
print('User count:', len(info))

sum = 0
for item in info['comments']:
    sum = sum + int(item['count'])
    
print(sum)