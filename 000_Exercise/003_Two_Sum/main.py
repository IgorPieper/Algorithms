# O(n^2)
def two_sum(a, b):
    i = 0
    ii = 1

    while True:
        if a[i] + a[ii] == b:
            return [i, ii]
        else:
            if ii < len(a)-1:
                ii += 1
            else:
                i += 1
                ii = i+1


# O(n)
def better_two_sum(a, b):
    seen = {}
    for i, num in enumerate(a):
        diff = b - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

        
a = [11, 15, 2, 7]
b = 9
