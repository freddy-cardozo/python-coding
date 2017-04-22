#--------------------------------------------------------
# Author : Freddy Cardozo
#
#
#
#
# This python pgm finds the G.C.D (Greatest Common Divisor)
# between 'N' number
# 
# -------------------------------------------------------

import re 
from sys import version_info as python_version 
from pdb import set_trace as st


#Function to find the G.C.D between N integers
def findGCD():
    smallest = sorted(numList, reverse=False)[0]
    for i in range(1, smallest + 1):
        if (list(map(lambda x: x%i, numList)).count(0) == len(numList)):
            gcd = i
    return gcd
    
# Generic function to display message to the O/p based upon python version
def printOp(msg):
    if (major, minor) > (3,0):
        eval("print (msg)")
    else:
        eval("print msg")

#Get the python version being used
(major, minor, micro, release, serial) = python_version

if (major, minor) > (3,0):
    numNumbers = int(input("ENTER THE NUMBER OF +ve INTEGERS TO FIND G.C.D : "))
else:
    numNumbers = int(raw_input("ENTER THE NUMBER OF +ve INTEGERS TO FIND G.C.D : "))

numList = []
for _ in range(1, numNumbers + 1):
    numList.append(int(input("ENTER NUMBER" + str(_))))

findGCD()    
