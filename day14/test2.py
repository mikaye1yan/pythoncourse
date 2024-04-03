class FootballPlayer:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_age(self):
        return "{} is age {}".format(self.name, self.age)
    def get_height(self):
        return "{} is {}cm".format(self.name, self.height)
    def get_weight(self):
        return "{} weighs {}kg".format(self.name, self.weight)
p1 =FootballPlayer("David Jones", 25, 175, 75)
print(p1.get_age())    
print(p1.get_height()) 
print(p1.get_weight())