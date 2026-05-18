from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for adj in graph[node]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)
graph = {'A':['B', 'C'],
         'B':['D', 'E'],
         'C':['F'],
         'D':[],
         'E':['F'],
         'F':[]}
bfs(graph, 'A')