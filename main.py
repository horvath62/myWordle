import re
from myClass import *

### WORDLE HELPER ###
print("<<<< SUPER WORDLE HELPER >>>>")

wordfile_20k = "fiveletter_20k_trimmed.txt"
wordfile_71k = "fiveletter_71k.txt"
wordfile_350k= "fiveletter_350k.txt"

# Make list of five letter words
w20k = Wordlist([], "20K WORD FILE")
w20k.readwordfile(wordfile_20k)

w71k = Wordlist([], "71K WORD FILE")
w71k.readwordfile(wordfile_71k)

w350k = Wordlist([], "350k WORD LIST")
w350k.readwordfile(wordfile_350k)

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



# ###############  PROCESSES AND PRINT  ##########################

# Elimination Words.   That dont contain any of the letters.
validwords = []
wordcount = 0
for w in w20k.words:
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

w99title = "ELIMINATION WORD LIST (don't contain any of the letters):"
w99 = Wordlist(validwords,w99title)
w99.printwords(12, 1000)

print("")






wr20k = Wordlist(w20k.searchresults(letterlist, letterdict),"WORDS FROM 20K WORD LIST")
wr20k.printwords(16,1000)

wr71k = Wordlist(w71k.searchresults(letterlist, letterdict),"WORDS FROM 71K WORD LIST")
wr71k = Wordlist(wr71k.uniquewords(wr20k.words), "Unique Words from 71K word list")
wr71k.printwords(16,1000)

wr350k = Wordlist(w350k.searchresults(letterlist, letterdict),"WORDS FROM 350K WORD LIST")
wr350k = Wordlist(wr350k.uniquewords(wr71k.words), "Unique Words from 350K word list")
wr350k = Wordlist(wr350k.uniquewords(wr20k.words), "Unique Words from 350K word list")
wr350k.printwords(16,1000)

print("")
print("------------------------------")





