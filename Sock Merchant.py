def sockMerchant(n, ar):
    pair = 0
    for a in (set(ar)):
        pair += ar.count(a)//2

    return pair


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))
