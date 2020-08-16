import random
def primary():
#  print("Keep it logically awesome.")
  
  file_object = open("quotes.txt", "a+")
  file_object.write("\n")
  file_object.write ("There is no substitute for hard work.")
  file_object.close()

  f = open("quotes.txt")
  quotes = f.readlines() # stored in an array
  f.close()


  last = 13
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__": # don't change this
  primary() # can change what the main function is named
