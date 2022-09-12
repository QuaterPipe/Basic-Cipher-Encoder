import vig
import cea
import bea
#      #
#      #
# MAIN #
#      #
#      #

#In this cipher there are just raw funtions that do what they are told and the main functions run them in a way that they work#
print("Welcome to my viginere cipher! ")
print("Plaintext means the stuff that you enter that is not jumbled \nCiphertext means the jumbled up text you made\nKey means what you are jumbling the plaintext by \nEncrypt means that you jumble up plaintext by a key  \nDecrypt means that you unjumble ciphertext by the key")
print("\n\nSo basically how this works is that by encrypting this jumbles up the text with the key in a special way that if you try to decrypt and enter the key you will get back what you wrote")

def beadecrypt():
  #this is the iteration you have to go through to decrypt#
  text = input("Enter your encrypted text!: ")
  key = input("Enter your key!: ")
  #converts to list of nubers#
  key = bea.convnum(key)
  text = bea.convnum(text)
  #deciphers numbers#
  text = bea.decipher(key,text)
  #converts to text#
  text = bea.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  print("\"" + text + "\"" + " is your decrypted text!")

def beaencrypt():
  #this is the iteration you have to go throught to ecrypt#
  text = input("Enter your plaintext!: ")
  key = input("Enter your key!: ")
  #converts to list of nubers#
  key = bea.convnum(key)
  text = bea.convnum(text)
  #enciphers numbers#
  text = bea.encipher(key, text)
  #converts to text#
  text = bea.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  print("\"" + text + "\"" + " is your encrypted text!: ")



def vigdecrypt():
  #this is the iteration you have to go through to decrypt#
  text = input("Enter your encrypted text!: ")
  key = input("Enter your key!: ")
  #converts to list of nubers#
  key = vig.convnum(key)
  text = vig.convnum(text)
  #deciphers numbers#
  text = vig.decipher(key, text)
  #converts to text#
  text = vig.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  print("\"" + text + "\"" + " is your decrypted text!")

def vigencrypt():
  #this is the iteration you have to go throught to ecrypt#
  text = input("Enter your plaintext!: ")
  key = input("Enter your key!: ")
  #converts to list of numbers#
  key = vig.convnum(key)
  text = vig.convnum(text)
  #enciphers numbers#
  text = vig.encipher(key, text)
  #converts to text#
  text = vig.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  print("\"" + text + "\"" + " is your encrypted text!: ")
#stilll in  progress#
def vigencryptfile():
  fname  = input("Enter your filename")
  f = open("{}".format(fname) + ".txt","r")
  r = f.read()
  key = input("Enter your key!: ")
  text = vig.convnum(r)
  key = vig.convnum(key)
  text = vig.encipher(key,text)
  text= vig.convtext(text)
  text = str(text.upper())
  f = open("{}".format(fname) + ".txt","w")
  f.write(text)
  f.close()
#still in progress#
def vigdecryptfile():
  fname = input("Enter your filename: ")
  f = open("{}".format(fname) + ".txt", "r")
  r = f.read()
  key = input("Enter your key!: ")
  text = vig.convnum(r)
  key = vig.convnum(key)
  text = vig.decipher(key, text)
  text = vig.convtext(text)
  text = str(text.upper())
  f = open("{}".format(fname) + ".txt", "w")
  f.write(text)
  f.close() 

def ceadecrypt():
  text = input("Enter your encrypted text!: ")
  key = input("Enter your key!: ")
  key = cea.convnum(key)
  text = cea.convnum(text)
  text = cea.decipher(key, text)
  text = cea.convtext(text)
  text = str(text.upper())
  print("\"" + text + "\"" + " is your decrypted text!")

def ceaencrypt():
  #this is the iteration you have to go throught to ecrypt#
  text = input("Enter your plaintext: ")
  key = input("Enter your key: ")
  #converts to list of numbers#
  key = cea.convnum(key)
  text = cea.convnum(text)
   #enciphers numbers#
  text = cea.encipher(key, text)
  #converts to text#
  text = cea.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  print("\"" + text + "\"" + " is your encrypted text!: ")
def ceaautodecrypt():
  text = input("Enter your Encrypted text: ")
  print("It will brute force by shifting your text one by one and it will show all iterations")
  print("Do note this is not 100% accurate and may let your text slip through.")
  text = cea.convnum(text)
  ranges = cea.autodecipher(text)
  values = []
  #takes all the valus in the ranges dictionary and turn it into a list#
  for q in range(26):
    try:
      values.append(ranges[str(q)])
    except KeyError:
      pass
  #finds the shift from the greatest value in values#
  for x, y in ranges.items():
    try:
      if y == max(values):
        shift = x
        break
    except KeyError:
      pass
  #removes any null values in values#
  res = []
  rangv = ranges.values()
  rangk = ranges.keys()
  for x in range(len(values)):
    try:
      if values[x] == 0:
        del values[x]
    except IndexError:
      pass
  d = list(rangk)
  for i in range(26):
    try:
      if str(i) in d:
        temp = cea.encipher(d[i],text)
        res.append("With a shift of " + str(d[i]) + ": " + str(cea.convtext(list(temp))))
    except IndexError:
      pass
  for i in range(len(res)):
    print(res[i])
  print(" is your result!")

possibleInputs = {
  "bd": beadecrypt(),
  "be": beaencrypt(),
  "ca": ceaautodecrypt(),
  "cd": ceadecrypt(),
  "ce": ceaencrypt(),
  "vd": vigencrypt(), 
  "ve": vigencrypt(),
  "ybd": beadecrypt(),
  "ybe": beaencrypt(),
  "yca": ceaautodecrypt(),
  "ycd": ceadecrypt(),
  "yce": ceaencrypt(),
  "yvd": vigencrypt(), 
  "yve": vigencrypt(),
  "y":"y",
  "n":"n"
  }

while True:
  print("Would you like to use viginer, beafort, or ceaser cipher; 1,2,3: ")
  red = 0
  choice = input()
  red.brute