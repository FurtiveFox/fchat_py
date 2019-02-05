import requests
import json
import urllib
import urllib.request
import urllib.parse

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
            response = self.s.post(E.DOMAIN + E.GETAPITICKET, data=payload)
            print(response.url)
            response_dict = json.loads(response.text)
            self.acct_dict = response_dict
        except requests.exceptions.RequestException as e:
            print(e)

    def get_ticket(self):
        """Authenticates with f-list web api and requests minimal info"""
        payload = {'account': self.account_name, 'password': self.password, 'no_characters': 'true', 'no_friends': 'true', 'no_bookmarks': 'true'}
        response = self.s.post(E.DOMAIN + E.GETAPITICKET, data=payload)
        print(response.url)
        response_dict = json.loads(response.text)
        self.ticket = response_dict['ticket']

    def get_mapping_data(self):

        payload = {}
        response = self.s.post(E.DOMAIN + E.MAPPINGLIST, data=payload)
        response_dict = json.loads(response.text)
        return response_dict

    def get_character_data(self, character):
        payload = {'account': self.account_name, 'ticket': self.ticket, 'name': character}
        response = requests.post(E.DOMAIN + E.CHARACTERDATA, data=payload)
        print(response.url)
        response_dict = json.loads(response.text)
        return response_dict

    def get_character_friends(self, character):
        payload = {'account': self.account_name, 'ticket': self.ticket, 'name': character}
        body = {'name': character}
        response = requests.post(E.DOMAIN + E.CHARACTERFRIENDS, data=payload)
        print(response.url)
        response_dict = json.loads(response.text)
        return response_dict
