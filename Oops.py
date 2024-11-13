class DemoClass:
    a = 10
    b = 40
    def sum(self):
        print(10+40)

demoobject = DemoClass()
demoobject1 = DemoClass()
print(demoobject.a)
print(demoobject1.b)
demoobject.sum();

class car:
    def __init__(self,brand,name,color):
        self.brand = brand
        self.name = name
        self.color = color
        self.carspecs = "Brand Name = " + brand + "\nModel Name = " + name + "\nColor = " + color

car1 = car("Koienseing","Ghost 1","Black")
print(car1.carspecs)


