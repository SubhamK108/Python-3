import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


name = input('Enter your First Name: ')
choice = 'Y'
while choice == 'Y':
    curses.initscr()
    win = curses.newwin(30, 100, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = KEY_RIGHT
    score = 0

    snake = [[4,10], [4,9], [4,8]] 
    food = [randint(1, 28), randint(1, 98)]

    win.addch(food[0], food[1], curses.ACS_PI)

    while key != 27:
        win.border(0)
        win.addstr(0, 2, ' Score : ' + str(score) + ' ')
        win.addstr(0, 45, ' SNAKE GAME ')
        win.addstr(0, 80, ' Player : ' + name + ' ')
        win.timeout(150 - (len(snake) // 5 + len(snake) // 10) % 120)
        
        prevKey = key
        event = win.getch()
        if event == -1:
            key = key
        else:
            key = event


        if key == ord(' '):
            key = -1
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
            key = prevKey

        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        if snake[0][0] == 0:
            snake[0][0] = 28
        if snake[0][1] == 0:
            snake[0][1] = 98
        if snake[0][0] == 29:
            snake[0][0] = 1
        if snake[0][1] == 99:
            snake[0][1] = 1

        if snake[0] in snake[1:]:
            break

        if snake[0] == food:
            food = []
            score += 1
            while food == []:
                food = [randint(1, 28), randint(1, 98)]
                if food in snake:
                    food = []
            win.addch(food[0], food[1], curses.ACS_PI)
        else:    
            last = snake.pop()
            win.addch(last[0], last[1], ' ')
        win.addch(snake[0][0], snake[0][1], 'O')
        
    curses.endwin()
    print('\n... GAME OVER ...\n')

    if score in range(0, 10):
        print(f"Decent try {name}; But you're still a Beginner.")
        print(f"You've got a score of {score}.")
    elif score in range(10, 20):
        print(f"Good play {name}; You're not bad.")
        print(f"You've got a score of {score}.")
    elif score in range(20, 30):
        print(f"Very good play {name}; You're quite good at this game.")
        print(f"You've got a score of {score}.")
    elif score in range(30, 40):
        print(f"Excellent play {name}; You're very good at this game.")
        print(f"You've got a score of {score}.")
    elif score >= 40:
        print(f"Brilliant play {name}; You're an absolute PRO.")
        print(f"You've got a score of {score}.")

    choice = input('\nDo you want to play again ?(Y/N): ').upper()