__author__ = 'alemaxona'

'''
models.py - Classes objects game | Классы объектов игры.
'''


class Storage(object):

    '''Players data storage. | Хранилище данных игроков.'''

    field = []

    player1 = ''  # {}
    field_player1 = []
    ship_player1 = {}
    shot_player1 = []

    player2 = ''

    @staticmethod
    def add_player1(value):
        Storage.player1 = value

    @staticmethod
    def add_player2(value):
        Storage.player2 = value

    @staticmethod
    def add_ship_player1(size, key):
        Storage.ship_player1[key] = size

    @staticmethod
    def add_shot_player1(value):
        Storage.shot_player1.append(value)


class Player(object):

    '''Gamers in game only two. | Количество игроков в игре - 2.'''

    def __init__(self, name, queue):
        self.name = name
        self.queue = queue
        if self.queue == 1:
            Storage.add_player1(name)
        else:
            Storage.add_player2(name)


class Field(object):

    '''Game field generator | Генератор карты игры.'''

    def __init__(self, size, size2):
        self.size = size
        self.size2 = size2
        self.result = None

    def init_field(self):
        # Используем генератор.
        self.result = [['*'] * self.size for i in range(self.size2)]
        # self.result = [['*' for j in range(self.size)] for i in range(self.size2)]  # ПРАВИЛЬНО!
        # self.size = [list(i) * int(self.size) for i in self.mark] * int(self.size2)  # НЕПРАВИЛЬНО!
        return self.result


class Ship(object):
    def __init__(self, size, key):
        self.size = size
        self.key = key
        Storage.add_ship_player1([self.size], self.key)

    def build_ship(self, coo1, coo2):
        self.x = int(coo1)
        self.y = int(coo2)


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

x = Ship([0, 0], 1)
print(Storage.ship_player1)
'''