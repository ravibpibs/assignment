a=[]
b=[]
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    c = int(input("enter elements:"))
    if (c % 2 == 0):
        a.append(c)
    else:
        b.append(c)
print("even element:",a)
print("odd elements:",b)



