
from scipy.spatial import distance as dis
import itertools as it

# blocks = [[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]]
# r = 3
# c = 4
r = 10
c = 2
blocks = [[1, 0],
          [1, 0],
          [1, 0],
          [0, 0],
          [0, 0],
          [1, 1],
          [0, 1],
          [1, 0],
          [0, 0],
          [1, 0]]
setup = []
for i in range(r):
    for j in range(c):
        if blocks[i][j] == 1:
            setup.append([i+1, j+1])

p = it.permutations(setup, len(setup))

E = []
some = 0
for item in p:
    for j in range(len(item) - 1):
        some += max(int(dis.chebyshev(item[0], item[j + 1])),
                    int(dis.chebyshev(item[j], item[j + 1])))

    E.append(some)

print(setup)
print(min(E))
