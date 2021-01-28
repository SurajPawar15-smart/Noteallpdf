# -*- coding: utf-8 -*-


import urllib.request

req=urllib.request.Request('https://pythonprogramming.net/',headers={'User-Agent':'Mozilla/5.0'})

resp=urllib.request.urlopen(req)

print(resp.read())

import urllib.parse

url="https://pythonprogramming.net/"

values={'q':'python'}

data=urllib.parse.urlencode(values)

data=data.encode('utf-8')

req=urllib.request.Request(url,data=data)

resp=urllib.request.urlopen(req)

