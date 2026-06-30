#bad this is recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversalRecursive(root):
    route = []
    def checkChild(node):
        if node.left is not None:
            checkChild(node.left)

        route.append(node.val)

        if node.right is not None:
            checkChild(node.right)

    if root is not None:
        checkChild(root)

    return route

root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.left.left = TreeNode(val=4)
root.left.right = TreeNode(val=5)
root.left.right.left = TreeNode(val=6)
root.left.right.right = TreeNode(val=7)
root.right = TreeNode(val=3)
root.right.right = TreeNode(val=8)
root.right.right.left = TreeNode(val=9)

print(inorderTraversalRecursive(root))