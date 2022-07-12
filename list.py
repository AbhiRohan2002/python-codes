x = [1, 2, 3, 4, 5]
print(x)
print(type(x))
sum = 0
for i in x:
    print(i, end=" ")
    sum += i
print(f'\nsum = {sum}')
print(min(x))
print(max(x))
x[0] = 10
x[2] = 6
print(x)
x.sort()
print(x)

