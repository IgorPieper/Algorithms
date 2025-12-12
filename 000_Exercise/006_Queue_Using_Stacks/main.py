class QueueUsingStacks:
    def __init__(self):
        self.__in_stack = []
        self.__out_stack = []

    # Add – O(1)
    def enqueue(self, value):
        self.__in_stack.append(value)

    # Remove – amortized O(1)
    def dequeue(self):
        if not self.__out_stack:
            if not self.__in_stack:
                raise IndexError("dequeue from empty queue")

            while self.__in_stack:
                self.__out_stack.append(self.__in_stack.pop())

        return self.__out_stack.pop()

    # Show – amortized O(1)
    def peek(self):
        if not self.__out_stack:
            if not self.__in_stack:
                return None
            while self.__in_stack:
                self.__out_stack.append(self.__in_stack.pop())

        return self.__out_stack[-1]

    def is_empty(self):
        return not (self.__in_stack or self.__out_stack)

    def __repr__(self):
        temp = self.__out_stack[::-1] + self.__in_stack
        return f"QueueUsingStacks(front -> {temp})"
