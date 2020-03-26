def birthdayCakeCandles(ar):
    tallest_candle = max(ar)
    candle_count = 0
    for height in ar:
        if height == tallest_candle:
            candle_count += 1
    return candle_count


ar_count = 4

ar = [3, 2, 1, 3]
print(birthdayCakeCandles(ar))
