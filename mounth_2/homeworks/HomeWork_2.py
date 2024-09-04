
from homework_1 import SuperHero

class FireHero(SuperHero):
    locality = 'Vulcan'
    fly = False

    def __init__(self, name: str, nickname: str, superpower: str, health_points: int, catchphrase: str, damage: int):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def become_stronger(self):
        self.fly = True
        self.health_points **= 2
    
    def is_stronger(self):
        print(f'{self.fly} in the True_phrase')
    def __data__(self):
        super().__data__()
        print(f'[DMG: {self.damage}], fly: {self.fly}')

class WaterHero(SuperHero):
    locality = 'Ocean'
    fly = False

    def __init__(self, name: str, nickname: str, superpower: str, health_points: int, catchphrase: str, damage: int):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def become_stronger(self):
        self.fly = True
        self.health_points **= 2
    
    def is_stronger(self):
        print(f'{self.fly} in the True_phrase')

class Villain(FireHero):
    people = 'monster'

    def __init__(self, name: str, nickname: str, superpower: str, health_points: int, catchphrase: str, damage: int):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)

    def gen_x(self):
        ...
    
    def crit(self):
        self.damage **= 2

if __name__ == '__main__':
    fireman = FireHero('Alex', 'FIREMAN', 'fire', 20, 'HotDog :)', 100)
    fireman.become_stronger()
    fireman.__data__()

    shadow = Villain('Sid Kagano', 'SHADOW', 'dark slime', 200, 'I AM ATOMIC', 200)
    shadow.crit()
    shadow.__data__()