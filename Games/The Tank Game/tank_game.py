from tank_class import Tank
import os
choice = 'Y'
while choice == 'Y':
    os.system('clear')
    player1 = input('Name of Player 1: ')
    player2 = input('Name of Player 2: ')
    player3 = input('Name of Player 3: ')
    p1, p2, p3 = Tank(player1, 20, 50), Tank(player2, 20, 50), Tank(player3, 20, 50)
    all_tanks = {
        'A' : p1,
        'B' : p2,
        'C' : p3
    }
    alive_tanks = len(all_tanks)
    def check_in_alltanks(tank):
        if tank.upper() not in all_tanks.keys():
            print (f'There is no tank named {tank}')
            return 0
        else:
            return 1
    while alive_tanks > 1:
        print ('\n')
        print ('*' * 45)
        print ('\n')
        for key, value in sorted(all_tanks.items()):
            print (key + '-->' + str(value))
        first = str(input('Who Fires ? '))
        if check_in_alltanks(first) == 0:
            continue
        first_tank = all_tanks[first.upper()]
        if first_tank.check_if_alive() == 0:
            continue
        second = str(input(f'{first_tank.tank_name} fires at whom ? '))
        if check_in_alltanks(second) == 0:
            continue
        second_tank = all_tanks[second.upper()]
        if second_tank.check_if_alive() == 0:
            continue
        if first_tank == second_tank:
            print (f"{first_tank.tank_name} can't fire at itself")
            continue
        print ('\n')
        print ('*' * 45)
        print ('\n')
        first_tank.fire_at(second_tank)
        if not second_tank.alive:
            alive_tanks -= 1
    print ('\n')
    print ('*' * 45)
    print ('\n')
    for tank in all_tanks.values():
        if tank.alive:
            print (str(tank) + 'is the Winner !!!')
            break
    choice = str(input('Do you want to play again (Y / N) ? ')).upper()
