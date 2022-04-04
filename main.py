import re

### WORDLE HELPER ###
print("<<<< SUPER WORDLE HELPER >>>>")

wordfile_common = "five_letter.txt"
wordfile_big = "five_letter_350k.txt"
# Open english list of words, save to list
print("Opening Word File:", wordfile_common)
print("Opening Word File:", wordfile_big)
print("")
f = open(wordfile_common, 'r', encoding='utf-8')
words_common = f.readlines()
f.close()

f = open(wordfile_big, 'r', encoding='utf-8')
words_big = f.readlines()
f.close()


# Make list of five letter words
wordscommon = []
wordsbig=[]

for w in words_common:
    if len(w.strip()) == 5:
        #print(w)
        wordscommon.append(w.strip())

for w in words_big:
    if len(w.strip()) == 5:
        #print(w)
        wordsbig.append(w.strip())


'''
#print back filtered words
fw = open("five_letter_350k.txt", 'w')
for w in words:
    fw.write(w)
    fw.write('\n')
fw.close()
'''

# Enter list of possible letter and possible locations (i.e. 1  thru 5 )
letterlist = []
letterdict = {}

print("Enter Letter followed by possible positions (i.e. A125)")
print("Enter zero for position if not in word (i.e. A0)")
print("Enter multiple letter not in word (i.e. BCSZ)")
print("Enter Return when done")
print("")

while True:
    alphanumber = input("Enter Letter Positions (i.e.A125 or A0)?")
    if len(alphanumber) == 0:
        break
    if len(alphanumber) == 1:
        #single char, elimination
        letter = alphanumber[0].lower()
        letterlist.append(letter)
        letterdict[letter] = [0]
    else:
        # more than one char
        if alphanumber[1].isdigit():
            #second char is a number
            letter = alphanumber[0].lower()
            letterlist.append(letter)
            locnumbers = alphanumber[1:]
            loclist = [int(a) for a in str(locnumbers)]
            letterdict[letter] = loclist
        else:
            #second number is not number, elimination list
            for letter in alphanumber:
                letterlist.append(letter.lower())
                letterdict[letter] = [0]



#print(letterlist)
#print(letterdict)
print("")
print("LETTER CRITERIA:")
print("Letter:  Position:")
for letter in letterlist:
    print(letter.upper(), '       ', end="")
    for location in letterdict[letter]:
        print(location, end="")
    print("")


# Search five letter Common Word List for Words meeting criteria
validwords = []
wordcount = 0
for w in wordscommon:
    wordtest = True
    for letter in letterlist:
        #print("letter:", letter)
        loclist = letterdict[letter]

        if loclist[0] == 0:
            positiontest = True
            for position in range(5):
                #print("  position:", position)
                if w[position-1] == letter:
                    positiontest = False

        else:
            positiontest = False
            for position in loclist:
                if w[position-1] == letter:
                    positiontest = True

        if positiontest == False:
            wordtest = False

    if wordtest == True:
        validwords.append(w)
        wordcount = wordcount + 1

# Print Results
print("")
print("MATCHING WORDS FROM 20k WORD LIST:", wordcount, "WORDS")
i = 0
for w in validwords:
    print(w, " ", end="")
    i = i + 1
    if i % 10 == 0:
        print("")
print("")

# Elimination Words.   That dont contain any of the letters.
validwords = []
wordcount = 0
for w in wordscommon:
    wordtest = False
    for letter in letterlist:
        #print("letter:", letter)
        positiontest = False
        for position in range(5):
            #print("  position:", position)
            if w[position-1] == letter:
                positiontest = True

        if positiontest == True:
            wordtest = True

    if wordtest == False:
        if wordcount < 50:
            validwords.append(w)
            wordcount = wordcount + 1

# Print Results
print("")
print("ELIMINATION WORD LIST:  ", wordcount, " Words that don't contain any of the letters")
i = 0
for w in validwords:
    print(w, " ", end="")
    i = i + 1
    if i % 10 == 0:
        print("")
print("")





# Search five letter Big Word List for Words meeting criteria
validwords = []
wordcount = 0
for w in wordsbig:
    wordtest = True
    for letter in letterlist:
        #print("letter:", letter)
        loclist = letterdict[letter]

        if loclist[0] == 0:
            positiontest = True
            for position in range(5):
                #print("  position:", position)
                if w[position-1] == letter:
                    positiontest = False

        else:
            positiontest = False
            for position in loclist:
                if w[position-1] == letter:
                    positiontest = True

        if positiontest == False:
            wordtest = False

    if wordtest == True:
        validwords.append(w)
        wordcount = wordcount + 1

# Print Results
print("")
print("MATCHING WORDS FROM 350K WORD LIST:", wordcount, "WORDS")
i = 0
for w in validwords:
    print(w, " ", end="")
    i = i + 1
    if i % 10 == 0:
        print("")


