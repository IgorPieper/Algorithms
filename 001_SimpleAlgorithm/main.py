large = ["nemo"] * 100000

def find_nemo(array):
    for item in array:
        if item == "nemo":
            print("Found NEMO!")


find_nemo(large)

# O(n) time complexity
