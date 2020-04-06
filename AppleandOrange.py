def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = sum([1 for x in apples if x+a >= s and x+a <= t])
    orange = sum([1 for o in oranges if o + b >= s and o + b <= t])
    return print(apple, orange, sep="\n")


s, t, a, b, = 7, 11, 5, 15
apples = [-2, 2, 1]
oranges = [5, -6]
countApplesAndOranges(s, t, a, b, apples, oranges)
