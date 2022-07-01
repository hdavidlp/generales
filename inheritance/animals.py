class Animal:
    @classmethod
    def description(cls):
        return "Animal"

class Bird (Animal):
    @classmethod
    def description(cls):
        return super().description() + " with wings"

class Flamingo(Bird):
    @classmethod
    def description(cls):
        return super().description() + " and fabulos pink feathers"

print (Animal.description())
print (Bird.description())
print (Flamingo.description())  