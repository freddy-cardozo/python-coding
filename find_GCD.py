#--------------------------------------------------------
# Author : Freddy Cardozo
#
#
#
#
# This python pgm finds the geometric mean of 'N' numbers 
# using the numpy python module
# -------------------------------------------------------

import numpy
import re
import sys

from sys import version_info as python_version 
from sys import argv as cmd_line_arguments
from pdb import set_trace as st
from time import sleep as sleeping

def findGeoMean():
    # Convert the list of Numbers into a numpy array
    numpyArray = numpy.array(numList)
    
    # Calculate the product of each element of the numpy array
    productArray = numpyArray.prod()
    
    # Calculate the geomean which is the 'N' root of the product of the elements of the array
    geoMean = float(productArray**(1/float(numNumbers)))
    return geoMean

def demoDisplay(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    sleeping(2)
    
def displayDemoMsg(msg, displaySerial=1):
    if displaySerial:
        for ch in msg:
            sys.stdout.write('\x1b[6;34;46m' + ch + '\x1b[0m')
            sys.stdout.flush()
            sleeping(0.05)
    else:
        sys.stdout.write(msg)
        sys.stdout.flush()
        sleeping(2)
#Get the python version being used
(pythonMajorVersion, pythonMinorVersion, micro, release, serial) = python_version
demo = None
numList = []

if '-demo' in cmd_line_arguments:
    demo=1
    msg = """THIS IS A PYTHON PROGRAM WHICH CALCULATES THE GEOMETRIC MEAN \nOF 'N' NUMBERS \n"""
    displayDemoMsg(msg)

if not demo:    
    if (pythonMajorVersion, pythonMinorVersion) > (3,0):
        numNumbers = int(input('\x1b[6;34;46m' + "\tENTER THE NUMBER OF NUMBERS TO FIND GEOMETRIC MEAN : " + '\x1b[0m'))
    else:
        numNumbers = int(raw_input('\x1b[6;34;46m' + "\tENTER THE NUMBER OF NUMBERS TO FIND GEOMETRIC MEAN : " + '\x1b[0m'))
else:
    displayDemoMsg("\tENTER THE NUMBER OF NUMBERS TO FIND GEOMETRIC MEAN : ", 0)
    displayDemoMsg("2\n", 0)
    numList = [12,48]
    numNumbers=2

for _ in range(1, numNumbers+1):
    if not demo:
        if (pythonMajorVersion, pythonMinorVersion) > (3,0):
            numList.append(float(input('\x1b[6;34;46m' + "\tENTER NUMBER" + str(_) + " : " + '\x1b[0m')))
        else:
            numList.append(float(raw_input('\x1b[6;34;46m' + "\tENTER NUMBER" + str(_) + " : "+ '\x1b[0m')))
    else:
        displayDemoMsg("\tENTER NUMBER" + str(_) + " : ", 0)
        displayDemoMsg(str(numList[_ - 1]) + "\n", 0)

gcd = findGeoMean()

sys.stdout.write('\n' + '\x1b[2;30;42m' + "\t GEOMETRIC MEAN = " + str(gcd) + ' ' + '\x1b[0m' + '\n')  
