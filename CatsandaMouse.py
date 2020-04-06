def catAndMouse(x, y, z):
    X = abs(x - z)
    Y = abs(y-z)
    if X < Y:
        cat = "Cat A"
    elif X > Y:
        cat = "Cat B"
    else:
        cat = "Mouse C"
    return cat

catAndMouse(x, y, z)
