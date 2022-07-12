x = ["raju", 13, 20, 8.9, True]
print(x)

y = x
print(y)
z = x + y
print(z)
z.extend(y)
print(z)
print(len(z))
print(z.count('raju'))
print(z[:10])

for i in z:
    if i == True:
        z.remove(i)
print(z)
z.clear()
print(z)
z = x.copy()
print(z)
for i in z:
    print(i)
i = 0
while i < len(z):
    print(z[i])
    i += 1

for i in range(len(z)):
    print(z[i])







