from collections import deque


class Queue:
    def __init__(self):
        self.__data = deque()

    # Add – O(1)
    def enqueue(self, value):
        self.__data.append(value)

    # Remove – O(1)
    def dequeue(self):
        if not self.__data:
            raise IndexError("dequeue from empty queue")
        return self.__data.popleft()

    # Show – O(1)
    def peek(self):
        if not self.__data:
            return None
        return self.__data[0]

    # Check if queue is empty – O(1)
    def is_empty(self):
        return len(self.__data) == 0

    # Return number of items – O(1)
    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Queue(front -> {list(self.__data)})"
