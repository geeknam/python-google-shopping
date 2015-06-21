import os
import requests

OAUTH_URL_GOOGLE = "https://accounts.google.com/o/oauth2/token"


class OAuth(object):

    def __init__(self, client_id, client_secret, refresh_token, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = os.getenv('GOOGLE_SHOPPING_ACCESS_TOKEN', None)

    def refresh_access_token(self):
        """
        Makes POST request to Google Auth endpoint to get
        the access token
        """
        response = requests.post(OAUTH_URL_GOOGLE, data={
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token"
        }).json()

        access_token = response['access_token']
        os.environ['GOOGLE_SHOPPING_ACCESS_TOKEN'] = access_token
        self.access_token = access_token
        return access_token

