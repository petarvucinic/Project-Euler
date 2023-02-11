
# in the center, start num
num = 1
# in 1st circle theres difference 2
x = 2
# final sum
suma = 0
# only odd so there is 500 repetitions
for i in range(500):
    # in one repetition we have four number to get
    for j in range(4):
        # we "make" that number 
        num += x 
        # and then add it to the sum
        suma += num 
    # increase by 2
    x += 2
print(suma + 1)