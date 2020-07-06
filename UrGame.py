
""" This is a Python script for running the ancient game of Ur. As I write this
on 05/07/2020, before actually coding anything, I hope it's not going to be too
complicated, but then again, you never know...
"""

from numpy.random import binomial

def roll_dice():

    """ In Ur, instead of rolling one die (such as a D6, for example), you roll
    four D4s, each of which has two dotted corners and two blank corners. Your
    roll is then the sum of the number of dotted corners that land upwards.

    Probabilistically, this is the equivalent of flipping four fair coins and
    taking your roll to be the number of heads; in other words, the dice rolls
    follow a Binomial(4, 0.5) distribution (as opposed to a normal D6 dice roll,
    which follows a Uniform(1/6) distribution).

    Explicitly, the distribution is as follows:

        P(X = 0) = 0.0625
        P(X = 1) = 0.25
        P(X = 2) = 0.375
        P(X = 3) = 0.25
        P(X = 4) = 0.0625

    Note here that X represents the roll outcome, which this function returns.

    """

    return int(binomial(4, 0.5, 1))

print(roll_dice())
