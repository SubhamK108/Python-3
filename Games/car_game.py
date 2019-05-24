car_moving = False
while True:
    command = input('> ').upper()
    if command == 'HELP':
        print('''
\nstart - to start the car
stop - to stop the car
quit - to exit the car\n
''')
    elif command == 'START':
        if car_moving:
            print('\nCar is already moving !\n')
        else:
            print('\nCar started... Ready to go !\n')
            car_moving = True
    elif command == 'STOP':
        if not car_moving:
            print('\nCar is already stopped !\n')
        else:
            print('\nCar stopped\n')
            car_moving = False
    elif command == 'QUIT':
        break
    else:
        print("I don't understand that !\n")
