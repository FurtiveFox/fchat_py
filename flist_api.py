import requests
import json

from constants import AppInfo as A
from constants import FlistEndpoints as E




class FlistAPI:

    def __init__(self, account):

        self.account_name = account.account_name
        self.password = account.password
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': A.USERAGENT})

    def init_auth(self):
        """Authenticates with f-list web api to get full acount info"""
        payload = {'account': self.account_name, 'password': self.password, 'new_character_list': "true"}
        try:
            response = self.s.post(E.DOMAIN + E.GETAPITICKET, params=payload)
            response_dict = json.loads(response.text)
            self.acct_dict = response_dict
        except requests.exceptions.RequestException as e:
            print(e)

    def get_ticket(self):
        """Authenticates with f-list web api and requests minimal info"""
        payload = {'account': self.account_name, 'password': self.password, 'no_characters': 'true', 'no_friends': 'true', 'no_bookmarks': 'true'}
        response = self.s.post(E.DOMAIN + E.GETAPITICKET, params=payload)
        response_dict = json.loads(response.text)
        self.ticket = response_dict['ticket']
