import random


class Hero:
    def __init__(self, name, aggressivity=10, life_value=100):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def q_hurt(self, enemy):
        enemy.life_value -= self.aggressivity
        if enemy.life_value <= 0:
            print('{} 已经死亡'.format(enemy.name))
        else:
            print(' {} 对 {} 使用了q技能，{}损失了{}滴血，还剩{}'.format(
                self.name,
                enemy.name,
                enemy.name,
                self.aggressivity,
                enemy.life_value
            ))

    def w_hurt(self, enemy):
        if random.random() > 0.6:
            enemy.life_value -= 1.2*self.aggressivity
        else:
            enemy.life_value -= self.aggressivity
        if enemy.life_value <= 0:
            print('{} 已经死亡'.format(enemy.name))
        else:
            print(' {} 对 {} 使用了q技能，{}损失了{}滴血，还剩{}'.format(
                self.name,
                enemy.name,
                enemy.name,
                self.aggressivity,
                enemy.life_value
            ))


a = Hero('德玛1')
b = Hero('德玛2')
a.w_hurt(b)