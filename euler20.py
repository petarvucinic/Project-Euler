
fac = 1 
suma = 0

for i in range(1, 101):
    fac *= i 
    
for i in str(fac):
    suma += int(i)
print(suma)