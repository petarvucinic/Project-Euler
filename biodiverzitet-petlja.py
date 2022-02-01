N, K = map(int, input().split())
i =  str(input())

y = i.split()

myset = set()

for i in y:
    m = int(i) // K 
    myset.add(m)

print(len(myset))

