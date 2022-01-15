# PRVI ZADATAK PETLJA - TAKMICENJE I KRUG KVALIF.
# c1, c2 = map(str, input().split())
# a1, a2 = map(int, input().split())
var = input()
c1 = var[0]
c2 = var[1]
a1, a2 = map(int, input().split())
lst = []
rezultat = []
konacno = ""
for i in range(a1):
    lst.append(c1)
for j in range(a2):
    lst.append(c2)
konacno = ""
if a1 - a2 == 1 or a1 - a2 == -1 or a1 - a2 == 0:
    while lst != []:        
        for i in range(1, len(lst)+1):
            if len(lst) == 1:
                for i in rezultat:
                    konacno += i
                for i in range(len(konacno)):
                    if lst[0] == konacno[0]:
                        pomocna = []
                        for i in konacno:
                            pomocna.append(i)
                        pomocna.append(lst[0])
                        lst.remove(lst[0])
                        krajnje = ""
                        for i in pomocna:
                            krajnje += i
                        print(krajnje)
                        break
                    elif lst[0] != konacno[0]:
                        pomocna = []
                        for i in konacno:
                            pomocna.append(i)
                        pomocna.insert(0, lst[0])
                        lst.remove(lst[0])
                        krajnje = ""
                        for i in pomocna:
                            krajnje += i
                        print(krajnje)
                        break
            elif lst[i] != lst[i-1]:
                rezultat.append(lst[i] + lst[i-1])
                lst.remove(lst[i])
                lst.remove(lst[i-1])
                if len(lst) == 0:
                    for i in rezultat:
                        konacno += i
                    print(konacno)
                break
else:
    print("nemoguce")