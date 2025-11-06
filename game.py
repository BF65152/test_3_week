import random
from core.player import Player
from core.goblin import Goblin
from core.orc import Orc

class Game:

    player = Player("chaim")
    monster = Orc("goblin")
    monster2 = Orc("orc")

    def start(self):
       pass

    @staticmethod
    def show_menu():
       choice = input("enter fight or exit")
       return choice

    @classmethod
    def create_player(cls):
        return cls.player.__dict__

    @classmethod
    def monster_random_choose(cls):
        choice_monster = random.choice([cls.monster.__dict__,cls.monster2.__dict__])
        return choice_monster

    @staticmethod
    def rol_dice6():
        kube = random.randint(1,6)
        return kube

    @staticmethod
    def rol_dice20():
        kube = random.randint(1, 20)
        return kube

    @classmethod
    def battle(cls):

        player1 = Game.monster_random_choose()
        monster1 = Game.create_player()
        player = Game.rol_dice6()
        monster = Game.rol_dice6()

        booli = True
        while booli:
            if player + player1["speed"] > monster + monster1["speed"]:
                c = Game.show_menu()
                if c == "exit":
                     break
                if c == "fight":
                   p = cls.player.attack()
                   if p > cls.monster.armor_rating:
                      r = Game.rol_dice6()
                      cls.player.hp += r
                   else:
                      m2 = cls.monster.attack()
                      if m2 > cls.player.armor_rating:
                          v = Game.rol_dice6()
                          cls.monster.hp += v
                      else:
                          continue
            elif player + player1["speed"] < monster + monster1["speed"]:
                m2 = cls.monster.attack()

            else:
                continue

