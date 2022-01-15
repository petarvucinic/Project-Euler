N, K = map(int, input().split())
pocetni = map(int, input().split())

redosled2 = []
for i in pocetni:
    redosled2.append(i)

if K == redosled2[-1]:
    print(redosled2[0])
else:
    for i in range(len(redosled2)):
        if redosled2[i] == K:
            m = redosled2.index(K)
            print(redosled2[m+1])