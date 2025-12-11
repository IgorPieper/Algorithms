class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0

        if value is not None:
            self.append(value)

    # Add at the end - O(1)
    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    # Add at the beginning - O(1)
    def prepend(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    # Go to index - O(n)
    def _traverse_to(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.prev

        return current

    # Add in any place - O(n)
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return

        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)
        leader = self._traverse_to(index - 1)
        follower = leader.next

        new_node.prev = leader
        new_node.next = follower
        leader.next = new_node
        follower.prev = new_node

        self.length += 1

    # Delete item from index - O(n)
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.length -= 1
            return removed.value

        if index == self.length - 1:
            removed = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return removed.value

        node = self._traverse_to(index)
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.length -= 1
        return node.value

    # Find element - O(n)
    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    # Show list - O(n)
    def print_forward(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        print(" <-> ".join(result))

    # Show list in reverse - O(n)
    def print_backward(self):
        current = self.tail
        result = []
        while current:
            result.append(str(current.value))
            current = current.prev
        print(" <-> ".join(result))
