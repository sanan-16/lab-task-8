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

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

def find_inorder_successor_predecessor(root, key):
    if root is None:
        return None, None

    successor = None
    predecessor = None

    current = root

    while current is not None:
        if key < current.key:
            successor = current
            current = current.left
        elif key > current.key:
            predecessor = current
            current = current.right
        else:
            if current.right is not None:
                successor = find_min(current.right)
            if current.left is not None:
                predecessor = find_max(current.left)
            break

    return successor, predecessor

# Example usage
root = TreeNode(15)
root.left = TreeNode(8)
root.right = TreeNode(20)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right.right = TreeNode(25)

target_key = 12
successor, predecessor = find_inorder_successor_predecessor(root, target_key)

print(f"In-order Successor of {target_key}: {successor.key if successor else None}")
print(f"In-order Predecessor of {target_key}: {predecessor.key if predecessor else None}")
