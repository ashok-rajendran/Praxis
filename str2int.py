#!/usr/bin/env python

inputStr = input('ENTER A STRING : ')
inputStr = inputStr.lower()
outputInt = ""

for eachChar in inputStr:
    ConvInt = ord(eachChar) - 96
    outputInt += str(ConvInt)

print("CONVERTED INTEGER : " + str(outputInt))
