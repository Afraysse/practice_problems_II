""" BINARY SEARCH TREES

A binary search tree (BST) or ordered binary tree is a node-based binary tree
data structure which has these properties:

1. Left subtree of a node contains only nodes with keys < node's keys 
2. Right subtree of a node contains only nodes with keys > node's keys 
3. Both left and right subtrees must be binary search trees 

"""


class Node(object):
    """Need to represent a tree node with 3 main attributes:
            Left/Right/Data
    """

    def __init__(self, data):
        """ Node constructor 

        @param data node data object
        """

        self.left = None
        self.right = None
        self.data = data 

    def __repr__(self):

        return "<data=%s>" % (self.data)
        # return str(self.data) also works 

    """ 
    CREATE A NODE - can pass any object in for the data so its flexible.

    root = Node(8)
    """

    def insert_node(self, data):
    """ Insert new node with data.

    Insert() is called recursively as we are locating the place where to add
    the new node in the tree.
    """ 

    if self.data:
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data 

    """ Adding more nodes. 

    root.insert(3)
    root.insert(10)
    root.insert(1)

    # adding second node (3)
        1 - root node's method insert() is called with data = 3 
        2 - 3 < 8 and left child is None so we attach the new node to it 

    # adding third node (10)
        1 - root node's method insert() is called with data = 10 
        2 - 10 > 3 and the right child is None so we attach the new node to it

    # adding fourth node (1)
        1 - root node's method insert() is called with data = 1
        2 - *1 < 8 so the root's left child (3) insert() method is called with 
        data = 1

        * call the insert() method on the subtree since left already has a node 

        3 - 1 < 3 and left child is None so we attach the new node to it 











