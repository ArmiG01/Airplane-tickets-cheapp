import requests

class FlightSearch:
    def __init__(self, fly_to, date_from, date_to, price_to):
        api = {
            "apikey": "xNit8VS6MQY00RC5duHB2FALDacWarq0"
        }
        pars = {
            "fly_from": "MOW",
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "price_to": price_to,
            "max_stopovers": 0
        }
        #This class is responsible for talking to the Flight Search API.
        self.onewway = requests.get("https://tequila-api.kiwi.com/v2/search", headers= api, params= pars).json()['data']


    def peresadki(self, fly_to, date_from, date_to, price_to):
        api = {
            "apikey": "xNit8VS6MQY00RC5duHB2FALDacWarq0"
        }
        pars = {
            "fly_from": "MOW",
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "price_to": price_to,
            "stopover_from": "1:00",
            "max_stopovers": 1
        }
        # This class is responsible for talking to the Flight Search API.
        self.peresadka = requests.get("https://tequila-api.kiwi.com/v2/search", headers=api, params=pars).json()['data']
