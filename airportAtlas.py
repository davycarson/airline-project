__author__ = "David Carson - C09441131"

#AirportAtlas File

import csv, os
from math import cos, sin, acos, pi, radians, asin, sqrt
from Airport import Airport

class AirportAtlas:

#initializing the AirportAtlas
    def __init__(self, airport_file):
        self.airportDict = self.loadAirportDict(airport_file)

#creating and airport dictionary using the csvfile airport.csv
    def loadAirportDict(self, airport_file):
        airportDict = {}
        with open (os.path.join(airport_file), "rt", encoding="utf8") as f:
            csvlines = csv.reader(f)
            for row in csvlines:
                try:
                    airportDict[row[4]]= Airport(row[4], row[1], row[3], row[2], float(row[6]), float(row[7]))
                except KeyError:

                    return airportDict

#getting the two airport codes, and getting the latitude and longitude values from there place in the csv file
    def getAirportCodes(self, code1, code2):
        airportDict = {}

        if code1 in airportDict:
            lat1 = float(airportDict[code1][6])
            long1 = float(airportDict[code1][7])

        if code2 in airportDict:
            lat2 = float(airportDict[code2][6])
            long2 = float(airportDict[code2][7])

#Harvesine formula for calculating the distances bewteeen two points on the earth
    def greatCircleDistance(self, lat1, long1, lat2, long2):
        earth_radius = 6371
        south1 = long1 * (2*(pi)/360)
        south2 = long2 * (2*(pi)/360)
        north1 = 90 - (lat1 * (2*(pi)/360))
        north2 = 90 - (lat2 * (2*(pi)/360))


        distance = acos((sin(north1))*(sin(north2))*(cos(south1 - south2)) + (cos(north1))*(cos(north2))) * earth_radius
        print("The distance between your airports is : {}".format(distance))
        return (distance)

#main to call the methods
def main():
    distance = AirportAtlas
    print(distance.getAirport())

if __name__ == "__main__":
    main()
