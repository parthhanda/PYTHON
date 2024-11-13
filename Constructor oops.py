class person:
    name = "Parth"
    srname = "Handa"
    def __init__(self): #this is an constructor
        print(f"{self.name} {self.srname} is a good person.")

a = person()
print("first name is ->" + " " + a.name)
print(f"surname is ->" + " " + a.srname)
b = person() # A constructor is automatically called when an object is made.
