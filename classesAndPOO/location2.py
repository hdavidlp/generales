from dataclasses import dataclass
from position import  EarthPosition
from locations import Location

@dataclass
class Location:
    name : str
    position : Location


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(57.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))