#!/software/python/3.4/bin/python
import sys
import operator
from sys import stdin
import re
import math
import time
t1 = time.clock()
searchWord = sys.argv[1]
givenWord = searchWord.lower()
 
result = "" 
wordPresent = 0

opFile= open("/home/rkandul/hadoop-stack/scripts/invertedIndexUniwordDL.txt", "r")
for line in opFile:
 if givenWord in line:
     word, postings = line.split('\t')
     if len(givenWord) == len(word):
       result = line
       wordPresent += 1
       break
 else: 
   continue
opFile.close()       
if  wordPresent == 0:
  print("word is not present in the collection or either it is a stop word") 
elif result:     
 #wordList=result.split(",")
 #word, docList = result.split("\t")
 if ',' in postings:
   tfTuple = tuple(postings.split(","))
 else:
   tfTuple = tuple(postings.split()) 
df = len(tfTuple)
docsN=806792
resultDict= dict()

if df >=1:
    listVar = 0
    tupleLength = len(tfTuple)
    #print("**************Total number of results: %s ********************* "%(str(tupleLength)))
    print("**************Total number of results: %s ********************* "%(str(tupleLength)))
    opFile= open("/home/rkandul/hadoop-stack/scripts/noOfTerms800k_2.txt", "r")
    totalDocLength = 0
    totalDocNum = 0
    for line in opFile:
       if '.xml' in line:
          fileName, dl = line.split(":")
       if dl == '':
          continue
       else:
          totalDocLength += int(dl)
          totalDocNum += 1

    avgDL = float(totalDocLength)/totalDocNum
    while listVar < tupleLength: 
       term = tfTuple[listVar]
       listVar += 1
       fileName, nums =  term.split(" ")
       fileName = fileName.strip()
       count, tf = nums.split(":")
       if count == '' or tf == '':
          continue
       idf =round(math.log10(docsN/df),5)
       k1 = 1.5
       b = 0.75
       k = k1*((1-b)+(b*int(count)/avgDL))
       #print(k)
       bm25 =round(idf * (k1+1)*int(tf)/(k+int(tf)),5)
       resultDict[fileName] = bm25
    

    sorted_resultDict = sorted(resultDict.items(), key = operator.itemgetter(1))
    sorted_resultDict.reverse()
    print("\n************* Displaying top 20 using TF-IDF ranking *********************\n")
    t4 = time.clock()
    print(round(t4-t1,3))

    j = 0
    for i in sorted_resultDict:
      j += 1
      if j <= 20: 
        print (i)
      else: break
       
