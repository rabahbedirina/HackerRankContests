def countingValleys(n, s):
    see = 0
    count_valley = 0
    count_mountain = 0

    for i in range(n):
        if s[i] == "U":
            see += 1
        else:
            see -= 1
        if see == 0 and s[i] == "U":
            count_valley += 1
        if see == 0 and s[i] == "D":
            count_mountain += 1

    return count_valley, count_mountain


n = 8
s = "UDDUUDDU"
print(countingValleys(n, s))
n = 8
s = "UDDDUDUU"
print(countingValleys(n, s))
n = 12
s = "DDUUDDUDUUUD"
print(countingValleys(n, s))
