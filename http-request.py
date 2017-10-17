import urllib.request, urllib.parse, urllib.error

import json

url = "https://maps.googleapis.com/maps/api/geocode/json?"

inp = input('enter the address of the user')

#sample address input
#address=1600+Amphitheatre+Parkway,+Mountain+View,+CA


# encode the url param 
finalUrl = url + urllib.parse.urlencode({"address":inp})
print(finalUrl)

# connect to the url
conn = urllib.request.urlopen(finalUrl)

#read the data/content after decoding 
data = conn.read().decode()

#parse the data/content as json
js = json.loads(data)


print(js["status"])

print(js["results"][0]['formatted_address'])