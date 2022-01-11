x = 1
suma = 0
while x <= 10**6:
    # str (x) but reversed
    x_str = str(x)[::-1]
    # just str(bin(x)
    x_bin = str(bin(x))[2::]
    # reversed x_bin
    y_bin = x_bin[::-1]
    # condition
    if str(x) == x_str and x_bin == y_bin:
        suma += x
    x += 1
print(suma)