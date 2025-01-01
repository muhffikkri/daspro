import random

def guess_a_number(guessed_number: int) -> list:
    """
    Guess a number between 0 and 100 and return the guessed number and the number of guesses.

    :param guessed_number: The number to be guessed.
    :type guessed_number: int
    :return: A list containing the guessed number and the number of guesses.
    :rtype: list

    :example:
    >>> guess_a_number(87)
    [87, <number_of_guesses>]

    :raises ValueError: If guessed_number is not between 0 and 100.
    """
    if not (0 <= guessed_number <= 100):
        raise ValueError("guessed_number must be between 0 and 100")

    ceil = 100
    floor = 0
    guesser = 0
    number_of_guess = 0
    
    while guesser != guessed_number:
        number_of_guess += 1
        guesser = random.randint(floor, ceil)
        if guesser < guessed_number:
            floor = guesser
        if guesser > guessed_number:
            ceil = guesser

    return [guesser, number_of_guess]

if __name__ == "__main__" : 
    print(guess_a_number(87))
    print(guess_a_number(60))