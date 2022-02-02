N = int(input())

lst = []

for i in range(N):
    x = str(input())
    pom = x.split()
    lst.append(pom)


lst2 = []
for i in lst:
    pom2 = []
    for j in i:
        pom2.append(int(j))
    lst2.append(pom2)


counter = 0 

for k in range(len(lst2)):
    konj1 = sum(lst2[k]) / 2

    for i in range(k+1, len(lst2)):

        konj2 = sum(lst2[i]) / 2

        for j in range(1, len(lst2[i])):

            if ( konj1 >= lst2[i][j-1] and konj1 <= lst2[i][j] ) and ( konj2 >= lst2[k][j-1] and konj2 <= lst2[k][j] ):
                counter += 1
    
print(counter)













