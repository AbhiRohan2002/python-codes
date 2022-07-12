x = int(input("enter the number"))
i, count = 1, 0
while i <= x//2:
    if x % i == 0:
        count += 1
        if count > 1:
            break
    i += 1
if count == 1:
    print(x, " is prime")
else:
    print(x, "not prime")

