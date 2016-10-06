""" TREE QUESTIONS """

""" CHECK IF TREE IS BALANCED - WITH EXCEPTIONS """

class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 

    def __str__(self):
        "Root node={0}.".format(self.data)

    def is_balanced(self):
        """ Contains nested function; raises error."""

        try:
            _num_descendants(self)
            return True
        except ValueError:
            return False

        def _num_descendants(node):
            """ Returns num of descendents or None if already imbalanced."""

            if not node:
                # base case: not a real node (child or leaf)
                return 0

            # get descendents on left; if None -- already imbalanced - bail out!
            left = _num_descendants(node.left)

            # get descendents on right; if None - bail out
            right = _num_descendants(node.right)

            if abs(left - right) > 1:
                # height varies by more than 1 -- imbalanced!
                raise ValueError() 

            # height of this node is height of our deepest descendant + ourselves
            return max(left, right) + 1 

        return _num_descendants

""" CHECK TREE BALANCED WITHOUT EXCEPTIONS. """

class Node(object):

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right 

    def __str__(self):
        "Root of tree={0}.".format(self.root)

    def is_balanced(self):

        # nested for order and organization
        def _num_descendents(node):

            # base case: not a real node 
            if node is None:
                return 0

            # else, get descendents on left 
            left = _num_descendants(node.left)

            # if left has none - bail out! already imbalanced
            if left is None:
                return None 

            right = _num_descendants(node.right)

            # if right has none - bail out! already imbalanced 
            if right is None:
                return None

            # left and right had nodes but heights vary more than 1 
            if abs(left - right) > 1:
                return None 

            # height of this node is the height of our deepest descendent + ourselves
            return max(left, right) + 1 

        return _num_descendants(self) is not None








