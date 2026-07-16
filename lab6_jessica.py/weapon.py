import random

class Weapon:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_damage = random.randint(self.max_damage // 2, self.max_damage)
        print(random_damage)
        return random_damage

if __name__ == "__main__":
    weapon_1 = Weapon("Web Whip", 50)
    print(weapon_1.name)
    print(weapon_1.max_damage)
    weapon_1.attack()