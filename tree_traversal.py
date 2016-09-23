class Node(object):

    __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data



def preOrder(root):
    """ Print out nodes of tree in depth first order, on one line"""

    to_visit = [root]

    while to_visit:
        current = to_visit.pop()
        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)

        print current.data,



def postOrder(root):

    if not root.left and not root.right:
        print root.data,
    else:
        if root.left:
            postOrder(root.left)
        if root.right:
            postOrder(root.right)
        print root.data,


def inOrder(root):

    if not root.left:
        print root.data,
    
    else:
        if root.left:
            inOrder(root.left)
            
        print root.data,
        
        if root.right:
            inOrder(root.right)



