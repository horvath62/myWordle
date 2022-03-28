

### WORDLE HELPER ###
print("<<<< SUPER WORDLE HELPER >>>>")

wordfile = "five_letter.txt"
wordfile = "english_words_350k.txt"
# Open english list of words, save to list
print("Opening Word File:", wordfile)
print("")
f = open(wordfile, 'r', encoding='utf-8')
words = f.readlines()
f.close()


# Make list of five letter words
w5 = []

for w in words:
    if len(w.strip()) == 5:
        #print(w)
        w5.append(w.strip())
#print(w5)


'''
fw = open("five_letter.txt", 'w')
for w in w5:
    fw.write(w)
    fw.write('\n')
fw.close()
'''





# Enter list of possible letter and possible locations (i.e. 1  thru 5 )
letterlist = []
letterdict = {}

while True:
    alphanumber = input("Enter Letter and Possible Positions (i.e. A125)\nEnter zero for position if not in word(i.e. A0?")
    if len(alphanumber) == 0:
        break
    letter = alphanumber[0].lower()
    letterlist.append(letter)
    locnumbers = alphanumber[1:]
    loclist = [int(a) for a in str(locnumbers)]
    letterdict[letter] = loclist
    print("")
    print("Enter Next Letter or Return when done")

#print(letterlist)
#print(letterdict)
print("")
print("LETTER CRITERIA:")
for letter in letterlist:
    print("Letter:", letter.upper(), "  Location: ", end="")
    for location in letterdict[letter]:
        print(location, end="")
    print("")


# Search five letter Word List for Words meeting criteria
validwords = []
wordcount = 0
for w in w5:
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
print("Matching Word Count:", wordcount)
print("")
i = 0
for w in validwords:
    print(w, " ", end="")
    i = i + 1
    if i % 10 == 0:
        print("")
print("")
print("")
print("Matching Word Count:", wordcount)

