#spanning trees are taken from a larger graph view and they represent the graph using every vertex, but only making a one-way trip instead of the graph multiple directions
#and it creates an acyclic, connected tree which can then be turnbed into a minimum spanning tree which is the spanning tree from the graph that takes the lowest cost to make with the edges

#disjoint set is the set where the intersection is the empty set, we use this as a data structure too
#it allows us to union and check the membership of the nodes using find and union
#find will check where each node is pointed to and if already poiinted to the same node, they are connected
#union will point to a common node
#so the data structure allows us to union two graphs into the same graph which is now connected but conaining no cycles
from collections import defaultdict
import heapq


class DisjointSet:
    #each node will have a parent pointer to check set memebership and a value, also neighbor value to attach to another node
    def __init__(self, parent, val):
        self.parent = parent
        self.val = val
    #find operation to check set membership-- gets the value of the current nodes parent, if same as node comparing with then in the same tree
    #get the parent by checking nodes neighbor until the parent value is that nodes value
    def find(self, node):
        #first pass is to get the root node of the node
        root = node
        while root.parent is not root:
            root = root.parent
        #go throug all nodes again setting their parent directly to the root(compression)
        while node.parent is not node:
            curr_parent = node.parent
            node.parent = root
            node = curr_parent
        return root


    #union will add an edge between two nodes but will make the parent equal to the same node
    #only runs if the result of find is a different parent node(they are not connected yet)
    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)
        #going to point node 2 parent to the parent of node 1 before adding edge between node 1 and 2
        if root1 is not root2:
            root2.parent = root1
        return
    
#this graph class will hold everything for kruskals algorithm
#starts with a normal graph made of an array edged which are undirected(both ways) and a weight
#we take in num of vertices so we can create the parent array tree
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []#going to have (weight, v1, v2) for the edges
    #method for adding an edge to the graph an it is undirectiounal
    def addEdge(self, v1, v2, w):
        self.graph.append([w,v1,v2])

    #this is going to use the parent array we create in the kruskals for the returning MST and take in an index(node) in that result tree
    #res_tree = [0,0,1] -> node 0 is pointed to itself(root), node 1 points to 0 and node 2 points to 1
    #each time union is accepted meaning the set memberships are diff(point to diff root) we are going to add to the actual tree rep array
    def find(self, res_tree, node):
        #first get the root of the nodes tree
        root = node
        while res_tree[root] != root:
            root = res_tree[root]
        #now currNode is the root node for that tree
        currNode = node
        #going to point each index to the root index that was in that path
        while res_tree[currNode] != currNode:
            currPointer = res_tree[currNode]
            res_tree[currNode] = root
            currNode = currPointer
        return root
    #union function for adding pointers to the parent array
    def union(self, res_tree, v1, v2):
        root1 = self.find(res_tree,v1)
        root2 = self.find(res_tree,v2)
        if root1 != root2:
            res_tree[root2] = root1 #now pointing the root2 array index at the root1 position since not in same tree
        else:
            return -1
        
    #kruskals alg function: going to take in the graph and create a MST from it which is going to be stored in the res_tree array 
    #it will contain the index pointers to each nodes root which will be what it is connected to on the graph
    #each index will hold the pointer and then we need to incremement the total cost each time
    def kruskals(self):
        totalV = self.vertices #num of vertices
        tree_final = []#the actual tree representation with the edges, diff than the tree structure made for the set membership with union-find
        graph = self.graph # this is the graph to work from 
        res_tree = [i for i in range(totalV)] #create the tree with all nodes pointing at themselves right now

        total_weight = 0 #this will store the total weight gotten from the edges that were successfully added to the tree

        edges_added = 0#this will be the break point-- once added v-1 edges we stop because that is the number to create the tree
        sortedGraph = sorted(graph, key= lambda edge: edge[0])#sorts the graph by the weight of each edge

        #loop while edges is less than num of vertices because we need one less edge so there are no cycle
        for weight, v1, v2 in sortedGraph:
            #try to add the vertices to the result tree by adding connection between
            if self.union(res_tree, v1,v2) == -1:
                print(f'Unable to add {v1} and {v2} as a direct connection in the result tree')
            else:
                total_weight+=weight
                tree_final.append([weight,v1,v2])
        for weight, vertex1, vertex2 in tree_final:
            print(f'{vertex1} <--> {vertex2}: Weight of {weight}')
        return tree_final

    #going to need the frequenecy map function to perform the searching with prims beause needs access to its edges since it is doing bfs liek search
    def adjacencyList(self, graph):
        adjacency_list = defaultdict(list)
        for w,v1,v2 in graph:
            adjacency_list[v1].append((w,v2,v1))
            adjacency_list[v2].append((w,v1,v2))#the third is the parent for actually adding the pointer in the array tree structure
        return adjacency_list

##Now going to implememnt Prims algorithm: Another Miniumum Spanning Tree algorithm
#this time we are going to choose any starting edge and then to check cycles we use a visited set instead of the union find because of how we add to the tree
#this time we add to the tree by creating a minheap and it will choose the smallest available node from all the endpoint edges that have not been visited yet
#this does not use union find because it is a growing tree rather than a bunch of floating fragments which is where union find shines because it shows where each fragment points to
    def prims(self):
        mst = [i for i in range(self.vertices)] #going to be the tree structure where each index is pointing to the next node(index), the values are where they point to
        visited = set() #visited set to make sure we dont go to an edge that is already in the membership set so there are no cycles
        graph = self.graph
        #adding the adjacency list since we are adding all of the edges to the minHeap each time sorted by the weight so its first
        adjList = self.adjacencyList(graph)

        minHeap = []#going to use minheap to store the minimum weight edge from the available edges from each node we have visited(kind of like bfs because checking all edges)
        #minheap is going to store all of the available edges from lowest weight to highest from the bfs-like-search and we choose smallest one based on weight
        for n in adjList[graph[0][1]]:
            minHeap.append(n)

        heapq.heapify(minHeap)#starts with the neighbors of the first vertex in edge list and chooses smallest from there
        #will run until the visited set is equal to the number of verticies because that means all of them are connected since only marked after added to the tree
        #initialize the mst with the first value
        mst[graph[0][1]] = (0, graph[0][1], graph[0][1])#sets starting vertex in the mst to have weight of 0 and pointing to iteself becasue it is the start
        visited.add(graph[0][1])#starting at the first edge in the graph array(does not matter tho)

        while len(visited) < self.vertices:
            #pop lowest edge weight from the heap and use that 
            currSmallest = heapq.heappop(minHeap)#remember that the vertex we are looking at is at index 1 becasue this include the weight, vertex, and parent
            if currSmallest[1] not in visited:
                visited.add(currSmallest[1])
                #at the current smallest node found we add to visited and to the tree strucutre and then add all of its neighbors as long as not already visited so no cycles
                mst[currSmallest[1]] = currSmallest#setting that index in the tree to point to its parent value which is the 3rd value in teh tuple(it is the dictionary key)
                #add its edge connections to the heap so they can be checked next time to compared to the other available
                for connection in adjList[currSmallest[1]]:
                    heapq.heappush(minHeap, connection)
        for w, v, parent in mst:
            print(f'{v} <--> {parent}: Weight of {w}')
        print(f'Total weight: {sum(edge[0] for edge in mst)}')
        return


        


if __name__ == '__main__':
    # 5-vertex graph, known-good MST:
    #   0-1(2) 0-3(6) 1-2(3) 1-3(8) 1-4(5) 2-4(7) 3-4(9)
    # cheapest edges that connect everything without a cycle:
    #   0-1(2) + 1-2(3) + 1-4(5) + 0-3(6) = 16
    g = Graph(5)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 3, 6)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 8)
    g.addEdge(1, 4, 5)
    g.addEdge(2, 4, 7)
    g.addEdge(3, 4, 9)

    res_tree = g.kruskals()

    # every vertex should resolve (via find, not just the raw array value)
    # to the same root, since the graph is fully connected

    print(res_tree)

    g.prims()
    




        





    