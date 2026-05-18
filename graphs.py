'''class graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edges(self, e, v):
        self.graph.setdefault(e, []).append(v)
        self.graph.setdefault(v, []).append(e)
    def display(self):
        for vertex in self.graph:
            print(vertex, '->', self.graph[vertex])
g = graph()
g.add_edges('A', 'B')
g.add_edges('A', 'D')
g.add_edges('A', 'C')
g.add_edges('B', 'C')
g.add_edges('D', 'C')
g.display()'''


#DIRECTED GRAPH
class graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edges(self, e, v):
        if e not in self.graph:
            self.graph[e] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[e].append(v)
    def display(self):
        for vertex in self.graph:
            print(vertex, '->', self.graph[vertex])
g = graph()
vertices = int(input("enter number of vertices:"))
for i in range(vertices):
    vertex = input("Enter vertex name:")
    g.add_vertex(vertex)
edges = int(input("enter number of edges:"))
for i in range(edges):
    e = input("enter source:")
    v = input("enter destination")
    g.add_edges(e, v)
g.display()