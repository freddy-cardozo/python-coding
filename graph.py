import re
from pdb import set_trace as st

def find_path(graphd, src, dest, path=[]):
    path = path + [src]
    st()
    if src == dest: 
        return path
    if not src in graphd:
        return None
    
    for node in graphd[src]:
        if node not in path:
            new_path = find_path(graphd, node, dest, path)
            if new_path : return new_path
    return None
    

graph = [[1,2], [2,3], [2, 4], [3, 5]]
nodes = list(set([ graph[row][col] for col in range(0, len(graph[0])) for row in range(0, len(graph))]))
graph_dict = {node:[] for node in nodes}
for i in range(0, len(graph)):
    graph_dict[graph[i][0]].append(graph[i][1])
print(graph_dict)

src_node = int(input("Enter the source node"))
dest_node = int(input("Enter the destination node"))

path = find_path(graph_dict, src_node, dest_node)
print(path)