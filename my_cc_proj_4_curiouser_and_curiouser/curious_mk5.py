# alice

import string

file = open('alice.txt')
lines = file.readlines()
file.close()

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



keys = wordlist.keys()


# fix problem 3: sort the keys before printing them.
## PRINT ALL THE WORDS THAT ARE ONLY USED N times
for key in sorted(keys):
    if wordlist[key] >= 500:
        print(key + " occurs " + str(wordlist[key]) + " times")


for line in lines:
    words = line.split()
    for word in words:
        if word == "cat":
                print (line)



# what is the longest word.
length = 0
word = ""
for key in sorted(keys):
    if len(key) > length:
        # longest so far
        length = len(key)
        word = key

# if there are several of the same length, we will just have the first one
print("longest word is " + word)


# all the words more than 11 letters long
for key in sorted(keys):
    if len(key) > 11:
        print (key)
