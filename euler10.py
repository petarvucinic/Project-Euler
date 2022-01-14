

import sympy

suma = 0

for i in range(2, 2000000):
    if sympy.isprime(i):
        suma += i
print(suma)


#  iliiiiiiiiiiii


suma = 0

def prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True
    

for i in range(2, 2000000):
    if prime(i):
        suma += i

print(suma)