# *************************************************************************************************
#
# Copyright (C) 2020 Eric Pogue.
# 
# This file is a stand-alone application liscensed under the BSD-3-Clause
# 
# You are free to reuse the code as long as you give credit to the author in the header of your 
# source code. 
# *************************************************************************************************

# Conner Skoumal
# skoumalcw@gmail.com

import sys 

print("\nNumbering Systems with Conner")
numberOfArgs = len(sys.argv)
print("Total arguments passed: " + str(numberOfArgs))

if numberOfArgs > 6:
	print("Too Many Arguments!")
	exit()

print("\nArgument 1: " + sys.argv[0])

if numberOfArgs >= 2:
	print("\nArgument 2: " + sys.argv[1])
	numberAsAString = sys.argv[1]
	numberAsAnInt = int(numberAsAString, base=10)
	numberAsHex = hex(numberAsAnInt)

	print("Input:  " + numberAsAString)
	print("Number: " + str(numberAsAnInt))
	print("Hex:    " + numberAsHex)
if numberOfArgs >= 3:
	print("\nArgument 3: " + sys.argv[2])
	numberAsAString = sys.argv[2]
	numberAsAnInt = int(numberAsAString, base=10)
	numberAsHex = hex(numberAsAnInt)

	print("Input:  " + numberAsAString)
	print("Number: " + str(numberAsAnInt))
	print("Hex:    " + numberAsHex)
if numberOfArgs >= 4:
	print("\nArgument 4: " + sys.argv[3])
	numberAsAString = sys.argv[3]
	numberAsAnInt = int(numberAsAString, base=10)
	numberAsHex = hex(numberAsAnInt)

	print("Input:  " + numberAsAString)
	print("Number: " + str(numberAsAnInt))
	print("Hex:    " + numberAsHex)
if numberOfArgs >= 5:
	print("\nArgument 5: " + sys.argv[4])
	numberAsAString = sys.argv[4]
	numberAsAnInt = int(numberAsAString, base=10)
	numberAsHex = hex(numberAsAnInt)

	print("Input:  " + numberAsAString)
	print("Number: " + str(numberAsAnInt))
	print("Hex:    " + numberAsHex)
if numberOfArgs >= 6:
	print("\nArgument 6: " + sys.argv[5])
	numberAsAString = sys.argv[5]
	numberAsAnInt = int(numberAsAString, base=10)
	numberAsHex = hex(numberAsAnInt)

	print("Input:  " + numberAsAString)
	print("Number: " + str(numberAsAnInt))
	print("Hex:    " + numberAsHex)
# Enhancement #3: Update the application so that it can accept up to 5 (base 10) numbers as arguments and
# display the Input, Number, and Hex of hex value of each of the numbers. 

# Enhancement #4: Add appropriate error checking and user friendly error messages for input parameters. 

print("")
