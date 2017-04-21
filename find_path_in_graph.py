#--------------------------------------------------------
# Author : Freddy Cardozo
#
#
#
#
# This python pgm checks if path exists between 2 nodes of 
# a graph 
# 
# -------------------------------------------------------

import re 
from sys import version_info as python_version 

def find_path(graphd, src, dest, path=[]): 
    path = path + [src] 
    if src == dest:  
       return path 
    if not src in graphd: 
        return None 
     
    for node in graphd[src]: 
        if node not in path: 
            new_path = find_path(graphd, node, dest, path) 
            if new_path : return new_path 
    return None 
    
# Generic function to display message to the O/p based upon python version
def printOp(msg):
    if (major, minor) > (3,0):
        eval("print (msg)")
    else:
        eval("print msg")

#Get the python version being used
(major, minor, micro, release, serial) = python_version

if (major, minor) > (3,0):
    numPaths = int(input("ENTER THE NUMBER OF PATHS : "))
else:
    numPaths = int(raw_input("ENTER THE NUMBER OF PATHS : "))

graph = []
for _ in range(1, numPaths + 1):
    graph.append(input("ENTER PATH{} : ".format(_)).split(' '))

nodes = list(set([ graph[row][col] for col in range(0, len(graph[0])) for row in range(0, len(graph))])) 

print('NODES : ' + str(nodes))
graph_dict = {node:[] for node in nodes} 
for i in range(0, len(graph)): 
    graph_dict[graph[i][0]].append(graph[i][1]) 
print('GRAPH DICTIONARY : ' + str(graph_dict)) 

if (major, minor) > (3,0):    
    src_node = input("Enter the source node")
    dest_node = input("Enter the destination node")
else:
    src_node  = raw_input("Enter the source node")
    dest_node = raw_input("Enter the destination node")

path = find_path(graph_dict, src_node, dest_node) 
printOp("->".join(path)) 
