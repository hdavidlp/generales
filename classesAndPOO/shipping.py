from pprint import pprint
from iso6346 import SerialsNumber


class ShippingContainer:
    # class atributes, shared with every instances
    
    HEIGHT_FT = 8.5
    WIDTH_FT  = 8.0
    
    next_serial = 1337

    @classmethod
    def _generete_serial(cls):
        result = cls.next_serial
        cls.next_serial+=1
        return result

    @classmethod
    def create_empty(cls, owner_code, lenght_ft, **kwargs):
        return cls(owner_code, lenght_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, lenght_ft, items, **kwargs):
        return cls(owner_code, lenght_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, lenght_ft, contents, **kwargs):
        self._owner_code = owner_code
        self._lenght_ft  = lenght_ft
        self._contents   = contents
        self._bic        = SerialsNumber._make_bic_code()

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32
    
    @staticmethod
    def _f_to_c(fahrenheight):
        return (fahrenheight - 32) * 5/9

    @property
    def volumne_ft3(self):
        return self._calc_volume()
        
    
    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self._lenght_ft
        


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUMNE_FT3 = 30

    def __init__(self, owner_code, lenght_ft, contents,*,celsius, **kwargs):
        super().__init__(owner_code, lenght_ft, contents, **kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError ("Temperature too hot!")
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    @property
    def _calc_volume(self):
        return (
            super()._calc_volume()
            - RefrigeratedShippingContainer.FRIDGE_VOLUMNE_FT3

        )
    @staticmethod
    def _make_bic_code():
        return SerialsNumber._make_bic_code()
        
    


# c1 = ShippingContainer("YML", ["books"])
# c2 = ShippingContainer("MAE", ["Clothes"])
# c8 = ShippingContainer.create_with_items("MAE", ["food","textiles"])
# r1 = RefrigeratedShippingContainer("MEA",["fish"], celsius=-18)
# print (f"Objetos {c8._bic} {c2._bic}")
# print (r1.celsius)
# r1.celsius = 2
# print (r1.celsius)

c = ShippingContainer.create_empty("YML", lenght_ft=20)
print(f"{c._owner_code}  {c.volumne_ft3}")

d = RefrigeratedShippingContainer.create_empty("LOW",lenght_ft=20, celsius=-10)
print(f"{d._owner_code}   {d.fahrenheit} ")


