# alice

file = open('alice.txt')
lines = file.readlines()
file.close()

count = 0
for line in lines:
    count = count + 1

print("There are " + str(count) + " lines in the file")
