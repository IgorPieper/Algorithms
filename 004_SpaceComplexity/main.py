def SayHi(n):
    for _ in range(len(n)):
        print("Hi")


SayHi([1, 2, 3, 4, 5])   
# O(1) space complexity

# -------------------------------- #

def SayHi2(n):
    hi_array = []
    for i in range(n):
        hi_array.append("hi")
    return hi_array


print(SayHi2(6))   
# O(n) space complexity
