#print prime no btw given range and count
m = int(input("enter 1st value"))
n = int(input("enter 2nd value"))
pcount = 0
for x in range(m, n+1):
    i = 1
    fcount = 0
    while i <= x // 2:
        if x % i == 0:
            fcount += 1
            if fcount > 1:
                break
        i += 1
    if fcount == 1:
        print(x, "is prime")
        pcount += 1

print("no of prime btw ", m, "and", n,"are", pcount)