min = int(input("enter a value"))
max = int(input("enter a value"))

while min <= max:
    i = 1
    print("printing math table:", min)
    while i <= 10:
        print(min, "*", i, "=", min*i)
        i += 1
    min += 1