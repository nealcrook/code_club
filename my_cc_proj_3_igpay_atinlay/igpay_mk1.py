# accept a line of text from the user and "translate" it into pig latin

text = input("Type something in and press ENTER: ")

# break the line of text into space-separated elements and put them into
# a list, named words
words = text.split()

# print the elements out one at a time
for word in words:
    print(word)

