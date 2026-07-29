#binary trees
from collections import deque


class TreeNode():

    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)
    ##pre order traversl for dfs: node->left->right is the order of processing(printing)
#since each node only has 1 path to it(parent) we dont need to keep a visited list because we can never get it again
#theres no route back to a node after its parent is popped off the stack
#so preorder dfs goes down ENTIRE left side and then entire right side and at each side it does the same thing for all the sub trees
    def preorder(self, node):
        callstack = [node]#start at node and then add the right and the left so that left is on top because we go node to left then right
        while callstack:
            currentNode = callstack.pop()
            print(currentNode)
            if currentNode.right:callstack.append(currentNode.right)
            if currentNode.left: callstack.append(currentNode.left)
    ##recursive dfs for preorder: going to work all the way down the left side before moving to the right side and will print the current node before each call
    #since it is printing node before the calls it means it goes node and then the left side will finish running which will print each node there and then the right side will go last printing each node there
    #base case is when the node is none because that means the side we called is a dead end, so then just return 
    def preorder_dfs(self, node):
        if node is None:
            return
        #this order makes sure the current node is printed and then the current node at each left call and finally all the nodes at the right call
        print(node)
        self.preorder_dfs(node.left)
        self.preorder_dfs(node.right)
        #this is dfs because returns the entire left subtree and then the entire right subtree and same for the calls, which means it goes down one path at a time
    #now for inorder dfs: will go left -> node -> right
    #this means we will not print any nodes until we work all the way left-- so it is smallest to largest if bst
    def inorder_dfs(self, node):
        if node is None:
            return
        self.inorder_dfs(node.left)
        print(node)
        self.inorder_dfs(node.right)
    ##now for post order dfs: this goes left -> right -> current node call
    #this will go down entire left and right subtrees before printing the top node call
    def postorder_dfs(self, node):
        if node is None:
            return
        self.postorder_dfs(node.left)
        self.postorder_dfs(node.right)
        print(node)
    #bfs: prints every node at the current level before moving to the next, and will print the left side first starting from a node
    def bfs(self,root):
        queue = deque([root])
        while queue:
            currNode = queue.popleft()#this is the node at the current level
            if currNode.left is not None: queue.append(currNode.left)
            if currNode.right is not None: queue.append(currNode.right)
            print(currNode)
    

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
#this tree is techinally from A
A.preorder_dfs(A)
A.postorder_dfs(A)
A.bfs(A)


    

