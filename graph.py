
#@authors: John Hernandez,Naomy Morales, Luis Diaz
#Created May 9,2020
from _collections_abc import Iterable

#Node class
class Vertex:
    def __init__(self,n):
        #nodes a created with a dictionary of its neighbors
        self.name = n
        self.neighbors = dict()

    def add_neighbor(self,v, weight, speed): #neighbors are dictionaries which values are tuples of distance and speed
        if v not in self.neighbors:
            self.neighbors.update({v:(weight,speed)})


    def get_neighbors(self): # gets all the neighbors
        return self.neighbors


#Graph class to carry nodes
class Graph():
    vertices = {}
    
    def add_vertex(self,vertex): #adding a new node
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_edge(self, u, v, weight=1,speed=20):#adding an edge
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v,weight,speed)
                if key == v:
                    value.add_neighbor(u,weight,speed)
            return True
        else:
            return False
    def print_graph(self): #prints the graph with the nodes as keys
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
    
    def get_vertices(self): #gets all the vertices
        return self.vertices

    def heuristic(self,start, goal, actualdistance):
        # heuristic function that utilizes the starting node's distance and speed, and the next nodes distance and speed to estimate path cost
        starting =self.vertices[start]
        goalie = self.vertices[goal]
        x1 = starting.get_neighbors()[0]
        y1 = starting.get_neighbors()[1]
        x2 = goalie.get_neighbors()[0]
        y2 = goalie.get_neighbors()[1]
        return ((x1 + x2) / (y1 + y2)) * actualdistance

    def a_star_search(self,start,end): #algorithm that uses the heuristic f(n)=g(n)+h(n) to calculate a optimal path
        frontier=[]
        explore=[]
        starting = self.vertices[start]
        goal=self.vertices[end]

        frontier.append(starting)

        while len(frontier)>0:
            current=frontier.pop()
            if current==goal:
                return "Goal has been reached"

            for neighbor in current.get_neighbors():

                #print(current.get_neighbors()[neighbor][0]) #testing if its printing neighbors

                value=current.get_neighbors()[neighbor][0]
                current_distances=[]
                current_distances.append(value)
                # if self.vertices(neighbor) in explore:
                #    continue
                #missing to add heuristic

            frontier.append(current.get_neighbors())
            frontier.sort()
            explore.append(current)

        return 'Fail to find a path'


#Uncomment to test functionality
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
g.add_edge('A', 'B',100)
g.add_vertex(Vertex('C'))
g.add_edge('A','C',20,60)
g.print_graph()

g.a_star_search('A','C')

































