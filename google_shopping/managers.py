import os
from requests import request
from products import ProductManager
from product_statuses import ProductStatusManager
from google_shopping.oauth import OAuth


class GoogleShopping(object):

    BASE_CONTENT_API_URL = 'https://www.googleapis.com/content/v2'

    def __init__(self, merchant_id, country_code, **kwargs):
        self.merchant_id = merchant_id
        self.country_code = country_code
        self.max_results = kwargs.get('max_results', 200)
        self.oauth = OAuth(
            client_id=os.environ['GOOGLE_SHOPPING_CLIENT_ID'],
            client_secret=os.environ['GOOGLE_SHOPPING_CLIENT_SECRET'],
            refresh_token=os.environ['GOOGLE_SHOPPING_REFRESH_TOKEN'],
        )
        self.oauth.refresh_access_token()

        self.products = ProductManager(self)
        self.product_statuses = ProductStatusManager(self)

    def request(self, url, method='POST', *args, **kwargs):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.oauth.access_token
        }
        if 'headers' in kwargs:
            kwargs['headers'].update(headers)
        else:
            kwargs['headers'] = headers
        parse_json = kwargs.pop('json', True)
        response = request(method, url, *args, **kwargs)
        if parse_json:
            response = response.json()
        return response

