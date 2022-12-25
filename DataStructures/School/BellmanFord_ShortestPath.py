from model.bellmanFord_Model import *



def bellamn_ford(nodes,edges,spruce_index="A",final_place = "Z"):

    path_lengths = {v: float("inf") for v in nodes}
    path_lengths[spruce_index] = 0

    paths = {v: [] for v in nodes}
    paths[spruce_index] = [spruce_index]

    for _ in range(len(nodes) - 1):
        for (u,v), w in edges.items():
            print(edges.items())
            if path_lengths[u] + w < path_lengths[v]:
                path_lengths[v] = path_lengths[u] + w
                paths[v] = paths[u] + [v]
           
    print("paths = ",paths)
    print("path leghnts = ",path_lengths)

    return path_lengths[final_place], paths[final_place]     



shortest_path_lenght,shortest_paths = bellamn_ford(nodes,edges,"A","Z")


print(shortest_paths,shortest_path_lenght)
