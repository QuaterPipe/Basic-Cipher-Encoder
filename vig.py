import re
#           #
# FUNCTIONS #
#           #
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
  for i in range(len(text)):
    if text[i] == "$":
      pass
    else:
      text[i] = int(text[i]) + 97
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
  #adds number of the key to the text#
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
      sum = text[i] + key[l]
      #if the sum is over 25 just subtract 26#
      if sum > 25:
        text[i] = sum - 26
      #if the sum is not over 25 nothing happens and the code keeps running#
      else:
        text[i] = sum
    l+=1
  #returnt a list of enciphered numbers#
  return text
  
def decipher(key, text):
  #subtracts number of the key iterations from the text#
  l=0
  for i in range(len(text)):
    if text[i] == "$" or text[i] == "^" or text[i] == "~" or text[i] == "!":
      pass
    else:
      if l >= len(key):
        l=0
      else:
        pass
      dif = text[i] - key[l]
      #checks if the difference is less than zero, if true turns difference into positive and then subtracts the difference from 26#
      if dif < 0:
        text[i] = 26 + dif
      else:
        text[i] = dif
    l+=1
  #returns list of dechiphered numbers#
  return text
#not done yet#
def autodecrypt(text):
  #shiftsall the text over by one '$'#
  def shift(text):
    texts = {}
    for x in range(len(text)):
      texts["text{0}".format(x)] = re.findall("[a-z]",text)
    for x in range(len(text)):
      texts["text{0}".format(x)]


  text1,text2,text3,text4,text5,text6,text7,text8 = shift(text)
  coincidences = list
