import random

# ceil = 100
# floor = 0
# guess = 0
# number_of_guess = 0

def guess_a_number(guessed_number) :
    ceil = 100
    floor = 0
    guesser = 0
    number_of_guess = 0
    
    while guesser != guessed_number :
        number_of_guess += 1
        guesser = random.randint(floor, ceil)
        if guesser < guessed_number : floor = guesser
        if guesser > guessed_number : ceil = guesser

    return [guesser, number_of_guess]

print(guess_a_number(87))
print(guess_a_number(60))