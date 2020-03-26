# Complete the formingMagicSquare function below.
# def formingMagicSquare(s):

#     p = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]], [
#         [8, 3, 4], [1, 5, 9], [6, 7, 2]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]], [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
#     rep = []
#     print(len(p))
#     for x in range(len(p)):
#         su = 0
#         for i in range(3):
#             for j in range(3):
#                 print(s[i][j])
#                 print(p[i][j])

#                 su += abs(s[i][j] - p[i][j])
#         rep.append(su)

#     return min(rep)
import itertools as it
import math as ma
r = 4
# text = range(0, 10)
# p = list(it.product(text, r))
# # for i in range(len(p)):
# #     # if p[i][0] == 7 and p[i][1] == 7:
# #     #     continue
# #     print(p[i])

# print(len(p))
# n = len(text)
per = (ma.factorial(10))/(ma.factorial(4)*ma.factorial(3)*ma.factorial(2))
print(per)


# s = [[3, 9, 4], [3, 5, 6], [7, 9, 3]]


# #
# #
# #
# #
#
#

# c = 5
# if s[0][0] == 4 or s[2][2] == 6:
#     a, b = 3, 1
# elif s[0][0] == 6 or s[2][2] == 4:
#     a, b = -3, -1
# elif s[2][0] == 6 or s[0][2] == 4:
#     a, b = 1, -3
# elif s[2][0] == 4 or s[0][2] == 6:
#     a, b = -1, 3

# mat = [[c - b, c + a + b, c - a], [c - a + b,
#                                   c, c + a - b], [c + a, c - a - b, c + b]]
