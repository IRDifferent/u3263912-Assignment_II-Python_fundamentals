#Stephen James | u3263912 | 10/09/2025 | Case Study 3

#Figure 1
def result_1():
    A = False
    B = False
    C = False
    
    a = not A
    b = not C
    c = not a and not b
    d = not B
    e = A and c and B
    f = A and B and C
    g = e or f
    return g

#Figure 2
def result_2():
    A = True
    B = True
    C = True

    h = not B
    i = h or C
    j = i and A
    return j


print(f"Figure a): {result_1()}")
print(f"Figure b): {result_2()}")

