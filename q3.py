class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.key

# Example usage
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)

min_value = find_min(root)
max_value = find_max(root)

print("Minimum value in the BST:", min_value)
print("Maximum value in the BST:", max_value)
