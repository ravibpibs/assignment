a=[]
b=[]
c=[]
for i in input().split():
    a.append(int(i))
for i in input().split():
    b.append(int(i))
print(a)
print(b)
c=a+b
c.sort()
print(c)
