
class Graph:
    def __init__(self):
        self.connections = {}

    @property
    def vertices(self):
        return self.connections.keys()

    @property
    def islands(self):
        return [i for i in self.connections.keys() if self.neighbors(i) == []]

    def add_edge(self, start, end, weight=1, bidirectional=True):
        if end in self.neighbors(start):
            self.purge(start, end)
        self.connections[start].append((end, weight))
        if bidirectional:
            self.connections[end].append((start, weight))

    def remove_edge(self, start, end, bidirectional=True):
        self.purge(start, end)
        if bidirectional:
            self.purge(end, start)

    def add_vertex(self):
        new = len(self.vertices)
        self.connections[new] = []

    def remove_vertex(self, index):
        self.connections.pop(index)
        if len(self.vertices) > 0:
            for i in self.vertices:
                self.purge(i, index)

    def connection(self, start, end):
        if start in self.vertices:
            return end in self.connections[start]
        else:
            return False

    def neighbors(self, start, with_weights=False):
        if with_weights:
            return self.connections[start]
        else:
            return [i[0] for i in self.connections[start]]

    def purge(self, start, target):
        self.connections[start] = [(j[0], j[1])
                                   for j in self.connections if j[0] != target]

    def weight(self, start, end):
        return [i[1] for i in self.connections[start] if i[0] == end][0]

    def dfs(self, vertex):
        explored = [vertex]
        paths = {vertex: 0}
        n = 0
        count = len(self.vertices) - len(self.islands) 

        if vertex in self.islands:
            return False

        while len(explored) < count:
            start = explored[n]
            for end in self.neighbors(start):
                if end not in explored:
                    path[end] = path[start] + weight(start, end)
                    explored.append(end)
            n += 1
        return paths
