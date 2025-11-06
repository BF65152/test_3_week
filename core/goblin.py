import random
from game import Game

class Goblin:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = "sword"

    def speak(self):
        print(f"the {self.type} {self.name} is angry")

    def attack(self):
        attack = Game()
        goblin = Goblin("goblin")
        a = attack.rol_dice20()
        result = a + goblin.speed
        return result


    def run_away(self):
        if self.hp < 10:
            pass