class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_bst(root, target):
    if root is None or root.key == target:
        return root

    if target < root.key:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

# Example usage
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)

target_value = 6
result = search_bst(root, target_value)

if result:
    print(f"Node with value {target_value} found in the BST.")
else:
    print(f"Node with value {target_value} not found in the BST.")
