x = int(input("enter a no"))
rev = 0
y = x
d = 0
while x > 0:
    d = x % 10
    rev = rev*10 + d
    x = x//10
print(rev)
if rev == y:
    print("its polindrome")
else:
    print("not polindrome")

