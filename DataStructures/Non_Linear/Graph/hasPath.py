from model.model_characters import *

def hasPath(graph, source, destination):
    queue = [source]
    while len(queue)>0:
        current = queue.pop(0)
        print(current)
        if current == destination: return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

print(hasPath(graph, 'a', 'f'))    