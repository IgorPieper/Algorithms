class Stack:
    def __init__(self):
        self.__data = []

    # Add – O(1)
    def push(self, value):
        self.__data.append(value)

    # Remove – O(1)
    def pop(self):
        if not self.__data:
            raise IndexError("pop from empty stack")
        return self.__data.pop()

    # Show top element – O(1)
    def peek(self):
        if not self.__data:
            return None
        return self.__data[-1]

    # Check if stack is empty – O(1)
    def is_empty(self):
        return len(self.__data) == 0

    # Return number of elements – O(1)
    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Stack(top -> {list(reversed(self.__data))})"
