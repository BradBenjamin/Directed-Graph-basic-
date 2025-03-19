import random
import copy

class Graph:
    def __init__(self):
        self.vertices ={}
    # Time complexity: O(1)
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    # Time complexity: THETA(1)
    def add_edge(self, start_vertex, end_vertex):
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            raise ValueError("Both vertices must exist in the graph")
        if end_vertex in self.vertices[start_vertex]:
            raise ValueError("Edge already exists")
        self.vertices[start_vertex].append(end_vertex)
    # Time complexity: THETA(1)
    def remove_edge(self, start_vertex, end_vertex):
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            raise ValueError("Both vertices must exist in the graph")
        self.vertices[start_vertex].remove(end_vertex)
    # Time complexity: O(V + E)
    def remove_vertex(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("Vertex does not exist")
        for vert in self.vertices:
            for end_vertex in self.vertices[vert]:
                if end_vertex == vertex:
                    self.vertices[vert].remove(end_vertex)
            self.vertices[vert] = [x - 1 if x >vertex else x for x in self.vertices[vert]]
        #assign every list of neighbours to its smaller vertex and delete the last one
        keys = list(self.vertices.keys())
        for i in range(len(keys)-1):  # Iterate over keys
            current_key = keys[i]
            next_key = keys[i+1]
            self.vertices[current_key] = self.vertices[next_key]
        del self.vertices[i+1]

    # Time complexity: O(n+m)
    def create_random(self, n, m):
        if m > n * (n - 1):
            raise ValueError("Number of edges exceeds maximum possible for n vertices")
        self.vertices = {v: [] for v in range(n)}
        edges = set()
        while len(edges) < m:
            from_vertex = random.randint(0, n - 1)
            to_vertex = random.randint(0, n - 1)
            if from_vertex != to_vertex and (from_vertex, to_vertex) not in edges:
                edges.add((from_vertex, to_vertex))
                self.add_edge(from_vertex, to_vertex)
    # Time complexity: THETA(1)
    def get_n(self):
        return len(self.vertices)
    # Time complexity: THETA(V)
    def get_m(self):
        return sum(len(neighbors) for neighbors in self.vertices.values())
    #Time Complexity: THETA(E)
    def is_edge(self, start, end):
        for end_vertex in self.vertices[start]:
            if end == end_vertex:
                return 1
        return 0
    # Time complexity: O(V+E)
    def copy_graph(self):
        return copy.deepcopy(self)
    # Time Complexity:THETA(1)
    def outbound_edges(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("Vertex not in graph")
        return self.vertices[vertex]
    # Time Complexity:THETA(E+V)
    def inbound_edges(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("Vertex not in graph")
        list_of_inbounds=[]
        for start_vertex in self.vertices:
            for end_vertex in self.vertices[start_vertex]:
                if end_vertex == vertex:
                    list_of_inbounds.append(start_vertex)
        return list_of_inbounds
    def deg(self, vertex, kind_of_degree):
        if vertex not in self.vertices:
            raise ValueError("Vertex not in graph")
        #Total degree - THETA(V+E)
        if kind_of_degree == 1:
            deg=0
            for start_vertex in self.vertices:
                for end_vertex in self.vertices[start_vertex]:
                    if end_vertex == vertex:
                        deg+=1
            deg+=len(self.vertices[vertex])
        #IN degree-THETA(V+E)
        if kind_of_degree == 2:
            deg=0
            for start_vertex in self.vertices:
                for end_vertex in self.vertices[start_vertex]:
                    if end_vertex == vertex:
                        deg += 1
        #OUT degree - THETA(1)
        if kind_of_degree == 3:
            deg=len(self.vertices[vertex])
        return deg
    # Time Complexity:THETA(V+E)
    def display_graph(self):
        for start_vertex in self.vertices:
            print(start_vertex, ": [", end='')
            ok_comma = 0
            for end_vertex in self.vertices[start_vertex]:
                if ok_comma == 0:
                    print(end_vertex, end='')
                else:
                    print(", ", end_vertex, end='')
                ok_comma = 1
            print("]")
    def __str__(self):
        vertices_str = f"Vertices: {list(self.vertices.keys())}\n"
        edges_str = "Edges:\n"
        for vertex, neighbors in self.vertices.items():
            for neighbor in neighbors:
                edges_str += f"{vertex} -> {neighbor}\n"
        return vertices_str + edges_str

def menu():
    print("Choose one of the following options: ")
    print("-1.Display graph as list of neighbours")
    print("0.Exit")
    print("1.Add a vertex")
    print("2.Add an edge")
    print("3.Remove a vertex")
    print("4.Remove an edge")
    print("5.Create a random graph")
    print("6.Get nr of vertices")
    print("7.Get nr of edges")
    print("8.Get degree of vertex")
    print("9.Check if is edge")
    print("10.Get outbound edges of vertex")
    print("11.Get inbound edges")
    print("12.Create copy of graph")
    print("13.Print the graph")


if __name__== "__main__":
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(2, 1)
    g.add_edge(3, 0)
    g.add_edge(3, 2)
    g.add_edge(1, 0)
    menu()
    x = int(input("Option: "))
    while x!=0:
        if x==-1:
            g.display_graph()
        if x==1:
            new_vertex = int(input("Vertex to be added: "))
            g.add_vertex(new_vertex)
        if x==2:
            new_start_index = int(input("Start index of the new edge: "))
            new_end_index = int(input("End index of the new edge: "))
            g.add_edge(new_start_index, new_end_index)
        if x==3:
            removed=int(input("Vertex to be removed: "))
            g.remove_vertex(removed)
        if x==4:
            start = int(input("Start of the edge to be removed: "))
            end = int(input("End of the edge to be removed: "))
            g.remove_edge(start, end)
        if x==5:
            n=int(input("N:"))
            m = int(input("M:"))
            g.create_random(n, m)
            g.display_graph()
        if x==6:
            print(g.get_n())
        if x==7:
            print(g.get_m())
        if x==8:
            vertex = int(input("Vertex to get degree for: "))
            print("Choose the type of degree you want:")
            print("1.Total degree")
            print("2.In degree")
            print("3.Out degree")
            kind_of_degree=int(input("Type of degree: "))
            print(g.deg(vertex, kind_of_degree))
        if x==9:
            start = int(input("Start of the edge you wanna check: "))
            end= int(input("End of the edge: "))
            if g.is_edge(start, end):
                print("The edge exists")
            else:
                print("The edge doesn't exist")
        if x==10:
            vertex = int(input("Vertex to get outbound edges for: "))
            print(g.outbound_edges(vertex))
        if x==11:
            vertex = int(input("Vertex to get inbound edges for: "))
            print(g.inbound_edges(vertex))
        if x==12:
            g.copy_graph()
        if x==13:
            print(g.__str__())
        x = int(input("Option: "))





