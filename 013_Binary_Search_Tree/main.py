class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # O(log n)
    def insert(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # O(log n)
    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    # O(log n)
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # O(log n)
    def delete(self, value):
        self.root = self._delete_rec(self.root, value)

    def _delete_rec(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_rec(node.left, value)
        elif value > node.value:
            node.right = self._delete_rec(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_rec(node.right, min_larger_node.value)

        return node

    # Traversal - O(n)
    def inorder(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node, result):
        if node:
            self._inorder_rec(node.left, result)
            result.append(node.value)
            self._inorder_rec(node.right, result)

    def __repr__(self):
        return f"BST(inorder={self.inorder()})"
