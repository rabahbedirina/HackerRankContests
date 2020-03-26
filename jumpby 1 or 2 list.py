def jumpingOnClouds(c):
    i = 0
    count = -1
    n = len(c)

    while i < n:
        print(i)
        if (i < n - 2)and (c[i + 2] == 0):
            i += 2

        else:
            i += 1
        count += 1
    return count


# c = [0, 0, 1, 0, 0, 1, 0]
# print(jumpingOnClouds(c))
c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))
