zbir_kvadrata = 0
kvadrat_zbira = 0

for i in range(1, 101):
    zbir_kvadrata += i**2
    kvadrat_zbira += i
print(kvadrat_zbira**2 - zbir_kvadrata)