import numpy
import numpy as np

n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for j in range(n):
    b.append(list(map(int, input().split())))


a = np.array(a)
b = np.array(b)


np.set_printoptions(legacy='1.13')
print(np.dot(a, b))


a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))


np.set_printoptions(legacy='1.13')
print(np.inner(a, b))
print(np.outer(a, b))
print numpy.polyval([1, -2, 0, 2], 4)


p = np.array(list(map(int, input().split())))
x = int(input())
print(np.polyval(p, x))


n = int(input())
a = []
for i in range(n):
    a.append(list(map(float, input().split())))
a = np.array(a)
np.set_printoptions(legacy='1.13')
print(np.linalg.det(a))


numpy.array(list(map(float, arr)))[::-1] reverse numpy array

n, m, p = map(int, input().split())


print(n, m, p)


n, m = map(int, input().split())

a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for j in range(n):
    b.append(list(map(int, input().split())))
a = np.array(a)
b = np.array(b)


np.set_printoptions(legacy='1.13')
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a % b)
print(a**b)
