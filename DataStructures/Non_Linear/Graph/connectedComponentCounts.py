from model.connectedComponents import *

def connectedComponentCounts(graph):
    visited = set()
    count = 0

    for node in graph:
        print(visited)
        if explore(graph,node,visited) == True:
            count += 1
    return count        


def explore(graph,current,visited):
    if current in visited: return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph,neighbor,visited)

    return True    


print(connectedComponentCounts(connectedComponentsGraph)  )  