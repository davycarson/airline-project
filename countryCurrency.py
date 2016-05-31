__author__ = "David Carson - C09441131"

#Country Currency
import csv, os

class CountryCurrency:

    country_currency_file = "csv/countrycurrency.csv"

#initializing the countryCurrency class
    def __init__(self, countryName, currencyCode, currencyName):
        self.countryName = countryName
        self.currencyCode = currencyCode
        self.currencyName = currencyName

#getting the country currency dictionary
    def getCountryCurrencyDict(self, country_currency_file):
        countryCurrencyDict = {}
        with open(os.path.join(country_currency_file), "rt", encoding="utf8") as f:
            csvfilelines = csv.reader(f)
            for row in csvfilelines:
                countryCurrencyDict[row[0]] = CountryCurrency(row[0], row[14],row[17])
        return countryCurrencyDict

#method to get the country name from the file
    def getCountryName(self, countryCurrencyDict):
        try:
            return self.countryCurrencyDict[0]
        except KeyError:
            return None

#method to get the currency name from the file
    def getCurrencyName(self, countryCurrencyDict):
        try:
            return self.countryCurrencyDict[17]
        except KeyError:
            return None


def main():
    currencyCountry = CountryCurrency

if __name__ == '__main__':
    main()
