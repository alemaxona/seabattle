__author__ = 'alemaxona'

"""
models.py - Classes objects game | Классы объектов игры.
"""

from copy import deepcopy


class Storage(object):

    """
    Players data storage. | Хранилище данных игроков.
    """

    field = []
    players = {}
    field_players = {}

    ships_player1 = {}
    ships_player2 = {}

    shots_players = {}

    @staticmethod
    def add_players(key, value):
        Storage.players[key] = value

    @staticmethod
    def add_ship_player1(ship, coo):
        Storage.ships_player1[ship] = coo

    @staticmethod
    def add_ship_player2(key, size):
        Storage.ships_player1[key] = size


class Player(object):

    """
    Gamers in game only two. | Количество игроков в игре - 2.

    Add players and write their in storage.
    """

    def __init__(self, name, queue):
        self.name = name
        self.queue = queue
        Storage.add_players(queue, name)


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
        self.result = [[' * '] * self.size for i in range(self.size2)]
        # self.result = [['*' for j in range(self.size)] for i in range(self.size2)]  # ПРАВИЛЬНО!
        # self.size = [list(i) * int(self.size) for i in self.mark] * int(self.size2)  # НЕПРАВИЛЬНО!
        return self.result

    def write_field_to_storage(self):
        Storage.field = deepcopy(self.result)

    def write_field_to_storage_players(self, obj):
        Storage.field_players[obj.queue] = deepcopy(self.result)


class Ship(object):
    def __init__(self, obj_player):
        self.player = obj_player.queue
        self.coo = None

    def write_ship(self, key, coo_ships):
        self.coo = coo_ships
        if self.player == 0:
            Storage.add_ship_player1(key, coo_ships)
        else:
            Storage.add_ship_player2(key, coo_ships)


class Shot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_busy(size, obj_player):

    """
    Check cell to free on players fields.

    If '*' - free.
    """
    if Storage.field_players[obj_player.queue][size[0]][size[1]] == ' * ':
        return 1
    elif Storage.field_players[obj_player.queue][size[0]][size[1]] == '[1]' or \
            Storage.field_players[obj_player.queue][size[0]][size[1]] == '[2]' or \
            Storage.field_players[obj_player.queue][size[0]][size[1]] == '[3]' or \
            Storage.field_players[obj_player.queue][size[0]][size[1]] == '[4]':
        return 0


# size = [[,], [,]] or [[,], [,], [,]] or [[,], [,] ,[,], [,]]
def ship_connection_check(coo):
    if len(coo) == 2:
        a = coo[0][0]  # [[*, ], [ , ]]
        b = coo[0][1]  # [[ ,*], [ , ]]
        c = coo[1][0]  # [[ , ], [*, ]]
        d = coo[1][1]  # [[ , ], [ ,*]]
        if (a == c and b + 1 == d) or (a - 1 == c and b == d) or (a + 1 == c and b == d) or (a == c and b - 1 == d):
            return 1
        else:
            return 0
    elif len(coo) == 3:
        a = coo[0][0]  # [[*, ], [ , ]]
        b = coo[0][1]  # [[ ,*], [ , ]]
        c = coo[1][0]  # [[ , ], [*, ]]
        d = coo[1][1]  # [[ , ], [ ,*]]
        e = coo[2][0]  # [[ , ], [ , ], [*, ]]
        f = coo[2][1]  # [[ , ], [ , ], [ ,*]]
        if ((a == c and b + 1 == d) or
            (a - 1 == c and b == d) or
            (a + 1 == c and b == d) or
            (a == c and b - 1 == d)) and \
                (b == d == f or a == c == e):
            return 1
        else:
            return 0
    elif len(coo) == 4:
        a = coo[0][0]  # [[*, ], [ , ]]
        b = coo[0][1]  # [[ ,*], [ , ]]
        c = coo[1][0]  # [[ , ], [*, ]]
        d = coo[1][1]  # [[ , ], [ ,*]]
        e = coo[2][0]  # [[ , ], [ , ], [*, ]]
        f = coo[2][1]  # [[ , ], [ , ], [ ,*]]
        g = coo[3][0]  # [[ , ], [ , ], [ , ], [*, ]]
        h = coo[3][1]  # [[ , ], [ , ], [ , ], [ ,*]]
        if ((a == c and b + 1 == d) or
            (a - 1 == c and b == d) or
            (a + 1 == c and b == d) or
            (a == c and b - 1 == d)) and \
                (b == d == f == h or a == c == e == g):
            return 1
        else:
            return 0


def check_max_ships_for_field():

    """
    Summing field cells for check the number of ships
    """

    if len(Storage.field) == 1:
        max_ship1 = 1
        max_ship2 = 0
        max_ship3 = 0
        max_ship4 = 0
        return [max_ship1, max_ship2, max_ship3, max_ship4]
    else:
        sum_cell = len(Storage.field[0]) * len(Storage.field[1])
        if sum_cell <= 9:
            max_ship1 = 1
            max_ship2 = 0
            max_ship3 = 0
            max_ship4 = 0
        if (sum_cell >= 10) and (sum_cell <= 20):
            max_ship1 = 2
            max_ship2 = 0
            max_ship3 = 0
            max_ship4 = 0
        elif (sum_cell >= 21) and (sum_cell <= 30):
            max_ship1 = 2
            max_ship2 = 1
            max_ship3 = 1
            max_ship4 = 0
        elif (sum_cell >= 31) and (sum_cell <= 50):
            max_ship1 = 3
            max_ship2 = 2
            max_ship3 = 1
            max_ship4 = 0
        elif (sum_cell >= 51) and (sum_cell <= 100):
            max_ship1 = 4
            max_ship2 = 3
            max_ship3 = 2
            max_ship4 = 1
        return [max_ship1, max_ship2, max_ship3, max_ship4]


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
#
#
# x = [0, 1]
# if Storage.field_players[0][x[0]][x[1]] == '[]':
#     print('true')
# else:
#     print('False')
