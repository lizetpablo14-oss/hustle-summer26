import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = [SpiderMan, Venom, IronMan, CaptainAmerica, Thor, Hulk]

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)