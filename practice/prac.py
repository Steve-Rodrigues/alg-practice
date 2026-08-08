#dfs practice
from collections import defaultdict, deque
import heapq #for the adj list representation of the graph given an edge list
def add_edge(v1,v2,weight,graph):
    graph[v1].append((weight, v2))
    graph[v2].append((weight, v1)) #this is undirected as both nodes are connected to each other
    return graph
#dfs function-- goes down an entire path before going down a different one
#since it is a graph we need to keep track of the paths(nodes) we have already traversed os we dont get stuck in a cycle
def dfs(graph, node,visited=None,res=None):
    if res is None:
        res = []#going to be the path tracker(going to be adding the current node each time before traversal)
    res.append(node)
    if visited is None:
        visited = set([node])#set for constant lookup
    #base case is if there are no more edges from this node that are not vivisted, we just return
    #go through edges and the first one that is not in the visited set will be performed dfs on
    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            dfs(graph, n, visited=visited,res=res)
    else:
        print(f'No more available paths from {node}')
    return res
#bfs time-- it goes level by level, so it uses a queue and pops the node that was in there first so it can visit its edges and then continues 
#needs to use a queue so that is completes level by level and keep track of what nodes we have already seen so its not included in another level
def bfs(graph, node, visited=None, res=None):
    if visited is None: visited = set([node])
    if res is None: res = []
    queue = deque([node])

    while queue:
        currNode = queue.popleft()#now time to explore this node
        res.append(currNode)
        for n in graph[currNode]:
            if n not in visited:
                queue.append(n)#visit it and explore later
                visited.add(n)
    return res
        
#dikjstra's algorithm: shortest path algorithm which gives the shortest cost(whether it be in distance or anything) from a starting node to every other node in the graph
#it creates a map of the distances to each node and we update that distance each time if the node we are at and teh edge weight of its neighbor added together is less than the node connecting it
#if so, we update the map and add that to the heap so we can check if the distance from that node to its neihgbors can be reduced too
def dikjstras(graph, root)->tuple:
    #create the initial distances map with everyyting except for start to infiinity
    path = {node:(0 if node!=node else node) for node in graph}
    distances = {node: (float('inf') if node != root else 0) for node in graph}
    minHeap = [(0,root)]#going to sort the distances found by the current distance to get to that node
    heapq.heapify(minHeap)
    while minHeap:
        cost, node = heapq.heappop(minHeap)
        for w,n in graph[node]:
            #relax the value at the neighbor if the current node gets there with less of a cost
            if distances[node] + w < distances[n]:
                path[n]=node#this key will store the node that relaxed it
                distances[n] = distances[node] + w
                heapq.heappush(minHeap,(distances[n], n))
    return (distances, path)
#will take in the path dict and the root node of the dikjstra alg so we can get the full path to get to each node in the graph
#we go through all of the keys in the path and at each key we will traverse the path until we reach the starting node--thats teh shortes path
def path_trav(path,startNode):
    end = defaultdict(list)
    end[startNode].append(startNode)
    for node in path:
        curr=[node]#remake every time--this stores the path from bottom to top, so we need to reverse it to get from start to end
        currNode = node
        saved_curr = node
        while currNode != startNode:
            currNode = path[currNode]
            curr.append(currNode)
        end[node] = list(reversed(curr))

    return end
 

if __name__ == "__main__":
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (1, 2, 2),
        (1, 3, 5),
        (2, 4, 3),
        (3, 4, 1),
        (3, 5, 2),
        (4, 5, 6),
    ]
    graph = defaultdict(list)#going to use a dict so it's O(1) lookup, the values are going to be the edges its connected to
    for v1, v2, w in edges:
        add_edge(v1, v2, w, graph)
    #print(dfs(graph, 0))
    distances, path = dikjstras(graph, 0)
    print('testing',path_trav(path, 0))

        
