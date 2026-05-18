def dfs(graph, node, visited, path):
    visited.add(node)
    path.append(node)
    print('visited:', node)
    print('current path:', path)
    for adj in graph[node]:
        if adj not in visited:
            dfs(graph, adj, visited, path)
    print('Backtracking from:', node)
    path.pop()
    visited.remove(node)
graph = {'A':['B', 'C'],
         'B':['D', 'E'],
         'C':['F'],
         'D':[],
         'E':[],
         'F':[]}
visited = set()
path = []
dfs(graph, 'A', visited, path)
