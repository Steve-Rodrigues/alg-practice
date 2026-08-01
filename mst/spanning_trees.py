#spanning trees are taken from a larger graph view and they represent the graph using every vertex, but only making a one-way trip instead of the graph multiple directions
#and it creates an acyclic, connected tree which can then be turnbed into a minimum spanning tree which is the spanning tree from the graph that takes the lowest cost to make with the edges

#disjoint set is the set where the intersection is the empty set, we use this as a data structure too
#it allows us to union and check the membership of the nodes using find and union
#find will check where each node is pointed to and if already poiinted to the same node, they are connected
#union will point to a common node
#so the data structure allows us to union two graphs into the same graph which is now connected but conaining no cycles
class DisjointSet:
    #each node will have a parent pointer to check set memebership and a value, also neighbor value to attach to another node
    def __init__(self, parent, val, next=None):
        self.parent = parent
        self.val = val, self.next = next
    #find operation to check set membership-- gets the value of the current nodes parent, if same as node comparing with then in the same tree
    #get the parent by checking nodes neighbor until the parent value is that nodes value
    def find(node):
        currNode = node
        while currNode.parent.val != currNode.val:
            currNode = currNode.next
        return currNode.val
    #union will add an edge between two nodes but will make the parent equal to the same node
    #only runs if the result of find is a different parent node(they are not connected yet)
    def union(self, n1, n2):
        n1Parent = self.find(n1)
        n2Parent = self.find(n2)
        #going to point node 2 parent to the parent of node 1 before adding edge between node 1 and 2
        if n1Parent != n2Parent:
            n2.parent = n1.parent
            n2.next = n1
        return
    

