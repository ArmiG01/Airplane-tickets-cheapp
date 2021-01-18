import requests
from datetime import datetime
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.time_do = datetime.now().strftime("%d/%m/%Y")
        month = int(datetime.now().strftime("%m")) + 6
        self.time_posle = datetime.now().strftime(f"%d/{month}/%Y")
        req = requests.get("https://api.sheety.co/c101e25ceed48ea2aa230e468634aaf1/cities/лист1")
        self.Cities = req.json()['лист1']
        self.Codes_Prices = {i['iataCode']: i['lowestPrice'] for i in self.Cities}
        users = requests.get("https://api.sheety.co/c101e25ceed48ea2aa230e468634aaf1/users/лист1")
        self.Users = users.json()['лист1']