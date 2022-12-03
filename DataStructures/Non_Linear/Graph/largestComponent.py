from model.connectedComponents import *

def largestComponent(graph):
    visited = set()
    largest = 0

    for node in graph:
        size = exploreSize(graph,node,visited)
        if size > largest:
            largest = size
    return largest


def exploreSize(graph,node,visited):
    if node in visited: return 0

    visited.add(node)
    size = 1

    for neighbor in graph[node]:
        size += exploreSize(graph,neighbor,visited)

    return size


print(largestComponent(connectedComponentsGraph) )