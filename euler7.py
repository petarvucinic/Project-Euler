
def prime(number):
    count = 0
    for x in range(2, number):
        if number % x == 0:
            return False 
    return True
    
count = 0
num = 2
while True:
    if prime(num):
        count += 1
    if count == 10001:
        print(num)
        break
    num += 1
    