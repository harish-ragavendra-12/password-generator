#password generator
import random

def pswd_generator():

    letters = 'abcdef'
    numbers = '123456'
    symbols = '!@#$%^'

    while True:
        print('Choose your option:')
        print('1.letters only')
        print('2.letters and numbers')
        print('3.letters, numbers and symbols')

        option = int(input('Enter option: '))

        if option == 1:
            select_pool = letters
        elif option == 2:
            select_pool = letters + numbers
        elif option == 3:
            select_pool = letters + numbers + symbols
        else:
            print('Invalid option')
            continue

        empty_password = ''
        pswd_length = 8

        for i in range(pswd_length):
            rand_char = random.choice(select_pool)
            empty_password = empty_password + rand_char
        print('Generated password:',empty_password)
        break

pswd_generator()