def angryProfessor(k, a):
    count = len([x for x in a if x <= 0])
    if count >= k:
        cancell = "NO"
    else:
        cancell = "YES"
    return cancell


t = int(input())

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)
    print(result)
