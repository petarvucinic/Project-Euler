
f2 = 1
lst = [0, 1]
f1 = 0 
while True:
    f1, f2 = f2, f1+f2
    lst.append(f2)
    if len(str(f2)) == 1000:
        print(lst.index(f2))
        break
    
