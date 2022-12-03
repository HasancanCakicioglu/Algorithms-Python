from model.model_characters import *

def breadthFirstPrint(graph,source):
    queue = [source]
    
    while len(queue)>0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

breadthFirstPrint(graph,'a')