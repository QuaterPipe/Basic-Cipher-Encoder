import bea
import cae
import vig
import re
import time

def beadecrypt():
  #this is the iteration you have to go through to decrypt#
  print("Enter your encrypted text!")
  text = input(">>>")
  print("Enter your key!")
  key = input(">>>")
  tic = time.perf_counter()
  #converts to list of nubers#
  key = bea.convnum(key)
  text = bea.convnum(text)
  #deciphers numbers#
  text = bea.decipher(key,text)
  #converts to text#
  text = bea.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  toc = time.perf_counter()
  print("\"" + text + "\"" + " is your decrypted text!")
  print("Excecuted successfully in {0} seconds!".format(round(tic - toc, 2)))

def beaencrypt():
  #this is the iteration you have to go throught to ecrypt#
  print("Enter your plaintext!")
  text = input(">>>")
  print("Enter your key!")
  key = input(">>>")
  tic = time.perf_counter()
  #converts to list of nubers#
  key = bea.convnum(key)
  text = bea.convnum(text)
  #enciphers numbers#
  text = bea.encipher(key, text)
  #converts to text#
  text = bea.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  toc = time.perf_counter()
  print("\"" + text + "\"" + " is your encrypted text!: ")
  print("Excecuted successfully in {0} seconds!".format(round(tic - toc, 2)))



def vigdecrypt():
  #this is the iteration you have to go through to decrypt#
  print("Enter your encrypted text!")
  text = input(">>>")
  print("Enter your key!")
  key = input(">>>")
  tic = time.perf_counter()
  #converts to list of nubers#
  key = vig.convnum(key)
  text = vig.convnum(text)
  #deciphers numbers#
  text = vig.decipher(key, text)
  #converts to text#
  text = vig.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  toc = time.perf_counter()
  print("\"" + text + "\"" + " is your decrypted text!")
  print("Excecuted successfully in {0} seconds!".format(round(tic - toc, 2)))

def vigencrypt():
  #this is the iteration you have to go throught to ecrypt#
  print("Enter your plaintext!")
  text = input(">>>")
  print("Enter your key!")
  key = input(">>>")
  tic = time.perf_counter()
  #converts to list of numbers#
  key = vig.convnum(key)
  text = vig.convnum(text)
  #enciphers numbers#
  text = vig.encipher(key, text)
  #converts to text#
  text = vig.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  toc = time.perf_counter()
  print("\"" + text + "\"" + " is your encrypted text!: ")
  print("Excecuted successfully in {0} seconds!".format(round(tic - toc, 2)))
  
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

def caedecrypt():
  #this is the iteration you have to go throught to decrypt#
  print("Enter your encrypted text!")
  text = input(">>>")
  print("Enter your shift!")
  key = input(">>>")
  tic = time.perf_counter()
  #converts to list of numbers#
  text = cae.convnum(text)
  #enciphers numbers#
  text = cae.decipher(list(key), text)
  #converts to text#
  text = cae.convtext(text)
  #makes all letters in string capital#
  text = str(text.upper())
  toc = time.perf_counter()
  print("\"" + text + "\"" + " is your decrypted text!")
  print("Excecuted successfully in {0} seconds!".format(round(tic - toc, 2)))

def caeencrypt():
  #this is the iteration you have to go throught to encrypt#
  print("Enter your plaintext!")
  text = input(">>>")
  print("Enter your shift!")
  key = input(">>>")
  tic = time.perf_counter()
  #converts to list of numbers#
  text = cae.convnum(text)
   #enciphers numbers#
  text = cae.encipher(list(key), text)
  #converts to text#
  text = cae.convtext(text)
  text = re.sub(")", "\s",text)
  #makes all letters in string capital#
  text = str(text.upper())
  toc = time.perf_counter()
  print("\"" + text + "\"" + " is your encrypted text!: ")
  print("Excecuted successfully in {0} seconds!".format(round(tic - toc, 2)))

def caeautodecrypt():
  text = input("Enter your Encrypted text: ")
  print("It will brute force by shifting your text one by one and it will show all iterations")
  print("Do note this is not 100% accurate and may let your text slip through.")
  text = cae.convnum(text)
  ranges = cae.autodecipher(text)
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
        temp = cae.encipher(d[i],text)
        res.append("With a shift of " + str(d[i]) + ": " + str(cae.convtext(list(temp))))
    except IndexError:
      pass
  for i in range(len(res)):
    print(res[i])
  print(" is your result!")


def InvalidCommand(command):
    pass
def Run():
    try:
        prompt = None
        StrPrompt = ""
        while prompt == "" or prompt == None or StrPrompt == "":
            StrPrompt = input(">>>")
            prompt = re.compile(StrPrompt)
        ListPrompt = list(StrPrompt)
        typ = re.search("-", StrPrompt)
        t = ListPrompt.index("-", ListPrompt.index("-") + 1,len(ListPrompt) - 1)
        print(StrPrompt[t])
        print(t)
        if StrPrompt == "help":
            print("A")
        if StrPrompt[typ.span()[0] + 1] == "v" or StrPrompt[typ.span()[0] + 1] == "V":
            if StrPrompt[t + 1] == 'e' or StrPrompt[t + 1] == 'E':
                vigencrypt()
            elif StrPrompt[t + 1] == 'd' or StrPrompt[t + 1] == 'D':
                vigdecrypt()
        if StrPrompt[typ.span()[0] + 1] == "b" or StrPrompt[typ.span()[0] + 1] == "B":
            if StrPrompt[t + 1] == 'e' or StrPrompt[t + 1] == 'E':
                beaencrypt()
            elif StrPrompt[t + 1] == 'd' or StrPrompt[t + 1] == 'D':
                beadecrypt()
        if StrPrompt[typ.span()[0] + 1] == "c" or StrPrompt[typ.span()[0] + 1] == "C":
            if StrPrompt[t + 1] == 'e' or StrPrompt[t + 1] == 'E':
                caeencrypt()
            elif StrPrompt[t + 1] == 'd' or StrPrompt[t + 1] == 'D':
                caedecrypt()
    except Exception:
        print("Invalid command or an error happened")
        Run()
        return 0

while True:
    Run()