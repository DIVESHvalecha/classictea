def dfs(graph,node,visited=None):
    if visited==None:
        visited=set()
    print(node,end=" ")


    visited.add(node)


    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)


graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
}


print("DFS TRAVERSAL:")
dfs(graph,'A')


