m1 = int(input("enter marks"))
m2 = int(input("enter marks"))
m3 = int(input("enter marks"))
avg = (m1 + m2 + m3)//3
print("average is", avg)
if avg >= 70:
    print("first class")
elif avg >= 60:
    print("second class")
elif avg >= 50:
    print("third class")
else:
    print("fail")
