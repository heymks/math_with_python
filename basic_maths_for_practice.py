import random as rnd
import sys

print('Please Enter the 1st No and 2nd No !')
print('At any time you want to abort, please enter abort !')
print('Enjoy Playing !')


def main():
    choice = input('''Please choose your Game
    For Addition > '+' 
    For Substraction > '-'
    For Multiplication > 'x'
    For F_Division > '//'
    For Division > '/'\n> ''')

    if choice == '+':
        addition()
    elif choice == '-':
        substraction()
    elif choice == '*':
        multiplication()
    elif choice == '//':
        f_division()
    elif choice == '/':
        division()
    elif choice == '':
        print('You need to choose a Game')
    else:
        sys.exit()


def addition():
    score = []

    num1 = input('1st No : ')
    if num1.lower() == 'abort':
        sys.exit()
    else:
        while not num1.isdigit():
            num1 = input('1st No : ')
        else:
            num1 = int(num1)

    num2 = input('2nd No : ')
    if num2.lower() == 'abort':
        sys.exit()
    else:
        while not num2.isdigit():
            num2 = input('2nd No : ')
        else:
            num2 = int(num2)

    num1_r = rnd.randint(num1, num2)
    num2_r = rnd.randint(num1, num2)

    print('>', num1_r, '+', num2_r)

    answer = input('> ')
    if answer.lower() == 'abort':
        sys.exit()
    else:
        while not answer.isdigit():
            answer = input('> ')
        else:
            answer = int(answer)

    while answer == num1_r + num2_r:
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)

        print('>', num1_r, '+', num2_r)

        answer = input('> ')
        if answer.lower() == 'abort':
            print(f'Thanks for playing !\nYour Score is {len(score)+1}')
            sys.exit()
        else:
            while not answer.isdigit():
                answer = input('> ')
            else:
                answer = int(answer)
                score.append(answer)

    else:
        print(f'Thanks for playing !\nYour Score is {len(score)}')


def substraction():
    score = []

    num1 = input('1st No : ')
    if num1.lower() == 'abort':
        sys.exit()
    else:
        while not num1.isdigit():
            num1 = input('1st No : ')
        else:
            num1 = int(num1)

    num2 = input('2nd No : ')
    if num2.lower() == 'abort':
        sys.exit()
    else:
        while not num2.isdigit():
            num2 = input('2nd No : ')
        else:
            num2 = int(num2)

    num1_r = rnd.randint(num1, num2)
    num2_r = rnd.randint(num1, num2)

    while num1_r < num2_r:
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)
    else:
        pass

    print('>', num1_r, '-', num2_r)

    answer = input('> ')
    if answer.lower() == 'abort':
        sys.exit()
    else:
        while not answer.isdigit():
            answer = input('> ')
        else:
            answer = int(answer)

    while answer == num1_r - num2_r:
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)

        while num1_r < num2_r:
            num1_r = rnd.randint(num1, num2)
            num2_r = rnd.randint(num1, num2)
        else:
            pass

        print('>', num1_r, '-', num2_r)

        answer = input('> ')
        if answer.lower() == 'abort':
            print(f'Thanks for playing !\nYour Score is {len(score)+1}')
            sys.exit()
        else:
            while not answer.isdigit():
                answer = input('> ')
            else:
                answer = int(answer)
                score.append(answer)

    else:
        print(f'Thanks for playing !\nYour Score is {len(score)}')


def multiplication():
    score = []

    num1 = input('1st No : ')
    if num1.lower() == 'abort':
        sys.exit()
    else:
        while not num1.isdigit():
            num1 = input('1st No : ')
        else:
            num1 = int(num1)

    num2 = input('2nd No : ')
    if num2.lower() == 'abort':
        sys.exit()
    else:
        while not num2.isdigit():
            num2 = input('2nd No : ')
        else:
            num2 = int(num2)

    num1_r = rnd.randint(num1, num2)
    num2_r = rnd.randint(num1, num2)

    print('>', num1_r, 'x', num2_r)

    answer = input('> ')
    if answer.lower() == 'abort':
        sys.exit()
    else:
        while not answer.isdigit():
            answer = input('> ')
        else:
            answer = int(answer)

    while answer == num1_r * num2_r:
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)

        print('>', num1_r, 'x', num2_r)

        answer = input('> ')
        if answer.lower() == 'abort':
            print(f'Thanks for playing !\nYour Score is {len(score)+1}')
            sys.exit()
        else:
            while not answer.isdigit():
                answer = input('> ')
            else:
                answer = int(answer)
                score.append(answer)

    else:
        print(f'Thanks for playing !\nYour Score is {len(score)}')


def f_division():
    score = []

    num1 = input('1st No : ')
    if num1.lower() == 'abort':
        sys.exit()
    else:
        while not num1.isdigit():
            num1 = input('1st No : ')
        else:
            num1 = int(num1)

    num2 = input('2nd No : ')
    if num2.lower() == 'abort':
        sys.exit()
    else:
        while not num2.isdigit():
            num2 = input('2nd No : ')
        else:
            num2 = int(num2)

    num1_r = rnd.randint(num1, num2)
    num2_r = rnd.randint(num1, num2)

    while num1_r < num2_r:
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)
    else:
        pass

    print('>', num1_r, '/', num2_r)

    answer = input('> ')
    if answer.lower() == 'abort':
        sys.exit()
    else:
        while not answer.isdigit():
            answer = input('> ')
        else:
            answer = int(answer)

    while answer == num1_r // num2_r:
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)

        while num1_r < num2_r:
            num1_r = rnd.randint(num1, num2)
            num2_r = rnd.randint(num1, num2)
        else:
            pass

        print('>', num1_r, '/', num2_r)

        answer = input('> ')
        if answer.lower() == 'abort':
            print(f'Thanks for playing !\nYour Score is {len(score)+1}')
            sys.exit()
        else:
            while not answer.isdigit():
                answer = input('> ')
            else:
                answer = int(answer)
                score.append(answer)

    else:
        print(f'Thanks for playing !\nYour Score is {len(score)}')


def division():
    score = []

    num1 = input('1st No : ')
    if num1.lower() == 'abort':
        sys.exit()
    else:
        while not num1.isdigit():
            num1 = input('1st No : ')
        else:
            num1 = int(num1)

    num2 = input('2nd No : ')
    if num2.lower() == 'abort':
        sys.exit()
    else:
        while not num2.isdigit():
            num2 = input('2nd No : ')
        else:
            num2 = int(num2)

    num1_r = rnd.randint(num1, num2)
    num2_r = rnd.randint(num1, num2)

    while num1_r < num2_r:
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)
    else:
        pass

    print('>', num1_r, '/', num2_r)

    answer = input('> ')
    if answer.lower() == 'abort':
        sys.exit()
    else:
        try:
            answer = float(answer)
        except ValueError:
            pass

        while type(answer) != float:
            try:
                answer = input()
                answer = float(answer)
            except ValueError:
                pass
        else:
            answer = float(answer)

    while answer == round(num1_r / num2_r, 1):
        num1_r = rnd.randint(num1, num2)
        num2_r = rnd.randint(num1, num2)

        while num1_r < num2_r:
            num1_r = rnd.randint(num1, num2)
            num2_r = rnd.randint(num1, num2)
        else:
            pass

        print('>', num1_r, '/', num2_r)

        answer = input('> ')
        if answer.lower() == 'abort':
            print(f'Thanks for playing !\nYour Score is {len(score)+1}')
            sys.exit()
        else:
            try:
                answer = float(answer)
            except ValueError:
                pass

            while type(answer) != float:
                try:
                    answer = input()
                    answer = float(answer)
                except ValueError:
                    pass
            else:
                answer = float(answer)
                score.append(answer)

    else:
        print(f'Thanks for playing !\nYour Score is {len(score)}')


main()
