from collections import deque
##vertex class stores individual vertices and which nodes they are connected to via edges
#they store their value and an adjacency list/dict which just has the keys of the adjacent vertices and values of the weight to get there on the edge
class Vertex():
#defualt weight is 0 because not all graphs are weighted
    def __init__(self, value):
        self.value = value
        self.edges = {}
    #getting all adjacent vertices just access the keys of the adjaceny dict(turns it into an adjacency list)
    def get_edges(self):
        return self.edges.keys()
    ##find out the cost of traveling to another vertex via edge
    def get_weight(self, vertex):
        if vertex not in self.edges.keys():
            return False
        else:
            return self.edges[vertex]
        
    #adding edge by adding to the adjacecny list and the weight/cost to get there on the edge
    def add_edge(self, vertex, weight=0):
        self.edges[vertex]=weight
        return vertex
    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.get_value())

##graph class to create the whole strucutre of the graph: it holds every vertice by value in map
class Graph():
    #holds all vertices as key of value and value of object instance
    def __init__(self,directed=False):
        self.directed = directed
        self.vertices = {}
    #can add edges between vertices here by accessing those vertices value and using their add_edge methods to create connection
    #takes in the values of vertices and we search those in our map
    def add_edge(self, v1, v2, weight=0):
        #get the vertex instance using value passed in
        v1 = self.vertices[v1]
        v2 = self.vertices[v2]
        #if not directed we add edge in both directions
        if not self.directed:
            v1.add_edge(v2, weight)
            v2.add_edge(v1, weight)
        else:
            v1.add_edge(v2, weight)
    #creating a vertex 
    def add_vertex(self, vertex_value):
        #create by adding the instance to vertex class
        vertex = Vertex(vertex_value)
        self.vertices[vertex_value] = vertex
        return vertex
    #getting the weight of getting to vertex along that edge
    def get_weight(self, v1_val, v2_val):
        v1 = self.vertices[v1_val]
        v2 = self.vertices[v2_val]
        #use values to access edge list
        weight = v1.get_weight(v2)
        return weight
    def get_vertex(self, v_value):
        return self.vertices[v_value]
    def get_vertices(self):
        return self.vertices.values()
  
    #checks if two vertices are adjacent(they are directly connected via edge)
    def is_adjacent(self, v1_val, v2_val):
        if (v1_val in self.vertices) and (v2_val in self.vertices):
            v1 = self.vertices[v1_val]
            v2 = self.vertices[v2_val]
            return v2 in v1.edges or v1 in v2.edges
        else:
            return False
    #number of edges (adjacent neighbors) it has
    def degree(self, v_value):
        vertex = self.vertices[v_value]
        return len(vertex.edges)
    #return vertice with highes degree
    def most_connected(self):
        high = []
        for vertex in self.vertices.keys():
            high.append((vertex, self.degree(vertex)))
        return max(high, key=lambda vertex: vertex[1])
    #return all vertices with 0 edges
    def find_isolated(self):
        vertices=[]
        for vertex in self.get_vertices():
            if not vertex.get_edges():
                vertices.append(vertex.get_value())
        return vertices
    #sum of all edge weights in graph
    def total_weight(self):
        sum_weight = 0
        for vertex in self.get_vertices():
            sum_weight += sum(vertex.edges.values())
        if not self.directed:
            sum_weight /= 2
        return sum_weight
    #return values of each vertex reachable from given one-- the ajdacent nodes
    def neighbor(self, v_value):
        vertex = self.vertices[v_value]
        adjacent_vertices = [edge.get_value() for edge in vertex.get_edges()]
        return adjacent_vertices

#breadth-first-search: checks each level(all the neighbors) in visit and explore order
#here we pass in the value and we need to go through the object and then get all its edges
def bfs(graph, start, target):
    #dont want to visit more than once
    visited = {start}
    #queue to keep track of the next up vertex and adding its neighbors
    queue = deque([start])
    #search will run as long as there are vertices in the queue becasue means we keep exploring
    while queue:
        #grab the connected edges from this vertex
        current_vertex = queue.popleft()
        #check if current vertex is equal to target
        if current_vertex == target:
            return current_vertex
        else:
            v = graph.vertices[current_vertex]
            #add all of the edges (adjacent vertices to the queue of this level)
            all_neighbors = v.edges.keys()
            #check if already visited and then add to queue
            for neighbor in all_neighbors:
                if neighbor.value not in visited:
                    visited.add(neighbor.value)
                    queue.append(neighbor.value)
                
            
    return -1
        
        

        

















            




    





    


        