

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
print("Enter Return when done")
print("")

while True:
    alphanumber = input("Enter Letter Positions (i.e.A125 or A0)?")
    if len(alphanumber) == 0:
        break
    letter = alphanumber[0].lower()
    letterlist.append(letter)
    locnumbers = alphanumber[1:]
    loclist = [int(a) for a in str(locnumbers)]
    letterdict[letter] = loclist

#print(letterlist)
#print(letterdict)
print("")
print("LETTER CRITERIA:")
for letter in letterlist:
    print("Letter:", letter.upper(), "  Location: ", end="")
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
print("Matching Word Count from Common Word List:", wordcount)
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
print("Matching Word Count from 350K word list:", wordcount)
i = 0
for w in validwords:
    print(w, " ", end="")
    i = i + 1
    if i % 10 == 0:
        print("")


