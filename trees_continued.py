
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

# used to translate expressions to postfix, prefix and infix
# also used inside compilers to parse, optimize and translate programs

""" PRINTING EXPRESSION TREES. """

# Preorder tree traversal

def print_tree(tree):
    """
    Preorder tree traversal: contents of root node appear before contents of leaf nodes. 
    Results in prefix notation output for expressions passed through.
    """
    if tree is None: return 
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

# >>> tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3))) 
# >>> print_tree(tree)
# + 1 * 2 3

""" GRAPHICAL REPRESENTATION FOR INORDER, INFIX OUTPUT. """

# keep track of level for each recursive call 
# by default, level begins at 0 

def print_tree_indented(tree, level=0):
    if tree is None: return 
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

# >>> print_tree_indented(tree, level=0)
#    3
#  *
#    2
#+
#  1











