import urllib.request
import json

nasa_api_key = 'sjptH8YZDCd4bdiuckx5tBH2z3KfERWqGLUffcGB'
api_url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={nasa_api_key}'


def use_urllib(api_url):

    request = urllib.request.Request(api_url)
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
        print(len(data.get('photos')))


use_urllib(api_url)
