import random
from game import Game

class Player:
    def __init__(self,name):
        self.name = name
        self.hp = 50
        self.speed = random.randint(5,10)
        self.power = random.randint(7,12)
        self.armor_rating = random.randint(5,15)
        self.profession = random.choice(["fighter","healing"])


    def speak(self):
        print(f"i am the player {self.name}")

    def attack(self):
        attack = Game()
        player = Player("chaim")
        a = attack.rol_dice20()
        result = a + player.speed
        return result

