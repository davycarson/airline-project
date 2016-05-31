__author__ = "David Carson - C09441131"

#Aircraft File

#creating a class for all airplanes types, the aircraft type and range which is the same as its max fuel are given
class AirCraft:
    rangeDict = {"A319": 3750,
                "A320": 12000,
                "A321":12000,
                "A330":13430,
                "737":5600,
                "747":9800,
                "757":7222,
                "767":7130,
                "777":9700,
                "BAE146":2909,
                "DC8":4800,
                "F50":2055,
                "MD11":12670,
                "A400M":3298,
                "C212":1811,
                "V22":1622}

    def __init__(self, aircraft_type = "", range = "", minFuel = "500"):
        self.aircraftType = aircraft_type
        self.range = range
        self.minFuel = minFuel

        if aircraft_type in rangeDict:
            print ("Aircraft is on list")





