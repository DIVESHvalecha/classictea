graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('D', 2), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}


h = {'A': 2, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 9, 'G': 0}


start, goal = 'A', 'G'


open_list = [(start, 0, [start])]  # (node, g, path)
while open_list:
    open_list.sort(key=lambda x: x[1] + h[x[0]])  # sort by f = g + h
    node, g, path = open_list.pop(0)
    if node == goal:
        print("Shortest Path:", " -> ".join(path))
        break
    for n, cost in graph[node]:
        open_list.append((n, g + cost, path + [n]))


