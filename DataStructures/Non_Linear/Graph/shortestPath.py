from model.edges_1 import *


def shortestPath(edges,nodeA,nodeB):
    graph = buildGraph(edges)
    print(graph)
    visited = set([nodeA])
    queue = [[nodeA,0]]

    while(len(queue)>0):
        [current,depth] = queue.pop(0)
        print("depth = ",depth)
        print("queque = ",queue)
        if current == nodeB: return depth
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor,depth+1])
    return -1      




def buildGraph(edges):
    graph = {}
    for edge in edges:
        [a,b] = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph 



#print(shortestPath(edges,'j','m'))
print(shortestPath(edgesOdev,'a','z'))