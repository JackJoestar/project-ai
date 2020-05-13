
from _collections_abc import Iterable
import heapq



#Node class
class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = dict()

    def add_neighbor(self,v, weight, speed):
        if v not in self.neighbors:
            self.neighbors.update({v:(weight,speed)})

    # def get_weight(self,weight):
    #     self.weight=weight
    #
    # def get_speed(self,speed):
    #     self.speed=speed
    #
    def get_neighbors(self):
        return self.neighbors

    #
    # def cost(self,current,next):
    #     #return self.weights.get(to_node, 1)
    #     return 0

#Graph class to carry nodes
class Graph():
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
    
    def get_vertices(self):
        return self.vertices
    def heuristic(self,start,next):
        first=self.vertices[start]
        second=self.vertices[next]




    # def heuristic(start, goal, actualdistance):  # maybe, i have no clue
    #     starting = Vertex(start)
    #     goalie = Vertex(goal)
    #     x1 = starting.get_weight()
    #     y1 = starting.get_speed()
    #     x2 = goalie.get_weight()
    #     y2 = goalie.get_speed()
    #     return ((x1 + x2) / (y1 + y2)) * actualdistance

    def a_star_search(self,start,end):
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

                #print(current.get_neighbors()[neighbor][0])

                value=current.get_neighbors()[neighbor][0]
                current_distances=[]
                current_distances.append(value)
                # if self.vertices(neighbor) in explore:
                #    continue


            frontier.append(current.get_neighbors())
            frontier.sort()
            explore.append(current)

        return 'fail'
















        # current=frontier.pop(0)
        # for neighbors in current.get_neighbors():
        #     print(neighbors)














# class PriorityQueue:
#     def __init__(self):
#         self.elements=[]
#     def empty_queue(self):
#         return len(self.elements)==0
#     def put(self,element,priority):
#         heapq.heappush(self.elements,(priority,element))
#     def get(self):
#         return heapq.heappop(self.elements)[1]


# def a_star_search(graph,start,end):
#     frontier=PriorityQueue()
#     frontier.put(start,0)
#     origin={}
#     cost={}
#     origin[start]=None
#     cost[start]=0
#     while not frontier.empty_queue():
#         current=frontier.get()
#         if current==end:
#             break
#         for next in graph.get_vertices(current):
#             new_cost=cost[current]+graph.cost(current,next)
#             if next not in cost or new_cost < cost[next]:
#                 cost[next]=new_cost
#                 priority=new_cost+heuristic(end,next)
#                 frontier.put(next,priority)
#                 origin[next]=current
#     return origin,cost

# def a_star_search(graph,start,end):
#
#     frontier=[]
#     explored=[]
#     starting=Vertex(start,None)
#     goal=Vertex(end,None)
#
#     frontier.append(starting)
#
#     while len(frontier)>0:
#         frontier.sort()
#
#         currentnode=frontier.pop(0)
#         explored.append(currentnode)
#
#         if currentnode==goal:
#             path={}
#             while currentnode!=starting:
#                 path.append(currentnode+':'+currentnode.g)
#                # currentnode=current_node.parent
#             path.append(starting+':'+starting.g)
#             return path[::-1]
#
#         neighbors=graph.get_vertices(currentnode.name)
#         for key,value in neighbors.items():
#             neighbor=Vertex(key,currentnode)
#             if neighbor in explored:
#                 continue
#             neighbor.g=currentnode.g+graph.get(currentnode.name,neighbor.name)
#             neighbor.h=heuristic.get(neighbor.name)
#             neighbor.f=neighbor.g+neighbor.h
#             for node in frontier:
#                 if(neighbor==node and neighbor.f>node.f):
#                     return False
#             frontier.append(neighbor)
#     return None
#










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

