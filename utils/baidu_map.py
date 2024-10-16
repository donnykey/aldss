#baidu_map.py
import requests
from config import BAIDU_MAP_AK

def search(city, region, keyword):
    url = 'http://api.map.baidu.com/place/v2/search'
    params = {
        'ak': BAIDU_MAP_AK,
        'output': 'json',
        'query': keyword,
        'region': region,
        'city': city,
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = []
    for item in data['results']:
        name = item['name']
        address = item['address']
        phone = item.get('telephone', '')
        result = {
            'name': name,
            'address': address,
            'phone': phone,
        }
        results.append(result)
    return results
