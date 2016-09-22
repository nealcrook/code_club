# alice

file = open('alice.txt')
lines = file.readlines()
file.close()

# Put EVERY word in this book into its own "bucket" and count the number of
# times that it occurred.

# For this we use a thing that Python calls a "dictionary"
wordlist = {}

for line in lines:
    words = line.split()
    for word in words:
        if word in wordlist:
            wordlist[word] = wordlist[word] + 1
        else:
            wordlist[word] = 1

keys = wordlist.keys()
for key in keys:
    print(key + " occurs " + str(wordlist[key]) + " times")

# there's a lot of output.. use CTRL-S to pause it
# use CTRL-C to stop!!

# 1. treats lower and upper case as different
# 2. treats punctuation as part of the word
# 3. the "keys" are in no particular order

#Duchess,occurs 8 times
#Duchess.occurs 3 times
#Duchess)occurs 1 times
#Duchess'occurs 1 times
#Duchess!occurs 3 times
