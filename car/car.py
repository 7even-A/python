class car:
    def __init__(self, Model, license, color, engine):
        self.Model = Model
        self.licsense = license
        self.color = color
        self.engine = engine

    def __str__(self):
        return f"I own a {self.color} {self.Model} with a {self.engine}, engine. My licsence plate is {self.licsense}"

    
    def Drive(self):
       print("Driving")
       
    def Reverse(self):
        print("Reversing")
    
    def Brake(self):
        print("Stopping the car...")

Car1 = car("Toyota","U8UDHW","red","Twin Turbo V8")
print(Car1)
print(Car1.Drive())
print(Car1.Reverse())
print(Car1.Brake())