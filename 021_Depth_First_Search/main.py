class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def traverse_in_order(node, out):
    if node is None:
        return out
    if node.left:
        traverse_in_order(node.left, out)
    out.append(node.value)
    if node.right:
        traverse_in_order(node.right, out)
    return out


def traverse_pre_order(node, out):
    if node is None:
        return out
    out.append(node.value)
    if node.left:
        traverse_pre_order(node.left, out)
    if node.right:
        traverse_pre_order(node.right, out)
    return out


def traverse_post_order(node, out):
    if node is None:
        return out
    if node.left:
        traverse_post_order(node.left, out)
    if node.right:
        traverse_post_order(node.right, out)
    out.append(node.value)
    return out


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return self
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return self
                current = current.right

    def lookup(self, value):
        if self.root is None:
            return None

        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
        return None

    def remove(self, value):
        if self.root is None:
            return False

        current = self.root
        parent = None

        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif current.value < parent.value:
                        parent.left = current.left
                    else:
                        parent.right = current.left

                elif current.right.left is None:
                    current.right.left = current.left
                    if parent is None:
                        self.root = current.right
                    elif current.value < parent.value:
                        parent.left = current.right
                    else:
                        parent.right = current.right

                else:
                    leftmost = current.right.left
                    leftmost_parent = current.right

                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    leftmost_parent.left = leftmost.right
                    leftmost.left = current.left
                    leftmost.right = current.right

                    if parent is None:
                        self.root = leftmost
                    elif current.value < parent.value:
                        parent.left = leftmost
                    else:
                        parent.right = leftmost

                return True

        return False

    def dfs_in_order(self):
        return traverse_in_order(self.root, [])

    def dfs_pre_order(self):
        return traverse_pre_order(self.root, [])

    def dfs_post_order(self):
        return traverse_post_order(self.root, [])


def traverse(node):
    if node is None:
        return None
    return {
        "value": node.value,
        "left": traverse(node.left),
        "right": traverse(node.right),
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

    print("DFS PostOrder:", tree.dfs_post_order())
    # print("DFS InOrder:", tree.dfs_in_order())
    # print("DFS PreOrder:", tree.dfs_pre_order())

    # print(traverse(tree.root))
