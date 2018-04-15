#--------------------------------------------------------
# Author : Freddy Cardozo
#
#
#
#
# This python pgm accepts the command line arguments passed to
# a python script using a json file (commandLineArg.json)  
# python processCommandLineArgument.py 
#   The above command executes the pgm

# -------------------------------------------------------

import re
import sys
import argparse
from sys import version_info as python_version 
from sys import argv as cmd_line_arguments
from collections import OrderedDict as od
from json import load as jsonLoad
from pdb import set_trace as st
from time import sleep as sleeping

# Read a Json File
def readJsonFile(jsonFile):
    jsonData = od(jsonLoad(open(jsonFile, mode='r')))
    return jsonData
	
# Process command line arguments
def processCommandLineArgs(cmdLineDict=od()):
    argParseObj = argparse.ArgumentParser(description="Parse the command line arguments")
    for option in cmdLineDict:
        subOptionArr = list()
        for subOption, subOptionValue in cmdLineDict[option].items():
            if type(subOptionValue) is str:
                subOptionArr.append("{}='{}'".format(subOption, str(subOptionValue)))
            else:
                subOptionArr.append("{}={}".format(subOption, str(subOptionValue)))
        subOptionStr = ','.join(subOptionArr)
        cmdLineStr = "'" +  option + "'" + ',' + subOptionStr
        cmdLineStr = "argParseObj.add_argument({})".format(cmdLineStr)
        ret = eval(cmdLineStr)
    cmdLineObj = argParseObj.parse_args()
    return cmdLineObj
    
# Generic function to display message to the O/p based upon python version
def printOp(msg):
    if (pythonMajorVersion, pythonMinorVersion) > (3,0):
        eval("print (msg)")
    else:
        sys.stdout.write(msg)

def demoDisplay(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    sleeping(2)
    
def displayDemoMsg(msg):
    for ch in msg:
        sys.stdout.write('\x1b[6;34;46m' + ch + '\x1b[0m')
        sys.stdout.flush()
        sleeping(0.05)

if __name__ == "__main__":
    #Get the python version being used
    (pythonMajorVersion, pythonMinorVersion, micro, release, serial) = python_version
    cmdLineDict  = readJsonFile('commandLineArg.json')
    cmdLineArgs = processCommandLineArgs(cmdLineDict)
    if cmdLineArgs.demo:
        demo=1
        msg = """THIS IS A PYTHON PROGRAM WHICH ACCEPTS THE COMMAND LINE ARGUMENTS PASSED TO PYTHON SCRIPTS VIA A JSON FILE (commandLineArg.json)\n""".upper()
        displayDemoMsg(msg)
