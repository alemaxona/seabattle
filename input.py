__author__ = 'alemaxona'

"""
input.py - Functions inputs with users or robots.
"""

from models import Storage, indent_from_ships
from random import randint, choice


def user_input_coo_field():
    while True:
        try:
            y = input('Rows (X) = ')
            x = input('\nColumns (Y) = ')
            coo_x = int(x)
            coo_y = int(y)
            if int(coo_x) < 3:
                print('Enter number Columns (Y) > 3')
                break
            elif int(coo_x) > 10:
                print('Max field size - 10x10.')
                break
            elif int(coo_y) <= 0:
                print('Enter number Rows (X) > 0')
                break
            elif int(coo_y) > 10:
                print('Max field size - 10x10.')
                break
            else:
                value3 = [coo_x, coo_y]
                return value3
        except ValueError:
            print('Enter only numbers')
            break


def user_input_coo_ship():
    while True:
        try:
            x = input('\nX = ')
            y = input('Y = ')
            coo_x = int(x)
            coo_y = int(y)
            if int(coo_x) <= 0:
                print('Enter number X > 0')
                break
            elif int(coo_y) <= 0:
                print('Enter number Y > 0')
                break
            elif int(coo_x - 1) >= len(Storage.field):
                print('Enter number X < or =', len(Storage.field))
                break
            elif int(coo_y) > len(Storage.field[0]):
                print('Enter number Y < or =', len(Storage.field[0]))
                break
            else:
                value3 = [(coo_x - 1), (coo_y - 1)]
                return value3
        except ValueError:
            print('Enter only numbers')
            break


def robot_input_coo_ship(player_obj, ship):
    # []
    if ship == 1:
        while True:
            x = randint(0, len(Storage.field) - 1)
            y = randint(0, len(Storage.field[0]) - 1)
            ship_coo_robot = [x, y]
            if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[1]':
                # Check indent
                if indent_from_ships(player_obj, ship_coo_robot) == 1:
                    return ship_coo_robot
                else:
                    continue
            else:
                continue
    # [][]
    elif ship == 2:
        while True:
            x = randint(0, len(Storage.field) - 1)
            y = randint(0, len(Storage.field[0]) - 1)
            ship_coo_robot = [x, y]
            result = []
            if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[1]' and\
                    Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[2]':
                if ship_coo_robot[0] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] - 1][ship_coo_robot[1]] == ' * ':
                        result.append([ship_coo_robot[0] - 1, ship_coo_robot[1]])
                if ship_coo_robot[0] + 1 <= len(Storage.field) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] + 1][ship_coo_robot[1]] == ' * ':
                        result.append([ship_coo_robot[0] + 1, ship_coo_robot[1]])
                if ship_coo_robot[1] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] - 1] == ' * ':
                        result.append([ship_coo_robot[0], ship_coo_robot[1] - 1])
                if ship_coo_robot[1] + 1 <= len(Storage.field[0]) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] + 1] == ' * ':
                        result.append([ship_coo_robot[0], ship_coo_robot[1] + 1])
                ship_coo_robot2 = choice(result)
                if ship_coo_robot != ship_coo_robot2:
                    # Check indent
                    if indent_from_ships(player_obj, ship_coo_robot) == 1:
                        # Check indent
                        if indent_from_ships(player_obj, ship_coo_robot2) == 1:
                            return [ship_coo_robot[0], ship_coo_robot[1], ship_coo_robot2[0], ship_coo_robot2[1]]
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
    # [][][]
    elif ship == 3:
        while True:
            x = randint(0, len(Storage.field) - 1)
            y = randint(0, len(Storage.field[0]) - 1)
            ship_coo_robot = [x, y]
            result = []
            result2 = []
            # []..[]
            if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[1]' and\
                    Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[2]' and \
                    Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[3]':
                if ship_coo_robot[0] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] - 1][ship_coo_robot[1]] == ' * ':
                        result.append([ship_coo_robot[0] - 1, ship_coo_robot[1]])
                if ship_coo_robot[0] + 1 <= len(Storage.field) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] + 1][ship_coo_robot[1]] == ' * ':
                        result.append([ship_coo_robot[0] + 1, ship_coo_robot[1]])
                if ship_coo_robot[1] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] - 1] == ' * ':
                        result.append([ship_coo_robot[0], ship_coo_robot[1] - 1])
                if ship_coo_robot[1] + 1 <= len(Storage.field[0]) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] + 1] == ' * ':
                        result.append([ship_coo_robot[0], ship_coo_robot[1] + 1])
                ship_coo_robot2 = choice(result)
                # [][]..[]
                if ship_coo_robot[0] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] - 1][ship_coo_robot[1]] == ' * ':
                        result2.append([ship_coo_robot[0] - 1, ship_coo_robot[1]])
                if ship_coo_robot[0] + 1 <= len(Storage.field) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] + 1][ship_coo_robot[1]] == ' * ':
                        result2.append([ship_coo_robot[0] + 1, ship_coo_robot[1]])
                if ship_coo_robot[1] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] - 1] == ' * ':
                        result2.append([ship_coo_robot[0], ship_coo_robot[1] - 1])
                if ship_coo_robot[1] + 1 <= len(Storage.field[0]) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] + 1] == ' * ':
                        result2.append([ship_coo_robot[0], ship_coo_robot[1] + 1])
                ship_coo_robot3 = choice(result2)
                if ship_coo_robot != ship_coo_robot2 and\
                        ship_coo_robot != ship_coo_robot3 and\
                        ship_coo_robot2 != ship_coo_robot3:
                    if (ship_coo_robot[0] == ship_coo_robot2[0] == ship_coo_robot3[0]) or\
                            (ship_coo_robot[1] == ship_coo_robot2[1] == ship_coo_robot3[1]):
                        # Check indent
                        if indent_from_ships(player_obj, ship_coo_robot) == 1:
                            # Check indent
                            if indent_from_ships(player_obj, ship_coo_robot2) == 1:
                                # Check indent
                                if indent_from_ships(player_obj, ship_coo_robot3) == 1:
                                    return [ship_coo_robot[0], ship_coo_robot[1], ship_coo_robot2[0],
                                            ship_coo_robot2[1], ship_coo_robot3[0], ship_coo_robot3[1]]
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
    # [][][][]
    elif ship == 4:
        while True:
            x = randint(0, len(Storage.field) - 1)
            y = randint(0, len(Storage.field[0]) - 1)
            ship_coo_robot = [x, y]
            result = []
            result2 = []
            result3 = []
            # []..[]
            if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[1]' and\
                    Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[2]' and \
                    Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[3]' and\
                    Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] != '[4]':
                if ship_coo_robot[0] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] - 1][ship_coo_robot[1]] == ' * ':
                        result.append([ship_coo_robot[0] - 1, ship_coo_robot[1]])
                if ship_coo_robot[0] + 1 <= len(Storage.field) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] + 1][ship_coo_robot[1]] == ' * ':
                        result.append([ship_coo_robot[0] + 1, ship_coo_robot[1]])
                if ship_coo_robot[1] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] - 1] == ' * ':
                        result.append([ship_coo_robot[0], ship_coo_robot[1] - 1])
                if ship_coo_robot[1] + 1 <= len(Storage.field[0]) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] + 1] == ' * ':
                        result.append([ship_coo_robot[0], ship_coo_robot[1] + 1])
                ship_coo_robot2 = choice(result)
                # [][]..[]
                if ship_coo_robot[0] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] - 1][ship_coo_robot[1]] == ' * ':
                        result2.append([ship_coo_robot[0] - 1, ship_coo_robot[1]])
                if ship_coo_robot[0] + 1 <= len(Storage.field) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] + 1][ship_coo_robot[1]] == ' * ':
                        result2.append([ship_coo_robot[0] + 1, ship_coo_robot[1]])
                if ship_coo_robot[1] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] - 1] == ' * ':
                        result2.append([ship_coo_robot[0], ship_coo_robot[1] - 1])
                if ship_coo_robot[1] + 1 <= len(Storage.field[0]) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] + 1] == ' * ':
                        result2.append([ship_coo_robot[0], ship_coo_robot[1] + 1])
                ship_coo_robot3 = choice(result2)
                # [][][]..[]
                if ship_coo_robot[0] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] - 1][ship_coo_robot[1]] == ' * ':
                        result3.append([ship_coo_robot[0] - 1, ship_coo_robot[1]])
                if ship_coo_robot[0] + 1 <= len(Storage.field) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] + 1][ship_coo_robot[1]] == ' * ':
                        result3.append([ship_coo_robot[0] + 1, ship_coo_robot[1]])
                if ship_coo_robot[1] - 1 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] - 1] == ' * ':
                        result3.append([ship_coo_robot[0], ship_coo_robot[1] - 1])
                if ship_coo_robot[1] + 1 <= len(Storage.field[0]) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] + 1] == ' * ':
                        result3.append([ship_coo_robot[0], ship_coo_robot[1] + 1])
                if ship_coo_robot[0] - 2 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] - 2][ship_coo_robot[1]] == ' * ':
                        result3.append([ship_coo_robot[0] - 2, ship_coo_robot[1]])
                if ship_coo_robot[0] + 2 <= len(Storage.field) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0] + 2][ship_coo_robot[1]] == ' * ':
                        result3.append([ship_coo_robot[0] + 2, ship_coo_robot[1]])
                if ship_coo_robot[1] - 2 >= 0:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] - 2] == ' * ':
                        result3.append([ship_coo_robot[0], ship_coo_robot[1] - 2])
                if ship_coo_robot[1] + 2 <= len(Storage.field[0]) - 1:
                    if Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1] + 2] == ' * ':
                        result3.append([ship_coo_robot[0], ship_coo_robot[1] + 2])
                ship_coo_robot4 = choice(result3)
                if ship_coo_robot != ship_coo_robot2 and\
                        ship_coo_robot != ship_coo_robot3 and\
                        ship_coo_robot != ship_coo_robot4 and\
                        ship_coo_robot2 != ship_coo_robot3 and\
                        ship_coo_robot2 != ship_coo_robot4 and\
                        ship_coo_robot3 != ship_coo_robot4:
                    if (ship_coo_robot[0] == ship_coo_robot2[0] == ship_coo_robot3[0] == ship_coo_robot4[0]) or\
                            (ship_coo_robot[1] == ship_coo_robot2[1] == ship_coo_robot3[1] == ship_coo_robot4[1]):
                        # Check indent
                        if indent_from_ships(player_obj, ship_coo_robot) == 1:
                            # Check indent
                            if indent_from_ships(player_obj, ship_coo_robot2) == 1:
                                # Check indent
                                if indent_from_ships(player_obj, ship_coo_robot3) == 1:
                                    # Check indent
                                    if indent_from_ships(player_obj, ship_coo_robot4) == 1:
                                        return [ship_coo_robot[0], ship_coo_robot[1],
                                                ship_coo_robot2[0], ship_coo_robot2[1],
                                                ship_coo_robot3[0], ship_coo_robot3[1],
                                                ship_coo_robot4[0], ship_coo_robot4[1]]
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue


def robot_input_coo_shot(obj_reverse, obj):
    z = Storage.field_players[obj_reverse.queue]
    sum_cell = len(Storage.field_players[0]) * len(Storage.field_players[0][0])
    # If field have only ships with one deck
    if sum_cell <= 20:
        while True:
            x = randint(0, (len(z) - 1))
            y = randint(0, (len(z[0]) - 1))
            # New shot in ' * '
            if z[x][y] != '[O]' and z[x][y] != '[X]':
                return [x, y]
            else:
                continue
    else:
        # First shot
        if len(obj.history_shots) == 0:
            while True:
                x = randint(0, (len(z) - 1))
                y = randint(0, (len(z[0]) - 1))
                return [x, y]
        # If the last shot in history is kill
        elif z[obj.history_shots[-1][0]][obj.history_shots[-1][1]] == '[X]':
            while True:
                x = randint(0, (len(z) - 1))
                y = randint(0, (len(z[0]) - 1))
                # новый шот в ' * '
                if z[x][y] != '[O]' and \
                    z[x][y] != '[X]' and \
                        z[x][y] != '[x]':
                    return [x, y]
                else:
                    continue
        # If the last shot in history is hit or miss ???
        elif z[obj.history_shots[-1][0]][obj.history_shots[-1][1]] == '[x]' or \
                z[obj.history_shots[-1][0]][obj.history_shots[-1][1]] == '[O]':
            rows = len(z) - 1
            columns = len(z[0]) - 1
            result = []
            # field corners
            if obj.history_shots[-1][0] == 0 and obj.history_shots[-1][1] == 0:  # [0, 0]
                while True:
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] + 1])
                    result.append([obj.history_shots[-1][0] + 1, obj.history_shots[-1][1]])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':  # ???
                        return r
                    else:
                        continue
            elif obj.history_shots[-1][0] == rows and obj.history_shots[-1][1] == 0:  # [rows, 0]
                while True:
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] + 1])
                    result.append([obj.history_shots[-1][0] - 1, obj.history_shots[-1][1]])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
            elif obj.history_shots[-1][0] == 0 and obj.history_shots[-1][1] == columns:  # [0, column]
                while True:
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] - 1])
                    result.append([obj.history_shots[-1][0] + 1, obj.history_shots[-1][1]])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
            elif obj.history_shots[-1][0] == rows and obj.history_shots[-1][1] == columns:  # [rows, column]
                while True:
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] - 1])
                    result.append([obj.history_shots[-1][0] - 1, obj.history_shots[-1][1]])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
            # field sides
            elif obj.history_shots[-1][0] != 0 and obj.history_shots[-1][1] == 0:  # [., 0]
                while True:
                    result.append([obj.history_shots[-1][0] - 1, obj.history_shots[-1][1]])
                    result.append([obj.history_shots[-1][0] + 1, obj.history_shots[-1][1]])
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] + 1])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
            elif obj.history_shots[-1][0] == 0 and obj.history_shots[-1][1] != 0:  # [0, .]
                while True:
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] - 1])
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] + 1])
                    result.append([obj.history_shots[-1][0] + 1, obj.history_shots[-1][1]])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
            elif obj.history_shots[-1][0] == rows and obj.history_shots[-1][1] != 0:  # [rows, .]
                while True:
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] - 1])
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] + 1])
                    result.append([obj.history_shots[-1][0] - 1, obj.history_shots[-1][1]])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
            elif obj.history_shots[-1][0] != 0 and obj.history_shots[-1][1] == columns:  # [., columns]
                while True:
                    result.append([obj.history_shots[-1][0] - 1, obj.history_shots[-1][1]])
                    result.append([obj.history_shots[-1][0] + 1, obj.history_shots[-1][1]])
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] - 1])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
            # other
            elif (0 < obj.history_shots[-1][0] < rows) and (0 < obj.history_shots[-1][1] < columns):
                while True:
                    result.append([obj.history_shots[-1][0] - 1, obj.history_shots[-1][1]])
                    result.append([obj.history_shots[-1][0] + 1, obj.history_shots[-1][1]])
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] - 1])
                    result.append([obj.history_shots[-1][0], obj.history_shots[-1][1] + 1])
                    r = choice(result)
                    if z[r[0]][r[1]] != '[O]' and z[r[0]][r[1]] != '[x]':
                        return r
                    else:
                        continue
