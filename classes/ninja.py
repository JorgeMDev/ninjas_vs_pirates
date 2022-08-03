class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print("Michaelangelo attacks!")
        return self

    def eat( self ):
        self.strength += 3
        print("Michaelangelo boost his strength with pizza")
        return self

class Captain_ninja(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.speed = 5

    def speed_attack(self, pirate):
        self.health -= 5
        pirate.health -= 10 * self.speed