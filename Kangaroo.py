def kangaroo(x1, v1, x2, v2):
    if v1 - v2 <= 0 or x2 - x1 <= 0:
        k = "NO"
    else:
        if (x2-x1) % (v1-v2) == 0:
            k = "YES"
            print("Jump =", (x2-x1) % (v1-v2))
        else:
            k = "NO"
    return k


x1, v1 = 21, 6
x2, v2 = 47, 3
print(kangaroo(x1, v1, x2, v2))
x1, v1 = 0, 2
x2, v2 = 5, 3
print(kangaroo(x1, v1, x2, v2))
