z=input("Type your string: ")
a=input("what to count: ")
b=input("what to fild at higest index value: ")
c=input("find ending with: ")
d=input("find starting with: ")
# count() >> use to know occurence in string
p=z.count(a)
q=z.rfind(b)
r=z.endswith(c)
s=z.startswith(d)
print(p)
print(q)
print(r)
print(s)