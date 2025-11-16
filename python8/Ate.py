class freddyfazbear():
    def __init__(self,name):
        self.name = name
        print(f"{self.name} an animatronic has been activated")
    def movement(self):
        print(f"{self.name} He wants play a game with you...")

    def run(self):
       print(f"{self.name} is now running toward u ...")

    def __del__(self):
        print(f"{self.name} Wasted")

robot = freddyfazbear("Freddy")
robot.movement()
robot.run()


bonnie = freddyfazbear("Bonnie")
bonnie.movement()
bonnie.run()

del robot
del bonnie