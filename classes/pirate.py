class Pirate:

    total_points = 0

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        Pirate.total_points += self.strength

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print("Jack Sparrow attacks!")
        return self

    def drink( self ):
        self.health += 5
        print("Jack Sparrow sips some rum to recover his health")
        return self

    @classmethod
    def mortal_attack(cls, ninja):
        ninja.health -= cls.total_points * 3
        cls.total_points = 0
        print("MORTAL ATTACK!")