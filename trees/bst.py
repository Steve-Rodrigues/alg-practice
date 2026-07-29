##Binary Search Trees (BST) is a binary tree where the left side is always less than the root and right side is always greater than the root
#so if you wanted to get valkues from smallest to greates you could do a dfs in the inorder way because goes all the way left (less) then middle then right which is greater
class BST():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right=right
    def __str__(self):
        return str(self.val)

#attempting to make a search function for the bst
##searching is O(logn) on avg because we are basically doing a binary search and if the value is greater thna the node we just go to the right half so we split in half each time
#however if the bst is only in one direction than it could be linear time since there are no other sides
def search(root, targ):
    #also check if the root is None because that means we could not find it, or it was an invalid bst 
    if root is None:
        return -1
    #check if the root is the target for the base case
    if root.val == targ:
        return root.val
    #if not we need to check which side it will be on
    elif targ < root.val: #on the left side, call the search again, now on that side
        return search(root.left, targ)
    else:#we need to search the right side
        return search(root.right, targ)
##inserting into bst: takes the root and the new node as args and inserts the new node where it belongs based on the root(either left or right)
#if the node taken in is None then the new one is set right there (thats the right spot)
#we return either the new node(base case) or the root(had to recurse) and that is because we set the roots left or right pointer equal to the result of the next function call
#this is so the root will be connected to the new placement and if the next call is still not NOne than the pointer did not chance
#so root is the root of the current calls subtree
def insertBST(root, newNode):
    #base case--creates and returns the node when in correct spot so the pointer is updated to it
    if root is None:
        node = BST(newNode)
        return node
    #move to the left if the value is smaller than root(just like binary search)
    elif newNode < root.val:
        #set the left pointer equal to result of this call just incase that is the empty spot
        root.left = insertBST(root.left, newNode)
    else:#must go to the right of the root
        root.right = insertBST(root.right, newNode)
    #return the root node (current node ) if not the correct spot yet
    return root

#deletion with bst: again avg is going to be logn because we just split the tree in half until finding the node

#need this function for case 3 which is when the target node has 2 children so we cant jsut delete it, needs to be replaced with a node that will keep the bst properties
#because both of the children can't point to one node (that would be more than 2 children per side) so we replace with smallest on the right side
#this works because leftmost on right side is smaller than the right child but bigger than the left since it was on the right side
def getSuccessor(curr):
    #curr is the current node(target)-- we want to traverse until the curr.left is None
    curr = curr.right #this sets to the right child
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr #returns the leftmost node to be placed in the target spot and pointers updated to this

def deleteBST(root, x):
    if root is None:
        return root
    #check which side to keep looking on (binary searching)
    if x < root.val: #on the left side, need to set pointer to the result of the call so we can update it for deletion
        root.left = deleteBST(root.left, x)
    elif root.val < x: #go to the right side
        root.right = deleteBST(root.right,x)
    #if we found the spot we must check the conditions (the children amount)
    else:
        #first check the single children cases, and then return either pointer still active to this parent pointer edge
        if root.right is None:#target has no right so it sets the parent pointer to the left child
            return root.left
        if root.left is None:
            return root.right
        else:#going to need to replace with smallest in right side
            newNode = getSuccessor(root)
            #set that equal to the target and then call delete on the new node.val so its paretn removes the pointer
            root.val = newNode.val
            root.right = deleteBST(root.right, newNode.val)
        return root#returning the root so the parent call points to it
    









    



        

