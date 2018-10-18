__author__ = 'alemaxona'

'''
models.py - Classes objects game | Классы объектов игры.
'''


class Storage(object):

    '''Players data storage. | Хранилище данных игроков.'''

    field = []

    players = {}

    field_player1 = []
    ship_player1 = {}
    shot_player1 = []

    field_player2 = []
    ship_player2 = {}
    shot_player2 = []

    @staticmethod
    def add_players(key, value):
        Storage.players[key] = value

    @staticmethod
    def add_ship_player1(key, size):
        Storage.ship_player1[key] = size

    @staticmethod
    def add_shot_player1(value):
        Storage.shot_player1.append(value)


class Player(object):

    '''Gamers in game only two. | Количество игроков в игре - 2.'''

    def __init__(self, name, queue):
        self.name = name
        self.queue = queue
        Storage.add_players(queue, name)


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
        self.size = [size]
        self.key = key

    def write_ship(self):
        Storage.add_ship_player1(self.key, self.size)


class Shot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_busy(size, number_player):
    if number_player == 1:
        if Storage.field_player1[size[0]][size[1]] != '*':
            return False
        else:
            return True
    else:
        if Storage.field_player2[size[0]][size[1]] != '*':
            return False
        else:
            return True


def check_build_ship_logic(size, key_ship, number_part_ship):
    if number_player == 1:
        if Storage.field_player1[0]:
            return False
        else:
            return True


# s = Storage
# s.add_shot([2,3])
# s.add_shot([3,3])
# print(s.shot)
#
# s1 = Storage
# print(s1.shot)
#
#
# field = Field(5, 5)
# field.init_field()
# for i in field.result:
#     print(i)
#
# x = Ship([0, 0], 1)
# x.write_ship()
# print(Storage.ship_player1)
