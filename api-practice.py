import urllib.request as request
import urllib.parse
import requests as r

params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
print(params)

url = f"http://www.musi-cal.com/cgi-bin/query?{params}"
print(url)

response=request.urlopen(url)
print(response)