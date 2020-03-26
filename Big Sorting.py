def bigSorting(unsorted):
    for i in range(n):
        unsorted[i] = int(unsorted[i])
    print(unsorted)
    list_sorted = sort(unsorted)
    print(list_sorted)

    for j in range(n-1):
        print(str(list_sorted[j]))
    return str(list_sorted[-1])


n = 6
unsorted = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']
print(bigSorting(unsorted))
# unsorted = [31415926535897932384626433832795, 1, 3, 10, 3, 5]
# print(bigSorting(unsorted))


# TypeError: sequence item 0: expected str instance, int found
