##this algorithm will take a message and minimize the number of bits that is needed to represent the message hence saving space on the file
#it does so by creating a frequency table (dict) of each character and then we are going to create a binary tree where the leaf nodes are the actual characters
#all other nodes are result of merging the 2 smallest currently in the heap, so the smallest frequencies will have the longest path from the root while the most used chars will have the shortes path, most used will be right next to the root
#then we will trace the path back to each leaf node to get the new code to store the characters, use dfs and keep track of the path, left children are 0 and right children are 1--doesnt matter just be consisten
#each node will be able to store the character, frequency, left and right pointers. the merged ones will only store the left and right pointers with the merged frequency
import heapq
class HuffmanNode():
    def __init__(self, value=None, frequ=None, left=None, right=None):
        self.value = value
        self.frequ = frequ
        self.left = left
        self.right = right
    ##need the less than dunder so we can actually compare objects
    def __lt__(self, other):
        return self.frequ < other.frequ

#create the initial mapping function to get the frequencies--takes in the message and returns dict of keys as chars and values as amount used
def frequencyMap(msg):
    map = {}
    for char in msg:
        #add if not in it yet
        if char not in map.keys():
            map[char] = 1
        else:
            map[char] += 1
    return map
#now that we have the map its time to create the tree structure using the heap
def createTree(map):
    #create the leaf nodes
    minHeap = []
    for char in map.keys():
        node = HuffmanNode(frequ=map[char],value=char)
        minHeap.append(node)
    heapq.heapify(minHeap)#now lets merge new nodes until only the root node is in the heap(push back merged each time)
    while len(minHeap) > 1:
        leftNode = heapq.heappop(minHeap)
        rightNode = heapq.heappop(minHeap)
        #create new node which will be a merged frequency leading to the root and push back to the heap so it can get there
        node = HuffmanNode(frequ=leftNode.frequ+rightNode.frequ,left=leftNode,right=rightNode)
        heapq.heappush(minHeap,node)
    #now we have the root node
    root = minHeap.pop()
    return root
#with that root node we are going to traverse the tree keeping the path taken for to get to each node
#use dfs and we know if we reached a leaf node if it has a value--if so we will add that to the map along with the res list up to that pioint
#choosing to make the left traversals be 0 and right be 1
def getPath(root,code='',map=None):
    if map is None:
        map={}
    currNode = root
    if currNode is not None:
        if currNode.value is not None:
            map[currNode.value] = code
        getPath(currNode.left, code+'0',map)
        getPath(currNode.right, code+'1',map)
    return map






