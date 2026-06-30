#bad this is recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    def inorderTraversalRecursive(root):
        route = []
        def checkChild(node):
            if node.left is not None:
                checkChild(node.left)
            else:
                route.append(None)
            
            route.append(node.val)
    
            if node.right is not None:
                checkChild(node.right)
            else:
                route.append(None)
            
        if root is not None:
            checkChild(root)

        print(route)
        return route

    return inorderTraversalRecursive(p) == inorderTraversalRecursive(q)

p = TreeNode(val=1)
p.left = TreeNode(val=2)
p.right = TreeNode(val=3)
q = TreeNode(val=1)
q.left = TreeNode(val=2)
q.right = TreeNode(val=3)

print(isSameTree(p, q))