'''Entity Hierarchy with super() - see ex_2_2_2_entities.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_2_2_2_*.py
'''

class Entity:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def is_alive(self):
        return self.hp > 0


class Player(Entity):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.inventory = []


class Enemy(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage

    def attack(self, target):
        target.hp = target.hp - self.damage

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("2.2.2", globals())
