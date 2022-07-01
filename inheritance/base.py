class Base:
    def __init__(self):
        print("Base Initializer")

    def f(self):
        print("Base.f()")

class Sub(Base):
    """ to override the initializer"""
    def __init__(self):
        super().__init__() # include init from base
        print("Sun initializer") # add behaivor
        
    
    """ to override the f method of base class"""
    def f(self):
        print ("Sub.f()")


# b = Base()

s = Sub()
s.f()


