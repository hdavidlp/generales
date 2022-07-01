class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError (f"Latitude {latitude} out of range")
        
        if not (-180 <= longitude <= +180):
            raise ValueError (f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude
    
    @property
    def latitude (self):
        return self._latitude

    @property
    def longitude (self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >=0 else "S"
    
    @property
    def longitud_hemisphere(self):
        return "E" if self.longitude >=0 else "W"



    def __repr__(self):
        """ repr is for the developers
        for good result, follow this conventions
        - include necesary states
        - tecnical implementation
        """
        return f"{typename(self)} (latitude:{self.latitude}, longitud:{self.longitude})"

    def __str__(self):
        """ str for all """
        return (
            f"{abs(self.latitude)}° {self.latitude_hemisphere}, "
            f"{abs(self.longitude)}° {self.longitud_hemisphere}"
        )
    
    def __format__(self, format_spec):
        """ Is for f"XXXX {obj}  """
        componenet_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int (suffix)
            componenet_format_spec = f".{num_decimal_places}f"



        latitude = format(abs(self.latitude), componenet_format_spec)
        longitude = format(abs(self.longitude), componenet_format_spec) 

        return (
            f"{latitude}° {self.latitude_hemisphere}, "
            f"{longitude}° {self.longitud_hemisphere}"
        )

def typename(self):
    return type(self).__name__

class EarthPosition(Position):
    pass

class MarsPosition(Position):
    pass


# mauna_ka = EarthPosition(19.82, -155.47)
# print(mauna_ka)

# Erebus = EarthPosition(-77.5, 167.2)
# print (str(Erebus))
# print (f"{Erebus:.2}")

Everest = EarthPosition(27.988056, 86.925278)
print ("Using repr for developers : ",repr(Everest))
print (f"Using repr implicit       : {Everest!r}")
print ("Using str for All         : ",str(Everest))
print (f"Using str for All         : {Everest!s}")
print (f"Using implicit for f print: {Everest}")
print (f"More flexible             : {Everest:.3}")






        