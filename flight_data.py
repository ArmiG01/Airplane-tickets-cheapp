from data_manager import DataManager
from flight_search import FlightSearch

class FlightData:
    def __init__(self):
        self.alldata = []
        dm = DataManager()
        for city in dm.Codes_Prices:
            fs = FlightSearch(city, dm.time_do, dm.time_posle, dm.Codes_Prices[city])
            data = {i['cityTo']: [i['flyFrom'], i['price'], i['local_departure'].split('T')[0]]
                         for i in fs.onewway}
            self.alldata.append(data)

            for i in self.alldata:
                if i == {}:
                    self.alldata.remove(i)
            print(self.alldata)
    def peres(self):
        self.alldata = []
        dm = DataManager()
        for city in dm.Codes_Prices:
            if len(self.alldata) == 0:
                fs = FlightSearch(city, dm.time_do, dm.time_posle, dm.Codes_Prices[city])
                fs.peresadki(city, dm.time_do, dm.time_posle, dm.Codes_Prices[city])
                data = {i['cityTo']: [i['flyFrom'], i['price'], i['local_departure'].split('T')[0], i['routes']]
                        for i in fs.peresadka if i['cityTo'] not in data.keys()}
                self.alldata.append(data)

                for i in self.alldata:
                    if i == {}:
                        self.alldata.remove(i)
                print(self.alldata)
        return self.alldata
