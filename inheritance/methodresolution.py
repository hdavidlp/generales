class A:
    def func(self):
        return "A.func"

class B(A):
    def func(self):
        return "B.func"

class C(A):
    def func(self):
        return "C.func"

class D(B, C):
    pass


d = D()

# To check the Method Resoluthion Order
# print (D.__mro__)

print (d.func())




