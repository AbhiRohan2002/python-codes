numbers = [x for x in range(1, 21)]
print(numbers)
even = [x for x in numbers if x%2 == 0]
print(even)
odd = [x + 1 for x in even]
print(odd)

squares = [x**2 for x in range(1, 101) if x**2 < 1000]
print(squares)
