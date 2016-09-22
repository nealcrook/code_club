# Birds on a wire
#

from random import randint

# wire[0] to wire [131]
wire_length = 132
wire = ["x"]*wire_length

def clear_wire():
    for i in range(0,wire_length):
        wire[i] = "_"

def print_wire():
    for i in range(0,wire_length-1):
        print(wire[i], end="")

def print_wire2():
    print("".join(wire))

# Try to add a bird at the position 'where'. If it's possible, return True
# and add the bird. If it's not possible, return False
def add_bird(where):
    if wire[where] == "_":
        if wire[where-1] == "_" or wire[where-1] == "^":
            if wire[where+1] == "_" or wire[where-1] == "^":
                # yes!
                wire[where] = "O"
                wire[where-1] = "^"
                wire[where+1] = "^"
                return True
    return False

# How many birds will fit on the wire?
def fill_wire():
    clear_wire()
    fitted = 0
    # try 600 times
    for attempt in range(0,300):
        # for wire_length=4
        # 0123
        # can't put a body at 0 or 3
        where = randint(1,wire_length-2)
        if add_bird(where):
            fitted = fitted + 1
    return fitted


# interactively, fill_wire()
# if you get an interesting result, print_wire2()

# Extras:

# write a loop to call fill_wire 100 times. After each time print
# the numberof birds and the wire.

# Extras: keep track the maximum number of birds and print it at the end

# Extras: no computer needed. What is the maximum number of birds that will fit
# on a wire. Hint: work it out for wires of length 3, 4, 5, 6 and infer a
# general rule.

