
""" ASSEMBLE NEW TREE """
class Tree:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 

    def __str__(self):
        return str(self.cargo)

""" Add children and construct parent. """

# constructing from 'bottom-up'
# allocate child nodes first 
left = Tree(2)
right = Tree(3)

# construct parent node and link children 
# more concisely written by nesting constructor invocations
tree = Tree(1, Tree(2), Tree(3))

#OR 

tree = Tree(1, left, right)

""" TREE TRAVERSAL"""

def total(tree): 
    """ Sum nodes recursively."""

    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

""" CONSTRUCTING AN EXPRESSION TREE."""

# infix equation: 1 + 2 * 3 

tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))







