#--------------------------------------------------------
# Author : Freddy Cardozo
#
#
#
#
# This python pgm finds the G.C.D (Greatest Common Divisor)
# between 'N' number
# python find_GCD.py -demo 
#   The above command gives a demo of this pgm
# python find_GCD.py 
#   The above command executes the pgm

# -------------------------------------------------------

import re
import sys
from sys import version_info as python_version 
from sys import argv as cmd_line_arguments
from pdb import set_trace as st
from time import sleep as sleeping

#Function to find the G.C.D between N integers
def findGCD():
    smallest = sorted(numList, reverse=False)[0]
    for i in range(1, smallest + 1):
        if (list(map(lambda x: x%i, numList)).count(0) == len(numList)):
            gcd = i
    return gcd
    
# Generic function to display message to the O/p based upon python version
def printOp(msg):
    if (pythonMajorVersion, pythonMinorVersion) > (3,0):
        eval("print (msg)")
    else:
        eval("print msg")

def demoDisplay(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    sleeping(2)
    
def displayDemoMsg(msg):
    for ch in msg:
        sys.stdout.write('\x1b[6;34;46m' + ch + '\x1b[0m')
        sys.stdout.flush()
        sleeping(0.05)
#Get the python version being used
(pythonMajorVersion, pythonMinorVersion, micro, release, serial) = python_version
demo = None
numList = []
if '-demo' in cmd_line_arguments:
    demo=1
    msg = """THIS IS A PYTHON PROGRAM WHICH CALCULATES THE G.C.D (GREATEST COMMON DIVISOR) \nOF 'N' NUMBER OF POSITIVE INTEGERS\n"""
    displayDemoMsg(msg)
if not demo:    
    if (pythonMajorVersion, pythonMinorVersion) > (3,0):
        numNumbers = int(input('\x1b[6;34;46m' + "\tENTER THE NUMBER OF +ve INTEGERS TO FIND G.C.D : " + '\x1b[0m'))
    else:
        numNumbers = int(raw_input('\x1b[6;34;46m' + "\tENTER THE NUMBER OF +ve INTEGERS TO FIND G.C.D : " + '\x1b[0m'))
else:
    demoDisplay("\tENTER THE NUMBER OF +ve INTEGERS TO FIND G.C.D : ")
    demoDisplay("2\n")
    numList = [12,48]
    numNumbers=2

for _ in range(1, numNumbers+1):
    if not demo:
        if (pythonMajorVersion, pythonMinorVersion) > (3,0):
            numList.append(int(input('\x1b[6;34;46m' + "\tENTER NUMBER" + str(_) + " : " + '\x1b[0m')))
        else:
            numList.append(int(raw_input('\x1b[6;34;46m' + "\tENTER NUMBER" + str(_) + " : "+ '\x1b[0m')))
    else:
        demoDisplay("\tENTER NUMBER" + str(_) + " : ")
        demoDisplay(str(numList[_ - 1]) + "\n")
    
gcd = findGCD()
printOp('\x1b[2;30;42m' + "\t  GCD = " + str(gcd) + '\x1b[0m')    
