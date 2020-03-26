
def miniMaxSum(arr):
    sumexc = []
    for i in range(len(arr)):
        som = 0
        for j, num in enumerate(arr):
            if i != j:
                som += num
        sumexc.append(som)
    minmax = [min(sumexc), max(sumexc)]
    return minmax


#
#
#
#
#
arr = [5, 5, 5, 5, 5]

print(miniMaxSum(arr))

print('expected minmax = [10, 14]')
