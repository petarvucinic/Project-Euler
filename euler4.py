maks = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        if str(i * j) == str(i * j)[::-1]:
            if i * j > maks:
                maks = i * j 
print(maks)
            
        