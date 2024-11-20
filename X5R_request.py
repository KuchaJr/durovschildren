import requests
import json


def req_api_5ka(name):
  search = requests.get(f"https://5d.5ka.ru/api/catalog/v2/stores/Y232/search?mode=delivery&q={name}&limit=24").json()
  product_id = search['products'][0]['plu']
  product_json = requests.get(f"https://5d.5ka.ru/api/catalog/v2/stores/Y232/products/{product_id}?mode=delivery&include_restrict=false").json()
  return product_json

product_name = 'шоколад milka'
product = req_api_5ka(product_name)

print(product['name'])
print(product['prices'][0]['value'])