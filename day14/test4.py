class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates
    def taste(self, food):
        response = f"{self.name} eats the {food}"
        if food in self.likes:
            response += " and loves it!"
        elif food in self.hates:
            response += " and hates it!"
        else:
            response += "!"
        return response
p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))  
print(p1.taste("cheese")) 
print(p1.taste("carrots"))  