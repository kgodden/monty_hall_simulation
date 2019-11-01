#! /usr/bin/python

import random

"""
    Simulates the Monty Hall problem with 3 doors

    The Monty Hall problem is a very (to me at least) counter-intuitive probability mind experiment which
    contorts my brain and fascinates me at the same time. I can just about understand the
    probabilistic arguments, but I still find it confusing.  This program is an experimental
    simulator to see what numbers we get when the player decides to stick or switch.

    If you are having problems understanding the outcome, I find it helps to imagine that there
    are a million doors rather than 3.  After you choose your door (1/1,000,000 chance of hiding the car)
    Monty opens up 999,998 doors that hide goats to leave one door still closed.  Now which door do you think
    is most likely to hide the car? The one you choose, or the one that Monty avoided opening while
    he opened all 999,998 other doors?!  It seems obvious to me that the other door that Monty left un opened
    has a massively higher chance of hiding the door than the original choice!  As N reduces to 3 this
    obviousness reduces greatly however!

    Summary:
    --------

    There are 3 doors, behind one lies a car, while behind the other two are goats.
    A player chooses a door at random.  Monty then opens one of the other doors to show that
    there is no car behind it.  Monty asks the player if they would like to stick with their
    door or switch to the other un-opened door.

    If the player sticks with their door then their chance of winning the car should be 1/3
    If the player switches door then their chances of winning the car increases to 2/3!!!

    For more info: https://en.wikipedia.org/wiki/Monty_Hall_problem
"""

def pick_random_door():
    """
    Pick a door at 'random', doors are 0-indexed so this will
    return a number between 0 and door_count - 1

    :return: the chosen door
    """

    return random.randint(0, 3 - 1)

def pick_monty_door(car_door, my_guess):
    """
    Pick a door for Monty to open,
    Monty opens up the first door that doesn't
    have a car and that play hasn't already chosen...

    :param car_door: The door behind which the car resides
    :param my_guess: The door which the play choose
    :return: The index of the door that Monty opens
    """

    for d in range(0, 3):
        if d == car_door:
            continue

        if d == my_guess:
            continue

        return d

def pick_other_door(my_guess, monty_door):
    """
    The player has chosen to switch their chosen door, so we
    need to pick another one for them.  We pick the door that

    a.) Doesn't match the player's original guess
    b.) Wasn't chosen by Monty

    :param my_guess:
    :param monty_door:
    :return: The other door's index
    """

    for d in range(0, 3):
        if d == my_guess:
            continue

        if d == monty_door:
            continue

        return d

def run_game():
    """
    Run a single game

    :return:  win/loose --> True/False
    """

    # Should the player switch their guess or stick
    # with their original one?
    switch = True

    # Pick the door with the car
    car_door = pick_random_door()
    print("Car is behind door %d" % car_door)

    # Player chooses a door
    my_guess = pick_random_door()
    print("Player has guessed door %d" % my_guess)

    # Monty opens up a door that doesn't have a
    # car behind it.
    monty_door = pick_monty_door(car_door, my_guess)
    print("Monty opens door %d" % monty_door)

    # Does the player switch doors after Monty
    # opens his??
    if switch:
        my_guess = pick_other_door(my_guess, monty_door)
        print("Player switches to door %d" % my_guess)

    if my_guess == car_door:
        print("Player wins!")
    else:
        print("Player looses ;-(")

    return my_guess == car_door

def run_games():
    wins = 0
    game = 0

    game_count = 10000

    while game < game_count:
        game += 1

        # Run a game and see if we win!
        if run_game():
            wins += 1

    print("Games: %d" % game)
    print("Wins: %d" % wins)

    print("------------------------------")

    if wins == 0:
        print("you didn't win any games!")
    else:
        win_rate = wins / game
        print("Win rate: %f" % win_rate)

if __name__ == "__main__":
    run_games()