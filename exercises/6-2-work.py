import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

uh = urllib.request.urlopen(serviceurl)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

universities = json.loads(data)
print('Number of Universities: ' + str(len(universities)))

for uni in universities:
    print('Fetching for ' + uni)
    url = serviceurl + urllib.parse.urlencode(
        { 'address': uni })

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    uni_data = json.loads(data)

    address = uni_data['results'][0]['formatted_address']
    place_id = uni_data["results"][0]['place_id']

    if 'ChIJA' in place_id:
        print('\nAddress: ' + address)
        print('Place Id: ' + place_id)




while False:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)