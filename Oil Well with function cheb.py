import itertools as it


def oilWell(blocks):
    setup = []
    for i in range(r):
        for j in range(c):
            if blocks[i][j] == 1:
                setup.append([i+1, j+1])
    p = it.permutations(setup, len(setup))

    def distance(p, q):
        return max([abs(x - y) for x, y in zip(p, q)])

    E = 999999999

    for item in p:

        some = 0
        maximum = 0
        for j in range(len(item) - 1):
            test = max(int(distance(item[0], item[j + 1])),
                       int(distance(item[j], item[j + 1])), maximum)
            if maximum < test:
                maximum = test
            some += test

        if some < E:
            E = some

    return E


# blocks = [[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]]
# r = 3
# c = 4
# print(oilWell(blocks))
# r = 10
# c = 2
# blocks = [[1, 0],
#           [1, 0],
#           [1, 0],
#           [0, 0],
#           [0, 0],
#           [1, 1],
#           [0, 1],
#           [1, 0],
#           [0, 0],
#           [1, 0]]

# print("expected 31", oilWell(blocks))

# r = 7
# c = 8


# blocks = [[1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1], [
#     0, 0, 1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 1, 1, 1]]

# print("expected 177", oilWell(blocks))

r = 10
c = 10
blocks = [[0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1, 1]]

print("expected 109", oilWell(blocks))
