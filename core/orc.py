import random
from game import Game

class Orc:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(0,5)
        self.power = random.randint(10,15)
        self.armor_rating = random.randint(2,8)
        self.weapon = random.choice(["knife","sword","ax"])

    def speak(self):
        print(f"the {self.type} {self.name} is angry")

    def attack(self):
        attack = Game()
        orc = Orc("orc")
        a = attack.rol_dice20()
        result = a + orc.speed
        return result