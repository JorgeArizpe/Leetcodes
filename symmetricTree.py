class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    
    def isSame(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False

        return isSame(node1.left, node2.right) and isSame(node1.right, node2.left)

    return isSame(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(2)
root3.right = TreeNode(2)
root3.right.left = TreeNode(2)

# print(isSymmetric(root))
# print(isSymmetric(root2))
print(isSymmetric(root3))