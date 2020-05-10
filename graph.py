'''
Created on May 9, 2020

@authors: Luis Diaz, Naomy Morales, John Hernandez

This is a graph module which will be used to create undirected weighted graphs.
For the purpose of this project, we added a speed parameter to represent the speed limit between two nodes.
The 2-tuple will be used by the algorithms to calculate the time it will take to reach from one node to another.
'''



#Node class
class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = dict()
    
    def add_neighbor(self,v, weight, speed):
        if v not in self.neighbors:
            self.neighbors.update({v:(weight,speed)})

#Graph class to carry nodes
class Graph:
    vertices = {}
    
    def add_vertex(self,vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_edge(self, u, v, weight=1,speed=20):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v,weight,speed)
                if key == v:
                    value.add_neighbor(u,weight,speed)
            return True
        else:
            return False
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
            

#Uncomment to test functionality
'''g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
g.add_edge('A', 'B',100)
g.add_vertex(Vertex('C'))
g.add_edge('A','C',20,60)
g.print_graph()'''

