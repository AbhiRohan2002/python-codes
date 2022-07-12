s1 = '  welocme  '
s2 = "hello world"
s3 = "asdf,ert, op"
a, b, c = s3.split(",")#string slicing
print(a, b, c)
print(len(s2))
print(len(s1.strip()))
print(s1.count('e'))
print(s2.count('l'))