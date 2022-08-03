from argparse import ONE_OR_MORE
from classes.ninja import Ninja
from classes.ninja import Captain_ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelangelo")

raphael = Captain_ninja("Raphael")

jack_sparrow = Pirate("Jack Sparrow")

print("Welcome to Pirates VS Ninjas")
print("Which character would you like to be? \n >")

choice = input("1) Pirate 2) Ninja 3) Capitain Ninja\n >")
if (choice == "1"):
    print("You are Jack Sparrow")
if (choice == "2"):
    print("You are Michelangelo")
if (choice == "3"):
    print("You are Raphael")

while jack_sparrow.health > 0 and michelangelo.health > 0 and raphael.health > 0 :

    if (choice == "1"):
        response = input("Will you 1) attack with your sword or 2) drink rhum to heal \n >")
        if (response == "1"):
            jack_sparrow.attack(michelangelo)
        if (response == "2"):
            jack_sparrow.drink()
        roll = random.randint(1,2)
        if roll == 1:
            michelangelo.attack(jack_sparrow)
        if roll == 2:
            michelangelo.eat()
        jack_sparrow.show_stats()
        michelangelo.show_stats()

    elif (choice == "2"):
        response = input("Will you 1) attack with a ninja's star or 2) eat some pizzas to gain some strength \n >")
        if (response == "1"):
            michelangelo.attack(jack_sparrow)
        if (response == "2"):
            michelangelo.eat()
        roll = random.randint(1,2)
        if roll == 1:
            jack_sparrow.attack(michelangelo)
        if roll == 2:
            jack_sparrow.drink()
        jack_sparrow.show_stats()
        michelangelo.show_stats()

    elif (choice == "3"):
        response = input("Will you 1) attack with a ninja's star or 2) eat some pizzas to gain some strength or 3) speed attack\n >")
        if (response == "1"):
            raphael.attack(jack_sparrow)
        if (response == "2"):
            raphael.eat()
        if (response == "3"):
            raphael.speed_attack(jack_sparrow)
        roll = random.randint(1,2)
        if roll == 1:
            jack_sparrow.attack(raphael)
        if roll == 2:
            jack_sparrow.drink()
        jack_sparrow.show_stats()
        raphael.show_stats()

    if (jack_sparrow.health <= 20 and jack_sparrow.health > 0):
        Pirate.mortal_attack(raphael)

if (jack_sparrow.health < 0):
    print("Game over, Jack Sparrow is dead")

if (michelangelo.health < 0):
    print("Game over, Michael Angelo is dead")

if (raphael.health < 0):
    print("Game over, Raphael is dead")

    