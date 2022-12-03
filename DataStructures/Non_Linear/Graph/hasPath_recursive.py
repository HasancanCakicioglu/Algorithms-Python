from model.model_characters import *


def hasPathRecursive(graph, source, destination):
    if source == destination: return True
    for neighbor in graph[source]:
        if hasPathRecursive(graph, neighbor, destination): return True
    return False

print(hasPathRecursive(graph, 'a', 'k'))    