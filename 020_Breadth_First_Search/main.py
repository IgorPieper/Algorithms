from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert: average - O(log n) worst - O(n)
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    # Lookup: average - O(log n) worst - O(n)
    def lookup(self, value):
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return current_node
        return None

    # Remove: average - O(log n) worst - O(n)
    def remove(self, value):
        current_node = self.root
        parent_node = None

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            else:
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    elif current_node.value < parent_node.value:
                        parent_node.left = current_node.left
                    else:
                        parent_node.right = current_node.left

                elif current_node.right.left is None:
                    current_node.right.left = current_node.left
                    if parent_node is None:
                        self.root = current_node.right
                    elif current_node.value < parent_node.value:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right = current_node.right

                else:
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right

                    while leftmost.left:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if parent_node is None:
                        self.root = leftmost
                    elif current_node.value < parent_node.value:
                        parent_node.left = leftmost
                    else:
                        parent_node.right = leftmost

                return True

        return False

    def breadth_first_search(self):
        if self.root is None:
            return []

        queue = deque([self.root])
        result = []

        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result


def traverse(node):
    if node is None:
        return None

    return {
        "value": node.value,
        "left": traverse(node.left),
        "right": traverse(node.right)
    }


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    tree.remove(170)

    print("Tree structure:")
    print(traverse(tree.root))

    print("\nBFS traversal:")
    print(tree.breadth_first_search())
