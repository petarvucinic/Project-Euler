def prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True
    

lst = []
n = 600851475143  
for i in range(2, n):
    if prime(i) and n % i == 0:
        print(i)
        
print("kraj")