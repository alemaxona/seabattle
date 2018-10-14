__author__ = 'alemaxona'

'''
models.py - Classes objects game
'''


class Storage(object):
    player1 = ''
    ship_player1 = {}
    shot_player1 = []
    field_player1 = []
    player2 = ''

    @staticmethod
    def add_player1(value):
        Storage.player1 = value

    @staticmethod
    def add_player2(value):
        Storage.player2 = value

    @staticmethod
    def add_ship_player1(key, value):
        Storage.ship_player1[key] = value

    @staticmethod
    def add_shot_player1(value):
        Storage.shot_player1.append(value)


class Gamer(object):

    ''' Gamers in game only two! '''

    queue = 0

    def __init__(self, name):
        self.name = name
        if Gamer.queue > 0:
            Storage.add_player2(name)
            Gamer.queue += 1
        else:
            Storage.add_player1(name)
            Gamer.queue += 1


class Field(object):

    ''' Field game '''

    def __init__(self, size, size2):
        self.size = size
        self.size2 = size2
        self.result = None

    def init_field(self):
        # Использовать генератор!
        self.result = [['*'] * self.size for i in range(self.size2)]
        # self.result = [['*' for j in range(self.size)] for i in range(self.size2)]  # ПРАВИЛЬНО!

        # self.size = [list(i) * int(self.size) for i in self.mark] * int(self.size2)  # НЕПРАВИЛЬНО!
        return self.size


class Ship(object):
    def __init__(self, size, key):
        self.size = size
        self.key = key

    def init_ship(self):
        Storage.add_ship_player1(self.key, self.size)


class Shot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


'''
s = Storage
s.add_shot([2,3])
s.add_shot([3,3])
print(s.shot)

s1 = Storage
print(s1.shot)


field = Field(5, 5)
field.init_field()
for i in field.result:
    print(i)
'''