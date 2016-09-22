# alice

import string

file = open('alice.txt')
lines = file.readlines()

# Put EVERY word in this book into its own "bucket" and count the number of
# times that it occurred.

# For this we use a thing that Python calls a "dictionary"
wordlist = {}


for line in lines:
    # fix problem 1: change everything to lower case
    line = line.lower()

    # fix problem 2: get rid of all the punctuation
    for c in string.punctuation:
        line=line.replace(c," ")
    
    words = line.split()
    for word in words:
        if word in wordlist:
            wordlist[word] = wordlist[word] + 1
        else:
            wordlist[word] = 1


file.close()

keys = wordlist.keys()

# fix problem 3: sort the keys before printing them.
for key in sorted(keys):
    print(key + " occurs " + str(wordlist[key]) + " times")



# there's a lot of output.. use CTRL-S to pause it
# use CTRL-C to stop!!

# the keys are in no particular order



#Duchess,occurs 8 times
#Duchess.occurs 3 times
#Duchess)occurs 1 times
#Duchess'occurs 1 times
#Duchess!occurs 3 times



# How many different words are used
# How many words are used just once
# What word is used most often - and how many times is it used?




