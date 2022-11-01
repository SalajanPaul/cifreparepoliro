x = int(input("Numar: "))
k = 0
while x != 0:
    c = x % 10 #restul
    if c % 2 == 0:
        k = k+1
    x = x // 10
print("Sunt {} cifre pare"  .format(k))


