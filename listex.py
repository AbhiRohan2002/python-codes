fruits = ['apple', 'banana', 'orange', 'mango', 'cherry', 'kiwi', 'gauva']
newlist = []
for i in fruits:
    if "a" in i:
         newlist.append(i)
print(newlist)

newlist = [x for x in fruits if "a" not in x]
print(newlist)
