import requests
import os
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')

def query_products():
    root = os.environ.get('apiroot',None)
    if root is None:
        root = config['api']['root']
    response = requests.get(f'{root}gdrive/products')
    products = json.loads(response.text)
    return products