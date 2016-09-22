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

# Try to fit a bird at the position 'where'. If it's possible, return TRUE
# and add the bird. If it's not possible, return FALSE
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




# test it..
print_wire2()
clear_wire()
print_wire2()
add_bird(30)
print_wire2()
add_bird(31)
print_wire2()
add_bird(32)
print_wire2()
# try testing at the command line


