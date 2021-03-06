#!/usr/bin/python

# Here binarySearch implies searching for two words with below conditions. 
#Let us take two words united, states
# united and states
# united or states
# united and not states

import sys
from sys import stdin
numOfArgs = len(sys.argv)
if numOfArgs == 4 or numOfArgs == 5:    
    searchWord1 = sys.argv[1]
    searchWord2 = sys.argv[numOfArgs-1]
    binaryTerm = sys.argv[2]
else: 
    sys.exit("Incorrect number of input arguments")
NOTInQuery = False    
if  numOfArgs == 5 and sys.argv[numOfArgs-2].lower() == "not":
 NOTInQuery = True
 
def contains_word(sentence, word):
    return ('' + word.upper() + '') in ('' + sentence.upper() + '')
    
processLine1 = None
processLine2 = None

for line in stdin:
  completeLine = line
  if  contains_word(completeLine, searchWord1):
      processLine1=     completeLine
  elif contains_word(completeLine, searchWord2):
      processLine2=     completeLine
  if processLine1 is not None and processLine2 is not None:
      break
    
wordList1=processLine1.split(",")
wordList2=processLine2.split(",")
wordList1Modified=[]
wordList2Modified=[]

def cleanLine(a,searchWord):
   z=0
   wordListModified=[]
   for k in a:
        z+=1
        if z==1:
            firstWord=k[len(searchWord)+1:]
            wordListModified.append( firstWord[:firstWord.rfind(":")])
            continue
        wordListModified.append( k[:k.rfind(":")])
   return wordListModified
    


wordList1Modified = cleanLine(wordList1,searchWord1)
wordList2Modified = cleanLine(wordList2,searchWord2)
print (wordList1Modified)
print (wordList2Modified)

andResult=[]
def printAndResult(a, b):
    print("\n**********Query result is below***********************\n")
    for i in a:
        if i in b:
            #print (i)
            andResult.append(i)
    return andResult
    
def printOrResult(a, b):
    OrResult=[]
    print("\n**********Query result is below***********************\n")
    for i in a:
        print (i)
    for j in b:      
        if j in a:
            continue
        print (j)
    OrResult.append(i)
    return OrResult
    
if binaryTerm.lower() == "and":
 andResult=printAndResult(wordList1Modified, wordList2Modified)
 if  NOTInQuery == False: 
  print(andResult)
 
if  NOTInQuery == True and binaryTerm.lower() == "and":
  for i in wordList1Modified :
      if i not in andResult: 
           print (i)
           
if binaryTerm.lower() == "or":
 printOrResult(wordList1Modified, wordList2Modified)
 

