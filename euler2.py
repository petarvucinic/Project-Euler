a = 1 
b = 1 
suma = 0
for i in range(1, 4000000):
    a, b = b, a + b 
    if b % 2 == 0:
        suma += b 
print(suma)
    
    