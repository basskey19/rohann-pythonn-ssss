class animal:
    def make_sound(self):
        return "some animal sound"
    
class dog(animal):
    def make_sound(self):
        return "bark"
    
class cat(animal):
    def make_sound(self):
        return "meow" 


dog = dog()
print(dog.make_sound()) 
cat = cat()
print(cat.make_sound())                 