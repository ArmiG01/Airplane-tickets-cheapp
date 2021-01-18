#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

dm = DataManager()
fs = FlightSearch
fd = FlightData()
if len(fd.alldata) != 0:
    for i in fd.alldata:
        for row in i.keys():
            key = row
            for j in dm.Users:
                nm = NotificationManager(adress=j['email'], name=j['firstname'], city=key, port=i[key][0], date=i[key][2], price=i[key][1])


else:
    for i in fd.peres():
        for row in i.keys():
            key = row
            for j in dm.Users:
                nm = NotificationManager(adress=j['email'], name=j['firstname'], city=key, port=i[key][0], date=i[key][2], price=i[key][1])
                nm.multiway(adress=j['email'], name=j['firstname'], city=key, port=i[key][0], date=i[key][2], price=i[key][1], peresadki=key[3])






