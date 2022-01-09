def najmanji_1_20(broj):
    for i in range(1, 21):
        if broj % i != 0:
            return False
    return True


broj = 1

while True:
    if najmanji_1_20(broj):
        break
    broj += 1
print(broj)