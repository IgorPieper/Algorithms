class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    # Add at the begining - O(1)
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.length == 0:
            self.tail = new_node

        self.length += 1

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
        new_node.next = leader.next
        leader.next = new_node
        self.length += 1

    # Delete item from index - O(n)
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index == 0:
            removed = self.head
            self.head = self.head.next
            self.length -= 1

            if self.length == 0:
                self.tail = None

            return removed.value

        leader = self._traverse_to(index - 1)
        unwanted = leader.next
        leader.next = unwanted.next

        if index == self.length - 1:
            self.tail = leader

        self.length -= 1
        return unwanted.value

    # Find element - O(n)
    def find(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    # Go to index - O(n)
    def _traverse_to(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # Show list - O(n)
    def print(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result))
