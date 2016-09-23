
class Node(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def binary_traversal(root):
    """
    >>> root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7) ) ), Node(10, right=Node(14, left=Node(13) ) ) )
    >>> binary_traversal(root)
    1
    3
    4
    6
    7
    8
    10
    13
    14
    """

    if not root.left and not root.right:
        print root.data

    else:
        if root.left:
            binary_traversal(root.left)

        print root.data

        if root.right:
            binary_traversal(root.right)




# root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7) ) ), Node(10, right=Node(14, left=Node(13) ) ) ) 

# binary_traversal(root)



if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n **ALL TESTS PASSED**"










