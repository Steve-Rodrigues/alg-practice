##a tree is an undirected graph with no cycles which is also heirarichally structured and ocntains n nodes with n-1 edges because each node is only connected once to its parent and children
#Binary trees: trees where each node can only have a max of 2 children and also has a root parent node which typically only has edges going outward
#binary search tres(bst): binary trees where the left child is less than the current node value and the right child is greater than the current node value
#bst allows for fast lookup because can choose direction baqsed on the current node value and the value you want to find
##also important to remember that tres are just arrays, we use the trees/graphs to represent them visually but they are just arrays with each node being represented with their edge connections

#implementing a tree node class (binary tree) so it has at most 2 children, each a pointer to left and right child 
from collections import deque
import random


class TreeNode():
    #make a node with a left pointer and right pointer to other nodes which are the children
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right=right
    ##adding a node to a side of the tree(not bst so choose the side)
    def add_node(self, side:str, node):
        if side.lower() == 'left':self.left = node
        else: self.right=node
        print(f'Added {node} as a {side} child')
#choose a node to start from and go from there--using bfs so level by level
def traverse(node):
        node_queue = deque([node])
        res = []
        while node_queue:
            #pop and add the children 
            current_node = node_queue.popleft()
            res.append(current_node.key)
            l_child, r_child = current_node.left, current_node.right
            if l_child is not None: node_queue.append(l_child)
            if r_child is not None: node_queue.append(r_child)
        return res
#traverse using dfs
def dfs_search(startNode):
     visited = {startNode}
     stack = [startNode]
     print(startNode.key)
     while stack:
        curr_node = stack[-1]
        #always start left to try
        if curr_node.left is not None and curr_node.left not in visited:
             stack.append(curr_node.left)
             visited.add(curr_node.left)
             print(curr_node.left.key)
        elif curr_node.right is not None and curr_node.right not in visited:
             stack.append(curr_node.right)
             visited.add(curr_node.right)
             print(curr_node.right.key)

        else:
             stack.pop()
        
        
        
          

root = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(3)
l2 = TreeNode(4)
r2 = TreeNode(5)
l3 = TreeNode(6)
root.add_node('left', l1)
root.add_node('right', r1)
l1.add_node('left', l2)
r1.add_node('right', r2)
l2.add_node('left', l3)
print(traverse(root))
dfs_search(root)



    


            


        


