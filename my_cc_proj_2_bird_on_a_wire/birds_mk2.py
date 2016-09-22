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


# test it..
print_wire2()
clear_wire()
print_wire2()

