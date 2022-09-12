import re
#           #
# Functions #
#           #
def convnum(text):
  #removes all spaces and lowers all letters#
  text = re.sub("\s", "$", text)
  text = text.lower()
  ltext = re.findall("[^1234567890@#%|&\<>.,?/!~^`+=-_]", text)
  #converts characters to numbers#
  for i in range(len(ltext)):
    try:
      ltext[i] = ord(ltext[i])
    except ValueError:
      pass
  i=0
  #subtracts 97 from all characters#
  for i in range(len(ltext)):
    try:
      ltext[i] = int(ltext[i]) - 97
    except ValueError:
      pass
  #returns list of numbers#
  return ltext

def convtext(text):
  #adds 97 so that can be turned into string#
  for i in range(len(text)):
    try:
      text[i] = int(text[i]) + 97
    except ValueError:
      pass
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
    try:
      pltext = pltext + str(text[i])
    except ValueError:
      pass
  #returns string#
  return pltext

def encipher(key, text):
  i=0
  #adds the text to the key#
  for i in range(len(text)):
    try:
      sum = int(text[i]) + int(key[0])
      if sum > 25:
        text[i] = sum - 26
      else:
        text[i] = sum
    except ValueError:
      pass

  return text

def decipher(key, text):
  i=0
  #subtracts the key from the text#
  for i in range(len(text)):
    try:
      dif = text[i] - key[0]
      if dif < 0:
        dif = abs(dif)
        text[i] = 26 - dif
      else:
        text[i] = dif
    except ValueError:
      pass
  return text


def autodecipher(text):
  #this makes every possible oject of the cipher#
  container = {}

  for x in range(0,26):
    #makes a new value of lists 26 times#
    container["{0}".format(x)] = list(text)
  #creats a list that is shifted by x#
  for x in range(0,26):
    try:
      lis = container[str(x)]
      for i in range(0,len(lis)):
        sum = int(lis[i]) + x
        #if x is over 25 subtract 26#
        if sum > 25:
          lis[i] = sum - 26
        else:
          lis[i] = sum
    except ValueError:
      pass
  for x in range(0, len(container)):
    try:
      string = container[str(x)]
      string = convtext(string)
      container[str(x)] = string
    except ValueError:
      pass
  #makes a dictionary of the counts of letters in a list and the percentage of  the letters to lenght of word#
  counts = {}
  percentages = {}
  perfPercent = {
    "97perc" : 8.12, "98perc" : 1.49, "99perc" : 2.71, "100perc" : 4.32, "101perc" : 12.02, "102perc" : 2.30, "103perc" : 2.03, "104perc" :5.92 , "105perc" : 7.31, "106perc" : 0.10, "107perc" : 0.69, "108perc" : 3.99, "109perc" : 2.61, "110perc" : 6.95, "111perc" : 7.68, "112perc" : 1.82, "113perc" : 0.11 , "114perc" : 6.02 , "115perc" : 6.28, "116perc" : 9.10, "117perc" : 2.88, "118perc" : 1.11, "119perc" : 2.09, "120perc" : 0.17, "121perc" : 2.11, "122perc" : 0.07 
  }
  #find amount of every letter in list#
  for x in range(97, 122):
    percentages["{}perc".format(x)] = 0
    counts["{}count".format(x)] = 0
  #finds the best canditate#
  for x in range(0, len(container)):
    try:
      temp = container[str(x)]
      for y in range(97,122):
        counts["{}count".format(y)] = temp.count(chr(y))
        percentages["{}perc".format(y)] = (counts["{}count".format(y)] / len(temp))
      for y in range(97,122):
        try:
          if (percentages["{}perc".format(y)]) > perfPercent["{}perc".format(y)]:
            del container[str(x)]
        except KeyError:
          pass
    except ValueError:
      pass
  numcontainer = container
  for t in range(0,26):
    try:
      numcontainer[str(t)] = convnum(numcontainer[str(t)])
    except KeyError:
      pass
    except ValueError:
      pass
  for y in range(0,len(container)):
    try:
      lis = container[str(y)]
    except KeyError:
      pass
    except ValueError:
      pass
  for i in range(0,len(numcontainer)):
    try:
      lis = numcontainer[str(i)]
      if 4 not in lis and 0 not in lis and 8 not in lis and 14 not in lis and 20 not in lis:
        del numcontainer[str(i)]
    except KeyError:
      pass
    except ValueError:
      pass
  result = {}
  for x in range(1,len(numcontainer) + 1):
    try:
      result["{1}".format(str(x))] = []
    except IndexError:
      pass
    except ValueError:
      pass
  ranges = {}
  for i in range(len(numcontainer)):
    try:
      count = 0
      lis  = numcontainer[str(i)]
      if 4 in lis:
        count+=12.02
      if 19 in lis:
        count+=9.10
      if 0 in lis:
        count+=8.12
      if 14 in lis:
        count+=7.68
      if 8 in lis:
        count+=7.31
      if 13 in lis:
        count+=6.95
      if 18 in lis:
        count+=6.28
      ranges["{}".format(str(i))] = count
    except KeyError:
      pass
    except ValueError:
      pass
  values = []
  for q in range(26):
    try:
      values.append(ranges[str(q)])
    except KeyError:
      pass
    except ValueError:
      pass
  
  return ranges