
lst = []

for a in range(2, 101):
    for b in range(2, 101):
        lst.append(a**b)
        
count = 0
for i in set(lst):
    count += 1
print(count)        
   
   
   