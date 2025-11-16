class sorceror:
    def __init__(self,name,Grade,eye ,Weakness,Techniques,DomainExpansion):
        self.name = name
        self.Grade = Grade
        self.eye = eye
        self.Weakness = Weakness
        self.Techniques = Techniques
        self.DomainExpansion = DomainExpansion

    def details(self):
        print(f"""
             ------------------------------------------------------------------------------------------------
              
              Hi This is confidential Code to know about Sorcerors
              I will provide the details about the Sorceror that you have mentioned.
              name :{self.name}
               Grade :{self.Grade}
              eye :{self.eye}  
              weakness :{self.Weakness}
              Techniques :{self.Techniques}
              DomainExpansion :{self.DomainExpansion}

             ------------------------------------------------------------------------------------------------   
                  """ )    

class Curse(sorceror):
    def __init__(self, name, Grade, eye, Weakness, Techniques, DomainExpansion):
        super().__init__(name, Grade, eye, Weakness, Techniques, DomainExpansion)

obj = Curse("geto","Special","brown","none","shadow","none") 
obj.details()                   