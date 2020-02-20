a=input("enter first string:")
b=input("enter second string:")
c=list(set(a)^set(b))
print("the letters are:")
for i in c:
    print(i)



