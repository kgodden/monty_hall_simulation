#! /usr/bin/python

#   Copyright 2019 Kevin Godden
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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
    has a massively higher chance of hiding the car than the original choice!  As N reduces to 3 this
    obviousness reduces greatly however!  This simulation can be run with more than 3 doors to experiment
    with this...

    Summary:
    --------

    There are 3 doors, behind one lies a car, while behind the other two are goats.
    A player chooses a door at random.  Monty then opens one of the other doors to show that
    there is no car behind it.  Monty asks the player if they would like to stick with their
    door or switch to the other un-opened door.

    If the player sticks with their door then their chance of winning the car should be 1/3
    If the player switches door then their chances of winning the car increases to 2/3!!!

    If you want to run the game with more doors to see how the probabilities change
    just change the door_count value below.

    For more info: https://en.wikipedia.org/wiki/Monty_Hall_problem
"""

# Should the player switch their guess or stick
# with their original one?
switch = True

# The number of doors in the game, should be 3 for
# the problem as normally stated.
door_count = 3

# The number of times to run the simulation
game_count = 10000

# Should we print lots of messages?
# If door_count is large change this to True to
# make simulation run faster.
quiet = False

def pick_random_door():
    """
    Pick a door at 'random', doors are 0-indexed so this will
    return a number between 0 and door_count - 1

    :return: the chosen door
    """

    return random.randint(0, door_count - 1)

def pick_monty_doors(car_door, players_guess):
    """
    Pick the doors for Monty to open, of the number
    of doors is 3 then Monty opens up the first door that doesn't
    have a car and that play hasn't already chosen...

    If door_count > 3 then Monty will open up all of the doors
    that hide goats avoiding the door that has been already picked

    :param car_door: The door behind which the car resides
    :param players_guess: The door which the play choose
    :return: A list of the indices of the doors that Monty opens
    """

    monty_doors = []

    for d in range(0, door_count):

        if len(monty_doors) == door_count - 2:
            break

        if d == car_door:
            continue

        if d == players_guess:
            continue

        monty_doors.append(d)

    return monty_doors

def pick_other_door(players_guess, monty_doors):
    """
    The player has chosen to switch their chosen door, so we
    need to pick another one for them.  We pick the door that

    a.) Doesn't match the player's original guess
    b.) Wasn't chosen by Monty

    :param players_guess:  The door that the player originally picked
    :param monty_doors: The doors that Monty has opened (usually just 1)
    :return: The other door's index
    """

    for d in range(0, door_count):

        # Can't switch to the player's original guess
        if d == players_guess:
            continue

        # Don;t pick a door that Monty has opened
        if d in monty_doors:
            continue

        return d

def run_game():
    """
    Run a single game

    :return:  win/loose --> True/False
    """

    # Pick the door with the car
    car_door = pick_random_door()

    if not quiet:
        print("Car is behind door %d" % car_door)

    # Player chooses a door
    players_guess = pick_random_door()

    if not quiet:
        print("Player has guessed door %d" % players_guess)

    # Monty opens up a door that doesn't have a
    # car behind it.
    monty_doors = pick_monty_doors(car_door, players_guess)

    if not quiet:
        print("Monty opens: " + str(monty_doors))

    # Does the player switch doors after Monty
    # opens his??
    if switch:
        players_guess = pick_other_door(players_guess, monty_doors)

        if not quiet:
            print("Player switches to door %d" % players_guess)

    if not quiet:
        if players_guess == car_door:
            print("Player wins!")
        else:
            print("Player looses ;-(")

    return players_guess == car_door

def run_games():
    wins = 0
    game = 0

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