# alice

file = open('alice.txt')
lines = file.readlines()
file.close()

line_count = 0
word_count = 0
alice_count = 0
for line in lines:
    line_count = line_count + 1
    words = line.split()
    for word in words:
        word_count = word_count + 1
        if word.lower() == "alice":
            alice_count = alice_count + 1

print("There are " + str(line_count) + " lines in the file")
print("There are " + str(word_count) + " words in the file")
print("There are " + str(alice_count) + " occurrences of the word alice in the file")

# I think you will agree that it "read" the book quite quickly!
