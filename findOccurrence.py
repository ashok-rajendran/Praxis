#!/usr/bin/env python

import os
import re
import sys

linebreaker = "*******************************************************************"
inputWord = raw_input("ENTER A WORD : ")
print(linebreaker)
inputWord = inputWord.upper().replace(' ','')
print("Removed Empty Spaces (If any) : " + inputWord)
checkNum = any(map(str.isdigit, inputWord))

if checkNum is True:
    print("INPUT CONTAINS ONE OR MORE NUMERIC VALUES, HENCE EXITING")
    print(linebreaker)
    sys.exit(0)
else:
    print(linebreaker)
    print("THE WORD IS : " + inputWord)

listWord = list(inputWord)
totalLength = len(listWord)
print("TOTAL LENGTH OF THE INPUT : " + str(totalLength))
print("CREATED A LIST FROM THE INPUT : " + str(listWord))
print(linebreaker)
keyValue = ""
initialVal = 0
lastLetter = totalLength - 1

for i in range(totalLength):
    i = initialVal
    if i >= totalLength:
        break
    eachChar = listWord[i]
    count = 1
    for nextChar in listWord:
        i += 1
        if i >= totalLength:
            break
        else:
            nextChar = listWord[i]
            if eachChar == nextChar:
                count += 1
                initialVal = i + count
            else:
                initialVal = i
                break
    addStr = str(count) + eachChar
    keyValue = keyValue + addStr

keyList = re.split('(\d+)', keyValue)
keyList = list(filter(None, keyList))
keyLen = len(keyList)
lastInt = keyLen - 2

if int(keyList[lastInt]) == 1:
    print("GENERATED OUTPUT KEY VALUE : " + keyValue[:-2])
else:
    print("GENERATED OUTPUT KEY VALUE : " + keyValue)

print(linebreaker)
