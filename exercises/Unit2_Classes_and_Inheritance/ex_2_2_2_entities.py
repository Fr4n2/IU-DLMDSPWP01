'''Entity Hierarchy with super() - see ex_2_2_2_entities.md for the full description.

Fill in the function(s) below, then run this file to test your work:
    python ex_2_2_2_*.py
'''

class Entity:
    def __init__(self, name, hp):
        # TODO
        raise NotImplementedError

    def is_alive(self):
        raise NotImplementedError


class Player(Entity):
    def __init__(self, name, hp):
        # TODO (use super())
        raise NotImplementedError


class Enemy(Entity):
    def __init__(self, name, hp, damage):
        # TODO (use super())
        raise NotImplementedError

    def attack(self, target):
        raise NotImplementedError

if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from grader import Grader
    Grader.run("2.2.2", globals())
