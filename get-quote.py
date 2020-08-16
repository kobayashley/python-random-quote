def primary():
#  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines() # stored in an array
  f.close()

  print(quotes[13])

if __name__== "__main__": # don't change this
  primary() # can change what the main function is named
