
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
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)








