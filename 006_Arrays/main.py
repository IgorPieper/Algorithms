strings = ['a', 'b', 'c', 'd']
strings2 = ['x' 'y', 'z']
print(strings)

# Add at the end - O(1)
strings.append('e')
print(strings)

# Delete from the end - O(1)
strings.pop()
print(strings)

# Add at given position - O(n)
strings.insert(0, 'x')
print(strings)

# Find and delete element - O(n)
strings.remove('c')
print(strings)

# Reverse list - O(n)
strings.reverse()
print(strings)

# Transform list into string - O(n)
oneString = "".join(strings)
print(oneString)

# Transform string into list - O(n)
print(list(oneString))

# Connecting 2 lists - O(n + m)
print(strings + strings2)

# Sorting list - O(n log n)
strings.sort()
print(strings)
