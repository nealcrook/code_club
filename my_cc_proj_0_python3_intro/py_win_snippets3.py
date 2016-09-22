# This is a comment. Any text after the comment character, which is
# usually called "hash" is ignored.

# Little snippets of python

# printing
print ("Welcome to python")

# 'name' is a variable
name = "Walkers Crisps"
print ("Hello my name is " + name)


# get user input
print ("What is your name")
your_name = input()

# comparison
print ("Hello " + your_name)
if (your_name == "Walkers Crisps"):
    print ("(But I doubt that really is your name)")

# "def" is short for "define" and is a way of bundling some code together
def who():
    print ("I am named Walkers Crisps, what is your name?")
    your_name = input()
    print ("Hello " + your_name)
    if (your_name == "Walkers Crisps"):
        print ("What an amazing coincidence!")


# now I can do that over and again very simply
who()
who()

# Back at the ">>>" prompt all those "def" things are remembered. For example
# you can type: who() to run that fragment of code again


# a loop
for i in range(0, 10):
    print ("Looping and my loop variable i is " + str(i))

# you can tell def to expect some information when it runs
# and you can tell it to return some information
def add_2(a_number):
    return 2 + a_number

print (add_2(2))
print (add_2(3))


# use some pre-build code from a "library" of code
from random import randint

def dice():
    num = randint(1,6)
    return num

for i in range(0, 100):
    print (dice(), end='')

print()

# lists
colours = ["red", "green", "orange", "purple", "yellow"]


print (colours)
print (colours[1])
print (colours[0])


def guess():
    print ("I have thought of a number between 1 and 100. Try to guess it")
    num = randint(1,100)
    tries = 0
    guess = -1
    while guess != num:
        tries = tries + 1
        print ("What is your guess",)
        guess = int(input())
        if guess > num:
            print ("Too high")
        elif guess < num:
            print ("Too low")
    print ("Correct! It took you " + str(tries) + " guesses")


def birthday1(name):
    for i in range(0,4):
        if (i==2):
            print ("Happy birthday dear " + name)
        else:
            print ("Happy birthday to you")


def birthday2(name):
    print ("Happy birthday to you")
    print ("Happy birthday to you")
    print ("Happy birthday dear " + name)
    print ("Happy birthday to you")
           


