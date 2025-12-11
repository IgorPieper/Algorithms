def revers_a_string(a):
    reversedA = []
    for aa in a:
        reversedA.insert(0, aa)
    return "".join(reversedA)


print(revers_a_string("Dupa z Trupa"))
