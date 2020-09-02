#!/usr/bin/env python

#inputStr = input('INPUT STRING : ')
#inputInt = input('numRows : ')
inputStr = "acknowledgements"
inputInt = 4

print(inputStr.upper())
print(inputInt)

print("expected_output : ")

print("A     L     E")
print("C   W E   M N")
print("K O   D E   T")
print("N     G      ")

level_one = inputInt - 1
level_two = inputInt - 2

level = level_one + level_two
inputStr = list(inputStr.upper())
length = len(inputStr)

space = ""

for i in range(inputInt):
    space += " "

print(space)
#work in progress
