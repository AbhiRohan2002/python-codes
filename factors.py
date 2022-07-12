x = int(input("enetr a no"))
i = 1
count = 0
sum = 0
while i <= x//2:
    if x % i == 0:
        print(i, "is a factor")
        count += 1
        sum = sum + i
    i += 1
if sum == x:
    print(x, " is perfect")
else:
    print(x, " not perfect")
print(count)
