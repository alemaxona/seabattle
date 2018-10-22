__author__ = 'alemaxona'

"""
models.py - Classes objects game | Классы объектов игры.
"""


class Storage(object):

    """
    Players data storage. | Хранилище данных игроков.
    """

    field = []
    players = {}
    field_players = {}

    ship_player1 = {}
    ship_player2 = {}

    shots_players = {}

    @staticmethod
    def add_players(key, value):
        Storage.players[key] = value

    @staticmethod
    def add_ship_player1(key, size):
        Storage.ship_player1[key] = size

    @staticmethod
    def add_ship_player2(key, size):
        Storage.ship_player1[key] = size


class Player(object):

    """
    Gamers in game only two. | Количество игроков в игре - 2.

    Add two players and record their fields.
    """

    def __init__(self, name, queue):
        self.name = name
        self.queue = queue
        Storage.add_players(queue, name)

    def write_field_to_storage_players(self):
        Storage.field_players[self.queue] = Storage.field.copy()


class Field(object):

    """
    Game field generator | Генератор карты игры.

    Generic field game.
    """

    def __init__(self, size):
        self.size = size[0]
        self.size2 = size[1]
        self.result = None

    def init_field(self):
        # Use generator. | Используем генератор.
        self.result = [['*'] * self.size for i in range(self.size2)]
        # self.result = [['*' for j in range(self.size)] for i in range(self.size2)]  # ПРАВИЛЬНО!
        # self.size = [list(i) * int(self.size) for i in self.mark] * int(self.size2)  # НЕПРАВИЛЬНО!
        return self.result

    def write_field_to_storage(self):
        Storage.field = self.result.copy()


# !!!
class Ship(object):
    def __init__(self, size, key, obj_player):
        self.size = [size]
        self.key = key
        self.player = obj_player.queue

    def write_ship(self):
        if self.player == 0:
            Storage.add_ship_player1(self.key, self.size)
        else:
            Storage.add_ship_player2(self.key, self.size)


class Shot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_busy(size, obj_player):
        if Storage.field_players[obj_player.queue][size[0]][size[1]] != '*':
            return False
        else:
            return True


def check_max_ships_for_field():

    """
    Summing field cells for check the number of ships
    """

    sum_cell = len(Storage.field[0]) * len(Storage.field[1])
    if sum_cell <= 20:
        max_ship1 = 1
        max_ship2 = 0
        max_ship3 = 0
        max_ship4 = 0
    elif sum_cell >= 21 and sum_cell <= 30:
        max_ship1 = 2
        max_ship2 = 1
        max_ship3 = 1
        max_ship4 = 0
    elif sum_cell >= 31 and sum_cell <= 50:
        max_ship1 = 3
        max_ship2 = 2
        max_ship3 = 1
        max_ship4 = 0
    elif sum_cell >= 51 and sum_cell <= 100:
        max_ship1 = 4
        max_ship2 = 3
        max_ship3 = 2
        max_ship4 = 1
    return [max_ship1, max_ship2, max_ship3, max_ship4]


def check_build_ship_logic():
    pass


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
