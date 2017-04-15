#--------------------------------------------------------
# Author : Freddy Cardozo
#
#
#
#
# This python pgm checks whether the network IP address is valid 
# 
# -------------------------------------------------------
import re
from sys import version_info as python_version 

# Generic function to display message to the O/p based upon python version
def printOp(msg):
    if (major, minor) > (3,0):
        eval("print (msg)")
    else:
        eval("print msg")

# Get the python version being used
(major, minor, micro, release, serial) = python_version

choice='y'
while(choice == 'y'):
    printOp('*'*20)
    if (major, minor) > (3, 0):
        ip = input("\tENTER THE IP ADDRESS : ")
    else:
        ip = raw_input("\tENTER THE IP ADDRESS : ")

    try:
        if [0<=int(x)<256 for x in re.split('\.',re.match(r'^\d+\.\d+\.\d+\.\d+$',ip).group(0))].count(True)==4:
            printOp("\t\tVALID IP  ADDRESS : " + ip)
        else:
            printOp("\t\tINVALID IP  ADDRESS : " + ip)
    except:
        printOp("\t\tINVALID IP  ADDRESS : " + ip)
    if (major, minor) > (3, 0):
        choice = input("\n\nDO YOU WANT TO CONTINUE (y/n) : ")
    else:
        choice = raw_input("DO YOU WANT TO CONTINUE (y/n) : ")
