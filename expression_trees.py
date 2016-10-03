
""" Building expression trees by parsing infix expressions."""

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def print_tree_preorder(tree):
        if tree is None: return
        print(tree.cargo, end=" ")
        print_tree_preorder(tree.left)
        print_tree_preorder(tree.right)

    def print_tree_postorder(tree):
        if tree is None: return
        print_tree_postorder(tree.left)
        print_tree_postorder(tree.right)
        print(tree.cargo, end=" ")

    def print_tree_inorder(tree):
        if tree is None: return 
        print_tree_inorder(tree.left)
        print(tree.cargo, end=" ")
        print_tree_inorder(tree.right)

    ### write tokenization function for converting input_string into token
    def string_to_token(expression_string):
        """ Convert a string into a tokenized list."""
        pass 

    def get_token(token_list, expected):
    """ Check first item in token list."""
        if token_list[0] == expected:
            del token_list[0]
            return True
        return False 

    # since token_list is mutable, changes here are visible to 
    # any other variable that refers to the same object. 

    def get_number(token_list):
        """ See if next number is int. Del if True, return new Tree node. """
        if get_token(token_list, '('):
            x = get_sum(token_list)         # grab the sub-expression enclosed
            if not get_token(token_list, ')')      # remove the parenthesis 
                raise ValueError('Missing close parenthesis') # throws an error if parenthesis is missing 
            return x 
        else:
            x = token_list[0]
            if type(x) != type(0): return None
            del token_list[0]
            return Tree(x, None, None)

    def get_product(token_list):
        """ Build an expression tree for products."""
        a = get_number(token_list)
        if get_token(token_list, "*"):
            b = get_product(token_list) # call recursively to deal with compound products
            return Tree("*", a, b)
        return a 

    # assuming get_number succeeds and returns a singleton tree
    # a product can be either a singleton tree or a a tree with a *
    # at the root, a number on the left and a product on the right

    def get_sum(token_list):
        """ Build a tree of either sums and products or simply a product."""
        a = get_product(token_list)
        if get_token(token_list, "+"):
            b = get_sum(token_list)
            return Tree("+", a, b)
        return a 







