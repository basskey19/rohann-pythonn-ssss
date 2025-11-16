class super:
    def __init__(self,heroes,villans):
        self.heroes = heroes
        self.villans = villans
        print("heroes and villans got affected by cosmic rays")
    def details(self):
        print(f"the superhero name is {self.heroes} and his arch-nemisis is {self.villans}")

    def changevillan(self,newvillan):
        self.villans = newvillan

Robj = super("mrfantastic","galactus")
Robj.details()
Robj.changevillan("Doctor doom")
Robj.details()        