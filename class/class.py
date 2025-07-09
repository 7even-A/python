class dog:
    def __init__(self, breed, age, name):
        self.breed = breed
        self.name = name
        self.age = age
    

    def __str__(self):
        return f"I have a {self.age} year old {self.breed} whose name is  {self.name}"
  
       


class cat:
    def __init__(self, breed, age, name):
        self.breed = breed
        self.name = name
        self.age = age
    

    def __str__(self):
        return f"I have a {self.age} year old {self.breed} whose name is {self.name}"
       




dog1 = dog("bulldawg", 5, "hawk")
print(dog1.age)
print(dog1.name)
print(dog1.breed)

cat1 = cat("cupcake", 7, "whiskers")
print(cat1)
print(cat1.breed)