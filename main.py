__author__ = 'alemaxona'

''' 
main.py - Game logic
'''

from time import sleep
from random import randint
from models import Field, \
    Player, \
    Storage, \
    check_busy, \
    check_max_ships_for_field, \
    ship_connection_check, \
    check_hit_shot, \
    check_ships, \
    check_repeat_shot, \
    indent_from_ships
from input import user_input_coo_ship, \
    user_input_coo_field, \
    robot_input_coo_ship, \
    robot_input_coo_shot


print('\n*** SEABATTLE ***\n\n')
game = 1
while game == 1:
    answer = input('\nStart game? (Y/N): ')
    if answer.upper() != 'Y' and answer.upper() != 'N':
        print('What?')
        continue
    elif answer.upper() == 'N':
        print('\nGoodbye...')
        break
    elif answer.upper() == 'Y':
        while True:
            print('\n************')
            print('* New game *')
            print('************')


# Select field size
            print('\nEnter field size:')
            while True:
                field_coo = user_input_coo_field()
                if isinstance(field_coo, list):
                    break


# Init field and write field in storage
            field = Field(field_coo)
            field.init_field()
            field.write_field_to_storage()


# Init player1
            print('\nYou can play against the robot. Enter “robot” for selection.')
            player1 = Player(input('Enter name player1: '), 0)
            print('Welcome player', player1.name)
# ROBOT
            if player1.name.upper() == 'ROBOT':
                player1.robot = 1

# Init player2
            print('\nYou can play against the robot. Enter “robot” for selection.')
            player2 = Player(input('Enter name player2: '), 1)
            if player2.name == player1.name:
                player2.name = player2.name + '.2'
                print('Welcome player', player2.name)
            else:
                print('Welcome player', player2.name)
# ROBOT
            if player2.name.upper() == 'ROBOT' or player2.name.upper() == 'ROBOT.2':
                player2.robot = 1


# Speed robots
            ROBOT_SPEED = 1    # Delay for 7 seconds.
            # sleep(ROBOT_SPEED)

# Write fields to players storage
            field.write_field_to_storage_players(player1)
            field.write_field_to_storage_players(player2)

# Show max number of ships for this field
            max_ships = check_max_ships_for_field()
            print('\nMaximum ships for this field size: '
                  '\nSingle deck ship -', max_ships[0])
            if max_ships[1] != 0:
                print('Two deck ship -', max_ships[1])
            if max_ships[2] != 0:
                print('Three deck ship -', max_ships[2])
            if max_ships[3] != 0:
                print('Four deck ship -', max_ships[3])
            # sleep(ROBOT_SPEED)


# Random chose queue players!
            QUEUE = randint(player1.queue, player2.queue)


# Enter coordinates all single deck ships - []
            flag = 0
            while flag != 2:
                if QUEUE == 0:
                    player_obj = player1
                else:
                    player_obj = player2
                i = 1
                n = 1.0
                while i <= max_ships[0]:
                    print('\n', player_obj.name, ', enter coordinates single deck ship (1 cell)\n')
                    num_x = 1
                    for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                        print(num_x, row)
                        num_x += 1
                    if player_obj.robot == 0:
                        ship_coo = user_input_coo_ship()
                        if isinstance(ship_coo, list):
                            if check_busy(ship_coo, player_obj) == 0:  # Check cell for busy
                                print('Place is busy! Enter coordinates again.')
                            else:
                                # Check indent
                                if indent_from_ships(player_obj, ship_coo) == 1:
                                    # Write map with single ships to players storage
                                    Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[1]'
                                    # Add ship to storage
                                    Storage.add_ships([ship_coo], player_obj)
                                    print('\n', end='')
                                    # num_y = [' * ' for i in range(len(Storage.field[0]))]
                                    # print(' ', num_y)
                                    num_x = 1
                                    for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                                        print(num_x, row)
                                        num_x += 1
                                    n += 0.1
                                    n = round(n, 1)  # Округление
                                    i += 1
                                else:
                                    print('Build ship error! Not indent!')
                    else:
                        print('\nROBOT enters coordinates single deck ships (1 cell)')
                        ship_coo_robot = robot_input_coo_ship(player_obj, 1)
                        # print('ROBOT coo -', ship_coo_robot)
                        # Write map with single ships to players storage
                        Storage.field_players[player_obj.queue][ship_coo_robot[0]][ship_coo_robot[1]] = '[1]'
                        # Add ship to storage
                        Storage.add_ships([ship_coo_robot], player_obj)
                        print('\n', end='')
                        # num_y = [' * ' for i in range(len(Storage.field[0]))]
                        # print(' ', num_y)
                        num_x = 1
                        for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                            print(num_x, row)
                            num_x += 1
                        sleep(ROBOT_SPEED)
                        n += 0.1
                        n = round(n, 1)  # Округление
                        i += 1


# Enter coordinates all two deck ships - [][]
                i = 1
                n = 2.0
                while i <= max_ships[1]:
                    print('\n', player_obj.name, ', enter coordinates two deck ships (2 cell))\n')
                    num_x = 1
                    for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                        print(num_x, row)
                        num_x += 1
                    if player_obj.robot == 0:
                        print('\nEnter coordinates 1/2 ship')
                        ship_coo = user_input_coo_ship()
                        print('Enter coordinates 2/2 ship')
                        ship_coo2 = user_input_coo_ship()
                        if isinstance(ship_coo, list) and isinstance(ship_coo2, list):
                            # Check indent
                            if indent_from_ships(player_obj, ship_coo) == 1:
                                # Check indent
                                if indent_from_ships(player_obj, ship_coo2) == 1:
                                    if ship_coo != ship_coo2:
                                        if check_busy(ship_coo, player_obj) == 0 or\
                                                check_busy(ship_coo2, player_obj) == 0:  # Check cell for busy
                                            print('Cell is busy! Enter coo again.')
                                            print('\n', end='')
                                            # Show map players with ship/s
                                            for row in Storage.field_players[player_obj.queue]:
                                                print(row)
                                        else:
                                            if ship_connection_check([ship_coo, ship_coo2]) == 1:
                                                # Write map with two ships to players storage
                                                Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[2]'
                                                Storage.field_players[player_obj.queue][ship_coo2[0]][ship_coo2[1]] = '[2]'
                                                # Add ship to storage
                                                Storage.add_ships([ship_coo, ship_coo2], player_obj)
                                                print('\n', end='')
                                                num_x = 1
                                                # Show map players with ship/s
                                                for row in Storage.field_players[player_obj.queue]:
                                                    print(num_x, row)
                                                    num_x += 1
                                                n += 0.1
                                                n = round(n, 1)  # Округление
                                                i += 1
                                            else:
                                                print('Build ship error!')
                                                print('\n', end='')
                                                num_x = 1
                                                # Show map players with ship/s
                                                for row in Storage.field_players[player_obj.queue]:
                                                    print(num_x, row)
                                                    num_x += 1
                                    else:
                                        print('Build ship error! The coordinates parts of ship must be unique!')
                                else:
                                    print('Build ship error! Not indent!')
                            else:
                                print('Build ship error! Not indent!')
                    else:
                        print('\nROBOT enters coordinates two deck ships (2 cell)')
                        ship_coo_robot = robot_input_coo_ship(player_obj, 2)
                        ship_robot = [ship_coo_robot[0], ship_coo_robot[1]]
                        ship_robot2 = [ship_coo_robot[2], ship_coo_robot[3]]
                        # Write map with two ships to players storage
                        Storage.field_players[player_obj.queue][ship_robot[0]][ship_robot[1]] = '[2]'
                        Storage.field_players[player_obj.queue][ship_robot2[0]][ship_robot2[1]] = '[2]'
                        # Add ship to storage
                        Storage.add_ships([ship_robot, ship_robot2], player_obj)
                        print('\n', end='')
                        num_x = 1
                        for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                            print(num_x, row)
                            num_x += 1
                        sleep(ROBOT_SPEED)
                        n += 0.1
                        n = round(n, 1)  # Округление
                        i += 1


# Enter coordinates all three deck ships - [][][]
                i = 1
                n = 3.0
                while i <= max_ships[2]:
                    print('\n', player_obj.name, ', enter coordinates three deck ships (3 cell))\n')
                    num_x = 1
                    for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                        print(num_x, row)
                        num_x += 1
                    if player_obj.robot == 0:
                        print('\nEnter coordinates 1/3 ship')
                        ship_coo = user_input_coo_ship()
                        print('Enter coordinates 2/3 ship')
                        ship_coo2 = user_input_coo_ship()
                        print('Enter coordinates 3/3 ship')
                        ship_coo3 = user_input_coo_ship()
                        if isinstance(ship_coo, list) and isinstance(ship_coo2, list) and isinstance(ship_coo3, list):
                            # Check indent
                            if indent_from_ships(player_obj, ship_coo) == 1:
                                # Check indent
                                if indent_from_ships(player_obj, ship_coo2) == 1:
                                    # Check indent
                                    if indent_from_ships(player_obj, ship_coo3) == 1:
                                        # Pre write! ship_coo1 != ship_coo2 != ship_coo3
                                        if ship_coo != ship_coo2 and ship_coo != ship_coo3 and ship_coo2 != ship_coo3:
                                            if check_busy(ship_coo, player_obj) == 0 or\
                                                    check_busy(ship_coo2, player_obj) == 0 or\
                                                    check_busy(ship_coo3, player_obj) == 0:  # Check cell for busy
                                                print('Cell is busy! Enter coo again.')
                                                print('\n', end='')
                                                num_x = 1
                                                # Show map players with ship/s
                                                for row in Storage.field_players[player_obj.queue]:
                                                    print(num_x, row)
                                                    num_x += 1
                                            else:
                                                if ship_connection_check([ship_coo, ship_coo2, ship_coo3]) == 1:
                                                    # Write map with two ships to players storage
                                                    Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[3]'
                                                    Storage.field_players[player_obj.queue][ship_coo2[0]][ship_coo2[1]] = '[3]'
                                                    Storage.field_players[player_obj.queue][ship_coo3[0]][ship_coo3[1]] = '[3]'
                                                    # Add ship to storage
                                                    Storage.add_ships([ship_coo, ship_coo2, ship_coo3], player_obj)
                                                    print('\n', end='')
                                                    num_x = 1
                                                    # Show map players with ship/s
                                                    for row in Storage.field_players[player_obj.queue]:
                                                        print(num_x, row)
                                                        num_x += 1
                                                    n += 0.1
                                                    n = round(n, 1)  # Округление
                                                    i += 1
                                                else:
                                                    print('Build ship error!')
                                                    print('\n', end='')
                                                    num_x = 1
                                                    # Show map players with ship/s
                                                    for row in Storage.field_players[player_obj.queue]:
                                                        print(num_x, row)
                                                        num_x += 1
                                        else:
                                            print('Build ship error!'
                                                  ' The coordinates of the parts of the ship must be unique!')
                                    else:
                                        print('Build ship error! Not indent!')
                                else:
                                    print('Build ship error! Not indent!')
                            else:
                                print('Build ship error! Not indent!')
                    else:
                        print('\nROBOT enters coordinates three deck ships (3 cell)')
                        ship_coo_robot = robot_input_coo_ship(player_obj, 3)
                        ship_robot = [ship_coo_robot[0], ship_coo_robot[1]]
                        ship_robot2 = [ship_coo_robot[2], ship_coo_robot[3]]
                        ship_robot3 = [ship_coo_robot[4], ship_coo_robot[5]]
                        # Write map with two ships to players storage
                        Storage.field_players[player_obj.queue][ship_robot[0]][ship_robot[1]] = '[3]'
                        Storage.field_players[player_obj.queue][ship_robot2[0]][ship_robot2[1]] = '[3]'
                        Storage.field_players[player_obj.queue][ship_robot3[0]][ship_robot3[1]] = '[3]'
                        # Add ship to storage
                        Storage.add_ships([ship_robot, ship_robot2, ship_robot3], player_obj)
                        print('\n', end='')
                        num_x = 1
                        for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                            print(num_x, row)
                            num_x += 1
                        sleep(ROBOT_SPEED)
                        n += 0.1
                        n = round(n, 1)  # Округление
                        i += 1


# Enter coordinates all four deck ships - [][][][]
                i = 1
                n = 4.0
                while i <= max_ships[3]:
                    print('\n', player_obj.name, ', enter coordinates four deck ships (4 cell))\n')
                    num_x = 1
                    for row in Storage.field_players[player_obj.queue]:  # Show map players with ship/s
                        print(num_x, row)
                        num_x += 1
                    if player_obj.robot == 0:
                        print('\nEnter coordinates 1/4 ship')
                        ship_coo = user_input_coo_ship()
                        print('Enter coordinates 2/4 ship')
                        ship_coo2 = user_input_coo_ship()
                        print('Enter coordinates 3/4 ship')
                        ship_coo3 = user_input_coo_ship()
                        print('Enter coordinates 4/4 ship')
                        ship_coo4 = user_input_coo_ship()
                        if isinstance(ship_coo, list) and\
                                isinstance(ship_coo2, list) and\
                                isinstance(ship_coo3, list) and\
                                isinstance(ship_coo4, list):
                            # Check indent
                            if indent_from_ships(player_obj, ship_coo) == 1:
                                # Check indent
                                if indent_from_ships(player_obj, ship_coo2) == 1:
                                    # Check indent
                                    if indent_from_ships(player_obj, ship_coo3) == 1:
                                        # Check indent
                                        if indent_from_ships(player_obj, ship_coo4) == 1:
                                            # Pre write! ship_coo1 != ship_coo2 != ship_coo3 != ship_coo4
                                            if ship_coo != ship_coo2 and ship_coo != ship_coo3 and ship_coo != ship_coo4 and\
                                                    ship_coo2 != ship_coo3 and ship_coo2 != ship_coo4 and\
                                                    ship_coo3 != ship_coo4:
                                                # Check cell for busy:  # Check cell for busy
                                                if check_busy(ship_coo, player_obj) == 0 or\
                                                        check_busy(ship_coo2, player_obj) == 0 or\
                                                        check_busy(ship_coo3, player_obj) == 0 or \
                                                        check_busy(ship_coo4, player_obj) == 0:
                                                    print('Cell is busy! Enter coo again.')
                                                    print('\n', end='')
                                                    num_x = 1
                                                    # Show map players with ship/s
                                                    for row in Storage.field_players[player_obj.queue]:
                                                        print(num_x, row)
                                                        num_x += 1
                                                else:
                                                    if ship_connection_check([ship_coo, ship_coo2, ship_coo3, ship_coo4]) == 1:
                                                        # Write map with two ships to players storage
                                                        Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[4]'
                                                        Storage.field_players[player_obj.queue][ship_coo2[0]][ship_coo2[1]] = '[4]'
                                                        Storage.field_players[player_obj.queue][ship_coo3[0]][ship_coo3[1]] = '[4]'
                                                        Storage.field_players[player_obj.queue][ship_coo4[0]][ship_coo4[1]] = '[4]'
                                                        # Add ship to storage
                                                        Storage.add_ships([ship_coo, ship_coo2, ship_coo3, ship_coo4], player_obj)
                                                        print('\n', end='')
                                                        num_x = 1
                                                        # Show map players with ship/s
                                                        for row in Storage.field_players[player_obj.queue]:
                                                            print(num_x, row)
                                                            num_x += 1
                                                        n += 0.1
                                                        n = round(n, 1)  # Округление
                                                        i += 1
                                                    else:
                                                        print('Build ship error!')
                                                        print('\n', end='')
                                                        num_x = 1
                                                        # Show map players with ship/s
                                                        for row in Storage.field_players[player_obj.queue]:
                                                            print(num_x, row)
                                                            num_x += 1
                                                            # Second cycle pass | Второй проход цикла.
                                            else:
                                                print('Build ship error!'
                                                      ' The coordinates of the parts of the ship must be unique!')
                                        else:
                                            print('Build ship error! Not indent!')
                                    else:
                                        print('Build ship error! Not indent!')
                                else:
                                    print('Build ship error! Not indent!')
                            else:
                                print('Build ship error! Not indent!')
                    else:
                        print('\nROBOT enters coordinates four deck ships (4 cell)')
                        ship_coo_robot = robot_input_coo_ship(player_obj, 4)
                        ship_robot = [ship_coo_robot[0], ship_coo_robot[1]]
                        ship_robot2 = [ship_coo_robot[2], ship_coo_robot[3]]
                        ship_robot3 = [ship_coo_robot[4], ship_coo_robot[5]]
                        ship_robot4 = [ship_coo_robot[6], ship_coo_robot[7]]
                        # Write map with two ships to players storage
                        Storage.field_players[player_obj.queue][ship_robot[0]][ship_robot[1]] = '[4]'
                        Storage.field_players[player_obj.queue][ship_robot2[0]][ship_robot2[1]] = '[4]'
                        Storage.field_players[player_obj.queue][ship_robot3[0]][ship_robot3[1]] = '[4]'
                        Storage.field_players[player_obj.queue][ship_robot4[0]][ship_robot4[1]] = '[4]'
                        # Add ship to storage
                        Storage.add_ships([ship_robot, ship_robot2, ship_robot3, ship_robot4], player_obj)
                        print('\n', end='')
                        num_x = 1
                        # Show map players with ship/s
                        for row in Storage.field_players[player_obj.queue]:
                            print(num_x, row)
                            num_x += 1
                        sleep(ROBOT_SPEED)
                        n += 0.1
                        n = round(n, 1)  # Округление
                        i += 1

                flag += 1
                if QUEUE == 1:
                    QUEUE = 0
                elif QUEUE == 0:
                    QUEUE = 1

# Shots logic
            print('\n\n*** Ships on the positions. Let the battle begin! ***')


# Write fields for shots to players storage
            field.write_shots_to_storage_players(player1)
            field.write_shots_to_storage_players(player2)


# Random chose queue players!
            QUEUE = randint(player1.queue, player2.queue)
            if QUEUE == player1.queue:
                print('\n\nThe computer chose the player who will start first. It\'s -', player1.name)
                sleep(ROBOT_SPEED)
            else:
                print('\n\nThe computer chose the player who will start first. It\'s -', player2.name)
                sleep(ROBOT_SPEED)

# Shots
            # !!!!!!!!
            ROBOT_SPEED = 4
            # !!!!!!!!
            while True:
                if QUEUE == 0:
                    player_obj = player1
                    player_obj_reverse = player2
                else:
                    player_obj = player2
                    player_obj_reverse = player1
                print('\n', player_obj.name, ', enter coordinates your shot\n')
                num_x = 1
                for row in Storage.shots_field_players[player_obj.queue]:  # Show map players with ship/s
                    print(num_x, row)
                    num_x += 1
                sleep(ROBOT_SPEED)
                if player_obj.robot == 0:
                    shot_coo = user_input_coo_ship()
                    if isinstance(shot_coo, list):
                        # Stats
                        player_obj.number_of_shots += 1
                        # Check repeat shot to one cell
                        if check_repeat_shot(shot_coo, player_obj) == 1:
                            print('You\'ve already shot here! The move goes to the player -', player_obj_reverse.name)
                            if QUEUE == 0:
                                QUEUE = 1
                            elif QUEUE == 1:
                                QUEUE = 0
                            continue
                        # Hit check
                        if check_hit_shot(shot_coo, player_obj_reverse) == 1:
                            print('The ship is kill! Keep going.')
                            # Stats
                            player_obj.target_shots += 1
                            # Write shots to field reverse player
                            Storage.field_players[player_obj_reverse.queue][shot_coo[0]][shot_coo[1]] = '[X]'
                            # Write shots to shots field
                            Storage.shots_field_players[player_obj.queue][shot_coo[0]][shot_coo[1]] = '[X]'
                            if check_ships(player_obj_reverse) == 0:
                                print('\n****************')
                                print('*** You win! ***')
                                print('****************')
                                break
                        elif check_hit_shot(shot_coo, player_obj_reverse) == 2:
                            print('You hit the ship! Keep going.')
                            # Stats
                            player_obj.target_shots += 1
                            # Write shots to field reverse player
                            Storage.field_players[player_obj_reverse.queue][shot_coo[0]][shot_coo[1]] = '[X]'
                            # Write shots to shots field
                            Storage.shots_field_players[player_obj.queue][shot_coo[0]][shot_coo[1]] = '[X]'
                        elif check_hit_shot(shot_coo, player_obj_reverse) == 0:
                            # Stats
                            Storage.shots_field_players[player_obj.queue][shot_coo[0]][shot_coo[1]] = '[O]'
                            print('You missed... The move goes to the player -', player_obj_reverse.name)
                            if QUEUE == 0:
                                QUEUE = 1
                            elif QUEUE == 1:
                                QUEUE = 0
                else:
                    shot_coo = robot_input_coo_shot(player_obj_reverse, player_obj)
                    print(player_obj.history_shots)
                    print(shot_coo)
                    player_obj.history_shots.append(shot_coo)
                    # Stats
                    player_obj.number_of_shots += 1
                    # Hit check
                    if check_hit_shot(shot_coo, player_obj_reverse) == 1:
                        print('Robot killed ship! Keep going.')
                        # Stats
                        player_obj.target_shots += 1
                        # Write shots to field reverse player
                        Storage.field_players[player_obj_reverse.queue][shot_coo[0]][shot_coo[1]] = '[X]'
                        # Write shots to shots field
                        Storage.shots_field_players[player_obj.queue][shot_coo[0]][shot_coo[1]] = '[X]'
                        if check_ships(player_obj_reverse) == 0:
                            print('\n******************')
                            print('*** Robot win! ***')
                            print('******************')
                            break
                    elif check_hit_shot(shot_coo, player_obj_reverse) == 2:
                        print('Robot hit the ship! Keep going.')
                        # Shots logic for robots
                        # Stats
                        player_obj.target_shots += 1
                        # Write shots to field reverse player
                        Storage.field_players[player_obj_reverse.queue][shot_coo[0]][shot_coo[1]] = '[x]'
                        # Write shots to shots field
                        Storage.shots_field_players[player_obj.queue][shot_coo[0]][shot_coo[1]] = '[x]'
                    elif check_hit_shot(shot_coo, player_obj_reverse) == 0:
                        # Write shots to field reverse player
                        Storage.field_players[player_obj_reverse.queue][shot_coo[0]][shot_coo[1]] = '[O]'
                        # Stats
                        Storage.shots_field_players[player_obj.queue][shot_coo[0]][shot_coo[1]] = '[O]'
                        print('Robot missed... The move goes to the player -', player_obj_reverse.name)
                        if QUEUE == 0:
                            QUEUE = 1
                        elif QUEUE == 1:
                            QUEUE = 0

            print('\n******* WINNER *******')
            print('       ', player_obj.name)


# Show stats
            print('\nPlayer:', player1.name,
                  '\nTotal shots:', player1.number_of_shots,
                  '\nTotal hits shots:', player1.target_shots,
                  '\nTotal miss shots:', player1.number_of_shots - player1.target_shots,
                  '\nShots map: \n')
            for row in Storage.shots_field_players[player1.queue]:
                print(row)

            print('\nPlayer:', player2.name,
                  '\nTotal shots:', player2.number_of_shots,
                  '\nTotal hits shots:', player2.target_shots,
                  '\nTotal miss shots:', player2.number_of_shots - player2.target_shots,
                  '\nShots map: \n')
            for row in Storage.shots_field_players[player2.queue]:
                print(row)

# Deleting param
            del field
            del Storage.shots_field_players
            del player1
            del player2


# New game cycle
            answer = input('\nDo you want start new game? (Y/N) ')
            if answer.upper() == 'Y':
                continue
            else:
                print('\nOk, goodbye...')
                game = 0
                break
