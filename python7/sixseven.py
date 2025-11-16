class porche911:
    def __init__(self, color,speed,company, sales,):
        self.color = color
        self.speed = speed
        self.company = company
        self.sales = sales
        print("/nobject has been created")

    def start(self):
        print(f"{self.color} red is my color")   

    def stop(self):
         print(f"{self.speed} 100km/h svmmmm vrmmmmmm")  

    def details(self):
         print(f"{self.company} duh porche")        
    def salees(self):
        print(f"{self.sales}1million+ sold at first month")      
    def alldetails(self):
        print(f"the color is {self.color}and the speed of the car is{self.speed}then company of the car is{self.company}almost{self.sales}buy now at porche website")           

bmwObj = porche911("red","911","R7","1,0000000")
bmwObj.start()
bmwObj.stop()
bmwObj.details()
bmwObj.alldetails()
bmwObj.salees()