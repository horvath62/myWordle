

### WORDLE HELPER ###
print("<<<< SUPER WORDLE HELPER >>>>")

wordfile = "20k_words.txt"
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

# Enter list of possible letter and legal locations (i.e. 1  thru 5 )
letterlist = []
letterdict = {}
while True:
    letter = input("Enter Single Lowercase Letter?")
    if len(letter) == 0:
        break
    letterlist.append(letter)
    locnumbers = input("Enter Possible Location (i.e. 125)?")
    loclist = [int(a) for a in str(locnumbers)]
    letterdict[letter] = loclist
    print("")
    print("Enter Next Letter or Return when done")

#print(letterlist)
#print(letterdict)
print("")
print("LETTER CRITERIA:")
for letter in letterlist:
    print("Letter:", letter, "  Location: ", end="")
    for location in letterdict[letter]:
        print(location, end="")
    print("")


# Search Word List for Words meeting criteria
validwords = []
wordcount = 0
for w in w5:
    wordtest = True
    for letter in letterlist:
        positiontest = False
        #print("letter:", letter)
        for position in letterdict[letter]:
            #print("  position:", position)
            if w[position-1] == letter:
                #print("      #### word:", w)
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


