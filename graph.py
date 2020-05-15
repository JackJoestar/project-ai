
#@authors: John Hernandez, Naomy Morales, Luis Diaz
#Created May 9,2020
from _collections_abc import Iterable
import components
import math
from graph import raph, Node
from utils import probability
import numpy as np
import sys

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

g.simulated_annealing_full( 'A', 'C')
g.a_star_search('A','C')


def h_x(self,start, goal):
    x1, y1 = (start)
    x2, y2 = (goal)

    x = int(x2) - int(x1)
    y = int(y2) - int(y1)
    return int(math.sqrt((x ** 2) + (y ** 2)))


def exp_schedule(k=200, lam=0.005, limit=100):
    
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)


def choices(neighbors_list,rand):
    
    choice = rand.randrange(len(neighbors_list))
    
    return neighbors_list[choice]

def simulated_annealing_full(graph, start, goal, rand, schedule=exp_schedule()):

    states = []
    start_node = Node(start,None)
    current = Node(start, None)

    for t in range(sys.maxsize):
        
        states.append(current.name)
        
        T = schedule(t)
        
        if T == 0:
            path = []
            while current != start_node:
                path.append(current.name + ': ' + str(current.f))
                current = current.parent
            path.append(start_node.name + ': ' + str(start_node.f))
            return path[::-1]
        
        neighbors = graph.get(current.name)
        
        if not neighbors:
            return current.name
        
        next_choice = Node(choices(list(neighbors),rand), current)

        current.f = components.componentAdjustments(rand, h_x(start.get(), goal))
        next_choice.f = components.componentAdjustments(rand, h_x(start.get(), goal))

        delta_e = current.f - next_choice.f
        if delta_e > 0 or probability(np.exp(delta_e / T)):
            current = next_choice


