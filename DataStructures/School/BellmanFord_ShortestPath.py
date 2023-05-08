from model.bellmanFord_Model import *




def bellamn_ford(nodes,edges,index="A",final_place = "Z"):

    path_lengths = {v: float("inf") for v in nodes}
    path_lengths[index] = 0

    paths = {v: [] for v in nodes}
    paths[index] = [index]

    for _ in range(len(nodes) - 1):
        for (u,v), w in edges.items():
            if(w<0):
                return "Error"
            #print(edges.items())
            if path_lengths[u] + w < path_lengths[v]:
                path_lengths[v] = path_lengths[u] + w
                paths[v] = paths[u] + [v]
           
    #print("paths = ",paths)
    #print("path leghnts = ",path_lengths)++

    return path_lengths[final_place], paths[final_place]     



shortest_path_lenght,shortest_paths = bellamn_ford(nodes,edges,"B","D")


print(shortest_paths,shortest_path_lenght)
