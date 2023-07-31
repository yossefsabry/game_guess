# import the random library
import random

list_guess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I use random.seed for stop random choose
# you can change the number of guess form random.seed(??)

random.seed(1)

z = random.choice(list_guess)

input_user = int(input("- guess the number :  "))

# while for the input if true the loop end if false the loop containe

while True:

    if input_user > z:

        print("- the number is lower than {} -".format(input_user))

        input_user = int(input("- guess the number :  "))

    elif input_user < z:

        print("- the number is higher than {} -".format(input_user))

        input_user = int(input("- guess the number :  "))

    else:

        print("- the guess '{}' is true  -".format(input_user))

        break
