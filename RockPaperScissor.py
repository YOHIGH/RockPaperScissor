import random
import os
import time


while True:
    os.system('cls||clear')
    try:
        mylist = ['ROCK', 'PAPER', 'SCISSOR']
        Bot = random.choice(mylist)
        print("Let's play ROCK PAPER SCISSOR\n\nChoose your option\n1)ROCK\n2)PAPER\n3)SCISSOR\n")
        inp = int(input("Enter your choice=>"))

        if inp == 1:
            if 'ROCK' == Bot:
                print("\nTIE.Try again")
            else:
                if Bot == 'PAPER':
                    print("\nAh! Your Rock lost against Paper")
                else:
                    print("\nOh! You won against Scissor")

        if inp == 2:
            if 'PAPER' == Bot:
                print("\nTIE.Try again")
            else:
                if Bot == 'ROCK':
                    print("\nOh! Your PAPER won against Rock")
                else:
                    print("\nAh! You lost against Scissor")

        if inp == 3:
            if 'SCISSOR' == Bot:
                print("\nTIE.Try again")
            else:
                if Bot == 'PAPER':
                    print("\nOh! Your Scissor won against Paper\n")
                else:
                    print("\nAh! You lost against Rock\n")
        if inp < 1 or inp > 3:
            print('\n"invalid choice"\n')
        print("========================================")
        print("Want to play more!? Type 'play'")
        Taken_inp = input('=>')
        if Taken_inp == 'play':
            pass
        else:
            break
    except:
        print('Invalid argument')
        time.sleep(1)
