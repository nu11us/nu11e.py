from collections import defaultdict

class Graph:
    def __init__(self):
        self.name_to_id = {}
        self.id_to_name = {}
        self.matrix = []
        self.edges = []

    def add_node(self, name):
        self.name_to_id[name] = len(self.matrix)
        self.id_to_name[len(self.matrix)] = name
        for i in range(len(self.matrix)):
            self.matrix[i].append(-1)
        self.matrix.append([-1 for i in range(len(self.matrix)+1)])

    def connect(self, source, destination, weight=1):
        s, d = self.name_to_id[source], self.name_to_id[destination]
        self.matrix[s][d] = weight
        self.edges.append((source, destination, weight))


def gen_residual(graph, flow):
    residual = Graph()
    residual.name_to_id = graph.name_to_id
    residual.id_to_name = graph.id_to_name
    residual.matrix = [[-1 for i in range(len(graph.matrix))] for j in range(len(graph.matrix))]
    for e in graph.edges:
        u = graph.name_to_id[e[0]]
        v = graph.name_to_id[e[1]]
        c = e[2]
        f = flow[u][v]
        if f == -1:         # shouldn't happen but just in case
            print('lol it happened')
            break
        if c - f > 0:
            residual.matrix[u][v] = c - f
            residual.edges.append((e[0],e[1], c-f))
        if f > 0:
            residual.matrix[v][u] = f
            residual.edges.append((e[1], e[0], f))
    return residual

def bfs(graph, strs, strt, path=[]):
    s, t = graph.name_to_id[strs], graph.name_to_id[strt]
    path = defaultdict(list)
    queue = [[s]]
    visited = [False for i in range(len(graph.matrix))]
    visited[s] = True

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == t:
            return path
        for i,j in enumerate(graph.matrix[node]):
            if j > -1 and not visited[i]:
                queue.append(path + [i])
        visited[i] = True

def augment(graph, residual, flow, path):
    caps = []
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        caps.append(graph.matrix[u][v])
    b = min(caps)

    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        if residual.matrix[u][v] == graph.matrix[u][v] - flow[u][v]:
            flow[u][v] = flow[u][v] + b
        elif residual.matrix[u][v] == flow[u][v]:
            flow[v][u] = flow[v][u] - b
    return flow

def ff(graph, s='s', t='t'):
    flow = [[0 if j!=-1 else -1 for j in i] for i in graph.matrix]
    residual = gen_residual(graph, flow)

    path = bfs(residual, s, t)
    print(path)
    while path:
        flow = augment(graph, residual, flow, path) 
        residual = gen_residual(graph, flow)
        path = bfs(residual, s, t)
        print(path)

    return flow

""" 
Example:
    net = Graph()
    net.add_node('s')
    net.add_node('t')
"""