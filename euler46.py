
def isPrime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True


odd = 3
while True:
    if odd % 2 != 0:
        for j in range(2, odd): 
            for square in range(1, odd):
                if odd == (j if isPrime(j) else False) + 2*(square**2):
                    print(odd)
                    break
    odd += 1








