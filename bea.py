import re

def convnum(text):
  #removes all spaces and lowers all letters#
  text = re.sub("\s", "$", text)
  text = text.lower()
  ltext = re.findall("[^1234567890@#%|&\<>.,?/!~^`+=-_]", text)
  #converts characters to numbers#
  for i in range(len(ltext)):
    if ltext[i] == "$":
      pass
    else:
      ltext[i] = ord(ltext[i])
  i=0
  #subtracts 97 from all characters#
  for i in range(len(ltext)):
    if ltext[i] == "$":
      pass
    else:
      ltext[i] = int(ltext[i]) - 97
  #returns list of numbers#
  return ltext

def convtext(text):
  #adds 97 so that can be turned into string#
  i=0
  for i in range(len(text)):
    if text[i] == "$":
      pass
    else:
      text[i] = int(text[i]) + 97
  i=0
  pltext = ""
  #converts numbers into characters#
  for i in range(len(text)):
    if text[i] == "$":
      text[i] = " "
    else:
      try:
        text[i] = chr(int(text[i]))
      except ValueError:
        pass
  i=0
  #converts list to string#
  for i in range(len(text)):
    pltext = pltext + str(text[i])
  #returns string#
  return pltext


def encipher(key, text):
  i=0
  l=0
  for i in range(len(text)):
    if text[i] == "$":
      pass
    else:
      #makes sure the key keeps looping back to 0 if it reaches the end#
      if l >= len(key):
        l=0
      else:
        pass
      dif = key[l] - text[i]
      #if the sum is over 25 just subtract 26#
      if dif < 0:
        dif = abs(dif)
        text[i] = 26 - dif
      #if the sum is not over 25 nothing happens and the code keeps running#
      else:
        text[i] = dif
    l+=1
  #returnt a list of enciphered numbers#
  return text

def decipher(key, text):
  #adds number of the key to the text#
  i=0
  l=0
  for i in range(len(text)):
    if text[i] == "$":
      pass
    else:
      #makes sure the key keeps looping back to 0 if it reaches the end#
      if l >= len(key):
        l=0
      dif = key[l] - text[i]
      #if the sum is over 25 just subtract 26#
      if dif < 0:
        dif = abs(dif)
        text[i] = 26 - dif
      #if the sum is not over 25 nothing happens and the code keeps running#
      else:
        text[i] = dif
    l+=1
  #returnt a list of enciphered numbers#
  return text