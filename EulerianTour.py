def find_eulerian_tour(graph):
    tour=[]
    find_tour(graph[0][0],graph,tour)
    return tour

def find_tour(u,E,tour): 
    for (a,b) in E:
        if a==u:
            E.remove((a,b))
            find_tour(b,E,tour)
        elif b==u:
            E.remove((a,b))
            find_tour(a,E,tour)
    tour.insert(0,u)

ls = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
print find_eulerian_tour( ls )
