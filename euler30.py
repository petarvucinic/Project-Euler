
suma = 0
for i in range(2, 10**9):
    prod = 0
    for j in str(i):
        prod += int(j)**5
    if prod == i:
        suma += prod
        print(suma)