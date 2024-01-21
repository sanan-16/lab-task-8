class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def kth_smallest_element(root, k):
    count = [0]  # Using a list to store the count since lists are mutable

    def in_order_traversal(node):
        if node is not None:
            # Traverse left subtree
            left_result = in_order_traversal(node.left)
            if left_result is not None:
                return left_result

            # Visit the current node
            count[0] += 1
            if count[0] == k:
                return node.key

            # Traverse right subtree
            return in_order_traversal(node.right)

    return in_order_traversal(root)

# Example usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

k = 3
result = kth_smallest_element(root, k)
print(f"The {k}-th smallest element in the BST is: {result}")
