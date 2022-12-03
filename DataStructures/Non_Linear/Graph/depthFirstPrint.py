from model.model_characters import *

def depthFirstPrint(graph,source):
    stack = [source]
    
    while len(stack)>0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

depthFirstPrint(graph,'a')
    