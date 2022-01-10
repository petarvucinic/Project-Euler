
x = 1

while True:
    mylist1 = []
    mylist2 = []
    mylist3 = []
    mylist4 = []
    mylist5 = []
    mylist6 = []
    for i in str(x):
            num1_ = 1 * x
            num2_ = 2 * x
            num3_ = 3 * x
            num4_ = 4 * x
            num5_ = 5 * x
            num6_ = 6 * x
    for a in str(num1_):
        mylist1.append(a)
    for a in str(num2_):
        mylist2.append(a)
    for a in str(num3_):
        mylist3.append(a)
    for a in str(num4_):
        mylist4.append(a)
    for a in str(num5_):
        mylist5.append(a)
    for a in str(num6_):
        mylist6.append(a)
    if set(mylist1) == set(mylist2) == set(mylist3) == set(mylist4) == set(mylist5) == set(mylist6):
        print(x)
        break

    x += 1
