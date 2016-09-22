# Modelling solution to the Monty Hall problem in PYTHON

from random import choice

# tactic: what to do when offered
#         1 -> keep "pick"
#         2 -> pick at random from closed doors
#         3 -> swap to other closed door
# messages: True if you want messages printed to show what's going on
def play(tactic, messages):
    doors = [1,2,3]

    # make our first choice of door
    pick = choice(doors)

    # pick which door the prize will be behind
    prize = choice(doors)   

    if messages:
        print("Run for pick = " + str(pick) + ", tactic = " + str(tactic));

    # The host will open a door. The host KNOWS WHERE THE PRIZE IS!!
    can_open = [1,2,3]

    # The host will NOT open the door with the prize behind it.
    can_open.remove(prize)

    # The host will NOT open the door you have chosen
    # .. but that might be the one with the prize behind it; we will
    # get an error if we try to remove it again, so need to check first
##    if (prize != pick):
    can_open.remove(pick)

    if messages:
        print("Host is going to open one of these:" + str(can_open))

    opens = choice(can_open)

    if messages:
        print("Host has opened door " + str(opens))

    # These are the doors that are still closed
    closed = [1,2,3]
    closed.remove(opens)

    new_pick = 0

    if tactic == 1:
        new_pick = pick
    elif tactic == 2:
        new_pick = choice(closed)
    else:
        # tactic must be 3
        closed.remove(pick)
        # can only be one door left - the one we want
        new_pick = closed[0]

    # how did we do?
    if new_pick == prize:
        return True
    return False

for tactic in range(1,4):
    success = 0
    for i in range(0, 1000):
        if play(tactic, False):
            success = success + 1
    print("For tactic " + str(tactic) + " won the prize " + str(success) + " times")
    
