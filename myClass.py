class Wordlist:
  def __init__(self, words, title ):
      self.words = words
      self.title = title

  def printwords(self, numcols):
      print("##########")
      print(self.title, " ", len(self.words), " Words" )
      i=0

      for w in self.words:
          print(w, " ", end="")
          i = i + 1
          if i % numcols == 0:
            print("")

      print("")
      print("##########")

