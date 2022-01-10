
x = 0
for  i in range(1, 1001):
    for j in range(1, 1001):
        x = x + i**(j*i)
        break

print(str(x)[-10::])
