class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root

    # Search for the node to be deleted
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        root.key = find_min(root.right).key

        # Delete the inorder successor
        root.right = delete_node(root.right, root.key)

    return root

# Helper function to print the inorder traversal of the tree
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Example usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Inorder Traversal before deletion:", end=" ")
inorder_traversal(root)

key_to_delete = 5
root = delete_node(root, key_to_delete)

print("\nInorder Traversal after deleting", key_to_delete, ":", end=" ")
inorder_traversal(root)
