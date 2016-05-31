__author__ = "David Carson - C09441131"

#Airport Class

import csv, os
#creating an airport class to hold all the inforamtion about the airports
class Airport:

    def __init__(self, airport_name, city_name, country_name, code, lat,
                 long):
        self.AirportName = airport_name
        self.CityName = city_name
        self.Country = country_name
        self.code = code
        self.Latitude = lat
        self.Longitude = long

#creating an __str__ to give descriptive output of the airport data
    def __str__(self):
        airport = ""
        return "(Airport Name: {}, City Name: {}, Country: {}, IATO Code: {}, Latitude: {}, Longitude: {})".format(
        self.AirportName, self.CityName, self.Country, self.code, self.Latitude, self.Longitude)

#making an airport dictinary from the csv file
    def loadAirportDict(self, airport_file):
        airports = {}
        with open (os.path.join(airport_file), "rt", encoding="utf8") as f:
            csvlines = csv.reader(f)
            for row in csvlines:
                try:
                    airports[row[4]]= Airport(row[4], row[1], row[3], row[2], row[6], row[7])
                except KeyError:

                    return airports
