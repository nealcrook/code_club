# accept a line of text from the user and "translate" it into pig latin
# two famous pig latin words: ixnay, amscray, 

text = input('Type something in and press ENTER: ')



# rules: http://en.wikipedia.org/wiki/Pig_Latin
# 1. take first consonant or consonant cluster, move it to the end and then add "ay"
# 2. for words that begin with a vowel, just add "ay" to the end

# if this had [] it would be a LIST. With () it is a TUPLE
vowels = ('a','e','i','o','u')

# work on the words, one at a time
def to_pig(text):
    igpay = ''
    words = text.split()
    for word in words:
        lc_word = word.lower()
        if lc_word.startswith( vowels ):
            igpay = igpay + word + 'ay '
        else:
            # better. Look for first vowel
            first_vowel = 0
            for letter in word:
                if letter.startswith(vowels):
                    # done!
                    break
                first_vowel = first_vowel + 1
            igpay = igpay + word[first_vowel:] + word[0:first_vowel] + 'ay '
    return igpay


# Extras
# 1. put the "for words.." loop into a procedure named to_pig. Remember that
# you will need to indent it (add spaces at the start of each line)
#
# 2. create a new procedure from_pig
#
# 3. test it by taking a sentence and translating it to and then from pig latin



exttay = to_pig(text)
print(exttay)

