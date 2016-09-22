# accept a line of text from the user and "translate" it into pig latin
# two famous pig latin words: ixnay, amscray, 

text = input("Type something in and press ENTER: ")

# break the line of text into space-separated elements and put them into
# a list, named words
words = text.split()


# rules: http://en.wikipedia.org/wiki/Pig_Latin
# 1. take first consonant or consonant cluster, move it to the end and then add "ay"
# 2. for words that begin with a vowel, just add "ay" to the end

# if this had [] it would be a LIST. With () it is a TUPLE
vowels = ('a','e','i','o','u')

# work on the words, one at a time
for word in words:
    lc_word = word.lower()
    if lc_word.startswith( vowels ):
        print (word + "ay ")
    else:
        # simple (works for some words)
        pig_word = word[1:] + word[0] + "ay"
        print (pig_word)       


#        where = 0
#        for letter in word:
#            if letter.startswith(vowels):
#                # done!
#            where = where + 1
            


    
    

