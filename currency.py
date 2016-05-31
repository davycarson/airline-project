__author__ = "David Carson - C09441131"

#Currency File

import csv, os

class Currency:

    currency_file = "csv/currencyrates.csv"

#initializing the class object
    def __init__(self, currencyName, currencyCode, rateToEuro):
        self.name = currencyName
        self.code = currencyCode
        self.rate = rateToEuro

    currencyDict = {}
#method to get the currency rate in euros
    def getEuroRate(self, rateToEuro):
        try:
            return self.currencyDict[float(rateToEuro)]
        except KeyError:
            return None

#method to get the currencies from the csv file
    def createCurrency(self, currency_file):
        currencyDict = {}
        with open(os.path.join(currency_file), "rt", encoding="utf8") as f:
            csvfilelines = csv.reader(f)
            for row in csvfilelines:
                try:
                    currencyDict[row[1]] = Currency(row[0],row[1], row[2])
                except KeyError:
                    return currencyDict

#method to calculate the rate of the currency to euro, getting code from currency dictionary
    def calculateRate(self, currencyCode, rateToEuro):
        currencyDict = {}
        conversion = float(currencyDict.get(currencyCode).rateToEuro)
        return conversion

    print(currencyDict)


def main():
    currencyrates = Currency()
    print (currencyrates.getCurrency())
    print (currencyrates.getEuroRate())

if __name__ == "__main__":
    main()
