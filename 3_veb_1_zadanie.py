def pol():
    try:
        x = float(input('число x: '))
        z = float(input('число y: '))
        ff = x // z
    except ZeroDivisionError:
        return
    return ff


dd = pol()
print(dd)
